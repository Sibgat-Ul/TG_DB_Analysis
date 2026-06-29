# ANALYSIS.md — What's Used vs. What Can Be Discarded

> **Scope:** classify all 559 tables of `ocms` into **keep / archive / drop** based on data
> volume, recency, and redundancy, so the PostgreSQL migration ([PSQL.md](PSQL.md)) carries
> forward only the live schema. Builds on the domains in [GROUPING.md](GROUPING.md).
>
> ⚠️ **"Discard" never means delete the data.** Every drop candidate is first dumped to an
> archive (`ocms_archive` schema / `.sql.gz`). The recommendations below decide what enters
> the *new* PostgreSQL schema, not what gets destroyed. The migration is **lossless**.

---

## 1. Method — three signals

| Signal | Source | Meaning |
|---|---|---|
| **Row count** | `COUNT(*)` per table | 0 rows = never used or a stub |
| **Recency** | `MAX(date column)` per table | last-touched year; < 2023 ⇒ likely abandoned |
| **Redundancy** | name/era clustering | two tables doing the same job (one is dead) |

Headline numbers:

| Bucket | Tables | Verdict |
|---|---:|---|
| **Live** — data dated **2025–2026** | **236** (216 in 2026 + 20 in 2025) | **KEEP** |
| Slowing — last data **2023–2024** | 50 | KEEP (verify) |
| **Stale** — last data **≤ 2022** | 73 | **ARCHIVE** |
| **Empty** — 0 rows | 66 | **DROP / defer** |
| No date column (small config) | ~134 | keep if a live lookup, else archive |

So roughly **240 tables carry the live system**; the other ~300 are lookups (mostly tiny &
fine to keep), abandoned modules, or empty stubs.

---

## 2. DROP candidates — 66 empty tables

These have **0 rows**. They fall into recognisable groups, which tells us *why* they're empty.

### 2a. Abandoned "Collar / Cuff" sub-feature (drop)
A whole collar-&-cuff variant of the knit/dye/finish flow was scaffolded but never used:
`knitting_delivaryChalanCollar`, `knitting_fabricRcvCollar`, `knitting_program_prod_collar`,
`knitting_subContractCollar`, `dyeing_fabricDelivaryCollar`, `finish_fabricRcvCollar`,
`inv_greyProcessChalanCollar`, `inv_greyProcessMrrCollar`. → **drop.**

### 2b. Abandoned process modules (drop after confirm)
Print / twisting / yarn work-order details and grey-process chalans never received data:
`workorder_emblishmentFabric`, `workorder_finishingDetails`, `workorder_yarn`,
`workorder_yarnDetails`, `inv_greyProcessChalan(+Details)`, `inv_greyProcessMrr*`,
`inventory_twistingIssueDetails`, `inventory_yarnRequisitionDetails`, `inventory_yarnTest`,
`inventory_embdIssueFabric`, `inventory_finishFabricOrderTransfer`, `inventory_sampleChalan(+Details)`,
`dyeing_finishingProduction`, `dyeing_finishRoll`, `dyeing_labReceipe`, `knit_qad(+_rolls)`,
`knit_target(+_yarns)`, `knitting_dailyProduction`, `knitting_dailyTarget(F)`,
`knitting_monthlyLoad`, `knitting_productionPlan`, `knitting_program_production`,
`knitting_target_daily`. → **drop** (the *live* equivalents exist elsewhere with data).

### 2c. Newer stubs — DEFER, don't drop
These are **empty but part of the newer snake_case build** (they carry `created_at`/
`deleted_at`) — a purchasing/requisition module that's wired up but not yet in production:
`ocms_purchase_requisition`, `ocms_purchase_requisition_details`, `ocms_requisition_quote`,
`ocms_requisition_quote_approval`, `ocms_supplier_profile`, `ocms_product_details`,
`ocms_product_supplier`. **Keep the structure** (migrate empty) — they belong to the future.

### 2d. Misc empty (drop)
`comm_bbLCDetails`, `comm_ci_history`, `comm_foc_docs`, `comm_masterLC_discounts`,
`comm_masterLC_notifyParty`, `comm_pi_block_items`, `dev_po_sheet`, `dev_trims_info_details`,
`inq_collarcuffinfo`, `inq_trims_info_details`, `inq_ydcombo`, `mkt_style_info`,
`mkt_trims_info`, `pack_attach`, `sample_po_sheet`, `short_emblishment_info`,
`stock_dyesChemMain`, `sub_breakdown_info`, `subcontract_basic_info`, `subcontract_fabric_info`,
`lib_comm_pay_term`, `ocmsProfile`.

---

## 3. ARCHIVE candidates — stale (last data ≤ 2022)

Real historical data, but the module is no longer written to. Migrate to an `ocms_archive`
schema (read-only), keep out of the active app. Highlights (full list of 73 in the query log):

| Why it's stale | Tables |
|---|---|
| **Superseded lookups** (replaced by a newer master — see §4) | `libProjectInfo` (→`dbProjectInfo`), `libbuyerYD` (→`libbuyer`), `libGeneralProductGroup`/`libGeneralProductItem` (2018, →`ocms_product_*`), `libYDInvProductGroup`/`libYDInvProductItem`, `libknittargetprod`, `libTnaStep`/`ocms_tna_step` (→`ocms_tna_*` 2026) |
| **Retired process modules** | `inventory_aopIssue(Details)`/`aopReceive(Details)` (AOP, 2020), `workorder_print(Details)`, `workorder_twisting(Details)`, `workorder_washing(Details)`, `workorder_finishing` (2020–22) |
| **Old commercial/dyeing variants** | `comm_piInfo`, `comm_cert`, `comm_cf_templates`, `comm_masterLCAmendment`, `comm_masterLcInvoice` (2022), `dyeing_lab*` (2020–21), `dyeing_*Collar` (2021), `dyeing_finishingRecipe` (2022, 5.5 k rows) |
| **Very old config** (2013–2018) | `libcolorprocess`, `libfabrictype`, `libydstripe`, `Lib_dying_mc_Loading`, `dbUserDepartment`/`dbUserDesignation` (→`libUserDepartment`/`libUserDesignation`), `libNoteColum`/`libNoteDepartment`, `libDyeingBatchStatus`, `lib_rack_info`, `libbuyerSampleStep` |

> Archive ≠ ignore: a few stale lookups (e.g. `libGeneralProductGroup`) are still **referenced
> by FK candidates in live tables** (see [RELATIONSHIP.md](RELATIONSHIP.md) §weak FKs). Keep
> those reachable until the referencing columns are cleaned.

---

## 4. Redundancy — duplicate tables (consolidate)

The clearest evidence of "scattered information." Pick **one survivor** per pair, migrate the
other's distinct rows into it, then archive the loser.

| Concept | Tables (survivor **bold**) | Evidence |
|---|---|---|
| **Supplier master** | **`lib_supplier`** (2 146 rows, `supplierID` unique) vs `libsupplier` (4 057 rows, `supplierID` **not** unique – 2 146 distinct) | `libsupplier.supplierID` ⊂ `lib_supplier.supplierID` at **99.9 %**. `libsupplier` is the old denormalised version (duplicate supplier rows per category). |
| **Yarn type** | **`lib_yarn_type`** vs `libyarntype` | snake_case vs camelCase duplicate |
| **Factory/company** | **`dbProjectInfo`** (13 rows, the live `projectID` master) vs `libProjectInfo` (2 rows, 2014) | `projectID` FK validates 100 % against `dbProjectInfo`, ~10 % against `libProjectInfo` |
| **Buyer master** | **`libbuyer`** (194, live) vs `libbuyerYD` (58, 2014) | `buyerID` validates 95–99 % against `libbuyer` |
| **User dept / designation** | **`libUserDepartment`/`libUserDesignation`** (live) vs `dbUserDepartment`/`dbUserDesignation` (2014) and `libGenUserDepartment` | three overlapping department lists |
| **Country** | **`libCountry`** (14) vs `libcountry` (6) | case-variant duplicates |
| **Product master** | **`ocms_product_*`** (2024+) vs `libGeneral*` / `libYDInv*` (2015–18) | newer product module supersedes old lookups |
| **TNA steps** | **`ocms_tna_step` / `ocms_tna_leadtime_library`** (2026) vs `libTnaStep` (2015) | |

There is also the **whole-DB era split**: the legacy camelCase core (`insertDate`, 362 tables)
vs the newer snake_case module (`created_at`, 47 tables). Where the two describe the same
concept (e.g. requisitions), the snake_case version is the intended future.

---

## 5. The live core — what's definitely KEEP

The system genuinely runs on ~240 tables with 2025–2026 data. The heaviest, most-active:

| Table | Rows | Domain | Last data |
|---|---:|---|---|
| `activity_log` | 4.65 M | System | 2026 |
| `production_sewingInfoDetails` | 2.18 M | Production | 2026 |
| `ocms_doc_approval_sts` | 1.69 M | Core OCMS | 2026 |
| `ocms_chemical_transaction` | 1.33 M | Core OCMS | 2026 |
| `dyeing_batchReceipe` | 1.31 M | Dyeing | 2026 |
| `inventory_DyesChemIssueDetailsSub` | 1.30 M | Inventory | 2026 |
| `ocms_purchase_requisition_approval` | 0.77 M | Core OCMS | 2026 |
| `bulk_trims_info_details` | 0.73 M | Bulk | 2026 |
| `inventory_trimsIssueDetails` | 0.45 M | Inventory | 2026 |
| `production_cuttingInfo` | 0.37 M | Production | 2026 |

…plus every `lib*` master still referenced (buyers, suppliers, yarn, dia, chemicals), the full
`workorder_*`, `knitting_*`, `dyeing_*`, `inventory_*` live sub-ledgers, and the `ocms_*`
workflow hub. These flow straight into [RELATIONSHIP.md](RELATIONSHIP.md) and [PSQL.md](PSQL.md).

---

## 6. Recommended action by tier

| Tier | Tables (≈) | Action in migration |
|---|---:|---|
| **A — Live core** | ~240 | Migrate to new PG schema, add FKs & constraints |
| **B — Live lookups (no date)** | ~120 | Migrate as reference tables; dedupe per §4 first |
| **C — Stale** | 73 | Dump to `ocms_archive` (read-only), exclude from app |
| **D — Empty / abandoned** | ~59 | Do **not** migrate; keep DDL in archive dump |
| **E — Empty newer stubs** | 7 | Migrate empty (future purchasing module) |

> **Before dropping/archiving anything**, run the redundancy merges in §4 and confirm with the
> app team that the §2b "abandoned process" modules (print, twisting, washing, AOP, collar)
> are truly retired — these are business decisions, not purely technical ones.
