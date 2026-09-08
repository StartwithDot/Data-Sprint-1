# Week Map

**All thirteen weeks on one page.** Open your own `students/DEx/weekY/problem_statement.md` for the actual tasks; this file is for seeing where you are and what is coming.

---

## The shape of the sprint

| Weeks | Phase | What is happening |
|---|---|---|
| 1 to 4 | Foundations | Understand the client. Learn SQL and Python on real messy data. First load into Snowflake. The gold layer takes its first shape on paper. |
| 5 to 8 | Craft | Readable SQL, the agreed data model, real extractors, window functions, tests. |
| 9 to 11 | The platform | The cohort stops practising separately and builds the one shared pipeline: bronze, dbt staging, gold, quality gates, the monthly refresh. |
| 12 to 13 | Delivery | Orchestrate it, break it on purpose, fix it, present it, hand it over. |

---

## Where the milestones sit

```
W1        W4        W5/W7         W9/W11       W13
│         │         │             │            │
Discovery First     Star Schema   SCD2         Project
Brief     Load      Design        Build        Handover
```

Each one is a gate. If the cohort is split across a gate, new task group work pauses until the group is back together. See `docs/06-team-roles.md` for how catch-up is run.

---

## Week 1 - Understand the ask

**Task groups:** Discovery Brief `[MILESTONE]` · The Whole System on One Page · Source Summaries and the Client Ask · Databases and Tables · Python Basics: Files and Functions

**By the end of this week you can:** describe the client's real problem in writing, draw the whole system on one page, create a database, schema, and table in Snowflake, and read a CSV in Python with a function that does one job.

| Track | You produce |
|---|---|
| B | The discovery brief, the source summaries, the onboarding paragraph, and the one-page system map |
| S | `dotset_db`, a raw schema, and the first raw MCA table |
| P | A downloader and a reader script with real functions |

**Milestone:** Discovery Brief. Nobody proceeds far until the cohort agrees on what is being built.

---

## Week 2 - Trust the data, join the data

**Task groups:** Data Integrity: Constraints · Queries, Grouping and Joins · Type Hints and Data Validation

**By the end of this week you can:** find NULL and duplicate keys and say what to do about them, answer a real business question with a GROUP BY, join two sources on CIN and explain the rows that do not match, and validate a record instead of trusting it.

| Track | You produce |
|---|---|
| S | Integrity checks on CIN, status and state counts, the IBBI to MCA join and its unmatched list |
| P | Type hints across your week 1 scripts, a hand-written validator, then the same thing in pydantic |

**Watch for:** the unmatched CIN list. Everyone finds rows that do not join, and the explanation matters more than the count.

---

## Week 3 - Missing values, messy strings

**Task groups:** Missing Values and Set Operations · SQL Functions: String, Date, Math

**By the end of this week you can:** display missing values without inventing them, compare two monthly snapshots with EXCEPT and INTERSECT, and clean state names and parse dates safely.

| Track | You produce |
|---|---|
| S | The "missing stays missing" write-up, month-over-month set comparisons, cleaned states, parsed dates, recovery rates, company age |


---

## Week 4 - First load, and the design begins

**Task groups:** First Snowflake Load `[MILESTONE]` · Design Record, ERD and Architecture · Pipeline Flow Diagram

**By the end of this week you can:** load files into Snowflake with row counts that match, draw the star schema diagram with named grain, justify the modelling choices, and draw the pipeline flow a reviewer can read.

| Track | You produce |
|---|---|
| P | An internal stage, a file format, and every RoC file loaded with a reconciliation table |
| B | The ERD, the grain statements, the decision record, and the pipeline flow diagram |

**Milestone:** First Snowflake Load. Every difference between rows in the file and rows in the table is zero or explained in writing.

---

## Week 5 - Readable SQL and the agreed model

**Task groups:** Views and CTEs · Star Schema Design `[MILESTONE]` · Retry Logic and Context Managers

**By the end of this week you can:** rewrite a nested query as CTEs someone else can read, design a star schema with named grain, and write code that survives a failing network call.

| Track | You produce |
|---|---|
| S | Views, CTE rewrites, and the star schema proposal |
| P | Retry with backoff, the RBI download, and context managers so files always close |

**Milestone:** Star Schema Design. Table names, column names, and the grain of the fact table are agreed cohort-wide.

---

## Week 6 - Big files and cleaner tooling

**Task groups:** Normalization · Generators and Large Files · Logging and Command Line Tools

**By the end of this week you can:** explain why bronze is not normalized and gold is, stream a file too large for memory, and produce logs someone can debug from.

| Track | You produce |
|---|---|
| S | The normalization write-up and a pivot of company status by state |
| P | A row generator, the state frequency map that feeds silver cleaning, logging, and a CLI tool |

**Watch for:** the state frequency map. Week 10 uses it directly in the shared dbt cleaning rules.

---

## Week 7 - Extractors and the design sign-off

**Task groups:** Object Oriented Extractors · Design Review from the Python Side `[MILESTONE]` · Design Review Update

**By the end of this week you can:** pull data out of a PDF and an HTML table, refactor extractors behind one base class, and put what you learned back into the design.

| Track | You produce |
|---|---|
| P | Three extractors behind one base class, and the pipeline risk paragraph |
| B | The risk notes and the updated pipeline flow diagram with its change list |

**Milestone:** Star Schema Design sign-off from the Python side. The design must survive what the Python work says can go wrong.

---

## Week 8 - Window functions and tests

**Task groups:** Window Functions · Testing with pytest

---

## Week 9 - History that survives

**Task groups:** Slowly Changing Dimensions (SCD2) `[MILESTONE]` · Parallel Downloads · Python and Snowflake Together · Technical Brief `[MILESTONE]`

**By the end of this week you can:** detect what changed between two monthly snapshots, apply those changes with MERGE so history is kept, answer "what was this company's status on 1 March", download files in parallel, connect Python to Snowflake without a password in the code, and write the technical brief with the platform architecture diagram.

| Track | You produce |
|---|---|
| S | Change detection, the SCD2 MERGE, and a point-in-time query |
| P | Parallel downloads with before and after timings, the GIL explanation, and the load verification script |
| D | The technical brief and the platform architecture diagram |

**Milestone:** SCD2 Build. This is the client's core requirement and the hardest logic in the sprint.

---

## Week 10 - The shared platform begins

**Task groups:** Stages and File Formats · Bronze Loads · Teach-Back: the Load Path `[MILESTONE]` · dbt Staging Models

**By the end of this week you can:** set up stages and file formats for four sources, load every source into bronze with file name and load timestamp, teach the load path to a teammate, and write dbt staging models with tests.

This is the week the work moves from `students/` into `platform/`. Read `07-platform-and-cicd-guide.md` before you touch anything there.

| Track | You produce |
|---|---|
| D | Stages and formats, all bronze tables with reconciliation, the teach-back, and the dbt project with staging models and tests |

**Milestone:** First Snowflake Load teach-back. You are done when someone else can do it while you watch.

---

## Week 11 - Gold layer and the monthly refresh

**Task groups:** Layer Contracts · Gold Layer with dbt · The Monthly Refresh `[MILESTONE]`

**By the end of this week you can:** state in writing what each layer is allowed to contain, trace every source column to its home in gold, build the dimensions and the fact table, and run a full monthly refresh end to end.

| Track | You produce |
|---|---|
| D | The layer contract, the column mapping, `dim_date`, `dim_company` with SCD2 proof, `fct_cirp_event`, and `dim_state` |
| P | The monthly snapshot script and a full refresh run log |

**Milestone:** The Monthly Refresh. Show one company with two version rows after two months, with every step's status recorded.

---

## Week 12 - Orchestrate, break, fix

**Task groups:** Quality Gates with Great Expectations · Airflow Orchestration · Peer Review · Break, Fix and Postmortem

**By the end of this week you can:** stop bad data before it reaches gold, orchestrate the monthly refresh so the gate stops the pipeline before gold is touched, review someone's work usefully, find an injected failure from evidence, and write a blameless postmortem.

| Track | You produce |
|---|---|
| D | Expectation suites for raw and gold, the monthly refresh DAG with a failure run proving the gate stops it |
| B | Two real reviews, the break-fix evidence trail, and the postmortem |

---

## Week 13 - Present and hand over

**Task groups:** Dashboard · Stakeholder Delivery · Final Architecture for Handover · Project Handover `[MILESTONE]`

**By the end of this week you can:** build a dashboard a non-technical analyst can read, present with zero tool names in the script, draw the final architecture, and hand over a project that runs from a clean checkout.

| Track | You produce |
|---|---|
| B | The dashboard and its plain-language labels, the presentation script and Q&A log, the final architecture, the runbook and the final README |
| D | The clean run and the archive |

**Milestone:** Project Handover. Someone follows only the runbook, on a fresh schema, and the pipeline runs.

---

## If you fall behind

Do not skip the milestone groups, and do not skip the written explanations. They are the parts that cannot be retrofitted later.

Each week file ends with a cut list in priority order. Follow it honestly, then say in Discord what you cut. A week where you did six tasks well and said which four you dropped is worth more than a week of ten half-finished ones.


**By the end of this week you can:** rank, compare to the previous row, split into deciles, pick the latest row per key, and prove your validator works with tests that run offline in CI.

| Track | You produce |
|---|---|
| S | RANK versus DENSE_RANK, LAG month-over-month, NTILE deciles, ROW_NUMBER latest-per-company |
| P | Validator tests, a PDF-parsing fixture, and tests wired into pull requests |
