# Week 1 — Understand the ask

**Data Sprint 1 · Week 1 of 10 · Theme: understand the client, then make your first table and your first script**

Read this whole file before you start anything. Then work through the stations in order.

---

## Before you open this file

| You need | Where |
|---|---|
| The client story and the four data sources | `docs/01-project-brief.md` |
| Git, Python, and Snowflake working | `docs/02-tools-setup.md` |
| Fork, clone, commit, pull request commands | `docs/03-student-guide.md` |
| A word you do not know | `docs/08-glossary.md` |
| This week's reading and videos | `docs/09-resources.md` |
| A tool that will not work | `docs/10-troubleshooting.md` |

Every task below names the exact file path to commit to, and that path sits inside this same week folder.

---

## By the end of this week you can

- Describe the client's real problem in writing, in language the client would recognise
- Explain what each of the four data sources is for, without reading from the brief
- Create a database, schemas, and a table in Snowflake, and say why every column is text
- Read a CSV in Python with functions that each do one job

## You do not clean any data this week

That is deliberate. Cleaning starts in week 3. This week is understanding plus first contact with the tools.

---

## The week at a glance

| Step | LEARN | DO |
|---|---|---|
| **1** | `docs/01-project-brief.md` sections 1 to 4 · the MCA data dictionary | B1.1 B1.2 — the discovery brief |
| **2** | The four source websites, hands on · `docs/09-resources.md` data sources table | B2.1 B2.2 — source summaries |
| **3** | Kudvenkat parts 1 to 2 · Snowflake "Key Concepts and Architecture" | S1.1 S1.2 — database, schemas, raw table |
| **4** | Python docs tutorial sections 4 to 5 · Real Python CSV article | S1.3 P1.1 — required columns, row counter |
| **5** | Pro Git chapters 2 to 3 · Chris Beams on commit messages | P1.2 P1.3 — header check, state filter |
| **6** | — | Cohort review: discovery brief walkthrough, terminology check |

---

## Station B1: Discovery Brief **[MILESTONE]**

- [ ] **B1.1** Read the client story in `docs/01-project-brief.md`, section 1. Write a one page discovery brief. It must cover: what we are building, who uses it, what questions it must answer, what is still unclear, and what "done" looks like. Use plain language, as if the client will read it.
  **Commit:** `discovery/discovery_brief.md`, open a pull request for peer review.

- [ ] **B1.2** Write down the five questions you would ask the client if you had thirty minutes with them. Focus on things the brief cannot decide alone, like how far back the history must go, and what "risk" means to them.
  **Commit:** append to `discovery/discovery_brief.md` in a "Open Questions" section, update the same pull request.

**Why this is a milestone:** building the wrong thing perfectly is the most expensive mistake in data work. Nobody moves far past week 1 until the cohort agrees on what is being built.

---

## Station B2: Discovery Brief, the Client Ask

- [ ] **B2.1** For each of the four data sources, write three sentences in your own words: what it is, which client question it answers, and how it arrives (file type and cadence). No copying from `docs/01-project-brief.md`.
  **Commit:** `discovery/source_summary.md`, open a pull request.

- [ ] **B2.2** Write the one paragraph business ask you would hand to a new teammate joining the project, so they understand the project without reading anything else.
  **Commit:** `discovery/teammate_onboarding.md`, open a pull request.

---

## Station S1: Databases and Tables

Foundation link: Kudvenkat parts 1 to 2 (databases, tables). Note that Kudvenkat teaches SQL Server; the differences that matter are listed in `docs/09-resources.md`.

- [ ] **S1.1** In Snowflake, create the project database and three schemas named BRONZE, SILVER, and GOLD. Write down in one sentence what each schema will hold.
  **Commit:** `sql/s1/01_create_database.sql` plus `sql/s1/notes.md`, open a pull request.

- [ ] **S1.2** Create the raw MCA table in BRONZE with one VARCHAR column per field in the RoC CSVs. Explain in one sentence why every column is VARCHAR at this stage.
  **Commit:** `sql/s1/02_create_raw_mca.sql`, update the pull request.

- [ ] **S1.3** Which columns in the raw MCA table must never be empty for a row to be a real company record? List them and explain why in one sentence each.
  **Commit:** append to `sql/s1/notes.md`, update the pull request.

---

## Station P1: Python Basics, Files and Functions

- [ ] **P1.1** Write a script that opens one RoC CSV file, counts the rows, and prints the count with the file name. Run it on three different RoC files.
  **Commit:** `python/p1/row_counter.py` plus output pasted in `python/p1/notes.md`, open a pull request.

- [ ] **P1.2** Write a function that takes a file path and returns the column names from the CSV header line. Use it to verify two RoC files have identical headers. Report whether they match.
  **Commit:** `python/p1/header_check.py` plus result in notes, update the pull request.

- [ ] **P1.3** Write a script that reads one raw CSV and writes a new CSV containing only rows where the state is a given value passed as text. Test it with "Kerala" on two files.
  **Commit:** `python/p1/state_filter.py`, update the pull request.

---

## End of week checklist

- [ ] B1.1, B1.2 — discovery brief with open questions, in a pull request
- [ ] B2.1, B2.2 — source summaries and the onboarding paragraph
- [ ] S1.1, S1.2, S1.3 — database, schemas, raw table, and the notes explaining both choices
- [ ] P1.1, P1.2, P1.3 — three scripts that run, with output pasted in notes
- [ ] At least one teammate's pull request reviewed with a real comment
- [ ] No data file, no credential, and no `.venv` anywhere in your commits

**If you are short on time, cut in this order:** P1.3, then B2.2. Never cut B1 or the notes files. The discovery brief is a milestone, and the written reasoning cannot be added back later.

Next: `week2/problem_statement.md`.
