# Week 1 Tasks

> **Before you start:** the setup steps and daily Git commands are in `docs/student-guide.md`. The client story and the four data sources are in `docs/project-brief.md`. Each task below tells you the exact file path to commit to, and that path sits inside this same week folder.

## Station B1: Discovery Brief **[MILESTONE]**

- [ ] **B1.1** Read the client story in `docs/project-brief.md`, section 1. Write a one page discovery brief. It must cover: what we are building, who uses it, what questions it must answer, what is still unclear, and what "done" looks like. Use plain language, as if the client will read it.
  **Commit:** `discovery/discovery_brief.md`, open a pull request for peer review.

- [ ] **B1.2** Write down the five questions you would ask the client if you had thirty minutes with them. Focus on things the brief cannot decide alone, like how far back the history must go, and what "risk" means to them.
  **Commit:** append to `discovery/discovery_brief.md` in a "Open Questions" section, update the same pull request.

## Station B2: Discovery Brief, the Client Ask

- [ ] **B2.1** For each of the four data sources, write three sentences in your own words: what it is, which client question it answers, and how it arrives (file type and cadence). No copying from `docs/project-brief.md`.
  **Commit:** `discovery/source_summary.md`, open a pull request.

- [ ] **B2.2** Write the one paragraph business ask you would hand to a new teammate joining tomorrow, so they understand the project without reading anything else.
  **Commit:** `discovery/teammate_onboarding.md`, open a pull request.

## Station S1: Databases and Tables

Foundation link: Kudvenkat parts 1 to 2 (databases, tables).

- [ ] **S1.1** In Snowflake, create the project database and three schemas named BRONZE, SILVER, and GOLD. Write down in one sentence what each schema will hold.
  **Commit:** `sql/s1/01_create_database.sql` plus `sql/s1/notes.md`, open a pull request.

- [ ] **S1.2** Create the raw MCA table in BRONZE with one VARCHAR column per field in the RoC CSVs. Explain in one sentence why every column is VARCHAR at this stage.
  **Commit:** `sql/s1/02_create_raw_mca.sql`, update the pull request.

- [ ] **S1.3** Which columns in the raw MCA table must never be empty for a row to be a real company record? List them and explain why in one sentence each.
  **Commit:** append to `sql/s1/notes.md`, update the pull request.

## Station P1: Python Basics, Files and Functions

- [ ] **P1.1** Write a script that opens one RoC CSV file, counts the rows, and prints the count with the file name. Run it on three different RoC files.
  **Commit:** `python/p1/row_counter.py` plus output pasted in `python/p1/notes.md`, open a pull request.

- [ ] **P1.2** Write a function that takes a file path and returns the column names from the CSV header line. Use it to verify two RoC files have identical headers. Report whether they match.
  **Commit:** `python/p1/header_check.py` plus result in notes, update the pull request.

- [ ] **P1.3** Write a script that reads one raw CSV and writes a new CSV containing only rows where the state is a given value passed as text. Test it with "Kerala" on two files.
  **Commit:** `python/p1/state_filter.py`, update the pull request.

