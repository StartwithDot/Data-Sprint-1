# Week Map

**All ten weeks on one page.** Open your own `students/DEx/weekY/problem_statement.md` for the actual tasks; this file is for seeing where you are and what is coming.

---

## The shape of the sprint

| Weeks | Phase | What is happening |
|---|---|---|
| 1 to 3 | Foundations | Understand the client. Learn SQL and Python on real messy data. First load into Snowflake. |
| 4 to 7 | Craft | Readable SQL, the agreed data model, real extractors, window functions, tests, history that survives a refresh. |
| 8 to 9 | The platform | The cohort stops practising separately and builds the one shared pipeline: bronze, dbt staging, gold, quality gates. |
| 10 | Delivery | Orchestrate it, break it on purpose, fix it, present it, hand it over. |

---

## Week 1 — Understand the ask

**Stations:** B1 Discovery Brief `[MILESTONE]` · B2 Working Agreement · S1 Databases and Tables · P1 Files and Functions

**By the end of this week you can:** describe the client's real problem in writing, create a database, schema, and table in Snowflake, and read a CSV in Python with a function that does one job.

| Track | You produce |
|---|---|
| B | The discovery brief and the team working agreement |
| S | `dotset_db`, a raw schema, and the first raw MCA table |
| P | A downloader and a reader script with real functions |

**Milestone:** Discovery Brief. Nobody proceeds far until the cohort agrees on what is being built.

---

## Week 2 — Trust the data, join the data

**Stations:** S2 Constraints and Data Integrity · S3 SELECT, GROUP BY, Joins · P2 Type Hints and Data Validation

**By the end of this week you can:** find NULL and duplicate keys and say what to do about them, answer a real business question with a GROUP BY, join two sources on CIN and explain the rows that do not match, and validate a record instead of trusting it.

| Track | You produce |
|---|---|
| S | Integrity checks on CIN, status and state counts, the IBBI to MCA join and its unmatched list |
| P | Type hints across your week 1 scripts, a hand-written validator, then the same thing in pydantic |

**Watch for:** the unmatched CIN list. Everyone finds rows that do not join, and the explanation matters more than the count.

---

## Week 3 — Missing values, messy strings, first load

**Stations:** S4 NULL Handling and Set Operations · S5 Functions · P3 First Snowflake Load `[MILESTONE]`

**By the end of this week you can:** display missing values without inventing them, compare two monthly snapshots with EXCEPT and INTERSECT, clean state names and parse dates safely, and load a file into Snowflake with row counts that match.

| Track | You produce |
|---|---|
| S | The "missing stays missing" write-up, month-over-month set comparisons, cleaned states, parsed dates, recovery rates, company age |
| P | An internal stage, a file format, and every RoC file loaded with a reconciliation table |

**Milestone:** First Snowflake Load. Every difference between rows in the file and rows in the table is zero or explained in writing.

---

## Week 4 — Readable SQL and the agreed model

**Stations:** B3 Design Record, ERD and Architecture · S6 Views and CTEs · S7 Star Schema Design `[MILESTONE]` · P4 Retry Logic and Context Managers

**By the end of this week you can:** rewrite a nested query as CTEs someone else can read, design a star schema with named grain, and write code that survives a failing network call.

| Track | You produce |
|---|---|
| B | The ERD, the grain statements, and the design record for choices the client would question |
| S | Views, CTE rewrites, and the star schema proposal |
| P | Retry with backoff, the RBI download, and context managers so files always close |

**Milestone:** Star Schema Design. Table names, column names, and the grain of the fact table are agreed cohort-wide.

---

## Week 5 — Big files and real extractors

**Stations:** S8 Normalization and Star Schema · P5 Generators · P6 Logging and CLI · P7 OOP and Custom Extractors

**By the end of this week you can:** explain why bronze is not normalized and gold is, stream a file too large for memory, produce logs someone can debug from, and pull data out of a PDF and an HTML table.

| Track | You produce |
|---|---|
| S | The normalization write-up and a pivot of company status by state |
| P | A row generator, the state frequency map that feeds silver cleaning, logging, a CLI tool, and three extractors behind one base class |

**Watch for:** the state frequency map. Weeks 8 and 9 use it directly.

---

## Week 6 — Window functions and tests

**Stations:** S9 Window Functions · P8 Star Schema Design `[MILESTONE]` · P9 Testing with pytest

**By the end of this week you can:** rank, compare to the previous row, split into deciles, pick the latest row per key, and prove your validator works with tests that run offline in CI.

| Track | You produce |
|---|---|
| S | RANK versus DENSE_RANK, LAG month-over-month, NTILE deciles, ROW_NUMBER latest-per-company |
| P | The pipeline risk paragraph for the design review, pytest tests, a PDF-parsing fixture, and tests wired into pull requests |

**Milestone:** Star Schema Design sign-off from the Python side. The design must survive what the Python work says can go wrong.

---

## Week 7 — History that survives

**Stations:** S10 MERGE and SCD2 Build `[MILESTONE]` · P10 Concurrency · P11 Snowflake Python Connector

**By the end of this week you can:** detect what changed between two monthly snapshots, apply those changes with MERGE so history is kept, answer "what was this company's status on 1 March", download files in parallel, and connect Python to Snowflake without a password in the code.

| Track | You produce |
|---|---|
| S | Change detection, the SCD2 MERGE, and a point-in-time query |
| P | Parallel downloads with before and after timings, the GIL explanation, and the load verification script that becomes a pipeline gate |

**Milestone:** SCD2 Build. This is the client's core requirement and the hardest logic in the sprint.

---

## Week 8 — The shared platform begins

**Stations:** D1 Discovery Brief `[MILESTONE]` · D2 Snowflake Fundamentals and Stages · D3 Raw Layer Load · D4 First Snowflake Load `[MILESTONE]` · D5 dbt Staging Models

**By the end of this week you can:** write the technical half of a discovery brief, set up stages and file formats for four sources, load every source into bronze with file name and load timestamp, teach the load path to a teammate, and write dbt staging models with tests.

This is the week the work moves from `students/` into `platform/`. Read `07-platform-and-cicd-guide.md` before you touch anything there.

| Track | You produce |
|---|---|
| D | The technical brief, stages and formats, all bronze tables with reconciliation, the teach-back, and the dbt project with staging models and tests |

---

## Week 9 — Gold layer and quality gates

**Stations:** P12 SCD2 Build `[MILESTONE]` · D6 Medallion plus Kimball · D7 dbt Marts and SCD2 · D8 Great Expectations

**By the end of this week you can:** run a full monthly refresh end to end, state in writing what each layer is allowed to contain, trace every source column to its home in gold, build the dimensions and the fact table, and stop bad data before it reaches gold.

| Track | You produce |
|---|---|
| P | The monthly snapshot script and a full refresh run log |
| D | The layer contract, the column mapping, `dim_date`, `dim_company` with SCD2 proof, `fct_cirp_event`, and expectation suites for raw and gold |

**Milestone:** SCD2 Build in dbt. Show one company with two version rows after two months.

---

## Week 10 — Orchestrate, break, fix, hand over

**Stations:** B4 Build and Peer Review · B5 Break and Fix · B6 Metabase Dashboard · B7 Stakeholder Delivery · B8 Project Handover `[MILESTONE]` · D9 Airflow Orchestration · D10 Project Handover `[MILESTONE]`

**By the end of this week you can:** review someone's work usefully, find an injected failure from evidence, write a postmortem, build a dashboard a non-technical analyst can read, present with zero tool names in the script, and hand over a project that runs from a clean checkout.

| Track | You produce |
|---|---|
| B | Two real reviews, the break-fix evidence trail, the postmortem, the dashboard and its plain-language labels, the presentation script and Q&A log, the runbook and the final README |
| D | The monthly refresh DAG with correct dependencies and a quality gate that stops the pipeline before gold, then the clean run and the archive |

**Milestone:** Project Handover. Someone follows only the runbook, on a fresh schema, and the pipeline runs.

---

## Where the milestones sit

```
W1        W3        W4/W6         W7/W9        W10
│         │         │             │            │
Discovery First     Star Schema   SCD2         Project
Brief     Load      Design        Build        Handover
```

Each one is a gate. If the cohort is split across a gate, new station work pauses until the group is back together. See `06-team-roles.md` for how catch-up is run.

---

## If you fall behind

Do not skip the milestone stations, and do not skip the written explanations. They are the parts that cannot be retrofitted later.

Each week file ends with a cut list in priority order. Follow it honestly, then say in Discord what you cut. A week where you did six tasks well and said which four you dropped is worth more than a week of ten half-finished ones.
