# Week 7 — History that survives

**Data Sprint 1 · Week 7 of 10 · Theme: apply a month of changes without destroying last month's truth**

Read this whole file before you start. Then work through the stations in order.

---

## Before you start

Git commands: `docs/03-student-guide.md`. Client story and sources: `docs/01-project-brief.md`. Unknown word: `docs/08-glossary.md`. Broken tool: `docs/10-troubleshooting.md`. Each task names the exact file path to commit to, inside this same week folder.

---

## By the end of this week you can

- Detect exactly what changed between two monthly snapshots
- Apply those changes with MERGE so old versions are closed, not overwritten
- Answer "what was this company's status on 1 March" and get March's answer, not today's
- Download files in parallel, and say why threads help here and not everywhere
- Connect Python to Snowflake with no password anywhere in the code

## The milestone this week

**S10 SCD2 Build.** This is the client's core requirement and the hardest logic in the sprint. Expect it to take longer than you think, and expect to get it wrong once before you get it right.

---

## The week at a glance

| Step | LEARN | DO |
|---|---|---|
| **1** | Kimball "Slowly Changing Dimensions" article | S10.1 — change detection |
| **2** | Kudvenkat part 68 (MERGE) | S10.2 — the SCD2 MERGE, on a test copy |
| **3** | Re-read your own S9.4 query | S10.3 — the point in time query |
| **4** | Real Python "Speed Up Your Program With Concurrency" | P10.1 P10.2 — parallel downloads, the GIL |
| **5** | Snowflake docs "Python Connector" | P11.1 P11.2 — connector, load verifier |
| **6** | — | Cohort review: SCD2 walkthrough, point in time proof |

---

## Station S10: MERGE and SCD2 Build **[MILESTONE]**

Foundation link: Kudvenkat part 68 (MERGE) and Station S9 window functions.

- [ ] **S10.1** Write the change detection query: join this month's snapshot to last month's on CIN and list every company where status, capital, or address changed. How many changes of each type?
  **Commit:** `sql/s10/01_change_detection.sql`, open a pull request.

- [ ] **S10.2** Write the MERGE statement that applies the month changes to dim_company: close changed rows with an end date, insert new version rows, insert brand new companies. Run it on a test copy first and report row counts before and after.
  **Commit:** `sql/s10/02_scd2_merge.sql` plus counts in `sql/s10/notes.md`, open a pull request.

- [ ] **S10.3** Write a query that answers: "What was company CIN X's status on 1 March 2026?" for three companies that changed status this year.
  **Commit:** `sql/s10/03_point_in_time.sql`, update the pull request.

**Run S10.2 on a test copy first, every time.** A MERGE with the match condition slightly wrong will silently overwrite history, and the whole point of the station is that history survives.

**Three checks that tell you S10.2 is correct:**
- Run it twice with the same input. The second run must change nothing. If row counts grow, it is not idempotent.
- Exactly one row per CIN has an open end date.
- A company that changed status has two rows, with no gap and no overlap between the old end date and the new start date.

---

## Station P10: Concurrency, Parallel Downloads

- [ ] **P10.1** Rewrite the RoC file download step to fetch all files in parallel using a thread pool. Time the old sequential version and the new parallel version on the same files. Record both times.
  **Commit:** `python/p10/parallel_download.py` plus timings in `python/p10/notes.md`, open a pull request.

- [ ] **P10.2** In three sentences, explain why threads help for downloads but would not help for heavy number crunching. Name the Python feature responsible.
  **Commit:** append to `python/p10/notes.md`, update the pull request.

**On P10.1:** be a good citizen. Do not open twenty connections to a government website. Keep the pool small, keep the timeout, and keep the retry from P4.

---

## Station P11: Snowflake Python Connector

- [ ] **P11.1** Write a script that connects to Snowflake with the Python connector, runs the row count query on one raw table, and logs the result. Credentials must come from environment variables, never from the code.
  **Commit:** `python/p11/snowflake_count.py`, open a pull request. Confirm in notes that no password appears anywhere in the committed files.

- [ ] **P11.2** Write the load verification script: after any COPY INTO, it compares the file row count to the table row count and exits with a failure code if they differ. This script will become an Airflow task.
  **Commit:** `python/p11/load_verifier.py`, update the pull request.

**On P11.1:** read your own diff before you push. A committed password is the one mistake in this sprint that cannot be quietly undone; see `docs/10-troubleshooting.md`, Git section, if it happens.

**On P11.2:** the exit code is the point. Airflow decides whether the pipeline continues by reading it, so a script that prints "mismatch" and exits successfully is worse than useless in week 10.

---

## End of week checklist

- [ ] S10.1 — change detection with counts per change type
- [ ] S10.2 — the MERGE, tested on a copy, with before and after row counts and the three correctness checks
- [ ] S10.3 — point in time answers for three companies that actually changed
- [ ] P10.1, P10.2 — parallel downloads with both timings, and the GIL explanation
- [ ] P11.1, P11.2 — connector script with credentials from the environment, and a verifier that exits non-zero on mismatch
- [ ] At least one teammate's pull request reviewed with a real comment
- [ ] You can explain SCD2 out loud, using one company from your own data as the example

**If you are short on time, cut in this order:** P10.1, then P11.2. Never cut S10. It is the milestone, the client's core requirement, and week 9 rebuilds it in dbt on top of what you learn here.

Next: `week8/problem_statement.md`.
