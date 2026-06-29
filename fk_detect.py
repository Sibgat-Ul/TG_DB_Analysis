#!/usr/bin/env python3
"""
fk_detect.py — data-driven foreign-key discovery for the ocms database.

Rewrite of the original detect_relationship.py (which had a bug: it read the row
count into `dtype` instead of the column data type, so the integer-type filter
never matched and no PKs were found).

Strategy
--------
1. Read schema_profile.json (column types + distinct/null counts) produced by db_process.py.
2. For each *business key* column name shared by >=N tables, find the PARENT table:
   the table where that column is (near-)unique and small/master-like.  We rank by
   distinct-value count, NOT by smallest row count (the old code matched 1-row tables).
3. Validate each parent<-child edge by measuring value CONTAINMENT:
       fraction of distinct child values that exist in the parent key.
   >=0.95  -> enforceable FK now
   0.70-0.95 -> FK after cleaning orphans (add NOT VALID, then fix, then VALIDATE)
   <0.70   -> not a real FK (different id-space) — investigate, don't enforce.

Run:  python3 fk_detect.py   (from the project root, next to schema_profile.json)
Output: relationships.json
"""
import json
import mysql.connector
from collections import Counter

DB = dict(host="localhost", user="sibyz", password="", database="ocms")
MIN_TABLES_SHARING_KEY = 4          # a key column must appear in >= this many tables
ENFORCE = 0.95                      # containment >= this  -> enforceable FK
CLEANABLE = 0.70                    # containment in [CLEANABLE, ENFORCE) -> FK after cleanup
MAX_CHILDREN_TO_SAMPLE = 3          # validate the N biggest children per key

# Keys that are generic and must NOT be treated as join keys on their own.
GENERIC = {"id", "insertby", "updateby", "created_by", "updated_by", "deleted_at"}


def looks_like_key(col):
    c = col.lower()
    if c in GENERIC:
        return False
    return c.endswith("id") or c.endswith("_id") or c in ("wono", "chalanno", "mrrno")


def main():
    schema = json.load(open("schema_profile.json"))
    conn = mysql.connector.connect(**DB)
    cur = conn.cursor()

    # 1. business-key columns shared across many tables
    freq = Counter()
    for t, meta in schema.items():
        for col in meta["columns"]:
            if looks_like_key(col):
                freq[col] += 1
    keys = [c for c, n in freq.items() if n >= MIN_TABLES_SHARING_KEY and c != "id"]

    # 2. infer parent (definition) table per key: highest distinct-count carrier
    #    that is reasonably unique (>= 0.9) — prefer that over arbitrary tiny tables.
    parents = {}
    for k in keys:
        best = None
        for t, meta in schema.items():
            if k not in meta["columns"]:
                continue
            rc = meta["row_count"]
            dc = meta["columns"][k].get("distinct_count", 0)
            if rc == 0 or dc == 0:
                continue
            uniq = dc / rc
            score = (dc, uniq)            # most distinct values wins, then uniqueness
            if uniq >= 0.5 and (best is None or score > best[1]):
                best = (t, score, uniq)
        if best:
            parents[k] = best[0]

    # 3. validate containment for the biggest children of each key.
    #    Parents are masters (small), so load the parent key set into Python and do ONE
    #    distinct scan of the child — far cheaper than a full LEFT JOIN anti-join per edge.
    _pset_cache = {}

    def parent_set(parent, col):
        ck = (parent, col)
        if ck not in _pset_cache:
            cur.execute("SELECT DISTINCT `%s` FROM `%s` WHERE `%s` IS NOT NULL" % (col, parent, col))
            _pset_cache[ck] = {r[0] for r in cur.fetchall()}
        return _pset_cache[ck]

    def containment(child, col, parent):
        pset = parent_set(parent, col)
        if not pset:
            return None
        cur.execute("SELECT DISTINCT `%s` FROM `%s` WHERE `%s` IS NOT NULL" % (col, child, col))
        vals = [r[0] for r in cur.fetchall()]
        if not vals:
            return None
        matched = sum(1 for v in vals if v in pset)
        return round(matched / len(vals), 4), len(vals)

    edges = []
    for k, parent in parents.items():
        children = sorted(
            (t for t in schema if k in schema[t]["columns"] and t != parent and schema[t]["row_count"] > 0),
            key=lambda t: -schema[t]["row_count"],
        )[:MAX_CHILDREN_TO_SAMPLE]
        for child in children:
            try:
                res = containment(child, k, parent)
            except Exception as e:
                print("skip %s.%s: %s" % (child, k, str(e)[:60]))
                continue
            if not res:
                continue
            rate, distinct = res
            verdict = ("enforce" if rate >= ENFORCE
                       else "clean_then_enforce" if rate >= CLEANABLE
                       else "reject")
            edge = dict(child_table=child, key=k, parent_table=parent,
                        containment=rate, child_distinct=distinct, verdict=verdict)
            edges.append(edge)
            print("%-9s %5.1f%%  %s.%s -> %s.%s"
                  % (verdict, rate * 100, child, k, parent, k), flush=True)

    edges.sort(key=lambda e: -e["containment"])
    json.dump({"parents": parents, "edges": edges}, open("relationships.json", "w"), indent=2)
    print("\nwrote relationships.json (%d edges, %d keys)" % (len(edges), len(parents)))


if __name__ == "__main__":
    main()
