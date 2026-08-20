# Resources

**Named sources, mapped to the week that needs them.** Never "go read about joins". Every entry here says what exactly to read or watch, and which station it feeds.

Everything listed is free unless marked otherwise. If a link has moved, search the exact title; these are all stable, well-known sources.

---

## How to use this file

Do not read ahead. Open the row for the week you are in, use it in the study time, then do the tasks in the build time. A task done before the reading takes three times as long and teaches half as much.

If a source and this repository disagree, this repository wins. Our rules are chosen for this project's data, not for a general audience.

---

## The spine: Kudvenkat SQL Server tutorial

The SQL track follows one video series end to end, because a single consistent teacher beats ten disconnected tutorials.

**Series:** "SQL Server tutorial for beginners" by Kudvenkat (pragimtech), on YouTube. Parts are numbered, and the week files point at exact part numbers.

| Week | Station | Kudvenkat parts | Topic |
|---|---|---|---|
| 1 | S1 | 1 to 2 | Databases, tables, data types |
| 2 | S2 | 3 to 8 | Constraints, identity, unique keys |
| 2 | S3 | 9 to 13 | SELECT, GROUP BY, joins, self join |
| 3 | S4 | 14 to 16, 86 to 89 | NULL replacement, COALESCE, UNION, EXCEPT, INTERSECT |
| 3 | S5 | 21 to 28 | String, date, and math functions |
| 4 | S6 | 39 to 42, 48 to 50 | Views, CTEs, subqueries |
| 5 | S8 | 51 to 53 | Normalization, pivot |
| 6 | S9 | 107 to 117 | OVER, ROW_NUMBER, RANK, DENSE_RANK, LEAD, LAG, NTILE |
| 7 | S10 | 68 | MERGE |

**One warning.** Kudvenkat teaches SQL Server. Snowflake differs in ways that matter to us:

| Kudvenkat shows | In Snowflake |
|---|---|
| `IDENTITY` columns | Use `AUTOINCREMENT` or a sequence |
| Enforced `UNIQUE` and `CHECK` | Declared but **not enforced**. Enforce with dbt tests instead. |
| `ISNULL()` | `IFNULL()` or `COALESCE()` |
| `GETDATE()` | `CURRENT_TIMESTAMP()` |
| `TOP 10` | `LIMIT 10` |
| `MINUS` not available | `EXCEPT` and `MINUS` both work |

When the video and Snowflake disagree, run it in Snowflake and note the difference in your notes file. That difference is often exactly what a cohort review question is about.

---

## Snowflake

| Source | What exactly | Feeds |
|---|---|---|
| Snowflake Docs, "Key Concepts and Architecture" | The page on separation of storage and compute | S1, D2 |
| Snowflake Docs, "Loading Data" overview | Stages, then file formats, then `COPY INTO` | P3, D2, D3 |
| Snowflake Docs, `COPY INTO <table>` reference | The `ON_ERROR` options and the load metadata columns | P3, D3 |
| Snowflake Docs, "Understanding Snowflake Table Structures" | Just enough to know why we do not tune micro-partitions in this sprint | S1 |
| Snowflake Quickstarts, "Getting Started with Snowflake" | Do the first two sections only, in your own schema | week 1 setup |

Read the docs, not blog posts, for anything load related. Snowflake's own documentation is unusually clear and version-correct.

---

## Python

| Source | What exactly | Feeds |
|---|---|---|
| Python docs tutorial, sections 4 and 5 | Control flow, then data structures | P1 |
| Real Python, "Reading and Writing CSV Files in Python" | The `csv` module section, not the pandas section | P1 |
| Python docs, `typing` module intro | Just function annotations | P2 |
| pydantic docs, "Models" page | Model definition and validation errors | P2 |
| Real Python, "Python Exceptions" | `try`, `except`, `else`, `finally`, and why bare `except` is a bug | P4 |
| `tenacity` docs, quickstart | Retry with exponential backoff | P4 |
| Real Python, "Introduction to Python Generators" | `yield`, and why memory stays flat | P5 |
| Python docs, `logging` HOWTO | Basic configuration and levels | P6 |
| Python docs, `argparse` tutorial | Positional and optional arguments, help text | P6 |
| Real Python, "Object-Oriented Programming in Python 3" | Classes, then inheritance | P7 |
| Python docs, `abc` module | `ABC` and `abstractmethod` for the extractor base class | P7 |
| Real Python, "Getting Started With Testing in Python" | The pytest section, plus fixtures | P9 |
| Real Python, "Speed Up Your Python Program With Concurrency" | The threading section, and the GIL explanation | P10 |
| Snowflake Docs, "Python Connector" | Connecting, then executing, then closing | P11 |
| `pdfplumber` README | `extract_table` and its quirks | P7 |
| Beautiful Soup docs, quick start | Finding a table and iterating rows | P7 |

---

## dbt

| Source | What exactly | Feeds |
|---|---|---|
| dbt Docs, "About dbt projects" | The folder layout and `dbt_project.yml` | D5 |
| dbt Learn, "dbt Fundamentals" course | Free. Modules on models, sources, and tests. Skip the dbt Cloud UI parts; we use dbt Core. | D5, D7 |
| dbt Docs, "Sources" | `sources.yml`, and `{{ source() }}` | D5 |
| dbt Docs, "Add tests to your DAG" | Generic tests: unique, not_null, accepted_values, relationships | D5, D7 |
| dbt Docs, "Snapshots" | The whole page. This is SCD2 in dbt. | D7 |
| dbt Docs, "Materializations" | view, table, incremental, and when each is right | D7 |

---

## Data modelling

| Source | What exactly | Feeds |
|---|---|---|
| Kimball Group, "Dimensional Modeling Techniques" (free web article set) | Fact tables, dimension tables, and grain | S7, D6 |
| Kimball Group, "Slowly Changing Dimensions" article | Types 1, 2, and 3, and when type 2 is required | S10, D7 |
| *The Data Warehouse Toolkit*, Kimball and Ross (book, paid) | Chapter 1 and chapter 2 only. Optional, but the clearest source that exists. | S7, D6 |
| Databricks glossary, "Medallion Architecture" | The short page. Ignore the Databricks-specific parts. | D6 |
| *Fundamentals of Data Engineering*, Reis and Housley (book, paid) | Chapter 3 on the data engineering lifecycle. Optional and very good. | B1, D6 |

---

## Data quality and orchestration

| Source | What exactly | Feeds |
|---|---|---|
| Great Expectations docs, "Try GX Core" quickstart | Expectations, suites, and validation results | D8 |
| Great Expectations docs, expectation gallery | Look up `expect_column_value_lengths_to_equal` and `expect_column_values_to_be_in_set` | D8 |
| Airflow docs, "Fundamental Concepts" tutorial | DAGs, tasks, dependencies with `>>` | D9 |
| Airflow docs, "Best Practices" | The idempotency section especially | D9 |
| Metabase docs, "Asking questions" and "Dashboards" | Enough to build four views on a gold table | B6 |

---

## Git and reviewing

| Source | What exactly | Feeds |
|---|---|---|
| Pro Git, chapters 2 and 3 | Basics, then branching. Free online at `git-scm.com/book`. | week 1, all weeks |
| GitHub Docs, "Contributing to a project" | Fork, branch, pull request | week 1 |
| GitHub Docs, "About pull request reviews" | How to leave a review comment that lands on a line | B4 |
| Google's engineering practices, "How to do a code review" | The "what to look for" page | B4 |
| Chris Beams, "How to Write a Git Commit Message" | The seven rules | all weeks |

---

## The data sources themselves

Bookmark these five. You will return to them all sprint.

| Source | Where | Format | Used by |
|---|---|---|---|
| MCA company registry | `data.gov.in`, Company Master Data catalog | CSV per RoC, inside ZIP | S and D tracks |
| IBBI insolvency data | `ibbi.gov.in`, publications and statistics | PDF | P7, D3 |
| MCA CDM statistics | The MCA CDM portal pages | HTML tables | P7, D3 |
| RBI policy rates | `rbi.org.in`, database on the Indian economy | CSV or HTML | P4, D3 |
| MCA data dictionary | Published alongside the registry catalog | PDF | S1, every column decision |

Read the MCA data dictionary properly in week 1. Most week 2 and week 3 confusion about columns is answered in it.

---

## Reading for the business track

| Source | What exactly | Feeds |
|---|---|---|
| Michael Nygard, "Documenting Architecture Decisions" (blog post) | The ADR format we use | B3 |
| Google SRE Book, "Postmortem Culture: Learning from Failure" | The blameless postmortem structure | B5 |
| Any RBI or SEBI due diligence circular you can find on company verification | Skim one. It shows why the client's questions are shaped the way they are. | B1 |

---

## What not to use

**Do not use an AI assistant to produce a deliverable.** Use it to explain an error message or an unfamiliar concept, the same way you would use a search engine. If you cannot rebuild the thing from memory at the cohort review, it is not yours, and that will be obvious immediately.

**Avoid tutorials that use a toy dataset.** Our data has commas inside quoted fields, four spellings of one state, and dates in three formats. A tutorial built on a clean five-row CSV teaches habits that fail in week 3.

**Avoid Stack Overflow answers older than about 2019 for Snowflake and dbt.** Both tools changed substantially. Prefer the official docs for anything version-sensitive.
