# Week 3 — Missing values, messy strings

**Data Sprint 1 · Week 3 of 13 · Theme: handle what is missing and clean what is messy, so the data says what it means**

Read this whole file before you start. Then work through the task groups in order.

---

## Before you start

Git commands: `docs/03-student-guide.md`. Client story and sources: `docs/01-project-brief.md`. Unknown word: `docs/08-glossary.md`. Broken tool: `docs/10-troubleshooting.md`. What a tool is for: `docs/11-tools-and-technology.md`. Each task names the exact file path to commit to, inside this same week folder.

---

## By the end of this week you can

- Display missing values without inventing them, and defend that rule in writing
- Compare two monthly snapshots with EXCEPT and INTERSECT
- Clean state names and parse dates safely, so one bad row does not fail the whole query

---

## The week at a glance

| Step | LEARN | DO |
|---|---|---|
| **1** | Kudvenkat parts 14 to 16 · Kudvenkat 86 to 89 | Tasks 1–2 — NULL display, UNION vs UNION ALL |
| **2** | Set operations in Snowflake docs | Tasks 3–4 — snapshot comparison, the missing-stays-missing rule |
| **3** | Kudvenkat parts 21 to 24 (string functions) | Tasks 5–6 — CIN length, cleaned states |
| **4** | Kudvenkat parts 25 to 28 (date, math) | Tasks 7–9 — dates, recovery rate, company age |
| **5** | — | Cohort review: NULL rule defence |

---

## 1 · Missing Values and Set Operations

Foundation link: Kudvenkat parts 14 to 16 (NULL replacement, COALESCE, UNION) and parts 86 to 89 (EXCEPT, INTERSECT).

- [ ] **Task 1 — Show missing capital** (ID `S4.1`): How many rows in the raw MCA table have empty or NULL paid up capital? Write a query that shows them as "Not reported" in the output without changing the stored data.
  **Commit:** `sql/s4/01_null_capital.sql`, open a pull request.

- [ ] **Task 2 — UNION ALL vs UNION** (ID `S4.2`): Combine all RoC raw tables into one list of CIN and company name using UNION ALL. Then do it with UNION. Report both row counts and explain the difference in two sentences.
  **Commit:** `sql/s4/02_union_all_vs_union.sql` plus counts in `sql/s4/notes.md`, update the pull request.

- [ ] **Task 3 — Compare two snapshots** (ID `S4.3`): Using EXCEPT or MINUS, list CINs that existed in last month's snapshot but not in this month's. How many disappeared? Then list CINs present in both months using INTERSECT.
  **Commit:** `sql/s4/03_except_intersect.sql`, update the pull request.

- [ ] **Task 4 — Defend the missing-stays-missing rule** (ID `S4.4`): In one paragraph, explain why the team rule is "missing stays missing" for capital fields, and what would go wrong for the client if zeros were written instead.
  **Commit:** append to `sql/s4/notes.md`, update the pull request.

**Note:** Task 3 (S4.3) is the same comparison the SCD2 logic performs in week 9. Keep the query and the counts.

---

## 2 · SQL Functions: String, Date, Math

Foundation link: Kudvenkat parts 21 to 28 (string, date, math functions).

- [ ] **Task 5 — Check CIN length** (ID `S5.1`): Write a query that checks every CIN is exactly 21 characters. List any that are not, with their lengths.
  **Commit:** `sql/s5/01_cin_length_check.sql`, open a pull request.

- [ ] **Task 6 — Clean the state column** (ID `S5.2`): Build a cleaned state column: uppercase, trimmed, with spelling variants mapped to one standard name using CASE. Show before and after counts per state.
  **Commit:** `sql/s5/02_clean_states.sql`, update the pull request.

- [ ] **Task 7 — Parse registration dates** (ID `S5.3`): Parse the registration date strings into real dates, using safe parsing that returns NULL instead of failing. How many rows failed to parse? List five examples.
  **Commit:** `sql/s5/03_parse_dates.sql` plus the failure count in `sql/s5/notes.md`, update the pull request.

- [ ] **Task 8 — Compute recovery rates** (ID `S5.4`): For each insolvency case with both admitted claims and realizable amounts, compute the recovery rate as a percentage rounded to one decimal. Which ten cases have the lowest recovery rates?
  **Commit:** `sql/s5/04_recovery_rate.sql`, update the pull request.

- [ ] **Task 9 — Compute company age** (ID `S5.5`): Compute each company's age in completed years at the snapshot date. Why does DATEDIFF in years give the wrong answer? Show both calculations for five companies.
  **Commit:** `sql/s5/05_company_age.sql` plus explanation in `sql/s5/notes.md`, update the pull request.

**Note:** the CASE mapping in Task 6 (S5.2) becomes the shared silver-layer cleaning rule in week 10. Write it so a teammate can read it.

---

## End of week checklist

- [ ] Tasks 1–4 — four queries with counts, plus the written NULL rule
- [ ] Tasks 5–9 — five queries, each with its answer written down
- [ ] At least one teammate's pull request reviewed with a real comment
- [ ] You can say out loud why bronze columns are VARCHAR and why missing stays missing

**If you are short on time, cut in this order:** Task 8 (S5.4), then Task 9 (S5.5), then Task 2 (S4.2). Never cut Task 4 (S4.4). The written rule cannot be added back later.

Next: `week4/problem_statement.md`.
