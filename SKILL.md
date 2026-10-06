---
name: data-sources-catalog
description: >-
  Search portable public data-source catalogs, series identifiers, SDMX dimensions and
  tool interfaces, including data not yet downloaded; 数据源、数据目录、有哪些数据、指标、字段、取数方法。
  Use for provider discovery and retrieval planning. Observation retrieval needs a separately
  authorized adapter and the provider's access conditions.
---

# Public data sources catalog

Use [registry.json](registry.json) for provider scope, discovery interfaces and access requirements.
Use [data-index.json](data-index.json) for public dataset/flow metadata and tool interface examples.
Start with [references/catalog.md](references/catalog.md), then query only relevant records.

Run commands from this skill directory, or invoke `scripts/lookup.py` by the path of your installation:

```sh
python scripts/lookup.py search OIS
python scripts/lookup.py show ecb-sdmx
python scripts/lookup.py data 房价 --source bis-sdmx --kind upstream_dataflow
python scripts/lookup.py data-show flow:ecb:ECB:EXR:1.0
python scripts/lookup.py tags EXR CURRENCY USD --catalog ecb-codes
python scripts/lookup.py tags FM08 Dollar --catalog boj-series
```

`data` searches contents and fields. `data-show` returns the full record and related public source.
`tags` searches bundled metadata dictionaries. All queries are offline; none executes a fetcher,
contacts an account, accesses a database or changes service configuration.

Separate provider catalogs, adapter compatibility, actual collection and archive coverage.
A returned flow or code combination does not prove observations exist or an adapter works.
Before constructing a SDMX key, use the exact flow agency/version and matching DSD dimension order.
For Census, inspect variables/groups/geography; for e-Stat, inspect table classifications; for SEC,
distinguish ticker lists, CIK submissions, taxonomy tags and company facts.

Read [references/retrieval.md](references/retrieval.md) for discovery and interpretation limits.
Keep personal deployment paths, credentials, account data and subscriptions outside this repository.
Populate your own maintaining-project and execution contract in a private deployment registry.
Do not infer private project entrypoints or call an optional paid service solely because it is listed.
Provider access conditions and data licensing remain applicable.

Update public catalogs from their declared official metadata endpoints. Preserve stable identifiers,
version/path distinctions and snapshot dates. Tool signatures are snapshots and need rechecking
against the actual connected implementation. Run `python scripts/lookup.py check` after changes,
and `render` to regenerate the public source table. This repository contains no universal fetcher.
