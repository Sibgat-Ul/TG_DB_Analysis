# GROUPING.md — Table Clustering for the `ocms` Database

> **Database:** `ocms` (MariaDB, InnoDB) · **559 tables** · **~23.0 M rows**
> **Domain:** Garment / knit-textile manufacturing ERP (OCMS = *Order & Costing Management System*).
> This document clusters the 559 tables into business domains. It is the foundation for
> [ANALYSIS.md](ANALYSIS.md) (what to keep/discard), [RELATIONSHIP.md](RELATIONSHIP.md)
> (foreign keys) and [PSQL.md](PSQL.md) (PostgreSQL migration).
> The full per-table listing is in [_TABLE_INVENTORY.md](_TABLE_INVENTORY.md).

---

## 1. How the grouping was done

There are **no foreign keys** in this database (0 declared FK constraints across 531 dumped
tables), so the schema gives no structural hints about which tables belong together. Three
signals were used instead:

1. **Table-name prefix.** The schema follows a strong `domain_entity` convention
   (`inventory_*`, `dyeing_*`, `knitting_*`, `workorder_*`, `ocms_*`, `lib*`, `db*` …).
   The first token before `_` is an almost perfect domain label.
2. **Shared "business key" columns.** Almost every table carries cross-cutting keys such as
   `projectID`, `jobID`, `order_id`, `woNo`/`wo_id`, `breakdownID`, `buyerID`. These trace the
   order lifecycle *across* domains and are analysed in [RELATIONSHIP.md](RELATIONSHIP.md).
3. **Row counts & recency** (MAX of each table's date column) to confirm a cluster is real and
   live versus an abandoned experiment.

Prefixes were normalised (e.g. `inv_` + `inventory_` + `stock_` → **Inventory**;
`knit*` + `knittingYarnAllocation` → **Knitting**; `inq_`+`sample_`+`dev_`+`sub_` →
**Sampling/Development**) to collapse historical spelling variants into one domain.

---

## 2. The 12 domains (at a glance)

| # | Domain | Tables | Rows | Role |
|---|--------|-------:|-----:|------|
| 01 | **System / Admin / Auth** | 16 | 4.70 M | Users, roles, module permissions, `activity_log` audit trail |
| 02 | **Reference / Lookup (`lib*`)** | 129 | 0.08 M | Master data: buyers, suppliers, yarn, dia, chemicals, countries… |
| 03 | **Core OCMS — Orders / TNA / Approvals / Products** | 31 | 3.99 M | Central workflow: doc approvals, TNA, requisitions, product master, chemical ledger |
| 04 | **Sampling / Development / Inquiry** | 59 | 0.37 M | Pre-order: inquiry (`inq_`), sampling (`sample_`), development (`dev_`) |
| 05 | **Bulk Order / Costing** | 22 | 1.29 M | Confirmed bulk orders, cost sheets, budgets, breakdowns |
| 06 | **Work Order** | 41 | 0.73 M | Internal work orders to knitting / dyeing / trims / embellishment |
| 07 | **Knitting** | 35 | 0.93 M | Knit production, yarn allocation, machine logs, delivery chalans |
| 08 | **Dyeing & Finishing** | 53 | 2.56 M | Batches, recipes, process status, finishing, chemical issue |
| 09 | **Production (Cut / Sew / Finish)** | 14 | 3.07 M | Cutting, sewing input/output, finishing, daily line production |
| 10 | **Inventory & Store** | 123 | 5.27 M | Receive/issue/stock for yarn, trims, fabric, dyes-chem, general |
| 11 | **Commercial / Invoicing / LC** | 31 | < 0.01 M | Master LC, invoices, MRR, commercial docs |
| 12 | **Packing & Shipment** | 5 | < 0.01 M | Pack lists, carton/shipment data |
| | **Total** | **559** | **23.0 M** | |

> Two domains dominate the row volume: **Inventory** (5.3 M) and **System** (4.7 M, almost
> all in `activity_log`). The **business core** (order → production → dyeing) is spread across
> domains 03–10, which is exactly why information feels "scattered."

---

## 3. The order lifecycle (how the domains connect)

The domains are not arbitrary buckets — they are **stages of one manufacturing pipeline**.
Reading left-to-right is the path of a single buyer order through the factory:

```
            ┌──────────────────── 02 Reference / lib* (buyers, suppliers, yarn, dia, chemicals) ──────────────────┐
            │                          cross-cutting master data, referenced everywhere                           │
            └─────────────────────────────────────────────────────────────────────────────────────────────────────┘
            ┌──────────── 01 System / Auth (projectID = factory unit, users, permissions, activity_log) ──────────┐
            └─────────────────────────────────────────────────────────────────────────────────────────────────────┘

  04 Sampling/Inquiry ──▶ 05 Bulk Order/Costing ──▶ 06 Work Order ─┬─▶ 07 Knitting ──▶ 08 Dyeing/Finishing ──┐
   (inq_, sample_, dev_)    (bulk_, cost sheet)      (workorder_)    │                                           ▼
        jobID                  order_id                 woNo/wo_id   └─────────────────────────────────▶ 09 Production
                                                                                                        (cut/sew/finish)
                                                                                                              │
   10 Inventory & Store  ◀───────── feeds / consumes materials at every stage ───────────────────────────────┘
        (receive / issue / stock)                                                                             │
                                                                                                              ▼
                                                                            11 Commercial/Invoice/LC ──▶ 12 Packing/Shipment
```

**The "spine" keys that stitch stages together** (detailed in [RELATIONSHIP.md](RELATIONSHIP.md)):

| Stage boundary | Key column | Originates in |
|---|---|---|
| Factory / tenant scope (all stages) | `projectID` | `dbProjectInfo` (13 factory units) |
| Inquiry → Sample → Order | `jobID` | `sample_basic_info` (~14 k jobs) |
| Bulk order line | `order_id` / `breakdownID` | bulk/sample order + size-color breakdown |
| Order → Work Order | `woNo`, `wo_id` | `workorder_*` headers (~32 k WOs) |
| Material master | `buyerID`, `supplierID`, `diaID`, `yarn*`, `chemical*ID` | `lib*` tables |

---

## 4. Domain detail

### 01 · System / Admin / Auth — 16 tables, 4.70 M rows
Authentication, authorisation and audit. Key tables:
`dbModule`, `dbModuleSub`, `dbModuleSubSec` (the application's module tree),
`dbModulePermission`, `dbUserRoll`, `dbUserRollPerm`, `dbProjectPermission` (RBAC),
`dbUserDepartment`, `dbUserDesignation`, `dbProjectInfo` (**the 13 factory/company units** —
the `projectID` master), `dbProjectCapacity`, `user`, `other_permissions`,
`user_other_permissions`, and **`activity_log` (4.65 M rows — 20 % of the whole DB)** which is
the system-wide audit log.

### 02 · Reference / Lookup (`lib*`) — 129 tables, 0.08 M rows
Master/lookup data. Small tables, high reuse. Notable masters:
`libbuyer` (194 buyers — `buyerID`), `lib_supplier` / `libsupplier` (suppliers — *duplicated*,
see [ANALYSIS.md](ANALYSIS.md)), `libdia` (472 dia — `diaID`), `libyarncount`, `libyarntype`,
`libyarncomposition`, `libstructure`, `libgsm`, `libcolordepth`, the `libDyeing*` family
(chemicals, recipes, machine profiles), `libTrims*`, `libCountry`, `libSampleType`,
`libTnaStep` / `libTnaBulk` (time-and-action templates), `libMerchendisingTeam`. These are the
right-hand side of most foreign keys.

### 03 · Core OCMS — Orders / TNA / Approvals / Products — 31 tables, 3.99 M rows
The central workflow engine, all `ocms_*` plus `general_*`, `mer_*`, `turag_*`:
`ocms_doc_approval` / `ocms_doc_approval_sts` (1.69 M — multi-step approval status),
`ocms_chemical_transaction` (1.33 M — chemical stock ledger),
`ocms_purchase_requisition` + `_approval` (0.77 M), `ocms_orderTnaTable` (0.16 M — order
Time-&-Action plan), `ocms_product_info` / `_category` / `_group` / `_details` /
`_supplier` (product master), `ocms_tna_step` / `_comments` / `_leadtime_library`,
`turag_stock_value_summary*`. This is the hub most other domains post into.

### 04 · Sampling / Development / Inquiry — 59 tables, 0.37 M rows
Everything *before* a confirmed bulk order:
`inq_*` (fabric/trims/yarn inquiry), `sample_basic_info` (**`jobID` master, ~14 k**),
`sample_breakdown_info`, `sample_type_info`, `sample_fabricationinfo*`, `dev_*` (PO sheet,
trims, basic info), `sub_*`, `short_*`, `mkt_*`, `requisitioncutting*`, `requisitiondyeing*`.

### 05 · Bulk Order / Costing — 22 tables, 1.29 M rows
Confirmed orders and money: `bulk_basic_info`, `bulk_breakdown_info`, `bulk_cost_sheet`,
`bulk_budgetCostActual`, `bulk_fabricationinfo*`, `bulk_trims_info_details` (0.73 M),
`bulk_yarnselection`, `bulk_dhl_info`, `order_*`. Carries `order_id` and `breakdownID`.

### 06 · Work Order — 41 tables, 0.73 M rows
Internal production orders issued to each section: `workorder_knitting(+Details)`,
`workorder_trims(+Details)` (0.17 M), `workorder_dyeing`, `workorder_emblishment*`,
`workorder_finishingDetails`, `workorder_sampleDetails`, `wo_*`, `work_order_document`
(0.09 M). Carries `woNo` / `wo_id`.

### 07 · Knitting — 35 tables, 0.93 M rows
`knittingYarnAllocation` (0.13 M, `jobID`/`woNo`), `knitting_prod_mc_dtls(+_pcs)` (machine
production), `knitting_fabricRcvDetails`, `knitting_delivaryChalanDetails`,
`knitting_dailyProduction` / `_dailyTarget`, `knitting_target_*`. (Several `knit_*`
tables here are empty stubs — see [ANALYSIS.md](ANALYSIS.md).)

### 08 · Dyeing & Finishing — 53 tables, 2.56 M rows
`dyeing_batchReceipe` (1.31 M, 55 cols), `dyeing_processStatus` (0.27 M, 44 cols),
`dyeing_batchQuality`, `dyeing_batchCard`, `dyeing_batchPlan`, `dyeing_finish*`,
`dyeing_turag_*` (factory-specific), `finish_*`, `finishing_*`, `chemical_*`. The recipe and
process-status tables are among the widest in the DB.

### 09 · Production (Cut / Sew / Finish) — 14 tables, 3.07 M rows
Shop-floor output: `production_sewingInfoDetails` (**2.18 M — largest business table**),
`production_sewingInput`, `production_cuttingInfo` (0.37 M), `production_finishingInfo`,
`production_fabricReceiveDetails`, `prod_*`. Few tables, huge rows.

### 10 · Inventory & Store — 123 tables, 5.27 M rows
The largest domain by table count and rows. Receive / issue / stock sub-ledgers per material:
`inventory_DyesChemIssueDetailsSub` (1.30 M), `inventory_trimsIssueDetails` (0.45 M),
`inventory_GeneralIssueDetails` (0.37 M), `inventory_grayFabricReceiveDetails` (0.15 M),
plus `inventory_*Receive*/*Issue*/*Stock*` for yarn, trims, print, AOP, embroidery, fabric,
shipment, twisting; and the older `inv_*` and `stock_*` variants.

### 11 · Commercial / Invoicing / LC — 31 tables, < 0.01 M rows
`comm_masterLC*` (LC details, amendments, invoices), `invoice_mrr_info_dtls` (note: large
MRR detail data actually lives under `invoice_*` despite the small `comm_*` rowcounts),
`invoice_wo_info*`, `income`. Mostly low-volume / partially-adopted (see [ANALYSIS.md](ANALYSIS.md)).

### 12 · Packing & Shipment — 5 tables, < 0.01 M rows
`packing_lists`, `packlist_*`, `pack_*`, `lib_pack_head_foot`. Smallest domain; likely a
newer or lightly-used module.

---

## 5. Cross-cutting concerns (not a single domain)

These patterns appear in **every** domain and shape the redesign:

- **Dual surrogate keys.** ~545 tables have both an auto-increment `id` *and* a business key
  (`projectID`, `buyerID`, `diaID`, …). The business key — not `id` — is what other tables
  join on. This is the single most important fact for [RELATIONSHIP.md](RELATIONSHIP.md).
- **Two audit-column eras.** Legacy camelCase (`insertBy`, `insertDate`, `updateBy`,
  `updateDate`, `isConfirm`) on **362** tables vs. newer Laravel-style snake_case
  (`created_at`, `updated_at`, `created_by`, `deleted_at`) on **47** tables — and the two
  sets never co-occur. This cleanly separates an older PHP core from a newer rewritten module
  and is a strong "is this table current?" signal used in [ANALYSIS.md](ANALYSIS.md).
- **Soft deletes** via `deleted_at` on 83 tables.
- **`projectID` everywhere (359 tables)** = multi-factory tenancy. Any redesign must keep it.

---

## 6. Next steps

1. [ANALYSIS.md](ANALYSIS.md) — within each domain above, separate live tables from empty /
   stale / duplicated ones.
2. [RELATIONSHIP.md](RELATIONSHIP.md) — promote the "spine" + `lib*` keys to real foreign keys.
3. [PSQL.md](PSQL.md) — port the cleaned, keyed schema to PostgreSQL.
