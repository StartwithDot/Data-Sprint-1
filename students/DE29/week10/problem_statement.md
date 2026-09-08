# Week 10 - The shared platform begins

**Data Sprint 1 · Week 10 of 13 · Theme: stop practising separately and build the one real pipeline**

Read this whole file before you start. Then work through the task groups in order.

---

## This week the work moves into the shared zone

Weeks 1 to 9 happened in your own folder, where a mistake cost you nothing. From this week, part of the work lands in `platform/`, which is the one real version the whole cohort depends on.

**Before you touch `platform/`, read `docs/07-platform-and-cicd-guide.md` and `docs/06-team-roles.md`.** Only that week's platform rotation writes there. If you are not on the rotation, you do the same stations in your own week folder, and you review the rotation's pull requests.

Git commands: `docs/03-student-guide.md`. Unknown word: `docs/08-glossary.md`. Broken tool: `docs/10-troubleshooting.md`. What a tool is for: `docs/11-tools-and-technology.md`.

---

## By the end of this week you can

- Set up stages and file formats for four sources that arrive in four different shapes
- Load every source into bronze with file name and load timestamp on every row
- Teach the load path to a teammate and watch them do it
- Write dbt staging models with tests that fail when the data is wrong

## The milestone this week

**D4 First Snowflake Load.** A teach-back: you are not done when it works, you are done when someone else can do it while you watch.

---

## The week at a glance

| Step | LEARN | DO |
|---|---|---|
| **1** | Snowflake docs "Loading Data" · stages and formats | Tasks 1–3 - stages, formats, Tasks question |
| **2** | `COPY INTO` reference, metadata columns | Tasks 4–5 - MCA loads, enrichment loads |
| **3** | - | Tasks 6–7 - reconciliation, teach-back |
| **4** | dbt "About dbt projects" · dbt Fundamentals modules on models, sources, tests | Tasks 8–10 - dbt project, staging models, tests |
| **5** | - | Cohort review: bronze reconciliation numbers, dbt test results |

---

## 1 · Stages and File Formats

- [ ] **Task 1 - Create the stages** (ID `D2.1`): Create the internal stages for all four sources with a clean folder prefix per source. List the stages and prefixes in a table.
  **Commit:** `sql/d2/01_stages.sql` plus the table in `sql/d2/notes.md`, open a pull request.

- [ ] **Task 2 - Define the file formats** (ID `D2.2`): Define the two file format objects the project needs (CSV with header, and any second format you found necessary). Justify each option you set, one line per option.
  **Commit:** `sql/d2/02_file_formats.sql` plus justification in notes, update the pull request.

- [ ] **Task 3 - When is a Task the right tool?** (ID `D2.3`): In one paragraph, explain when the team would choose a Snowflake Task over manual COPY INTO, and which of our four sources genuinely justifies one.
  **Commit:** append to `sql/d2/notes.md`, update the pull request.

**On Task 2:** record the encoding each source needed too. If one file only parsed as `latin-1`, that is a real property of the source and the next person must be told.


---

## 2 · Bronze Loads

- [ ] **Task 4 - Load all MCA files** (ID `D3.1`): Load all MCA RoC files into bronze raw tables, one per RoC, all columns VARCHAR, with file name and load timestamp recorded per row.
  **Commit:** `sql/d3/01_mca_raw_loads.sql` plus `sql/d3/load_summary.md`, open a pull request.

- [ ] **Task 5 - Load the enrichment sources** (ID `D3.2`): Load the extracted IBBI CSV, the CDM CSV, and the RBI CSV into their own bronze tables with the same metadata pattern.
  **Commit:** `sql/d3/02_enrichment_raw_loads.sql`, update the pull request.

- [ ] **Task 6 - Reconcile every table** (ID `D3.3`): Write the reconciliation query set: for every bronze table, rows in file versus rows in table. Every number must match or carry a written explanation.
  **Commit:** `sql/d3/03_reconciliation.sql` plus results in `sql/d3/load_summary.md`, update the pull request.

**Why the file name and load timestamp matter:** they are the only way, in three weeks, to answer "which file did this wrong row come from". That is lineage, and it costs two columns.

---

## 3 · Teach-Back: the Load Path **[MILESTONE]**

- [ ] **Task 7 - Teach the load path** (ID `D4.1`): Demonstrate the full manual load path to a teammate: stage, PUT, COPY, verify. Have them repeat it on a different RoC file while you watch. Both of you record what happened in notes.
  **Commit:** `sql/d4/teachback_notes.md` from each of you, open one pull request together.

**On Task 7:** the notes are the deliverable, not the load. Write where they got stuck and what you had to explain twice. That is the honest measure of whether the load path is documented well enough for week 13's handover.

---

## 4 · dbt Staging Models

- [ ] **Task 8 - Initialize the dbt project** (ID `D5.1`): Initialize the dbt project connected to Snowflake, with bronze sources declared. Commit the project skeleton with a README explaining the folder layout.
  **Commit:** `platform/dbt/` project folder plus `platform/dbt/README.md`, open a pull request.

- [ ] **Task 9 - Write the MCA staging model** (ID `D5.2`): Write the MCA staging model: typed columns, cleaned state names using your P5 frequency map, parsed dates, validated CINs flagged. Add not null and unique tests where they belong.
  **Commit:** `platform/dbt/models/staging/stg_mca.sql` plus its test configuration, update the pull request.

- [ ] **Task 10 - Write the remaining staging models** (ID `D5.3`): Write staging models for the IBBI, CDM, and RBI sources, with the same discipline. Run dbt tests and paste the results.
  **Commit:** the staging models plus `platform/dbt/test_results.md`, update the pull request.

**Never commit `profiles.yml`.** It holds your Snowflake password and it belongs in `~/.dbt/`. Check your diff.

**On Task 9:** bad CINs are flagged, not deleted. Silver types and cleans; it does not decide what counts as a real company. That decision belongs in gold, where it is visible.

**If a dbt model runs but the table is empty,** read `target/compiled/` to see the SQL dbt actually ran. See `docs/10-troubleshooting.md`, dbt section.

---

## End of week checklist

- [ ] Tasks 1–3 - stages with prefixes, file formats with justified options, the Tasks paragraph
- [ ] Tasks 4–6 - every source in bronze with file name and load timestamp, and a reconciliation line per table
- [ ] Task 7 - teach-back notes from both people, in one pull request
- [ ] Tasks 8–10 - dbt project with a README, four staging models, tests run with results pasted
- [ ] No `profiles.yml`, no `.env`, no data files in any commit
- [ ] If you were on the platform rotation, your entry in `docs/platform-rotation-log.md` is updated

**If you are short on time, cut in this order:** Task 10 (D5.3, do MCA only), then Task 3 (D2.3). Never cut Task 6 (D3.3) or Task 7 (D4.1). Unreconciled bronze poisons everything above it, and the teach-back is a milestone.

Next: `week11/problem_statement.md`.
