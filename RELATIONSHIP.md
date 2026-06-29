# RELATIONSHIP.md — Foreign Keys & Lossless Redesign

> **Goal:** turn the implicit, undeclared relationships in `ocms` into explicit foreign keys,
> and propose a redesign that loses **zero** data. Builds on the domains in
> [GROUPING.md](GROUPING.md) and the keep/drop tiers in [ANALYSIS.md](ANALYSIS.md).
> Detection is reproducible via [`fk_detect.py`](fk_detect.py) → `relationships.json`.

The database declares **0 foreign keys** today. But the relationships *exist* — they're just
enforced (badly) in application code. We recover them from the data.

---

## 1. The key architecture you must understand first

Almost every table (≈545 of 559) has **two** integer keys:

```
CREATE TABLE libbuyer (
    id       INT AUTO_INCREMENT PRIMARY KEY,   -- local surrogate, used by nobody else
    buyerID  INT,                              -- the BUSINESS key everyone joins on
    buyerName VARCHAR(...), ...
);
```

- **`id`** — per-table auto-increment. It is the physical PK but is **not** referenced by other
  tables.
- **The business key** (`buyerID`, `projectID`, `diaID`, `jobID`, `order_id`, `woNo`…) — this is
  the *logical* key that child tables carry and join on.

**Consequence for FK design:** foreign keys must point at the **business key**, not at `id`.
That means the business key needs a `UNIQUE` constraint in the master table before it can be an
FK target. (Where the business key is *not* unique today — e.g. `libsupplier.supplierID` — that
table is the duplicated one and is consolidated per [ANALYSIS.md §4](ANALYSIS.md).)

Most-shared key columns (number of tables carrying them):

| Key | Tables | Role |
|---|---:|---|
| `projectID` | 359 | factory/company unit (tenant) |
| `jobID` | 217 | the order "job" (born at sampling) |
| `breakdownID` | 143 | order size/colour breakdown line |
| `diaID` | 126 | knit diameter |
| `order_id` | 79 | bulk order line |
| `buyerID` | 68 | buyer |
| `mrrNo` | 67 | material receive report no. |
| `woNo` / `wo_id` | 96 / 57 | work-order number |

---

## 2. Confirmed foreign keys (validated against the data)

Containment = % of distinct child values that exist in the parent key (measured by
[`fk_detect.py`](fk_detect.py)). **≥ 95 % ⇒ enforce now.**

### 2a. Cross-cutting / tenancy

| Child (examples) | Column | → Parent | Containment | Verdict |
|---|---|---|---:|---|
| *all 359 tables* | `projectID` | **`dbProjectInfo.projectID`** | 100 % | ✅ enforce |
| permission tables | `modID` | **`dbModule.modID`** | 94–100 % | ✅ enforce |
| permission tables | `subModID` | **`dbModuleSub.subModID`** | 98–99 % | ✅ enforce |

### 2b. Reference / `lib*` masters

| Child (examples) | Column | → Parent | Containment | Verdict |
|---|---|---|---:|---|
| dyeing/inventory/workorder | `buyerID` | **`libbuyer.buyerID`** | 95–99 % | ✅ enforce |
| inventory/MRR | `supplierID` | **`lib_supplier.supplierID`** | 99.9 % | ✅ enforce (use `lib_supplier`, not `libsupplier`) |
| `libDyeingChemicalName/Local` | `chemicalTypeID` | **`libDyeingChemicalType`** | 100 % | ✅ enforce |
| `libDyeingChemicalName/Local` | `chemicalClassID` | **`libDyeingChemicalClass`** | 99–100 % | ✅ enforce |

### 2c. Order lifecycle "spine"

| Child (examples) | Column | → Parent | Containment | Verdict |
|---|---|---|---:|---|
| `knittingYarnAllocation`, `dyeing_batchReceipe`, `production_sewingInfoDetails` | `jobID` | **`sample_basic_info.jobID`** | 95–97 % | ⚠️ clean (≈3–5 % orphans) then enforce |
| `bulk_trims_info_details`, `workorder_trimsDetails` | `order_id` | **bulk order header** (`order_id` carried 1:1 by `bulk_budgetCostActual`) | 99 % | ⚠️ confirm true header, then enforce |
| `workorder_trimsDetails`, `inventory_trimsReceiveDetails` | `woNo` | **`workorder_trims.woNo`** | 100 % | ✅ enforce (trims WO) |
| `inventory_grayFabricReceiveDetails` | `woNo` | **`workorder_knitting.woNo`** | 93 % | ⚠️ clean then enforce (knit WO) |

### 2d. Material traceability (discovered by `fk_detect.py`)

These line-level links were surfaced automatically and validate strongly — they trace physical
material from work order → receive/issue → inventory:

| Child (examples) | Column | → Parent | Containment | Verdict |
|---|---|---|---:|---|
| `inventory_trimsIssueDetails`, `inventory_trimsReceiveDetails` | `trims_id` | **`workorder_trimsDetails.trims_id`** | 100 % | ✅ enforce |
| `inventory_grayFabricReceiveDetails`, `knitting_fabricRcvDetails` | `roll_id` | **`knitting_delivaryChalanDetails.roll_id`** | 100 % | ✅ enforce |
| `inventory_grayFabricReceiveDetails`, `knitting_fabricRcvDetails` | `mrr_id` | **`invoice_mrr_info_dtls.mrr_id`** | 97–99 % | ✅ enforce |
| `knitting_fabricRcvDetails` | `mrrNo` | **`inventory_trimsReceive.mrrNo`** | 91 % | ⚠️ clean then enforce |
| `mkt_cost_info` | `style_id` | **`mkt_fabric_info.style_id`** | 100 % | ✅ enforce |

> Full machine-generated edge list (111 edges across 41 keys: **34 enforce, 14 clean-then-enforce,
> 63 reject**) is in `relationships.json` from [`fk_detect.py`](fk_detect.py).

> **`woNo` is polymorphic.** It is a work-order number, but the *type* of work order
> (trims / knitting / dyeing / embellishment / washing) lives in a different `workorder_*`
> header table. So `woNo` can't get a single FK — see §4 redesign (split by WO type or add a
> `wo_type` discriminator + a unified `work_order` parent).

---

## 3. Rejected / "needs investigation" edges (do NOT blindly FK)

The detector also surfaced low-containment edges — important because they look like FKs by
name but **aren't**, and forcing a constraint would fail or corrupt meaning:

| Edge by name | Containment | Reality |
|---|---:|---|
| `*.diaID` → `libdia.diaID` | 16–21 % | Child `diaID` uses a different id-space (e.g. dyeing/knitting carry their own dia codes); `dyeing_batchPlan` even has 814 distinct vs 472 in `libdia`. **Investigate** before mapping. |
| `*.countryID` → `libCountry.countryID` | 0 % | `production_*.countryID` is not the country lookup at all (likely a free code). **Not an FK.** |
| `*.itemID` → `libGeneralProductItem.itemID` | 0 % | `inventory_*.itemID` has **1.1 M** distinct values — it's an inventory item id, not the 15-row product-group lookup. The real item master is the (newer) `ocms_product_*` set. |
| `*.groupID` → `libGeneralProductGroup` | ~10 % | superseded lookup (see [ANALYSIS.md §4](ANALYSIS.md)); remap to `ocms_product_group`. |

**Lesson:** name-matching alone is wrong here. Every proposed FK in this database must be
**validated by value containment** (that's why `fk_detect.py` measures it).

---

## 4. Proposed redesign — lossless, incremental

Principle: **add structure, don't reshape data.** Keep every existing column and row; layer
keys and constraints on top. Nothing is dropped except confirmed-dead tables ([ANALYSIS.md](ANALYSIS.md)).

### Step 1 — Promote business keys to unique keys (no data change)
For each master, add `UNIQUE` on the business key (after the dedup merges in
[ANALYSIS.md §4](ANALYSIS.md)):
```sql
ALTER TABLE dbProjectInfo  ADD CONSTRAINT uq_project  UNIQUE (projectID);
ALTER TABLE libbuyer       ADD CONSTRAINT uq_buyer     UNIQUE (buyerID);
ALTER TABLE lib_supplier   ADD CONSTRAINT uq_supplier  UNIQUE (supplierID);
ALTER TABLE sample_basic_info ADD CONSTRAINT uq_job    UNIQUE (jobID);
-- chemical type/class, module/submodule, workorder_* headers, ...
```

### Step 2 — Add the confirmed FKs from §2 (enforce vs NOT VALID)
- **≥ 95 %** edges: add directly.
- **70–95 %** edges: add as `NOT VALID` (PostgreSQL) so new rows are checked while existing
  orphans are tolerated, then clean orphans, then `VALIDATE CONSTRAINT`.
```sql
-- clean (≥95%):
ALTER TABLE inventory_DyesChemIssueDetailsSub
  ADD CONSTRAINT fk_buyer FOREIGN KEY (buyerID) REFERENCES libbuyer (buyerID);

-- dirty (≈95%), Postgres staged approach:
ALTER TABLE production_sewingInfoDetails
  ADD CONSTRAINT fk_job FOREIGN KEY (jobID) REFERENCES sample_basic_info (jobID) NOT VALID;
-- ...fix/quarantine orphan jobIDs...
ALTER TABLE production_sewingInfoDetails VALIDATE CONSTRAINT fk_job;
```
Orphans found during validation go to a `*_orphans` quarantine table — **nothing is deleted.**

### Step 3 — Resolve the polymorphic `woNo`
Two acceptable patterns:
- **(A) Per-type FKs** — keep `workorder_knitting`, `workorder_trims`, … as separate headers
  and FK each consumer to the right one (works because each `woNo` space is type-scoped). Lowest
  effort, matches current data.
- **(B) Unified `work_order` parent** — one header table `(woNo PK, wo_type, projectID, …)`
  populated from all `workorder_*` heads, with a `wo_type` discriminator; consumers FK to it.
  Cleaner long-term; do it during/after the PG move.

### Step 4 — Standardise audit & soft-delete columns
Unify the two eras ([GROUPING.md §5](GROUPING.md)) into one convention in the new schema:
`created_at, created_by, updated_at, updated_by, deleted_at` — backfill from
`insertDate/insertBy/updateDate/updateBy` (lossless rename + copy). This removes a major source
of "scattered" inconsistency.

### Step 5 — Normalise obvious denormalisation (optional, post-migration)
Tables repeat text that should be FKs: `supplierName`, `buyerName`, `color`, `colorCode`,
`yarnCount`, `structure`, `gsm`, `uom` are stored as strings in dozens of detail tables. After
FKs exist, these can become lookups (`*_id` + view that re-exposes the name) — **only with a
backward-compatible view** so existing reports keep working. Defer until the app is ready.

---

## 5. Suggested order of attack

1. Run [`fk_detect.py`](fk_detect.py) to regenerate `relationships.json` (full edge list +
   containment for every shared key — this doc summarises the high-value ones).
2. Do the **dedup merges** ([ANALYSIS.md §4](ANALYSIS.md)) — FK targets must be unique first.
3. Add `UNIQUE` keys (Step 1), then **enforceable FKs** (§2, ≥95 %).
4. Stage the **cleanable FKs** with `NOT VALID`, quarantine orphans, `VALIDATE`.
5. Carry the keyed schema into PostgreSQL — see [PSQL.md](PSQL.md), which folds all of this
   into the migration DDL.

> **Lossless guarantee:** Steps 1–4 only *add* constraints and *quarantine* (never delete)
> orphan rows. Every original row remains, either in its table or in a `*_orphans` sibling.
