# Glossary

Every term used in Data Sprint 1, defined plainly. If a document or a task uses a word you do not know, it is here.

Terms are grouped by where you meet them. Most definitions include the tradeoff or the reason, because at the cohort review you will be asked for the reason and not the definition.

---

## The client and the data

**CIN** — Corporate Identification Number. The 21-character unique identifier the Ministry of Corporate Affairs gives every registered Indian company. It is the join key for almost everything in this project. Its length is fixed, which makes it easy to validate and a good first data quality check.

**MCA** — Ministry of Corporate Affairs. Publishes the company registry: name, CIN, incorporation date, status, registered address, authorised and paid-up capital.

**RoC** — Registrar of Companies. The regional office a company is registered with. The MCA registry is published as one file per RoC, which is why the raw layer has several MCA tables rather than one.

**IBBI** — Insolvency and Bankruptcy Board of India. Publishes insolvency case outcomes. Our copy arrives as a PDF, which is why an extractor has to be written rather than a file downloaded.

**CIRP** — Corporate Insolvency Resolution Process. The formal insolvency proceeding. In the star schema, one CIRP event is one row in the fact table.

**CDM** — Company Data Master portal. MCA's statistics pages, published as HTML tables rather than files. State-level context data comes from here.

**RBI** — Reserve Bank of India. Provides the policy rate series used as economic context.

**Paid-up capital** — The money shareholders have actually paid in, as opposed to authorised capital, which is the maximum the company is allowed to raise. Frequently blank in the registry, which is what makes it a good NULL-handling exercise.

**Company status** — The registry's state for a company: Active, Strike Off, Under Liquidation, Amalgamated, and others. Status changes over time, which is the reason the project needs history tracking at all.

**Due diligence** — Checking that a company is real, active, and not in trouble before lending to it or buying it. That is our client's job, and the reason this platform exists.

---

## Warehouse basics

**Data warehouse** — A database built for analysis rather than for running an application. Optimised for scanning millions of rows to answer a question, not for updating one row quickly.

**Snowflake** — The cloud data warehouse this sprint uses. Storage and compute are separate, which is why a warehouse can be suspended without losing data.

**Warehouse (in Snowflake)** — The compute, not the storage. It costs money while it is running, which is why it auto-suspends and why exploratory queries use `LIMIT`.

**Database, schema, table** — Three levels of naming. The database holds schemas, a schema holds tables. We use schemas to separate the layers: raw, staging, marts.

**Stage** — A named location Snowflake can read files from before they become table rows. An internal stage lives inside Snowflake; an external stage points at cloud storage.

**File format (object)** — A saved set of parsing rules: the delimiter, whether to skip a header, how quotes are handled, what counts as NULL. Defining it once as an object means every load parses the same way.

**COPY INTO** — The Snowflake command that loads staged files into a table. The row count it reports must match the row count in the file, and reconciling those two numbers is the point of the First Snowflake Load milestone.

**PUT** — The command that uploads a local file to an internal stage. `PUT` then `COPY INTO` is the two-step path from your laptop to a table.

**Idempotent** — Running something twice leaves the same result as running it once. A load script that duplicates rows on a second run is not idempotent, and every pipeline in this project is required to be.

---

## SQL and modelling

**DDL and DML** — DDL creates and alters structure: `CREATE`, `ALTER`, `DROP`. DML changes data: `INSERT`, `UPDATE`, `DELETE`, `MERGE`.

**Primary key** — The column that uniquely identifies a row. Snowflake accepts the declaration but does not enforce it, which is why uniqueness in this project is enforced with tests rather than with constraints.

**Constraint** — A rule the database enforces: NOT NULL, UNIQUE, CHECK, FOREIGN KEY. In Snowflake only NOT NULL is enforced. This surprises people, and station S2 exists so the surprise happens early.

**NULL** — Unknown, not zero and not empty string. `NULL = NULL` is not true, which is why `IS NULL` exists. Writing zero where the value is unknown is the mistake station S4 is designed to prevent.

**COALESCE** — Returns the first non-NULL argument. Used for display, so a report can show "Not reported" without changing the stored value.

**JOIN types** — `INNER` keeps only matching rows. `LEFT` keeps all rows from the left side. In this project the rows that do *not* match are usually the interesting finding, which is why left joins and unmatched lists appear so often.

**UNION versus UNION ALL** — `UNION` removes duplicate rows and therefore costs a sort. `UNION ALL` keeps everything and is faster. If the counts differ, you have just discovered duplicates.

**EXCEPT / MINUS and INTERSECT** — Set difference and set overlap. Comparing this month's snapshot to last month's is exactly a set difference, which is how disappeared CINs are found.

**CTE (Common Table Expression)** — A named result defined with `WITH` at the top of a query. Same result as a nested subquery, far easier for a reviewer to read, which is the whole point of station S6.

**View** — A saved query that behaves like a table. Nothing is stored; it runs each time it is used.

**Window function** — A function that computes across a set of rows related to the current row, without collapsing them into one row like `GROUP BY` does. `OVER (PARTITION BY ... ORDER BY ...)` defines the window.

**RANK versus DENSE_RANK versus ROW_NUMBER** — On a tie, `RANK` skips numbers (1, 2, 2, 4), `DENSE_RANK` does not (1, 2, 2, 3), and `ROW_NUMBER` never ties (1, 2, 3, 4). Picking the latest row per company needs `ROW_NUMBER`, because it must return exactly one row.

**LAG and LEAD** — The previous and next row's value in the window. Month-over-month change is `LAG`.

**NTILE** — Splits rows into a stated number of buckets. `NTILE(10)` gives deciles.

**MERGE (upsert)** — One statement that inserts rows that are new, updates rows that changed, and leaves the rest alone. It is how a monthly snapshot is applied without wiping history.

**Normalization** — Structuring tables so each fact is stored once. Excellent for systems that write data, awkward for analysis because answering a question requires many joins.

**Denormalization** — Deliberately repeating data so queries are simpler and faster. The gold layer is denormalized on purpose.

**Grain** — What one row of a table represents. "One CIRP event per company per filing date" is a grain. Naming the grain is the first thing to agree in a star schema, and the most common thing to get wrong.

---

## Pipeline architecture

**Medallion architecture** — Three layers, each with a job.

* **Bronze (raw)** — Exactly what arrived, all columns as text, plus the file name and load timestamp. Nothing is cleaned. If bronze is wrong, the source file is wrong.
* **Silver (staging)** — Typed, cleaned, deduplicated. State names standardised, dates parsed, bad CINs flagged. Business meaning is not applied yet.
* **Gold (marts)** — The tables the dashboard uses. Denormalized star schema, business logic applied, tested.

The tradeoff: three copies of the data cost more storage, and buy the ability to find out *where* a wrong number came from.

**Why bronze columns are VARCHAR** — A typed column rejects the whole file when one row has a bad date. Losing a file is worse than storing a bad value you can find and fix later.

**Star schema (Kimball)** — One central fact table of events surrounded by dimension tables describing the things involved. Named after its shape on a diagram.

**Fact table** — The events. Numeric and countable, one row per occurrence. `fct_cirp_event` is one row per insolvency event.

**Dimension table** — The context. Who, what, where, when. `dim_company`, `dim_state`, `dim_date`.

**Surrogate key** — A meaningless key generated by us, used instead of the natural business key. Needed with SCD2, because CIN is no longer unique once one company has several version rows.

**SCD2 (Slowly Changing Dimension type 2)** — Instead of overwriting a changed value, close the old row with an end date and insert a new row with a start date. That is what lets the client ask "what was this company's status on 1 March" and get the right answer instead of today's answer. It is also the hardest logic in this sprint.

**Point-in-time query** — A query that filters SCD2 rows by a date between start and end, returning the value as it was on that date.

**Data lineage** — The traceable path from a number on a dashboard back to the source file and row it came from. The reason bronze keeps the file name and load timestamp.

**Reconciliation** — Proving rows in the file equal rows in the table. Every difference is zero or has a written explanation. No exceptions.

---

## Tools

**Git** — Version control. Tracks every change, and records who made it.

**Fork** — Your own copy of the class repository on GitHub. You push to your fork, never directly to the class repository.

**Clone** — A local copy of a repository on your machine.

**`origin` and `upstream`** — `origin` is your fork. `upstream` is the class repository you pull updates from.

**Branch** — A named line of work. One branch per task keeps a pull request small enough to actually review.

**Commit** — One recorded change with a message. In this sprint, one task equals one commit, and the message starts with the task ID.

**Pull request (PR)** — A request to merge your branch into the class repository. Where review happens.

**Squash merge** — Collapsing all commits in a PR into one. **We never use it here**, because it erases individual authorship, and the authorship record is part of what you are building.

**Merge conflict** — Two people changed the same lines. Git stops and asks you to decide. Resolution steps are in `10-troubleshooting.md`.

**dbt** — A tool for writing transformations as SQL `SELECT` statements, which it turns into tables and views, with tests and dependency ordering. Replaces hand-maintained scripts that nobody can run in the right order.

**dbt model** — One `.sql` file containing one `SELECT`. dbt handles the `CREATE` and the ordering.

**dbt test** — A declared expectation, such as unique or not null on a column, or a relationship from a fact to a dimension. Runs with `dbt test`.

**Great Expectations** — A data validation tool. Checks the *content* of the data against declared expectations, such as "CIN is 21 characters" or "state is in this list", and can stop the pipeline before bad data reaches gold.

**Airflow** — Orchestration. Runs pipeline steps in the right order, on a schedule, with retries, and shows you where it failed. A DAG is one pipeline definition.

**DAG** — Directed Acyclic Graph. The dependency graph of pipeline steps: this before that, and no loops.

**Metabase** — The dashboard tool. Points at the gold layer, which is the only layer non-technical users should ever see.

**CI (Continuous Integration)** — Automated checks that run on every pull request. In this repository they lint SQL, lint Python, run tests, and compile dbt.

**Linter** — A tool that checks style and obvious errors. SQLFluff for SQL, flake8 for Python. Configured in `.sqlfluff` and `.flake8`.

---

## How we work

**Station** — A small group of related tasks with one theme, for example `Station S3: SELECT, GROUP BY, Joins`.

**Milestone station** — A checkpoint the whole cohort must reach before anyone moves far past it, because later work depends on a shared decision. Marked `[MILESTONE]`.

**Track** — One of the four skill lines: B business and delivery, S SQL and modelling, P Python, D data platform.

**Practice zone** — `students/DEx/weekY/`. Your own folder. Everyone does every task here.

**Shared zone** — `platform/` and `delivery/`. The one real pipeline. Only that week's platform rotation writes here.

**Platform rotation** — The small group with write access to the shared zone for a week. Rotates so everyone gets a turn, logged in `platform-rotation-log.md`.

**Review lead** — The person responsible for reviewing pull requests in a given week. Rotates.

**ADR (Architecture Decision Record)** — A short written record of a decision: what was chosen, what was rejected, and why. Written for the decision a client would question.

**Postmortem** — A written account after a failure: what broke, why, how it was found, what was done, and what change stops it recurring. Blames the system, not the person.

**Runbook** — Operating instructions for the finished platform: how to refresh each source, what to check when a run fails, who to contact. Judged by whether a stranger can run the pipeline using only the runbook.

**Teach-back** — Explaining a thing you just learned to a teammate while they do it themselves. Used at station D4, because being able to do something and being able to explain it are different skills.
