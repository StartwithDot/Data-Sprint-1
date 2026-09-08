# Week 4 - First load, and the design begins

**Data Sprint 1 · Week 4 of 13 · Theme: get every file into Snowflake with counts that match, then start designing the gold layer**

Read this whole file before you start. Then work through the task groups in order.

---

## Before you start

Git commands: `docs/03-student-guide.md`. Client story and sources: `docs/01-project-brief.md`. Unknown word: `docs/08-glossary.md`. Broken tool: `docs/10-troubleshooting.md`. What a tool is for: `docs/11-tools-and-technology.md`. Each task names the exact file path to commit to, inside this same week folder.

---

## By the end of this week you can

- Load files into Snowflake and prove the row counts match
- Draw the star schema diagram and write the grain of each gold table
- Justify medallion layering, a star at gold, and why not Data Vault
- Draw the pipeline flow so a reviewer can see where each tool sits

## The milestone this week

**P3 First Snowflake Load.** Every difference between rows in the file and rows in the table is zero, or explained in writing. No exceptions, no rounding, no "close enough".

---

## The week at a glance

| Step | LEARN | DO |
|---|---|---|
| **1** | Snowflake docs "Loading Data" · `COPY INTO` reference | Tasks 1–3 - stage, format, all loads |
| **2** | Kimball "Dimensional Modeling Techniques" · Nygard on ADRs | Tasks 4–5 - the ERD and the grain statements |
| **3** | Databricks "Medallion Architecture" page | Task 6 - the modelling decision record |
| **4** | Mermaid docs (flowchart syntax) · re-read your week 1 system map | Task 7 - the pipeline flow diagram |
| **5** | - | Cohort review: load reconciliation numbers, design kickoff |

---

## 1 · First Snowflake Load **[MILESTONE]**

- [ ] **Task 1 - Create the stage and file format** (ID `P3.1`): In Snowflake, create an internal stage and a CSV file format with header skipping and quoted field handling. Write down what each file format option does in one line.
  **Commit:** `sql/p3/01_stage_and_format.sql` plus `sql/p3/notes.md`, open a pull request.

- [ ] **Task 2 - Load the first file** (ID `P3.2`): PUT one RoC CSV into the stage and COPY it into the raw table. Record the row count loaded and the row count in the file. They must match.
  **Commit:** `sql/p3/02_first_load.sql` plus both counts in notes, update the pull request.

- [ ] **Task 3 - Load the remaining files** (ID `P3.3`): Load the remaining RoC files, each into its own raw table. Produce a summary table: file name, rows in file, rows loaded, difference. Every difference must be zero or explained.
  **Commit:** `sql/p3/03_all_loads.sql` plus `sql/p3/load_summary.md`, update the pull request.

**If `COPY INTO` loads zero rows or fewer rows than expected**, that is normal on the first attempt. `docs/10-troubleshooting.md`, Snowflake section, lists the causes in order of likelihood. Diagnose it; do not add `FORCE = TRUE` to make the number look right.


---

## 2 · Design Record, ERD and Architecture

- [ ] **Task 4 - Draw the star schema ERD** (ID `B3.1`): Draw the star schema diagram for the gold layer. It must show dim_company, the insolvency fact table, the state context dimension, and the date dimension, with the join keys labeled. Use draw.io, mermaid, or paper photographed clearly.
  **Commit:** `design/erd.md` (embed the diagram), open a pull request.

- [ ] **Task 5 - Write the grain statements** (ID `B3.2`): Write the grain statement for each gold table, in one sentence each, starting with "One row in this table represents...".
  **Commit:** append to `design/erd.md`, update the pull request.

- [ ] **Task 6 - Write the modelling decision record** (ID `B3.3`): Write a half page design record: why Medallion layering, why a Kimball star at gold, why not Data Vault. One honest paragraph each.
  **Commit:** `design/modeling_decision.md`, open a pull request.

**On Task 6:** "because the roadmap said so" is not a reason. Name what each choice costs. Medallion means storing the data three times; a star means denormalizing on purpose; Data Vault is more auditable and much slower to build. A reviewer should be able to disagree with you on the evidence you gave.

---

## 3 · Pipeline Flow Diagram

- [ ] **Task 7 - Draw the pipeline flow** (ID `A2.1`): Draw the pipeline flow diagram: the four sources on the left, then each hop through raw files → stage → bronze → silver (staging) → gold (star schema) → dashboard, with the tool at each hop (Python extractors, `COPY INTO`, dbt, Great Expectations, Airflow) and a monthly refresh arrow running through it. Mark where the quality gate sits. Use the same style as your week 1 system map so the two line up, and keep it to one page.
  **Commit:** `design/pipeline_flow.md` (embed the diagram), open a pull request.

**On Task 7:** this is the picture the technical brief and the handover will point back to. You will update it in week 7 with what the real extractors teach you, so do not polish it into a museum piece.

---

## End of week checklist

- [ ] Tasks 1–3 - stage, format, every RoC file loaded, and `load_summary.md` with a zero or an explanation on every line
- [ ] Tasks 4–5 - the ERD and the grain statements
- [ ] Task 6 - the honest decision record
- [ ] Task 7 - the pipeline flow diagram
- [ ] At least one teammate's pull request reviewed with a real comment
- [ ] You can say out loud the difference between rows in the file and rows in the table

**If you are short on time, cut in this order:** Task 7's polish, then Task 6 (B3.3), then Task 3 (P3.3) formatting. Never cut Task 2 (P3.2). The first load is the milestone and the whole cohort waits on it.

Next: `week5/problem_statement.md`.
