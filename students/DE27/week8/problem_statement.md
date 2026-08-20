# Week 8 — The shared platform begins

**Data Sprint 1 · Week 8 of 10 · Theme: stop practising separately and build the one real pipeline**

Read this whole file before you start. Then work through the stations in order.

---

## This week the work moves into the shared zone

Weeks 1 to 7 happened in your own folder, where a mistake cost you nothing. From this week, part of the work lands in `platform/`, which is the one real version the whole cohort depends on.

**Before you touch `platform/`, read `docs/07-platform-and-cicd-guide.md` and `docs/06-team-roles.md`.** Only that week's platform rotation writes there. If you are not on the rotation, you do the same stations in your own week folder, and you review the rotation's pull requests.

Git commands: `docs/03-student-guide.md`. Unknown word: `docs/08-glossary.md`. Broken tool: `docs/10-troubleshooting.md`.

---

## By the end of this week you can

- Write the technical half of a discovery brief, including the risks you actually expect
- Set up stages and file formats for four sources that arrive in four different shapes
- Load every source into bronze with file name and load timestamp on every row
- Teach the load path to a teammate and watch them do it
- Write dbt staging models with tests that fail when the data is wrong

## The milestones this week

**D1 Discovery Brief** and **D4 First Snowflake Load.** D4 is a teach-back: you are not done when it works, you are done when someone else can do it while you watch.

---

## The week at a glance

| Step | LEARN | DO |
|---|---|---|
| **1** | Your week 1 brief, re-read · `docs/07-platform-and-cicd-guide.md` | D1.1 — the technical brief |
| **2** | Snowflake docs "Loading Data" · stages and formats | D2.1 D2.2 D2.3 — stages, formats, Tasks question |
| **3** | `COPY INTO` reference, metadata columns | D3.1 D3.2 — MCA loads, enrichment loads |
| **4** | — | D3.3 D4.1 — reconciliation, teach-back |
| **5** | dbt "About dbt projects" · dbt Fundamentals modules on models, sources, tests | D5.1 D5.2 D5.3 — dbt project, staging models, tests |
| **6** | — | Cohort review: bronze reconciliation numbers, dbt test results |

---

## Station D1: Discovery Brief **[MILESTONE]**

- [ ] **D1.1** Write the technical half of the discovery brief: the four sources, their formats, their cadences, and the top three technical risks you see. One page maximum.
  **Commit:** `discovery/technical_brief.md`, open a pull request.

**On D1.1:** week 1's brief was for the client. This one is for the engineer who inherits the pipeline. Name risks you have actually hit in weeks 2 to 7: the PDF layout shifting, four spellings of one state, CINs that do not join, a source that has no stable download URL.

---

## Station D2: Snowflake Fundamentals, Stages

- [ ] **D2.1** Create the internal stages for all four sources with a clean folder prefix per source. List the stages and prefixes in a table.
  **Commit:** `sql/d2/01_stages.sql` plus the table in `sql/d2/notes.md`, open a pull request.

- [ ] **D2.2** Define the two file format objects the project needs (CSV with header, and any second format you found necessary). Justify each option you set, one line per option.
  **Commit:** `sql/d2/02_file_formats.sql` plus justification in notes, update the pull request.

- [ ] **D2.3** In one paragraph, explain when the team would choose a Snowflake Task over manual COPY INTO, and which of our four sources genuinely justifies one.
  **Commit:** append to `sql/d2/notes.md`, update the pull request.

**On D2.2:** record the encoding each source needed too. If one file only parsed as `latin-1`, that is a real property of the source and the next person must be told.

---

## Station D3: Raw Layer Load, All Sources

- [ ] **D3.1** Load all MCA RoC files into bronze raw tables, one per RoC, all columns VARCHAR, with file name and load timestamp recorded per row.
  **Commit:** `sql/d3/01_mca_raw_loads.sql` plus `sql/d3/load_summary.md`, open a pull request.

- [ ] **D3.2** Load the extracted IBBI CSV, the CDM CSV, and the RBI CSV into their own bronze tables with the same metadata pattern.
  **Commit:** `sql/d3/02_enrichment_raw_loads.sql`, update the pull request.

- [ ] **D3.3** Write the reconciliation query set: for every bronze table, rows in file versus rows in table. Every number must match or carry a written explanation.
  **Commit:** `sql/d3/03_reconciliation.sql` plus results in `sql/d3/load_summary.md`, update the pull request.

**Why the file name and load timestamp matter:** they are the only way, three weeks from now, to answer "which file did this wrong row come from". That is lineage, and it costs two columns.

---

## Station D4: First Snowflake Load **[MILESTONE]**

- [ ] **D4.1** Demonstrate the full manual load path to a teammate: stage, PUT, COPY, verify. Have them repeat it on a different RoC file while you watch. Both of you record what happened in notes.
  **Commit:** `sql/d4/teachback_notes.md` from each of you, open one pull request together.

**On D4.1:** the notes are the deliverable, not the load. Write where they got stuck and what you had to explain twice. That is the honest measure of whether the load path is documented well enough for week 10's handover.

---

## Station D5: dbt Staging Models

- [ ] **D5.1** Initialize the dbt project connected to Snowflake, with bronze sources declared. Commit the project skeleton with a README explaining the folder layout.
  **Commit:** `platform/dbt/` project folder plus `platform/dbt/README.md`, open a pull request.

- [ ] **D5.2** Write the MCA staging model: typed columns, cleaned state names using your P5 frequency map, parsed dates, validated CINs flagged. Add not null and unique tests where they belong.
  **Commit:** `platform/dbt/models/staging/stg_mca.sql` plus its test configuration, update the pull request.

- [ ] **D5.3** Write staging models for the IBBI, CDM, and RBI sources, with the same discipline. Run dbt tests and paste the results.
  **Commit:** the staging models plus `platform/dbt/test_results.md`, update the pull request.

**Never commit `profiles.yml`.** It holds your Snowflake password and it belongs in `~/.dbt/`. Check your diff.

**On D5.2:** bad CINs are flagged, not deleted. Silver types and cleans; it does not decide what counts as a real company. That decision belongs in gold, where it is visible.

**If a dbt model runs but the table is empty,** read `target/compiled/` to see the SQL dbt actually ran. See `docs/10-troubleshooting.md`, dbt section.

---

## End of week checklist

- [ ] D1.1 — one page technical brief with three risks you have actually seen
- [ ] D2.1, D2.2, D2.3 — stages with prefixes, file formats with justified options, the Tasks paragraph
- [ ] D3.1, D3.2, D3.3 — every source in bronze with file name and load timestamp, and a reconciliation line per table
- [ ] D4.1 — teach-back notes from both people, in one pull request
- [ ] D5.1, D5.2, D5.3 — dbt project with a README, four staging models, tests run with results pasted
- [ ] No `profiles.yml`, no `.env`, no data files in any commit
- [ ] If you were on the platform rotation, your entry in `docs/platform-rotation-log.md` is updated

**If you are short on time, cut in this order:** D5.3 (do MCA only), then D2.3. Never cut D3.3 or D4.1. Unreconciled bronze poisons everything above it, and D4 is a milestone.

Next: `week9/problem_statement.md`.
