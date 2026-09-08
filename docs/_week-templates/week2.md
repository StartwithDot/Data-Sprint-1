# Week 2 - Trust the data, join the data

**Data Sprint 1 · Week 2 of 13 · Theme: find what is wrong with the data, then make two sources talk to each other**

Read this whole file before you start. Then work through the task groups in order.

---

## Before you start

Setup steps and Git commands: `docs/03-student-guide.md`. Client story and the four sources: `docs/01-project-brief.md`. Unknown word: `docs/08-glossary.md`. Broken tool: `docs/10-troubleshooting.md`. What a tool is for: `docs/11-tools-and-technology.md`. Each task names the exact file path to commit to, inside this same week folder.

---

## By the end of this week you can

- Find NULL and duplicate keys in a real registry, and say what to do about them
- Answer a business question with GROUP BY, not with a spreadsheet
- Join two sources on CIN and explain the rows that do not match
- Validate a record instead of trusting it, first by hand and then with pydantic

## The thing to watch this week

Everyone's IBBI to MCA join leaves unmatched rows. The count is easy. The *explanation* is the work, and it is what you will be asked about at the cohort review.

---

## The week at a glance

| Step | LEARN | DO |
|---|---|---|
| **1** | Kudvenkat parts 3 to 8 · Snowflake docs on constraints | Tasks 1–3 - integrity checks |
| **2** | Kudvenkat parts 9 to 11 (SELECT, GROUP BY) | Tasks 4–5 - status and state counts |
| **3** | Kudvenkat parts 12 to 13 (joins, self join) | Tasks 6–8 - the IBBI join, the unmatched list, the status-change self join |
| **4** | Python docs `typing` intro | Task 9 - type hints |
| **5** | pydantic docs, "Models" page | Tasks 10–11 - validator by hand, then with pydantic |
| **6** | - | Cohort review: unmatched CIN explanations, validation approaches |

---

## 1 · Data Integrity: Constraints

Foundation link: Kudvenkat parts 3 to 8 (constraints, identity, unique keys). Remember Snowflake does not enforce UNIQUE or CHECK; see `docs/09-resources.md` for the full difference list.

- [ ] **Task 1 - Find empty CINs** (ID `S2.1`): Write a query that finds any rows in the raw MCA table where CIN is empty or NULL. How many did you find in your loaded data?
  **Commit:** `sql/s2/01_null_cin_check.sql` plus the result count in `sql/s2/notes.md`, open a pull request.

- [ ] **Task 2 - Find duplicate CINs** (ID `S2.2`): Write a query that finds duplicate CIN values within one RoC file's raw table. List the first ten duplicate CINs you find.
  **Commit:** `sql/s2/02_duplicate_cin.sql`, update the pull request.

- [ ] **Task 3 - Enforce one company, one CIN** (ID `S2.3`): Snowflake does not enforce UNIQUE or CHECK constraints. In three sentences, explain how the team should enforce "one company, one CIN" anyway.
  **Commit:** append to `sql/s2/notes.md`, update the pull request.

---

## 2 · Queries, Grouping and Joins

Foundation link: Kudvenkat parts 9 to 13 (SELECT, GROUP BY, joins, self join).

- [ ] **Task 4 - Count companies by status** (ID `S3.1`): How many companies are in each company status, across the whole registry? Order from most common to least common.
  **Commit:** `sql/s3/01_status_counts.sql`, open a pull request.

- [ ] **Task 5 - Count active companies by state** (ID `S3.2`): How many active companies are registered in each state? Name the top five states and their counts.
  **Commit:** `sql/s3/02_active_by_state.sql`, update the pull request.

- [ ] **Task 6 - Join IBBI to the registry** (ID `S3.3`): Join the IBBI insolvency rows to the MCA registry on CIN. How many insolvency rows found a matching company? How many did not?
  **Commit:** `sql/s3/03_cirp_join_counts.sql`, update the pull request.

- [ ] **Task 7 - Explain the unmatched CINs** (ID `S3.4`): List ten insolvency CINs that did not match the registry, with their company names from the IBBI file. In two sentences, suggest why they might not match.
  **Commit:** `sql/s3/04_unmatched_cins.sql` plus explanation in `sql/s3/notes.md`, update the pull request.

- [ ] **Task 8 - Compare two monthly snapshots** (ID `S3.5`): Using a self join on two monthly snapshots of the registry, list companies whose status was Active last month and is Strike Off this month. How many are there?
  **Commit:** `sql/s3/05_status_change_selfjoin.sql`, update the pull request.

**Note:** Task 8 (S3.5) is the first time you compute a change between two months. Week 9 turns exactly this into the SCD2 logic, so keep the query.

---

## 3 · Type Hints and Data Validation

- [ ] **Task 9 - Add type hints** (ID `P2.1`): Add type hints to all three P1 scripts. Every function must declare its input types and return type.
  **Commit:** updated files in `python/p1/`, reference your P1 pull request in the new commit message.

- [ ] **Task 10 - Write a validator by hand** (ID `P2.2`): Write a validation function that checks one insolvency record: CIN is 21 characters, dates parse, amounts are numbers. It must return clear error messages, not crash. Test it on five good and five bad records.
  **Commit:** `python/p2/record_validator.py` plus test output in `python/p2/notes.md`, open a pull request.

- [ ] **Task 11 - Rewrite the validator with pydantic** (ID `P2.3`): Rewrite the validator using pydantic models. List in notes two things pydantic gave you that the manual version did not.
  **Commit:** `python/p2/pydantic_validator.py`, update the pull request.

**Note:** this validator is reused in week 7 (P7 extractors) and week 8 (P9 tests). Write it as if someone else will call it.

---

## End of week checklist

- [ ] Tasks 1–3 - integrity checks with counts, plus the enforcement argument in notes
- [ ] Tasks 4–8 - five queries, each with its answer written down, not just the SQL
- [ ] Tasks 9–11 - type hints, hand-written validator, pydantic version, and the comparison
- [ ] At least one teammate's pull request reviewed with a real comment
- [ ] Your unmatched CIN explanation is written in your own words and you can say it out loud

**If you are short on time, cut in this order:** Task 5 (S3.2), then Task 11 (P2.3). Never cut Tasks 6–7 (S3.3, S3.4) or the notes files. The join and its unmatched rows are the point of the week.

Next: `week3/problem_statement.md`.
