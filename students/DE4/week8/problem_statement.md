# Week 8 Tasks

## Station D1: Discovery Brief **[MILESTONE]**

- [ ] **D1.1** Write the technical half of the discovery brief: the four sources, their formats, their cadences, and the top three technical risks you see. One page maximum.
  **Commit:** `discovery/technical_brief.md`, open a pull request.

## Station D2: Snowflake Fundamentals, Stages

- [ ] **D2.1** Create the internal stages for all four sources with a clean folder prefix per source. List the stages and prefixes in a table.
  **Commit:** `sql/d2/01_stages.sql` plus the table in `sql/d2/notes.md`, open a pull request.

- [ ] **D2.2** Define the two file format objects the project needs (CSV with header, and any second format you found necessary). Justify each option you set, one line per option.
  **Commit:** `sql/d2/02_file_formats.sql` plus justification in notes, update the pull request.

- [ ] **D2.3** In one paragraph, explain when the team would choose a Snowflake Task over manual COPY INTO, and which of our four sources genuinely justifies one.
  **Commit:** append to `sql/d2/notes.md`, update the pull request.

## Station D3: Raw Layer Load, All Sources

- [ ] **D3.1** Load all MCA RoC files into bronze raw tables, one per RoC, all columns VARCHAR, with file name and load timestamp recorded per row.
  **Commit:** `sql/d3/01_mca_raw_loads.sql` plus `sql/d3/load_summary.md`, open a pull request.

- [ ] **D3.2** Load the extracted IBBI CSV, the CDM CSV, and the RBI CSV into their own bronze tables with the same metadata pattern.
  **Commit:** `sql/d3/02_enrichment_raw_loads.sql`, update the pull request.

- [ ] **D3.3** Write the reconciliation query set: for every bronze table, rows in file versus rows in table. Every number must match or carry a written explanation.
  **Commit:** `sql/d3/03_reconciliation.sql` plus results in `sql/d3/load_summary.md`, update the pull request.

## Station D4: First Snowflake Load **[MILESTONE]**

- [ ] **D4.1** Demonstrate the full manual load path to a teammate: stage, PUT, COPY, verify. Have them repeat it on a different RoC file while you watch. Both of you record what happened in notes.
  **Commit:** `sql/d4/teachback_notes.md` from each of you, open one pull request together.

## Station D5: dbt Staging Models

- [ ] **D5.1** Initialize the dbt project connected to Snowflake, with bronze sources declared. Commit the project skeleton with a README explaining the folder layout.
  **Commit:** `/dbt/` project folder plus `dbt/README.md`, open a pull request.

- [ ] **D5.2** Write the MCA staging model: typed columns, cleaned state names using your P5 frequency map, parsed dates, validated CINs flagged. Add not null and unique tests where they belong.
  **Commit:** `dbt/models/staging/stg_mca.sql` plus its test configuration, update the pull request.

- [ ] **D5.3** Write staging models for the IBBI, CDM, and RBI sources, with the same discipline. Run dbt tests and paste the results.
  **Commit:** the staging models plus `dbt/test_results.md`, update the pull request.

