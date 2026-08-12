# Week 4 Tasks

## Station B3: Design Record, ERD and Architecture

- [ ] **B3.1** Draw the star schema diagram for the gold layer. It must show dim_company, the insolvency fact table, the state context dimension, and the date dimension, with the join keys labeled. Use draw.io, mermaid, or paper photographed clearly.
  **Commit:** `design/erd.md` (embed the diagram), open a pull request.

- [ ] **B3.2** Write the grain statement for each gold table, in one sentence each, starting with "One row in this table represents...".
  **Commit:** append to `design/erd.md`, update the pull request.

- [ ] **B3.3** Write a half page design record: why Medallion layering, why a Kimball star at gold, why not Data Vault. One honest paragraph each.
  **Commit:** `design/modeling_decision.md`, open a pull request.

## Station S6: Views and CTEs

Foundation link: Kudvenkat parts 38 to 41 (views) and 47 to 50 (CTEs).

- [ ] **S6.1** Rewrite the S3.3 insolvency join query as a chain of two CTEs: first filter, then join. Explain in one sentence why this is easier to review.
  **Commit:** `sql/s6/01_cte_rewrite.sql`, open a pull request.

- [ ] **S6.2** Create a view named v_company_current that shows only the latest snapshot version of each company. Which gold layer table will this view eventually mirror?
  **Commit:** `sql/s6/02_current_view.sql` plus the answer in `sql/s6/notes.md`, update the pull request.

- [ ] **S6.3** Using a CTE, find states whose strike off rate this month is above the national average strike off rate.
  **Commit:** `sql/s6/03_above_avg_states.sql`, update the pull request.

## Station S7: Star Schema Design **[MILESTONE]**

- [ ] **S7.1** Write the grain statement for each planned gold table: dim_company, fct_cirp_event, dim_state, dim_date. One sentence each, starting "One row in this table represents...".
  **Commit:** `design/grain_statements.md`, open a pull request.

- [ ] **S7.2** List every column planned for dim_company, and mark each as SCD Type 1 or Type 2 with a one line reason.
  **Commit:** `design/dim_company_columns.md`, update the pull request.

- [ ] **S7.3** Draw the full star schema diagram, reviewed by two teammates before submission. Record their names in the file.
  **Commit:** `design/star_schema_final.md`, open a pull request.

## Station P4: Retry Logic and Context Managers

- [ ] **P4.1** Write a retry decorator that retries a failed function up to three times with a waiting gap that doubles each time. Test it on a function that fails twice then succeeds.
  **Commit:** `python/p4/retry_decorator.py` plus test output in `python/p4/notes.md`, open a pull request.

- [ ] **P4.2** Write the RBI download script: fetch the policy rate file, retry on failure using your decorator, save it untouched into `data/raw/rbi/` with the pull date in the file name.
  **Commit:** `python/p4/rbi_download.py`, update the pull request.

- [ ] **P4.3** Rewrite your file handling in P1 and P2 scripts using context managers so files always close safely. Note in one sentence what problem this prevents.
  **Commit:** updated scripts, plus note in `python/p4/notes.md`, update the pull request.

