# Week 3 — Missing values, messy strings, first load

**Data Sprint 1 · Week 3 of 10 · Theme: handle what is missing, clean what is messy, and get a file into Snowflake with counts that match**

Read this whole file before you start. Then work through the stations in order.

---

## Before you start

Git commands: `docs/03-student-guide.md`. Client story and sources: `docs/01-project-brief.md`. Unknown word: `docs/08-glossary.md`. Broken tool: `docs/10-troubleshooting.md`. Each task names the exact file path to commit to, inside this same week folder.

---

## By the end of this week you can

- Display missing values without inventing them, and defend that rule in writing
- Compare two monthly snapshots with EXCEPT and INTERSECT
- Clean state names and parse dates safely, so one bad row does not fail the whole query
- Load a file into Snowflake and prove the row counts match

## The milestone this week

**P3 First Snowflake Load.** Every difference between rows in the file and rows in the table is zero, or explained in writing. No exceptions, no rounding, no "close enough".

---

## The week at a glance

| Step | LEARN | DO |
|---|---|---|
| **1** | Kudvenkat parts 14 to 16 · Kudvenkat 86 to 89 | S4.1 S4.2 — NULL display, UNION vs UNION ALL |
| **2** | Set operations in Snowflake docs | S4.3 S4.4 — snapshot comparison, the missing-stays-missing rule |
| **3** | Kudvenkat parts 21 to 24 (string functions) | S5.1 S5.2 — CIN length, cleaned states |
| **4** | Kudvenkat parts 25 to 28 (date, math) | S5.3 S5.4 S5.5 — dates, recovery rate, company age |
| **5** | Snowflake docs "Loading Data" · `COPY INTO` reference | P3.1 P3.2 P3.3 — stage, format, all loads |
| **6** | — | Cohort review: load reconciliation numbers, NULL rule defence |

---

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

**Note:** S4.3 is the same comparison the SCD2 logic performs in week 7. Keep the query and the counts.

---

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

**Note:** the CASE mapping in S5.2 becomes the shared silver-layer cleaning rule in week 8. Write it so a teammate can read it.

---

## Station P3: First Snowflake Load **[MILESTONE]**

- [ ] **P3.1** In Snowflake, create an internal stage and a CSV file format with header skipping and quoted field handling. Write down what each file format option does in one line.
  **Commit:** `sql/p3/01_stage_and_format.sql` plus `sql/p3/notes.md`, open a pull request.

- [ ] **P3.2** PUT one RoC CSV into the stage and COPY it into the raw table. Record the row count loaded and the row count in the file. They must match.
  **Commit:** `sql/p3/02_first_load.sql` plus both counts in notes, update the pull request.

- [ ] **P3.3** Load the remaining RoC files, each into its own raw table. Produce a summary table: file name, rows in file, rows loaded, difference. Every difference must be zero or explained.
  **Commit:** `sql/p3/03_all_loads.sql` plus `sql/p3/load_summary.md`, update the pull request.

**If `COPY INTO` loads zero rows or fewer rows than expected**, that is normal on the first attempt. `docs/10-troubleshooting.md`, Snowflake section, lists the causes in order of likelihood. Diagnose it; do not add `FORCE = TRUE` to make the number look right.

---

## End of week checklist

- [ ] S4.1 to S4.4 — four queries with counts, plus the written NULL rule
- [ ] S5.1 to S5.5 — five queries, each with its answer written down
- [ ] P3.1, P3.2, P3.3 — stage, format, every RoC file loaded, and `load_summary.md` with a zero or an explanation on every line
- [ ] At least one teammate's pull request reviewed with a real comment
- [ ] You can say out loud why bronze columns are VARCHAR and why missing stays missing

**If you are short on time, cut in this order:** S5.4, then S5.5, then S4.2. Never cut P3 or S4.4. P3 is the milestone and the whole cohort waits on it.

Next: `week4/problem_statement.md`.
