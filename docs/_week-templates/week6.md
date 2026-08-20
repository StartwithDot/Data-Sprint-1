# Week 6 — Window functions and tests

**Data Sprint 1 · Week 6 of 10 · Theme: compare a row to its neighbours, then prove your code works without running it by hand**

Read this whole file before you start. Then work through the stations in order.

---

## Before you start

Git commands: `docs/03-student-guide.md`. Client story and sources: `docs/01-project-brief.md`. Unknown word: `docs/08-glossary.md`. Broken tool: `docs/10-troubleshooting.md`. Each task names the exact file path to commit to, inside this same week folder.

---

## By the end of this week you can

- Rank, compare to the previous row, split into deciles, and pick the latest row per key
- Say why ROW_NUMBER and not RANK is correct when you need exactly one row
- Prove your validator works with tests that run offline, every time, in CI

## The milestone this week

**P8 Star Schema Design, Python side.** The design agreed in week 4 must survive what the Python work now says can go wrong. If your extractor produces duplicate CINs or unparseable dates, the design has to handle it, and this is the week to say so.

---

## The week at a glance

| Step | LEARN | DO |
|---|---|---|
| **1** | Kudvenkat parts 107 to 110 (OVER, ROW_NUMBER) | S9.1 — RANK vs DENSE_RANK |
| **2** | Kudvenkat parts 111 to 114 (LAG, LEAD) | S9.2 — month over month change |
| **3** | Kudvenkat parts 115 to 117 (NTILE and others) | S9.3 S9.4 — deciles, latest per company |
| **4** | Real Python "Getting Started With Testing in Python" | P8.1 P9.1 — risk paragraph, validator tests |
| **5** | pytest fixtures section · GitHub Actions basics | P9.2 P9.3 — parser fixture, tests in CI |
| **6** | — | Cohort review: design review sign-off, window function walkthrough |

---

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

**Note:** S9.3 has a NULL trap. Paid up capital is missing for many companies, and where those rows land in the deciles changes the answer. Say what you did with them.

**Note:** S9.4 is the pattern the SCD2 build uses next week to find the current version row. Keep it.

---

## Station P8: Star Schema Design **[MILESTONE]**

- [ ] **P8.1** Join the group design review. Bring one written paragraph: which part of the pipeline your Python work feeds, and what can go wrong in it that the design must survive.
  **Commit:** `design/pipeline_risk_notes.md`, open a pull request.

**On P8.1:** be specific. "The IBBI PDF can shift its column order between quarters, so the extractor must match on header text and not on position, and the fact table needs a load timestamp to tell two quarters apart" is a risk. "Data quality issues" is not.

---

## Station P9: Testing with pytest

- [ ] **P9.1** Write pytest tests for your P2 validator: at least five tests covering good records, bad CINs, bad dates, and bad amounts.
  **Commit:** `python/p9/test_validator.py` plus a screenshot or paste of the passing run in `python/p9/notes.md`, open a pull request.

- [ ] **P9.2** Write tests for the IBBI extractor's parsing logic using a small saved sample of PDF text as a fixture, so tests run offline.
  **Commit:** `python/p9/test_ibbi_parser.py` plus the fixture file, update the pull request.

- [ ] **P9.3** Set up the tests to run automatically on every pull request. Paste the passing check from your own pull request as proof.
  **Commit:** the CI configuration file at the repository root, update the pull request.

**On P9.2:** a test that downloads a PDF is not a test, it is a network call that fails on a bad connection. The fixture is a few lines of saved text committed alongside the test, which is why it is allowed in Git while real source files are not.

**If pytest says `no tests ran`,** the file or function name does not start with `test_`. See `docs/10-troubleshooting.md`.

---

## End of week checklist

- [ ] S9.1 to S9.4 — four queries, each with the answer written down, plus the RANK and ROW_NUMBER explanations
- [ ] P8.1 — a specific, named risk your Python work creates for the design
- [ ] P9.1, P9.2, P9.3 — five or more validator tests, an offline parser fixture, and a green check on your own pull request
- [ ] At least one teammate's pull request reviewed with a real comment
- [ ] You can explain, out loud, the difference between RANK, DENSE_RANK, and ROW_NUMBER

**If you are short on time, cut in this order:** S9.3, then P9.2. Never cut S9.4 or P8.1. S9.4 is next week's SCD2 pattern, and P8.1 is the milestone.

Next: `week7/problem_statement.md`.
