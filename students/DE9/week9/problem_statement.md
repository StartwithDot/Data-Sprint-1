# Week 9 — Gold, and the gate in front of it

**Data Sprint 1 · Week 9 of 10 · Theme: build the tables the client actually uses, and refuse to publish them when they are wrong**

Read this whole file before you start. Then work through the stations in order.

---

## Before you start

Platform rules before you touch `platform/` or `quality/`: `docs/07-platform-and-cicd-guide.md` and `docs/06-team-roles.md`. Git commands: `docs/03-student-guide.md`. Unknown word: `docs/08-glossary.md`. Broken tool: `docs/10-troubleshooting.md`.

---

## By the end of this week you can

- State, in writing, what each layer is allowed to do and what it is forbidden to do
- Trace every source column to its final home, or say why it was dropped
- Build dim_date, an SCD2 dim_company, and a fact table with relationship tests
- Run a monthly refresh end to end and show the status of every step
- Write a quality gate that stops bad data before it reaches gold

## The milestone this week

**P12 SCD2 Build, end to end.** Not the query from week 7, but the whole monthly refresh: new files land, silver runs, the merge applies, quality checks pass. One run, every step's status recorded.

---

## The week at a glance

| Step | LEARN | DO |
|---|---|---|
| **1** | Kimball on conformed dimensions · your own week 4 grain statements | D6.1 D6.2 — layer contract, column mapping |
| **2** | dbt docs "Snapshots" | D7.1 D7.2 — dim_date, SCD2 dim_company |
| **3** | dbt docs "Tests", relationship tests | D7.3 — the fact table and dim_state |
| **4** | Great Expectations "Getting Started" | D8.1 D8.2 — raw suite, gold gate |
| **5** | — | D8.3 P12.1 P12.2 — GE vs dbt, snapshot prep, full refresh |
| **6** | — | Cohort review: SCD2 proof, gold gate results |

---

## Station P12: SCD2 Build **[MILESTONE]**

- [ ] **P12.1** Write the monthly snapshot preparation script: download the new RoC files, verify row counts against the catalog page, land them in the stage, and log a one line summary per file.
  **Commit:** `python/p12/snapshot_prep.py`, open a pull request.

- [ ] **P12.2** Run the full monthly refresh end to end on test schemas: land new files, run the silver models, run the SCD2 merge, run the quality checks. Paste the final status of every step.
  **Commit:** `python/p12/refresh_run_log.md`, update the pull request.

**On P12.2:** test schemas, not the shared ones. A failed step is a fine result as long as the log says which step failed and why. A run log that only says "success" tells the reader nothing.

---

## Station D6: Medallion plus Kimball

- [ ] **D6.1** Write the layer contract: one short section each for bronze, silver, and gold, stating what is allowed in that layer and what is forbidden. Example: no business logic in bronze, no untyped columns in silver, no uncleaned codes in gold.
  **Commit:** `design/layer_contract.md`, open a pull request.

- [ ] **D6.2** Map every source column to its final home: which gold table and which gold column it ends in, or "dropped" with a reason. A table is expected.
  **Commit:** `design/column_mapping.md`, update the pull request.

**On D6.2:** "dropped" needs a reason, and the reason is the useful part. Six months from now, when a client asks why a column is missing from the dashboard, this file is the answer.

---

## Station D7: dbt Marts, Gold Layer, SCD2

- [ ] **D7.1** Build dim_date as a dbt model covering every date the project needs, with columns for year, quarter, month, and week.
  **Commit:** `platform/dbt/models/marts/dim_date.sql`, open a pull request.

- [ ] **D7.2** Build dim_company as an SCD2 dbt snapshot or merge model, tracking status, capital, and address with start and end dates. Prove it works: show one company with two version rows after two monthly runs.
  **Commit:** `platform/dbt/models/marts/dim_company.sql` plus proof query results in `platform/dbt/scd2_proof.md`, update the pull request.

- [ ] **D7.3** Build fct_cirp_event joined to the company dimension by CIN, and the state context dimension from CDM data. Add relationship tests from fact to dimension.
  **Commit:** `platform/dbt/models/marts/fct_cirp_event.sql` and `platform/dbt/models/marts/dim_state.sql` plus test results, update the pull request.

**On D7.1:** dim_date must cover the full range of every source, including future dates the fact table can reach. A fact row with a date that has no dimension row is a broken join, discovered late.

**On D7.3:** the relationship test will fail, because week 2 already told you some insolvency CINs are not in the registry. That is a real finding, not a bug in your model. Decide what the gold layer does with those rows and write the decision down.

---

## Station D8: Great Expectations

- [ ] **D8.1** Write expectation suites for the raw MCA files: CIN length, allowed status values, no fully empty rows, state names within the known list.
  **Commit:** `quality/expectations/mca_suite.json` (or the format your setup uses) plus a run report in `quality/notes.md`, open a pull request.

- [ ] **D8.2** Write the gold layer gate: every CIN in fct_cirp_event must exist in dim_company, every end date must be after its start date, no overlapping version periods per company. Run it against the built marts and paste results.
  **Commit:** `quality/expectations/gold_suite.json` plus run report, update the pull request.

- [ ] **D8.3** In three sentences, explain what Great Expectations catches that dbt tests do not, and why the project runs both.
  **Commit:** append to `quality/notes.md`, update the pull request.

**On D8.2:** the three checks are exactly the SCD2 correctness checks from week 7, now automated. That is the point: a rule you had to remember to run by hand is a rule that eventually does not get run.

**When an expectation fails, fix the data or the rule, never the threshold.** Loosening a check until it passes is the failure mode this station exists to teach you to avoid.

---

## End of week checklist

- [ ] P12.1, P12.2 — snapshot prep script and a full refresh run log with per-step status
- [ ] D6.1, D6.2 — layer contract with forbidden lists, and a complete column map with reasons for drops
- [ ] D7.1, D7.2, D7.3 — dim_date, dim_company with two-version proof, fact plus dim_state with relationship tests
- [ ] D8.1, D8.2, D8.3 — raw suite, gold gate with the three SCD2 checks, and the GE versus dbt answer
- [ ] Every dbt and GE run has its results pasted, including failures
- [ ] If you were on the platform rotation, your entry in `docs/platform-rotation-log.md` is updated

**If you are short on time, cut in this order:** D8.1, then D6.2. Never cut D7.2 or D8.2. The SCD2 dimension is what the client asked for, and the gate is what stops it shipping wrong.

Next: `week10/problem_statement.md`.
