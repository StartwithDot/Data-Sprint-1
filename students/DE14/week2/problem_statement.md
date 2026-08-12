# Week 2 Tasks

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

## Station P2: Type Hints and Data Validation

- [ ] **P2.1** Add type hints to all three P1 scripts. Every function must declare its input types and return type.
  **Commit:** updated files in `python/p1/`, reference your P1 pull request in the new commit message.

- [ ] **P2.2** Write a validation function that checks one insolvency record: CIN is 21 characters, dates parse, amounts are numbers. It must return clear error messages, not crash. Test it on five good records and five records you deliberately broke.
  **Commit:** `python/p2/record_validator.py` plus test output in `python/p2/notes.md`, open a pull request.

- [ ] **P2.3** Rewrite the validator using pydantic models. List in notes two things pydantic gave you that the manual version did not.
  **Commit:** `python/p2/pydantic_validator.py`, update the pull request.

