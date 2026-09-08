# Week 8 - Window functions and tests

**Data Sprint 1 · Week 8 of 13 · Theme: compare a row to its neighbours, then prove your code works without running it by hand**

Read this whole file before you start. Then work through the task groups in order.

---

## Before you start

Git commands: `docs/03-student-guide.md`. Client story and sources: `docs/01-project-brief.md`. Unknown word: `docs/08-glossary.md`. Broken tool: `docs/10-troubleshooting.md`. What a tool is for: `docs/11-tools-and-technology.md`. Each task names the exact file path to commit to, inside this same week folder.

---

## By the end of this week you can

- Rank, compare to the previous row, split into deciles, and pick the latest row per key
- Say why ROW_NUMBER and not RANK is correct when you need exactly one row
- Prove your validator works with tests that run offline, every time, in CI

---

## The week at a glance

| Step | LEARN | DO |
|---|---|---|
| **1** | Kudvenkat parts 107 to 110 (OVER, ROW_NUMBER) | Task 1 - RANK vs DENSE_RANK |
| **2** | Kudvenkat parts 111 to 114 (LAG, LEAD) | Task 2 - month over month change |
| **3** | Kudvenkat parts 115 to 117 (NTILE and others) | Tasks 3–4 - deciles, latest per company |
| **4** | Real Python "Getting Started With Testing in Python" | Task 5 - validator tests |
| **5** | pytest fixtures section · GitHub Actions basics | Tasks 6–7 - parser fixture, tests in CI |
| **6** | - | Cohort review: window function walkthrough |

---

## 1 · Window Functions

Foundation link: Kudvenkat parts 107 to 117 (OVER, ROW_NUMBER, RANK, LEAD, LAG, NTILE, and others).

- [ ] **Task 1 - RANK vs DENSE_RANK** (ID `S9.1`): Rank states by active company count, using RANK and DENSE_RANK. Show one example where the two give different results, and explain why in two sentences.
  **Commit:** `sql/s9/01_state_rankings.sql`, open a pull request.

- [ ] **Task 2 - Month over month change** (ID `S9.2`): Compute the month over month change in new company registrations per month, using LAG. Which month had the biggest drop?
  **Commit:** `sql/s9/02_mom_registrations.sql`, update the pull request.

- [ ] **Task 3 - Capital deciles** (ID `S9.3`): Split companies into ten deciles by paid up capital within each state using NTILE. How many companies fall in the top decile of Maharashtra?
  **Commit:** `sql/s9/03_capital_deciles.sql`, update the pull request.

- [ ] **Task 4 - Latest row per company** (ID `S9.4`): For each CIN, use ROW_NUMBER over snapshots to pick the latest row per company. Explain in one sentence why ROW_NUMBER and not RANK is the right tool here.
  **Commit:** `sql/s9/04_latest_per_company.sql` plus explanation in `sql/s9/notes.md`, update the pull request.

**Note:** Task 3 (S9.3) has a NULL trap. Paid up capital is missing for many companies, and where those rows land in the deciles changes the answer. Say what you did with them.

**Note:** Task 4 (S9.4) is the pattern the SCD2 build uses next week to find the current version row. Keep it.

---

## 2 · Testing with pytest

- [ ] **Task 5 - Test the validator** (ID `P9.1`): Write pytest tests for your P2 validator: at least five tests covering good records, bad CINs, bad dates, and bad amounts.
  **Commit:** `python/p9/test_validator.py` plus a screenshot or paste of the passing run in `python/p9/notes.md`, open a pull request.

- [ ] **Task 6 - Test the PDF parser offline** (ID `P9.2`): Write tests for the IBBI extractor's parsing logic using a small saved sample of PDF text as a fixture, so tests run offline.
  **Commit:** `python/p9/test_ibbi_parser.py` plus the fixture file, update the pull request.

- [ ] **Task 7 - Run the tests in CI** (ID `P9.3`): Set up the tests to run automatically on every pull request. Paste the passing check from your own pull request as proof.
  **Commit:** the CI configuration file at the repository root, update the pull request.

**On Task 6:** a test that downloads a PDF is not a test, it is a network call that fails on a bad connection. The fixture is a few lines of saved text committed alongside the test, which is why it is allowed in Git while real source files are not.

**If pytest says `no tests ran`**, the file or function name does not start with `test_`. See `docs/10-troubleshooting.md`.

---

## End of week checklist

- [ ] Tasks 1–4 - four queries, each with the answer written down, plus the RANK and ROW_NUMBER explanations
- [ ] Task 5 - five or more validator tests, with a passing run pasted
- [ ] Tasks 6–7 - an offline parser fixture, and a green check on your own pull request
- [ ] At least one teammate's pull request reviewed with a real comment
- [ ] You can explain, out loud, the difference between RANK, DENSE_RANK, and ROW_NUMBER

**If you are short on time, cut in this order:** Task 3 (S9.3), then Task 6 (P9.2). Never cut Task 4 (S9.4). It is next week's SCD2 pattern.

Next: `week9/problem_statement.md`.
