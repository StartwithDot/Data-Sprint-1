# Week 6 Tasks

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

