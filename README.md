# `ocms` Database Refactor — Findings

Analysis of the `ocms` MariaDB database (garment/knit-textile manufacturing ERP) ahead of a
PostgreSQL migration. **559 tables, ~23 M rows, zero declared foreign keys.**

Read in order:

1. **[GROUPING.md](GROUPING.md)** — clusters all 559 tables into 12 business domains and shows
   how they form one order→production→shipment pipeline. Start here.
2. **[ANALYSIS.md](ANALYSIS.md)** — what's live vs. empty/stale/duplicated; keep/archive/drop
   tiers. (~240 tables carry the live system; ~33 % can be retired before migration.)
3. **[RELATIONSHIP.md](RELATIONSHIP.md)** — recovers the implicit foreign keys (validated by
   value containment) and proposes a lossless, incremental redesign.
4. **[PSQL.md](PSQL.md)** — MariaDB→PostgreSQL migration runbook, with every concrete blocker
   found in the data (zero-dates, mixed-case names, money-as-double, …).

Supporting artifacts:
- **[_TABLE_INVENTORY.md](_TABLE_INVENTORY.md)** — full per-table listing (domain, rows, cols,
  last-data year), auto-generated.
- **[fk_detect.py](fk_detect.py)** — reproducible foreign-key discovery (rewrite of the
  original buggy `detect_relationship.py`); run from the project root to regenerate
  `relationships.json`.

### Key facts that shaped everything
- **Dual keys:** ~545 tables have both a local `id` and a *business key* (`projectID`, `jobID`,
  `buyerID`, …). FKs must target the business key, not `id`.
- **Two build eras:** legacy camelCase (`insertDate`, 362 tables) vs newer snake_case
  (`created_at`, 47 tables) — a strong "is this current?" signal.
- **`projectID` (359 tables)** = multi-factory tenancy; present in nearly everything.

> Source profiling lives in [`../db_process.py`](../db_process.py) → `schema_profile.json`.
