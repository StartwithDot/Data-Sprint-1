# Week 9 — History that survives

**Data Sprint 1 · Week 9 of 13 · Theme: apply a month of changes without destroying last month's truth, then write the technical brief**

Read this whole file before you start. Then work through the task groups in order.

---

## Before you start

Git commands: `docs/03-student-guide.md`. Client story and sources: `docs/01-project-brief.md`. Unknown word: `docs/08-glossary.md`. Broken tool: `docs/10-troubleshooting.md`. What a tool is for: `docs/11-tools-and-technology.md`. Each task names the exact file path to commit to, inside this same week folder.

---

## By the end of this week you can

- Detect exactly what changed between two monthly snapshots
- Apply those changes with MERGE so old versions are closed, not overwritten
- Answer "what was this company's status on 1 March" and get March's answer, not today's
- Download files in parallel, and say why threads help here and not everywhere
- Connect Python to Snowflake with no password anywhere in the code
- Write the technical half of the discovery brief, with a platform architecture diagram

## The milestones this week

**S10 SCD2 Build.** This is the client's core requirement and the hardest logic in the sprint. Expect it to take longer than you think, and expect to get it wrong once before you get it right.

**D1 Technical Brief.** The written plan the platform build in weeks 10 to 12 executes against.

---

## The week at a glance

| Step | LEARN | DO |
|---|---|---|
| **1** | Kimball "Slowly Changing Dimensions" article | Task 1 — change detection |
| **2** | Kudvenkat part 68 (MERGE) | Task 2 — the SCD2 MERGE, on a test copy |
| **3** | Re-read your own S9.4 query | Task 3 — the point in time query |
| **4** | Real Python "Speed Up Your Program With Concurrency" | Tasks 4–5 — parallel downloads, the GIL |
| **5** | Snowflake docs "Python Connector" | Tasks 6–7 — connector, load verifier |
| **6** | Your week 1 brief, re-read · `docs/07-platform-and-cicd-guide.md` | Tasks 8–9 — the technical brief and the architecture diagram |
| **7** | — | Cohort review: SCD2 walkthrough, point in time proof, risk list |

---

## 1 · Slowly Changing Dimensions (SCD2) **[MILESTONE]**

Foundation link: Kudvenkat part 68 (MERGE) and the window functions from week 8.

- [ ] **Task 1 — Detect the changes** (ID `S10.1`): Write the change detection query: join this month's snapshot to last month's on CIN and list every company where status, capital, or address changed. How many changes of each type?
  **Commit:** `sql/s10/01_change_detection.sql`, open a pull request.

- [ ] **Task 2 — Apply the changes with MERGE** (ID `S10.2`): Write the MERGE statement that applies the month changes to dim_company: close changed rows with an end date, insert new version rows, insert brand new companies. Run it on a test copy first and report row counts before and after.
  **Commit:** `sql/s10/02_scd2_merge.sql` plus counts in `sql/s10/notes.md`, open a pull request.

- [ ] **Task 3 — Answer a point in time question** (ID `S10.3`): Write a query that answers: "What was company CIN X's status on 1 March 2026?" for three companies that changed status this year.
  **Commit:** `sql/s10/03_point_in_time.sql`, update the pull request.

**Run Task 2 on a test copy first, every time.** A MERGE with the match condition slightly wrong will silently overwrite history, and the whole point of the week is that history survives.

**Three checks that tell you Task 2 is correct:**
- Run it twice with the same input. The second run must change nothing. If row counts grow, it is not idempotent.
- Exactly one row per CIN has an open end date.
- A company that changed status has two rows, with no gap and no overlap between the old end date and the new start date.

---

## 2 · Parallel Downloads

- [ ] **Task 4 — Download in parallel** (ID `P10.1`): Rewrite the RoC file download step to fetch all files in parallel using a thread pool. Time the old sequential version and the new parallel version on the same files. Record both times.
  **Commit:** `python/p10/parallel_download.py` plus timings in `python/p10/notes.md`, open a pull request.

- [ ] **Task 5 — Explain why threads help** (ID `P10.2`): In three sentences, explain why threads help for downloads but would not help for heavy number crunching. Name the Python feature responsible.
  **Commit:** append to `python/p10/notes.md`, update the pull request.

**On Task 4:** be a good citizen. Do not open twenty connections to a government website. Keep the pool small, keep the timeout, and keep the retry from week 5.

---

## 3 · Python and Snowflake Together

- [ ] **Task 6 — Connect Python to Snowflake** (ID `P11.1`): Write a script that connects to Snowflake with the Python connector, runs the row count query on one raw table, and logs the result. Credentials must come from environment variables, never from the code.
  **Commit:** `python/p11/snowflake_count.py`, open a pull request. Confirm in notes that no password appears anywhere in the committed files.

- [ ] **Task 7 — Write the load verifier** (ID `P11.2`): Write the load verification script: after any COPY INTO, it compares the file row count to the table row count and exits with a failure code if they differ. This script will become an Airflow task.
  **Commit:** `python/p11/load_verifier.py`, update the pull request.

**On Task 6:** read your own diff before you push. A committed password is the one mistake in this sprint that cannot be quietly undone; see `docs/10-troubleshooting.md`, Git section, if it happens.

**On Task 7:** the exit code is the point. Airflow decides whether the pipeline continues by reading it, so a script that prints "mismatch" and exits successfully is worse than useless in week 12.

---

## 4 · Technical Brief **[MILESTONE]**

- [ ] **Task 8 — Write the technical brief** (ID `D1.1`): Write the technical half of the discovery brief: the four sources, their formats, their cadences, and the top three technical risks you see. One page maximum.
  **Commit:** `discovery/technical_brief.md`, open a pull request.

- [ ] **Task 9 — Draw the platform architecture** (ID `D1.2`): Draw the platform architecture diagram for the technical brief: every component from the four sources to the dashboard, where the platform rotation's work lands, and where the automated checks (dbt tests, Great Expectations, Airflow) run. Extend your week 4 pipeline flow diagram rather than starting over.
  **Commit:** `design/platform_architecture.md` (embed the diagram), add it to the technical brief pull request.

**On Task 8:** week 1's brief was for the client. This one is for the engineer who inherits the pipeline. Name risks you have actually hit in weeks 2 to 9: the PDF layout shifting, four spellings of one state, CINs that do not join, a source that has no stable download URL.

**On Task 9:** the technical brief and this diagram are what the platform build in weeks 10 to 12 executes against. If the diagram and the brief disagree, the brief wins, and the diagram is wrong.

---

## End of week checklist

- [ ] Task 1 — change detection with counts per change type
- [ ] Task 2 — the MERGE, tested on a copy, with before and after row counts and the three correctness checks
- [ ] Task 3 — point in time answers for three companies that actually changed
- [ ] Tasks 4–5 — parallel downloads with both timings, and the GIL explanation
- [ ] Tasks 6–7 — connector script with credentials from the environment, and a verifier that exits non-zero on mismatch
- [ ] Tasks 8–9 — the technical brief and the platform architecture diagram
- [ ] At least one teammate's pull request reviewed with a real comment
- [ ] You can explain SCD2 out loud, using one company from your own data as the example

**If you are short on time, cut in this order:** Task 5 (P10.2), then Task 7 (P11.2). Never cut Tasks 1–3 (S10). It is the milestone, the client's core requirement, and week 11 rebuilds it in dbt on top of what you learn here.

Next: `week10/problem_statement.md`.
