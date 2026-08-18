# Week 10 Tasks

> **Before you start:** the setup steps and daily Git commands are in `docs/student-guide.md`. The client story and the four data sources are in `docs/project-brief.md`. Each task below tells you the exact file path to commit to, and that path sits inside this same week folder.

## Station B4: Build, PR and Peer Review

- [ ] **B4.1** Review two pull requests from teammates. For each, leave at least one real comment: a question, a spotted mistake, or a suggested improvement. No "looks good" reviews.
  **Commit:** nothing new; paste the links to your two reviewed pull requests in `delivery/review_log.md` and open a pull request with that file.

- [ ] **B4.2** Fix one piece of review feedback you received on your own work, and reply to the reviewer explaining what you changed.
  **Commit:** the fix in its original folder, reference the original pull request in your new commit message.

## Station B5: Break and Fix, Postmortem

- [ ] **B5.1** The program leads will introduce a failure into the project data or pipeline. Find what broke, using logs, tests, and row counts. Write down the evidence trail that led you to the cause.
  **Commit:** `delivery/break_fix_notes.md`, open a pull request.

- [ ] **B5.2** Write a one page postmortem: what broke, why it happened, how it was found, what was done to fix it, and what one change would stop it from happening again.
  **Commit:** `delivery/postmortem.md`, open a pull request.

## Station B6: Metabase Dashboard

- [ ] **B6.1** Build a dashboard in Metabase on top of the gold tables with at least these four views: company status counts by state, insolvency events by quarter, capital distribution by business activity, and a company search that shows current status plus status history.
  **Commit:** export or screenshot the dashboard definition into `dashboard/dashboard_definition.md` with a short description of each view, open a pull request.

- [ ] **B6.2** Write the plain language label and one sentence explanation for each dashboard view, as it should appear to a non technical analyst.
  **Commit:** append to `dashboard/dashboard_definition.md`, update the pull request.

## Station B7: Stakeholder Delivery

- [ ] **B7.1** Write a five minute stakeholder presentation script. It must contain zero tool names. It must say what the data shows, what the client should do with it, and what the platform cannot tell them.
  **Commit:** `delivery/presentation_script.md`, open a pull request.

- [ ] **B7.2** Present to a peer playing the client. Record their three hardest questions and your answers, or "I did not know" where true.
  **Commit:** `delivery/qa_log.md`, open a pull request.

## Station B8: Project Handover **[MILESTONE]**

- [ ] **B8.1** Write the runbook: how to refresh each data source, what to check when a run fails, who to contact for what, and where every piece of documentation lives.
  **Commit:** `delivery/runbook.md`, open a pull request.

- [ ] **B8.2** Write the final README for the repository root, so a stranger can understand what this project is, how it is structured, and how to run it.
  **Commit:** `/README.md`, open a pull request.

## Station D9: Airflow Orchestration

- [ ] **D9.1** Write the monthly refresh DAG: snapshot preparation, bronze loads, dbt build, Great Expectations gate, with correct dependency order. Draw or describe the dependency graph in notes.
  **Commit:** `airflow/monthly_refresh_dag.py` plus `airflow/notes.md`, open a pull request.

- [ ] **D9.2** Add the failure behavior: the quality gate must stop the pipeline before gold tables are touched, and the failure must be visible in logs with the source file named.
  **Commit:** updated DAG plus a paste of a deliberate failure run in `airflow/notes.md`, update the pull request.

## Station D10: Project Handover **[MILESTONE]**

- [ ] **D10.1** Run the full pipeline from a clean checkout on a fresh Snowflake schema, following only the runbook. Record every place the runbook was unclear or wrong, and fix it.
  **Commit:** updated `delivery/runbook.md` plus `delivery/clean_run_log.md`, open a pull request.

- [ ] **D10.2** Archive the project: final README, all documentation linked, every pull request merged or explicitly closed with a reason.
  **Commit:** final state of the repository, final pull request titled "Project handover".
