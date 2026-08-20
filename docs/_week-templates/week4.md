# Week 4 — Readable SQL and the agreed model

**Data Sprint 1 · Week 4 of 10 · Theme: write SQL someone else can review, then agree the shape of the gold layer**

Read this whole file before you start. Then work through the stations in order.

---

## Before you start

Git commands: `docs/03-student-guide.md`. Client story and sources: `docs/01-project-brief.md`. Unknown word: `docs/08-glossary.md`. Broken tool: `docs/10-troubleshooting.md`. Each task names the exact file path to commit to, inside this same week folder.

---

## By the end of this week you can

- Rewrite a nested query as CTEs a teammate can read without asking you questions
- State the grain of a table in one sentence, and know why that sentence matters
- Design a star schema and defend it against the alternatives
- Write code that survives a failing network call instead of crashing

## The milestone this week

**S7 Star Schema Design.** Table names, column names, and the grain of the fact table get agreed cohort-wide. Everything in weeks 8 and 9 is built on the names decided here, so a private naming choice becomes everyone's problem later.

---

## The week at a glance

| Step | LEARN | DO |
|---|---|---|
| **1** | Kimball "Dimensional Modeling Techniques" · Nygard on ADRs | B3.1 B3.2 — the ERD and the grain statements |
| **2** | Databricks "Medallion Architecture" page | B3.3 — the modelling decision record |
| **3** | Kudvenkat parts 38 to 41 (views) | S6.1 S6.2 — CTE rewrite, current view |
| **4** | Kudvenkat parts 47 to 50 (CTEs) | S6.3 S7.1 S7.2 — above-average states, grain, SCD types |
| **5** | Real Python "Python Exceptions" · `tenacity` quickstart | S7.3 P4.1 P4.2 P4.3 — final diagram, retries, context managers |
| **6** | — | Cohort review: star schema sign-off, naming agreement |

---

## Station B3: Design Record, ERD and Architecture

- [ ] **B3.1** Draw the star schema diagram for the gold layer. It must show dim_company, the insolvency fact table, the state context dimension, and the date dimension, with the join keys labeled. Use draw.io, mermaid, or paper photographed clearly.
  **Commit:** `design/erd.md` (embed the diagram), open a pull request.

- [ ] **B3.2** Write the grain statement for each gold table, in one sentence each, starting with "One row in this table represents...".
  **Commit:** append to `design/erd.md`, update the pull request.

- [ ] **B3.3** Write a half page design record: why Medallion layering, why a Kimball star at gold, why not Data Vault. One honest paragraph each.
  **Commit:** `design/modeling_decision.md`, open a pull request.

**On B3.3:** "because the roadmap said so" is not a reason. Name what each choice costs. Medallion means storing the data three times; a star means denormalizing on purpose; Data Vault is more auditable and much slower to build. A reviewer should be able to disagree with you on the evidence you gave.

---

## Station S6: Views and CTEs

Foundation link: Kudvenkat parts 38 to 41 (views) and 47 to 50 (CTEs).

- [ ] **S6.1** Rewrite the S3.3 insolvency join query as a chain of two CTEs: first filter, then join. Explain in one sentence why this is easier to review.
  **Commit:** `sql/s6/01_cte_rewrite.sql`, open a pull request.

- [ ] **S6.2** Create a view named v_company_current that shows only the latest snapshot version of each company. Which gold layer table will this view eventually mirror?
  **Commit:** `sql/s6/02_current_view.sql` plus the answer in `sql/s6/notes.md`, update the pull request.

- [ ] **S6.3** Using a CTE, find states whose strike off rate this month is above the national average strike off rate.
  **Commit:** `sql/s6/03_above_avg_states.sql`, update the pull request.

---

## Station S7: Star Schema Design **[MILESTONE]**

- [ ] **S7.1** Write the grain statement for each planned gold table: dim_company, fct_cirp_event, dim_state, dim_date. One sentence each, starting "One row in this table represents...".
  **Commit:** `design/grain_statements.md`, open a pull request.

- [ ] **S7.2** List every column planned for dim_company, and mark each as SCD Type 1 or Type 2 with a one line reason.
  **Commit:** `design/dim_company_columns.md`, update the pull request.

- [ ] **S7.3** Draw the full star schema diagram, reviewed by two teammates before submission. Record their names in the file.
  **Commit:** `design/star_schema_final.md`, open a pull request.

**On S7.2:** Type 1 overwrites and loses history. Type 2 keeps a version row. The client asked "what was this company's status on 1 March", so at least one column must be Type 2, and you must be able to say which and why. Week 7 and week 9 build exactly what you write here.

---

## Station P4: Retry Logic and Context Managers

- [ ] **P4.1** Write a retry decorator that retries a failed function up to three times with a waiting gap that doubles each time. Test it on a function that fails twice then succeeds.
  **Commit:** `python/p4/retry_decorator.py` plus test output in `python/p4/notes.md`, open a pull request.

- [ ] **P4.2** Write the RBI download script: fetch the policy rate file, retry on failure using your decorator, save it untouched into `data/raw/rbi/` with the pull date in the file name.
  **Commit:** `python/p4/rbi_download.py`, update the pull request.

- [ ] **P4.3** Rewrite your file handling in P1 and P2 scripts using context managers so files always close safely. Note in one sentence what problem this prevents.
  **Commit:** updated scripts, plus note in `python/p4/notes.md`, update the pull request.

**Note:** every network call in this project needs a timeout. A download that hangs forever with no timeout is the failure P4 exists to prevent, and `data/raw/` is gitignored, so the downloaded file must never appear in your commit.

---

## End of week checklist

- [ ] B3.1, B3.2, B3.3 — diagram, grain statements, and the honest decision record
- [ ] S6.1, S6.2, S6.3 — CTE rewrite, current view, above-average states
- [ ] S7.1, S7.2, S7.3 — grain statements, dim_company columns with SCD types, final diagram with two named reviewers
- [ ] P4.1, P4.2, P4.3 — retry decorator with proof it retried, RBI download, context managers
- [ ] At least one teammate's pull request reviewed with a real comment
- [ ] Your table and column names match what the cohort agreed, not what you wrote first

**If you are short on time, cut in this order:** S6.3, then P4.3, then B3.1 (since S7.3 supersedes it). Never cut S7. It is the milestone, and weeks 8 and 9 cannot start without it.

Next: `week5/problem_statement.md`.
