# Week 5 — Readable SQL and the agreed model

**Data Sprint 1 · Week 5 of 13 · Theme: write SQL someone else can review, then agree the shape of the gold layer**

Read this whole file before you start. Then work through the task groups in order.

---

## Before you start

Git commands: `docs/03-student-guide.md`. Client story and sources: `docs/01-project-brief.md`. Unknown word: `docs/08-glossary.md`. Broken tool: `docs/10-troubleshooting.md`. What a tool is for: `docs/11-tools-and-technology.md`. Each task names the exact file path to commit to, inside this same week folder.

---

## By the end of this week you can

- Rewrite a nested query as CTEs a teammate can read without asking you questions
- State the grain of a table in one sentence, and know why that sentence matters
- Design a star schema and defend it against the alternatives
- Write code that survives a failing network call instead of crashing

## The milestone this week

**S7 Star Schema Design.** Table names, column names, and the grain of the fact table get agreed cohort-wide. Everything in weeks 9 and 11 is built on the names decided here, so a private naming choice becomes everyone's problem later.

---

## The week at a glance

| Step | LEARN | DO |
|---|---|---|
| **1** | Kudvenkat parts 38 to 41 (views) | Tasks 1–2 — CTE rewrite, current view |
| **2** | Kudvenkat parts 47 to 50 (CTEs) | Task 3 — above-average states |
| **3** | Kimball "Dimensional Modeling Techniques" | Tasks 4–6 — grain, SCD types, final diagram with two reviewers |
| **4** | Real Python "Python Exceptions" · `tenacity` quickstart | Tasks 7–8 — retry decorator, RBI download |
| **5** | Python `with` statement tutorial | Task 9 — context managers |
| **6** | — | Cohort review: star schema sign-off, naming agreement |

---

## 1 · Views and CTEs

Foundation link: Kudvenkat parts 38 to 41 (views) and 47 to 50 (CTEs).

- [ ] **Task 1 — Rewrite the join as CTEs** (ID `S6.1`): Rewrite the S3.3 insolvency join query as a chain of two CTEs: first filter, then join. Explain in one sentence why this is easier to review.
  **Commit:** `sql/s6/01_cte_rewrite.sql`, open a pull request.

- [ ] **Task 2 — Create the current-company view** (ID `S6.2`): Create a view named v_company_current that shows only the latest snapshot version of each company. Which gold layer table will this view eventually mirror?
  **Commit:** `sql/s6/02_current_view.sql` plus the answer in `sql/s6/notes.md`, update the pull request.

- [ ] **Task 3 — Find above-average strike-off states** (ID `S6.3`): Using a CTE, find states whose strike off rate this month is above the national average strike off rate.
  **Commit:** `sql/s6/03_above_avg_states.sql`, update the pull request.

---

## 2 · Star Schema Design **[MILESTONE]**

- [ ] **Task 4 — Write the gold grain statements** (ID `S7.1`): Write the grain statement for each planned gold table: dim_company, fct_cirp_event, dim_state, dim_date. One sentence each, starting "One row in this table represents...".
  **Commit:** `design/grain_statements.md`, open a pull request.

- [ ] **Task 5 — Mark dim_company columns as SCD 1 or 2** (ID `S7.2`): List every column planned for dim_company, and mark each as SCD Type 1 or Type 2 with a one line reason.
  **Commit:** `design/dim_company_columns.md`, update the pull request.

- [ ] **Task 6 — Draw the final star schema** (ID `S7.3`): Draw the full star schema diagram, reviewed by two teammates before submission. Record their names in the file.
  **Commit:** `design/star_schema_final.md`, open a pull request.

**On Task 5:** Type 1 overwrites and loses history. Type 2 keeps a version row. The client asked "what was this company's status on 1 March", so at least one column must be Type 2, and you must be able to say which and why. Week 9 and week 11 build exactly what you write here.

---

## 3 · Retry Logic and Context Managers

- [ ] **Task 7 — Write a retry decorator** (ID `P4.1`): Write a retry decorator that retries a failed function up to three times with a waiting gap that doubles each time. Test it on a function that fails twice then succeeds.
  **Commit:** `python/p4/retry_decorator.py` plus test output in `python/p4/notes.md`, open a pull request.

- [ ] **Task 8 — Download the RBI file** (ID `P4.2`): Write the RBI download script: fetch the policy rate file, retry on failure using your decorator, save it untouched into `data/raw/rbi/` with the pull date in the file name.
  **Commit:** `python/p4/rbi_download.py`, update the pull request.

- [ ] **Task 9 — Close files safely** (ID `P4.3`): Rewrite your file handling in P1 and P2 scripts using context managers so files always close safely. Note in one sentence what problem this prevents.
  **Commit:** updated scripts, plus note in `python/p4/notes.md`, update the pull request.

**Note:** every network call in this project needs a timeout. A download that hangs forever with no timeout is the failure Task 7 exists to prevent, and `data/raw/` is gitignored, so the downloaded file must never appear in your commit.

---

## End of week checklist

- [ ] Tasks 1–3 — CTE rewrite, current view, above-average states
- [ ] Tasks 4–6 — grain statements, dim_company columns with SCD types, final diagram with two named reviewers
- [ ] Tasks 7–9 — retry decorator with proof it retried, RBI download, context managers
- [ ] At least one teammate's pull request reviewed with a real comment
- [ ] Your table and column names match what the cohort agreed, not what you wrote first

**If you are short on time, cut in this order:** Task 3 (S6.3), then Task 9 (P4.3). Never cut Tasks 4–6 (S7). It is the milestone, and weeks 9 and 11 cannot start without it.

Next: `week6/problem_statement.md`.
