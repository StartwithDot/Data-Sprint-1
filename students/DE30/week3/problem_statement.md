# Week 3 Tasks

> **Before you start:** the setup steps and daily Git commands are in `docs/student-guide.md`. The client story and the four data sources are in `docs/project-brief.md`. Each task below tells you the exact file path to commit to, and that path sits inside this same week folder.

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

## Station P3: First Snowflake Load **[MILESTONE]**

- [ ] **P3.1** In Snowflake, create an internal stage and a CSV file format with header skipping and quoted field handling. Write down what each file format option does in one line.
  **Commit:** `sql/p3/01_stage_and_format.sql` plus `sql/p3/notes.md`, open a pull request.

- [ ] **P3.2** PUT one RoC CSV into the stage and COPY it into the raw table. Record the row count loaded and the row count in the file. They must match.
  **Commit:** `sql/p3/02_first_load.sql` plus both counts in notes, update the pull request.

- [ ] **P3.3** Load the remaining RoC files, each into its own raw table. Produce a summary table: file name, rows in file, rows loaded, difference. Every difference must be zero or explained.
  **Commit:** `sql/p3/03_all_loads.sql` plus `sql/p3/load_summary.md`, update the pull request.

