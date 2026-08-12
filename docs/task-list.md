# DOTSET Project 1: Task List
## India Company Risk and Verification Data Platform

This is the daily working document. Tasks are organized station by station, following the four roadmap tracks. There is no calendar. Finish one station, then move to the next. Milestone stations are marked with **[MILESTONE]**. The whole group should reach a milestone before anyone moves far past it.

**How to work on every task.** Fork the shared repository once at the start. For each task: pull the latest from the shared repository, do the work in your fork, commit it in the folder named for that task, push to your fork, open a pull request into the shared repository. Every task below ends with its commit or pull request instruction.

**Repository folder structure used throughout:**

```
/dotset-project-1
  /discovery
  /design
  /sql
  /python
  /data-notes
  /dbt
  /quality
  /airflow
  /dashboard
  /delivery
```

---

# TRACK: Business and Delivery

## Station B1: Discovery Brief **[MILESTONE]**

- [ ] **B1.1** Read the client ask in Document 1, section 1. Write a one page discovery brief. It must cover: what we are building, who uses it, what questions it must answer, what is still unclear, and what "done" looks like. Use plain language, as if the client will read it.
  **Commit:** `discovery/discovery_brief.md`, open a pull request for peer review.

- [ ] **B1.2** Write down the five questions you would ask the client if you had thirty minutes with them. Focus on things the brief cannot decide alone, like how far back the history must go, and what "risk" means to them.
  **Commit:** append to `discovery/discovery_brief.md` in a "Open Questions" section, update the same pull request.

## Station B2: Discovery Brief, the Client Ask

- [ ] **B2.1** For each of the four data sources, write three sentences in your own words: what it is, which client question it answers, and how it arrives (file type and cadence). No copying from Document 1.
  **Commit:** `discovery/source_summary.md`, open a pull request.

- [ ] **B2.2** Write the one paragraph business ask you would hand to a new teammate joining tomorrow, so they understand the project without reading anything else.
  **Commit:** `discovery/teammate_onboarding.md`, open a pull request.

## Station B3: Design Record, ERD and Architecture

- [ ] **B3.1** Draw the star schema diagram for the gold layer. It must show dim_company, the insolvency fact table, the state context dimension, and the date dimension, with the join keys labeled. Use draw.io, mermaid, or paper photographed clearly.
  **Commit:** `design/erd.md` (embed the diagram), open a pull request.

- [ ] **B3.2** Write the grain statement for each gold table, in one sentence each, starting with "One row in this table represents...".
  **Commit:** append to `design/erd.md`, update the pull request.

- [ ] **B3.3** Write a half page design record: why Medallion layering, why a Kimball star at gold, why not Data Vault. One honest paragraph each.
  **Commit:** `design/modeling_decision.md`, open a pull request.

## Station B4: Build, PR and Peer Review

- [ ] **B4.1** Review two pull requests from teammates. For each, leave at least one real comment: a question, a spotted mistake, or a suggested improvement. No "looks good" reviews.
  **Commit:** nothing new; paste the links to your two reviewed pull requests in `delivery/review_log.md` and open a pull request with that file.

- [ ] **B4.2** Fix one piece of review feedback you received on your own work, and reply to the reviewer explaining what you changed.
  **Commit:** the fix in its original folder, reference the original pull request in your new commit message.

## Station B5: Break and Fix, Postmortem

- [ ] **B5.1** The program leads will introduce a failure into the project data or pipeline. Find what broke, using logs, tests, and row counts. Write down the evidence trail that led you to the cause.
  **Commit:** `delivery/break_fix_notes.md`, open a pull request.

- [ ] **B5.2** Write a one page postmortem: what broke, why it happened, how it was found, what was done to fix it, and what one change would stop it from happening again.
  **Commit:** `delivery/postmortem.md`, open a pull request.

## Station B6: Metabase Dashboard

- [ ] **B6.1** Build a dashboard in Metabase on top of the gold tables with at least these four views: company status counts by state, insolvency events by quarter, capital distribution by business activity, and a company search that shows current status plus status history.
  **Commit:** export or screenshot the dashboard definition into `dashboard/dashboard_definition.md` with a short description of each view, open a pull request.

- [ ] **B6.2** Write the plain language label and one sentence explanation for each dashboard view, as it should appear to a non technical analyst.
  **Commit:** append to `dashboard/dashboard_definition.md`, update the pull request.

## Station B7: Stakeholder Delivery

- [ ] **B7.1** Write a five minute stakeholder presentation script. It must contain zero tool names. It must say what the data shows, what the client should do with it, and what the platform cannot tell them.
  **Commit:** `delivery/presentation_script.md`, open a pull request.

- [ ] **B7.2** Present to a peer playing the client. Record their three hardest questions and your answers, or "I did not know" where true.
  **Commit:** `delivery/qa_log.md`, open a pull request.

## Station B8: Project Handover **[MILESTONE]**

- [ ] **B8.1** Write the runbook: how to refresh each data source, what to check when a run fails, who to contact for what, and where every piece of documentation lives.
  **Commit:** `delivery/runbook.md`, open a pull request.

- [ ] **B8.2** Write the final README for the repository root, so a stranger can understand what this project is, how it is structured, and how to run it.
  **Commit:** `/README.md`, open a pull request.

---

# TRACK: SQL and Data Modeling

## Station S1: Databases and Tables

Foundation link: Kudvenkat parts 1 to 2 (databases, tables).

- [ ] **S1.1** In Snowflake, create the project database and three schemas named BRONZE, SILVER, and GOLD. Write down in one sentence what each schema will hold.
  **Commit:** `sql/s1/01_create_database.sql` plus `sql/s1/notes.md`, open a pull request.

- [ ] **S1.2** Create the raw MCA table in BRONZE with one VARCHAR column per field in the RoC CSVs. Explain in one sentence why every column is VARCHAR at this stage.
  **Commit:** `sql/s1/02_create_raw_mca.sql`, update the pull request.

- [ ] **S1.3** Which columns in the raw MCA table must never be empty for a row to be a real company record? List them and explain why in one sentence each.
  **Commit:** append to `sql/s1/notes.md`, update the pull request.

## Station S2: Constraints and Data Integrity

Foundation link: Kudvenkat parts 3 to 8 (constraints, identity, unique keys).

- [ ] **S2.1** Write a query that finds any rows in the raw MCA table where CIN is empty or NULL. How many did you find in your loaded data?
  **Commit:** `sql/s2/01_null_cin_check.sql` plus the result count in `sql/s2/notes.md`, open a pull request.

- [ ] **S2.2** Write a query that finds duplicate CIN values within one RoC file's raw table. List the first ten duplicate CINs you find.
  **Commit:** `sql/s2/02_duplicate_cin.sql`, update the pull request.

- [ ] **S2.3** Snowflake does not enforce UNIQUE or CHECK constraints. In three sentences, explain how the team should enforce "one company, one CIN" anyway.
  **Commit:** append to `sql/s2/notes.md`, update the pull request.

## Station S3: SELECT, GROUP BY, Joins

Foundation link: Kudvenkat parts 9 to 13 (SELECT, GROUP BY, joins, self join).

- [ ] **S3.1** How many companies are in each company status, across the whole registry? Order from most common to least common.
  **Commit:** `sql/s3/01_status_counts.sql`, open a pull request.

- [ ] **S3.2** How many active companies are registered in each state? Name the top five states and their counts.
  **Commit:** `sql/s3/02_active_by_state.sql`, update the pull request.

- [ ] **S3.3** Join the IBBI insolvency rows to the MCA registry on CIN. How many insolvency rows found a matching company? How many did not?
  **Commit:** `sql/s3/03_cirp_join_counts.sql`, update the pull request.

- [ ] **S3.4** List ten insolvency CINs that did not match the registry, with their company names from the IBBI file. In two sentences, suggest why they might not match.
  **Commit:** `sql/s3/04_unmatched_cins.sql` plus explanation in `sql/s3/notes.md`, update the pull request.

- [ ] **S3.5** Using a self join on two monthly snapshots of the registry, list companies whose status was Active last month and is Strike Off this month. How many are there?
  **Commit:** `sql/s3/05_status_change_selfjoin.sql`, update the pull request.

## Station S4: NULL Handling and Set Operations

Foundation link: Kudvenkat parts 14 to 16 (NULL replacement, COALESCE, UNION) and parts 86 to 89 (EXCEPT, INTERSECT).

- [ ] **S4.1** How many rows in the raw MCA table have empty or NULL paid up capital? Write a query that shows them as "Not reported" in the output without changing the stored data.
  **Commit:** `sql/s4/01_null_capital.sql`, open a pull request.

- [ ] **S4.2** Combine all RoC raw tables into one list of CIN and company name using UNION ALL. Then do it with UNION. Report both row counts and explain the difference in two sentences.
  **Commit:** `sql/s4/02_union_all_vs_union.sql` plus counts in `sql/s4/notes.md`, update the pull request.

- [ ] **S4.3** Using EXCEPT or MINUS, list CINs that existed in last month's snapshot but not in this month's. How many disappeared? Then list CINs present in both months using INTERSECT.
  **Commit:** `sql/s4/03_except_intersect.sql`, update the pull request.

- [ ] **S4.4** In one paragraph, explain why the team rule is "missing stays missing" for capital fields, and what would go wrong for the client if zeros were written instead.
  **Commit:** append to `sql/s4/notes.md`, update the pull request.

## Station S5: Functions (String, Date, Math)

Foundation link: Kudvenkat parts 21 to 28 (string, date, math functions).

- [ ] **S5.1** Write a query that checks every CIN is exactly 21 characters. List any that are not, with their lengths.
  **Commit:** `sql/s5/01_cin_length_check.sql`, open a pull request.

- [ ] **S5.2** Build a cleaned state column: uppercase, trimmed, with spelling variants mapped to one standard name using CASE. Show before and after counts per state.
  **Commit:** `sql/s5/02_clean_states.sql`, update the pull request.

- [ ] **S5.3** Parse the registration date strings into real dates, using safe parsing that returns NULL instead of failing. How many rows failed to parse? List five examples.
  **Commit:** `sql/s5/03_parse_dates.sql` plus the failure count in `sql/s5/notes.md`, update the pull request.

- [ ] **S5.4** For each insolvency case with both admitted claims and realizable amounts, compute the recovery rate as a percentage rounded to one decimal. Which ten cases have the lowest recovery rates?
  **Commit:** `sql/s5/04_recovery_rate.sql`, update the pull request.

- [ ] **S5.5** Compute each company's age in completed years at the snapshot date. Why does DATEDIFF in years give the wrong answer? Show both calculations for five companies.
  **Commit:** `sql/s5/05_company_age.sql` plus explanation in `sql/s5/notes.md`, update the pull request.

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

## Station S8: Normalization and Star Schema

Foundation link: Kudvenkat parts 51 to 53 (normalization, pivot).

- [ ] **S8.1** In three short paragraphs, explain: why the bronze layer is not normalized, why the gold layer is a denormalized star, and what problem each choice solves.
  **Commit:** `design/normalization_notes.md`, open a pull request.

- [ ] **S8.2** Pivot company counts so each state's row shows separate columns for Active, Strike Off, and Under Liquidation. Which state has the highest Strike Off column?
  **Commit:** `sql/s8/01_pivot_states.sql`, update the pull request.

## Station S9: Window Functions

Foundation link: Kudvenkat parts 107 to 117 (OVER, ROW_NUMBER, RANK, LEAD, LAG, NTILE, and others).

- [ ] **S9.1** Rank states by active company count, using RANK and DENSE_RANK. Show one example where the two give different results, and explain why in two sentences.
  **Commit:** `sql/s9/01_state_rankings.sql`, open a pull request.

- [ ] **S9.2** Compute the month over month change in new company registrations per month, using LAG. Which month had the biggest drop?
  **Commit:** `sql/s9/02_mom_registrations.sql`, update the pull request.

- [ ] **S9.3** Split companies into ten deciles by paid up capital within each state using NTILE. How many companies fall in the top decile of Maharashtra?
  **Commit:** `sql/s9/03_capital_deciles.sql`, update the pull request.

- [ ] **S9.4** For each CIN, use ROW_NUMBER over snapshots to pick the latest row per company. Explain in one sentence why ROW_NUMBER and not RANK is the right tool here.
  **Commit:** `sql/s9/04_latest_per_company.sql` plus explanation in `sql/s9/notes.md`, update the pull request.

## Station S10: MERGE and SCD2 Build

Foundation link: Kudvenkat part 68 (MERGE) and Station S9 window functions.

- [ ] **S10.1** Write the change detection query: join this month's snapshot to last month's on CIN and list every company where status, capital, or address changed. How many changes of each type?
  **Commit:** `sql/s10/01_change_detection.sql`, open a pull request.

- [ ] **S10.2** Write the MERGE statement that applies the month changes to dim_company: close changed rows with an end date, insert new version rows, insert brand new companies. Run it on a test copy first and report row counts before and after.
  **Commit:** `sql/s10/02_scd2_merge.sql` plus counts in `sql/s10/notes.md`, open a pull request.

- [ ] **S10.3** Write a query that answers: "What was company CIN X's status on 1 March 2026?" for three companies that changed status this year.
  **Commit:** `sql/s10/03_point_in_time.sql`, update the pull request.

---

# TRACK: Python

## Station P1: Python Basics, Files and Functions

- [ ] **P1.1** Write a script that opens one RoC CSV file, counts the rows, and prints the count with the file name. Run it on three different RoC files.
  **Commit:** `python/p1/row_counter.py` plus output pasted in `python/p1/notes.md`, open a pull request.

- [ ] **P1.2** Write a function that takes a file path and returns the column names from the CSV header line. Use it to verify two RoC files have identical headers. Report whether they match.
  **Commit:** `python/p1/header_check.py` plus result in notes, update the pull request.

- [ ] **P1.3** Write a script that reads one raw CSV and writes a new CSV containing only rows where the state is a given value passed as text. Test it with "Kerala" on two files.
  **Commit:** `python/p1/state_filter.py`, update the pull request.

## Station P2: Type Hints and Data Validation

- [ ] **P2.1** Add type hints to all three P1 scripts. Every function must declare its input types and return type.
  **Commit:** updated files in `python/p1/`, reference your P1 pull request in the new commit message.

- [ ] **P2.2** Write a validation function that checks one insolvency record: CIN is 21 characters, dates parse, amounts are numbers. It must return clear error messages, not crash. Test it on five good records and five records you deliberately broke.
  **Commit:** `python/p2/record_validator.py` plus test output in `python/p2/notes.md`, open a pull request.

- [ ] **P2.3** Rewrite the validator using pydantic models. List in notes two things pydantic gave you that the manual version did not.
  **Commit:** `python/p2/pydantic_validator.py`, update the pull request.

## Station P3: First Snowflake Load **[MILESTONE]**

- [ ] **P3.1** In Snowflake, create an internal stage and a CSV file format with header skipping and quoted field handling. Write down what each file format option does in one line.
  **Commit:** `sql/p3/01_stage_and_format.sql` plus `sql/p3/notes.md`, open a pull request.

- [ ] **P3.2** PUT one RoC CSV into the stage and COPY it into the raw table. Record the row count loaded and the row count in the file. They must match.
  **Commit:** `sql/p3/02_first_load.sql` plus both counts in notes, update the pull request.

- [ ] **P3.3** Load the remaining RoC files, each into its own raw table. Produce a summary table: file name, rows in file, rows loaded, difference. Every difference must be zero or explained.
  **Commit:** `sql/p3/03_all_loads.sql` plus `sql/p3/load_summary.md`, update the pull request.

## Station P4: Retry Logic and Context Managers

- [ ] **P4.1** Write a retry decorator that retries a failed function up to three times with a waiting gap that doubles each time. Test it on a function that fails twice then succeeds.
  **Commit:** `python/p4/retry_decorator.py` plus test output in `python/p4/notes.md`, open a pull request.

- [ ] **P4.2** Write the RBI download script: fetch the policy rate file, retry on failure using your decorator, save it untouched into `data/raw/rbi/` with the pull date in the file name.
  **Commit:** `python/p4/rbi_download.py`, update the pull request.

- [ ] **P4.3** Rewrite your file handling in P1 and P2 scripts using context managers so files always close safely. Note in one sentence what problem this prevents.
  **Commit:** updated scripts, plus note in `python/p4/notes.md`, update the pull request.

## Station P5: Generators and Large File Handling

- [ ] **P5.1** Write a generator that yields one row at a time from a large RoC CSV without loading the whole file into memory. Use it to count rows and to count rows with empty capital fields, in one pass.
  **Commit:** `python/p5/row_generator.py` plus counts in `python/p5/notes.md`, open a pull request.

- [ ] **P5.2** Use the generator to build a state name frequency map for the largest RoC file: every distinct state spelling and its row count. This map will feed the silver layer cleaning rules.
  **Commit:** `python/p5/state_frequency.py` plus the top twenty entries in notes, update the pull request.

- [ ] **P5.3** In three sentences, explain why the generator version can handle a file larger than your laptop's memory while the P1 approach cannot.
  **Commit:** append to `python/p5/notes.md`, update the pull request.

## Station P6: Logging and CLI Tools

- [ ] **P6.1** Replace every print call in your P4 and P5 scripts with proper logging: INFO for progress, WARNING for skipped rows, ERROR for failures. Logs must include timestamps.
  **Commit:** updated scripts in `python/p4/` and `python/p5/`, reference the original pull requests in the commit message.

- [ ] **P6.2** Turn the RBI download script into a command line tool: it must accept an output folder argument and a date argument, with helpful error messages for bad input.
  **Commit:** `python/p6/rbi_cli.py` plus example invocations in `python/p6/notes.md`, open a pull request.

## Station P7: OOP and Custom Extractors

- [ ] **P7.1** Write the IBBI PDF extractor: download the CIRP PDF, extract the table rows, validate each row with your P2 validator, and write one CSV to `data/raw/ibbi/` named with the quarter and pull date.
  **Commit:** `python/p7/ibbi_extractor.py` plus the first ten extracted rows in `python/p7/notes.md`, open a pull request.

- [ ] **P7.2** Write the MCA CDM portal extractor: read the state statistics table from the web page, convert Indian number formats to plain numbers, and write one CSV to `data/raw/cdm/`.
  **Commit:** `python/p7/cdm_extractor.py` plus sample output, update the pull request.

- [ ] **P7.3** Refactor all three extractors (RBI, IBBI, CDM) behind one abstract base class with a shared pull, validate, and save contract. Each source becomes a subclass. Write two sentences on what the refactor removed.
  **Commit:** `python/p7/extractors/` folder with the refactored code plus notes, update the pull request.

## Station P8: Star Schema Design **[MILESTONE]**

- [ ] **P8.1** Join the group design review. Bring one written paragraph: which part of the pipeline your Python work feeds, and what can go wrong in it that the design must survive.
  **Commit:** `design/pipeline_risk_notes.md`, open a pull request.

## Station P9: Testing with pytest

- [ ] **P9.1** Write pytest tests for your P2 validator: at least five tests covering good records, bad CINs, bad dates, and bad amounts.
  **Commit:** `python/p9/test_validator.py` plus a screenshot or paste of the passing run in `python/p9/notes.md`, open a pull request.

- [ ] **P9.2** Write tests for the IBBI extractor's parsing logic using a small saved sample of PDF text as a fixture, so tests run offline.
  **Commit:** `python/p9/test_ibbi_parser.py` plus the fixture file, update the pull request.

- [ ] **P9.3** Set up the tests to run automatically on every pull request. Paste the passing check from your own pull request as proof.
  **Commit:** the CI configuration file at the repository root, update the pull request.

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

## Station P12: SCD2 Build **[MILESTONE]**

- [ ] **P12.1** Write the monthly snapshot preparation script: download the new RoC files, verify row counts against the catalog page, land them in the stage, and log a one line summary per file.
  **Commit:** `python/p12/snapshot_prep.py`, open a pull request.

- [ ] **P12.2** Run the full monthly refresh end to end on test schemas: land new files, run the silver models, run the SCD2 merge, run the quality checks. Paste the final status of every step.
  **Commit:** `python/p12/refresh_run_log.md`, update the pull request.

---

# TRACK: Data Platform

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

## Station D6: Medallion plus Kimball

- [ ] **D6.1** Write the layer contract: one short section each for bronze, silver, and gold, stating what is allowed in that layer and what is forbidden. Example: no business logic in bronze, no untyped columns in silver, no uncleaned codes in gold.
  **Commit:** `design/layer_contract.md`, open a pull request.

- [ ] **D6.2** Map every source column to its final home: which gold table and which gold column it ends in, or "dropped" with a reason. A table is expected.
  **Commit:** `design/column_mapping.md`, update the pull request.

## Station D7: dbt Marts, Gold Layer, SCD2

- [ ] **D7.1** Build dim_date as a dbt model covering every date the project needs, with columns for year, quarter, month, and week.
  **Commit:** `dbt/models/marts/dim_date.sql`, open a pull request.

- [ ] **D7.2** Build dim_company as an SCD2 dbt snapshot or merge model, tracking status, capital, and address with start and end dates. Prove it works: show one company with two version rows after two monthly runs.
  **Commit:** `dbt/models/marts/dim_company.sql` plus proof query results in `dbt/scd2_proof.md`, update the pull request.

- [ ] **D7.3** Build fct_cirp_event joined to the company dimension by CIN, and the state context dimension from CDM data. Add relationship tests from fact to dimension.
  **Commit:** `dbt/models/marts/fct_cirp_event.sql` and `dbt/models/marts/dim_state.sql` plus test results, update the pull request.

## Station D8: Great Expectations

- [ ] **D8.1** Write expectation suites for the raw MCA files: CIN length, allowed status values, no fully empty rows, state names within the known list.
  **Commit:** `quality/expectations/mca_suite.json` (or the format your setup uses) plus a run report in `quality/notes.md`, open a pull request.

- [ ] **D8.2** Write the gold layer gate: every CIN in fct_cirp_event must exist in dim_company, every end date must be after its start date, no overlapping version periods per company. Run it against the built marts and paste results.
  **Commit:** `quality/expectations/gold_suite.json` plus run report, update the pull request.

- [ ] **D8.3** In three sentences, explain what Great Expectations catches that dbt tests do not, and why the project runs both.
  **Commit:** append to `quality/notes.md`, update the pull request.

## Station D9: Airflow Orchestration

- [ ] **D9.1** Write the monthly refresh DAG: snapshot preparation, bronze loads, dbt build, Great Expectations gate, with correct dependency order. Draw or describe the dependency graph in notes.
  **Commit:** `airflow/monthly_refresh_dag.py` plus `airflow/notes.md`, open a pull request.

- [ ] **D9.2** Add the failure behavior: the quality gate must stop the pipeline before gold tables are touched, and the failure must be visible in logs with the source file named.
  **Commit:** updated DAG plus a paste of a deliberate failure run in `airflow/notes.md`, update the pull request.

## Station D10: Project Handover **[MILESTONE]**

- [ ] **D10.1** Run the full pipeline from a clean checkout on a fresh Snowflake schema, following only the runbook. Record every place the runbook was unclear or wrong, and fix it.
  **Commit:** updated `delivery/runbook.md` plus `delivery/clean_run_log.md`, open a pull request.

- [ ] **D10.2** Archive the project: final README, all documentation linked, every pull request merged or explicitly closed with a reason.
  **Commit:** final state of the repository, final pull request titled "Project handover".
