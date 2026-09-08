# Week 11 - Gold layer and the monthly refresh

**Data Sprint 1 · Week 11 of 13 · Theme: build the tables the client actually uses, then run the refresh that keeps them honest**

Read this whole file before you start. Then work through the task groups in order.

---

## Before you start

Platform rules before you touch `platform/` or `quality/`: `docs/07-platform-and-cicd-guide.md` and `docs/06-team-roles.md`. Git commands: `docs/03-student-guide.md`. Unknown word: `docs/08-glossary.md`. Broken tool: `docs/10-troubleshooting.md`. What a tool is for: `docs/11-tools-and-technology.md`.

---

## By the end of this week you can

- State, in writing, what each layer is allowed to do and what it is forbidden to do
- Trace every source column to its final home, or say why it was dropped
- Build dim_date, an SCD2 dim_company, and a fact table with relationship tests
- Run a monthly refresh end to end and show the status of every step

## The milestone this week

**P12 The Monthly Refresh, end to end.** Not the query from week 9, but the whole monthly refresh: new files land, silver runs, the merge applies, quality checks pass. One run, every step's status recorded.

---

## The week at a glance

| Step | LEARN | DO |
|---|---|---|
| **1** | Kimball on conformed dimensions · your own week 5 grain statements | Tasks 1–2 - layer contract, column mapping |
| **2** | dbt docs "Snapshots" | Tasks 3–4 - dim_date, SCD2 dim_company |
| **3** | dbt docs "Tests", relationship tests | Task 5 - the fact table and dim_state |
| **4** | - | Tasks 6–7 - snapshot prep, full refresh |
| **5** | - | Cohort review: SCD2 proof, refresh run log |

---

## 1 · Layer Contracts

- [ ] **Task 1 - Write the layer contract** (ID `D6.1`): Write the layer contract: one short section each for bronze, silver, and gold, stating what is allowed in that layer and what is forbidden. Example: no business logic in bronze, no untyped columns in silver, no uncleaned codes in gold.
  **Commit:** `design/layer_contract.md`, open a pull request.

- [ ] **Task 2 - Map every source column** (ID `D6.2`): Map every source column to its final home: which gold table and which gold column it ends in, or "dropped" with a reason. A table is expected.
  **Commit:** `design/column_mapping.md`, update the pull request.

**On Task 2:** "dropped" needs a reason, and the reason is the useful part. Six months from now, when a client asks why a column is missing from the dashboard, this file is the answer.


---

## 2 · Gold Layer with dbt

- [ ] **Task 3 - Build dim_date** (ID `D7.1`): Build dim_date as a dbt model covering every date the project needs, with columns for year, quarter, month, and week.
  **Commit:** `platform/dbt/models/marts/dim_date.sql`, open a pull request.

- [ ] **Task 4 - Build SCD2 dim_company** (ID `D7.2`): Build dim_company as an SCD2 dbt snapshot or merge model, tracking status, capital, and address with start and end dates. Prove it works: show one company with two version rows after two monthly runs.
  **Commit:** `platform/dbt/models/marts/dim_company.sql` plus proof query results in `platform/dbt/scd2_proof.md`, update the pull request.

- [ ] **Task 5 - Build the fact table and dim_state** (ID `D7.3`): Build fct_cirp_event joined to the company dimension by CIN, and the state context dimension from CDM data. Add relationship tests from fact to dimension.
  **Commit:** `platform/dbt/models/marts/fct_cirp_event.sql` and `platform/dbt/models/marts/dim_state.sql` plus test results, update the pull request.

**On Task 3:** dim_date must cover the full range of every source, including future dates the fact table can reach. A fact row with a date that has no dimension row is a broken join, discovered late.

**On Task 5:** the relationship test will fail, because week 2 already told you some insolvency CINs are not in the registry. That is a real finding, not a bug in your model. Decide what the gold layer does with those rows and write the decision down.

---

## 3 · The Monthly Refresh **[MILESTONE]**

- [ ] **Task 6 - Write the snapshot preparation script** (ID `P12.1`): Write the monthly snapshot preparation script: download the new RoC files, verify row counts against the catalog page, land them in the stage, and log a one line summary per file.
  **Commit:** `python/p12/snapshot_prep.py`, open a pull request.

- [ ] **Task 7 - Run the full refresh** (ID `P12.2`): Run the full monthly refresh end to end on test schemas: land new files, run the silver models, run the SCD2 merge, run the quality checks. Paste the final status of every step.
  **Commit:** `python/p12/refresh_run_log.md`, update the pull request.

**On Task 7:** test schemas, not the shared ones. A failed step is a fine result as long as the log says which step failed and why. A run log that only says "success" tells the reader nothing.

---

## End of week checklist

- [ ] Tasks 1–2 - layer contract with forbidden lists, and a complete column map with reasons for drops
- [ ] Tasks 3–5 - dim_date, dim_company with two-version proof, fact plus dim_state with relationship tests
- [ ] Tasks 6–7 - snapshot prep script and a full refresh run log with per-step status
- [ ] Every dbt run has its results pasted, including failures
- [ ] If you were on the platform rotation, your entry in `docs/platform-rotation-log.md` is updated

**If you are short on time, cut in this order:** Task 2 (D6.2), then Task 7 (P12.2) polish. Never cut Task 4 (D7.2). The SCD2 dimension is what the client asked for.

Next: `week12/problem_statement.md`.
