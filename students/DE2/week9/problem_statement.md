# Week 9 Tasks

> **Before you start:** the setup steps and daily Git commands are in `docs/student-guide.md`. The client story and the four data sources are in `docs/project-brief.md`. Each task below tells you the exact file path to commit to, and that path sits inside this same week folder.

## Station P12: SCD2 Build **[MILESTONE]**

- [ ] **P12.1** Write the monthly snapshot preparation script: download the new RoC files, verify row counts against the catalog page, land them in the stage, and log a one line summary per file.
  **Commit:** `python/p12/snapshot_prep.py`, open a pull request.

- [ ] **P12.2** Run the full monthly refresh end to end on test schemas: land new files, run the silver models, run the SCD2 merge, run the quality checks. Paste the final status of every step.
  **Commit:** `python/p12/refresh_run_log.md`, update the pull request.

## Station D6: Medallion plus Kimball

- [ ] **D6.1** Write the layer contract: one short section each for bronze, silver, and gold, stating what is allowed in that layer and what is forbidden. Example: no business logic in bronze, no untyped columns in silver, no uncleaned codes in gold.
  **Commit:** `design/layer_contract.md`, open a pull request.

- [ ] **D6.2** Map every source column to its final home: which gold table and which gold column it ends in, or "dropped" with a reason. A table is expected.
  **Commit:** `design/column_mapping.md`, update the pull request.

## Station D7: dbt Marts, Gold Layer, SCD2

- [ ] **D7.1** Build dim_date as a dbt model covering every date the project needs, with columns for year, quarter, month, and week.
  **Commit:** `platform/dbt/models/marts/dim_date.sql`, open a pull request.

- [ ] **D7.2** Build dim_company as an SCD2 dbt snapshot or merge model, tracking status, capital, and address with start and end dates. Prove it works: show one company with two version rows after two monthly runs.
  **Commit:** `platform/dbt/models/marts/dim_company.sql` plus proof query results in `platform/dbt/scd2_proof.md`, update the pull request.

- [ ] **D7.3** Build fct_cirp_event joined to the company dimension by CIN, and the state context dimension from CDM data. Add relationship tests from fact to dimension.
  **Commit:** `platform/dbt/models/marts/fct_cirp_event.sql` and `platform/dbt/models/marts/dim_state.sql` plus test results, update the pull request.

## Station D8: Great Expectations

- [ ] **D8.1** Write expectation suites for the raw MCA files: CIN length, allowed status values, no fully empty rows, state names within the known list.
  **Commit:** `quality/expectations/mca_suite.json` (or the format your setup uses) plus a run report in `quality/notes.md`, open a pull request.

- [ ] **D8.2** Write the gold layer gate: every CIN in fct_cirp_event must exist in dim_company, every end date must be after its start date, no overlapping version periods per company. Run it against the built marts and paste results.
  **Commit:** `quality/expectations/gold_suite.json` plus run report, update the pull request.

- [ ] **D8.3** In three sentences, explain what Great Expectations catches that dbt tests do not, and why the project runs both.
  **Commit:** append to `quality/notes.md`, update the pull request.

