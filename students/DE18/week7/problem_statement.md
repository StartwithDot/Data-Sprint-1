# Week 7 Tasks

## Station S10: MERGE and SCD2 Build

Foundation link: Kudvenkat part 68 (MERGE) and Station S9 window functions.

- [ ] **S10.1** Write the change detection query: join this month's snapshot to last month's on CIN and list every company where status, capital, or address changed. How many changes of each type?
  **Commit:** `sql/s10/01_change_detection.sql`, open a pull request.

- [ ] **S10.2** Write the MERGE statement that applies the month changes to dim_company: close changed rows with an end date, insert new version rows, insert brand new companies. Run it on a test copy first and report row counts before and after.
  **Commit:** `sql/s10/02_scd2_merge.sql` plus counts in `sql/s10/notes.md`, open a pull request.

- [ ] **S10.3** Write a query that answers: "What was company CIN X's status on 1 March 2026?" for three companies that changed status this year.
  **Commit:** `sql/s10/03_point_in_time.sql`, update the pull request.

## Station P10: Concurrency, Parallel Downloads

- [ ] **P10.1** Rewrite the RoC file download step to fetch all files in parallel using a thread pool. Time the old sequential version and the new parallel version on the same files. Record both times.
  **Commit:** `python/p10/parallel_download.py` plus timings in `python/p10/notes.md`, open a pull request.

- [ ] **P10.2** In three sentences, explain why threads help for downloads but would not help for heavy number crunching. Name the Python feature responsible.
  **Commit:** append to `python/p10/notes.md`, update the pull request.

## Station P11: Snowflake Python Connector

- [ ] **P11.1** Write a script that connects to Snowflake with the Python connector, runs the row count query on one raw table, and logs the result. Credentials must come from environment variables, never from the code.
  **Commit:** `python/p11/snowflake_count.py`, open a pull request. Confirm in notes that no password appears anywhere in the committed files.

- [ ] **P11.2** Write the load verification script: after any COPY INTO, it compares the file row count to the table row count and exits with a failure code if they differ. This script will become an Airflow task.
  **Commit:** `python/p11/load_verifier.py`, update the pull request.

