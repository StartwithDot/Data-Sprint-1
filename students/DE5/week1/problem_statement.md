# Week 1 - Understand the ask

**Data Sprint 1 · Week 1 of 13 · Theme: understand the client, then make your first table, your first script, and your first diagram**

Read this whole file before you start anything. Then work through the task groups in order.

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
| What a tool is for and why we use it | `docs/11-tools-and-technology.md` |

**How your tasks are numbered:** each week numbers its tasks 1 to N in the order you should do them. Every task also keeps a stable ID like `S1.1` - that ID is what goes in your commit message and pull request title, so anyone can find the task behind any commit.

Every task below names the exact file path to commit to, and that path sits inside this same week folder.

---

## By the end of this week you can

- Describe the client's real problem in writing, in language the client would recognise
- Explain what each of the four data sources is for, without reading from the brief
- Draw the whole system on one page, so a non-technical person can see how it fits together
- Create a database, schemas, and a table in Snowflake, and say why every column is text
- Read a CSV in Python with functions that each do one job

## You do not clean any data this week

That is deliberate. Cleaning starts in week 3. This week is understanding plus first contact with the tools.

---

## The week at a glance

| Step | LEARN | DO |
|---|---|---|
| **1** | `docs/01-project-brief.md` sections 1 to 4 · the MCA data dictionary | Tasks 1–3 - the discovery brief, the open questions, the one-page system map |
| **2** | The four source websites, hands on · `docs/09-resources.md` data sources table | Tasks 4–5 - source summaries and the onboarding paragraph |
| **3** | Kudvenkat parts 1 to 2 · Snowflake "Key Concepts and Architecture" | Tasks 6–8 - database, schemas, raw table |
| **4** | Python docs tutorial sections 4 to 5 · Real Python CSV article | Tasks 9–10 - row counter, header check |
| **5** | Pro Git chapters 2 to 3 · Chris Beams on commit messages | Task 11 - state filter, first clean commits |
| **6** | - | Cohort review: discovery brief walkthrough, terminology check |

---

## 1 · Discovery Brief **[MILESTONE]**

- [ ] **Task 1 - Write the discovery brief** (ID `B1.1`): Read the client story in `docs/01-project-brief.md`, section 1. Write a one page discovery brief. It must cover: what we are building, who uses it, what questions it must answer, what is still unclear, and what "done" looks like. Use plain language, as if the client will read it.
  **Commit:** `discovery/discovery_brief.md`, open a pull request for peer review.

- [ ] **Task 2 - List the open questions** (ID `B1.2`): Write down the five questions you would ask the client if you had thirty minutes with them. Focus on things the brief cannot decide alone, like how far back the history must go, and what "risk" means to them.
  **Commit:** append to `discovery/discovery_brief.md` in an "Open Questions" section, update the same pull request.

- [ ] **Task 3 - Draw the whole system on one page** (ID `A1.1`): Draw the end-to-end picture: the four data sources on the left, the pipeline in the middle (files, Snowflake, the dashboard), and the people who use it on the right. Label each source with its format (CSV, PDF, HTML table, CSV). A non-technical person must be able to read it without you explaining it. Use Mermaid in a Markdown file - it renders on GitHub and is easy to review in a pull request - or any diagram tool you already know.
  **Commit:** `design/context_diagram.md` (embed the diagram), add it to the discovery brief pull request.

**Why this is a milestone:** building the wrong thing perfectly is the most expensive mistake in data work. Nobody moves far past week 1 until the cohort agrees on what is being built.

**On Task 3:** keep it to one page. If a box needs its own smaller boxes inside it, you have added too much detail. This diagram is the whole project's table of contents; you will redraw it with more detail in weeks 4, 7, 9, and 13.

---

## 2 · Source Summaries and the Client Ask

- [ ] **Task 4 - Summarise the four sources** (ID `B2.1`): For each of the four data sources, write three sentences in your own words: what it is, which client question it answers, and how it arrives (file type and cadence). No copying from `docs/01-project-brief.md`.
  **Commit:** `discovery/source_summary.md`, open a pull request.

- [ ] **Task 5 - Write the onboarding paragraph** (ID `B2.2`): Write the one paragraph business ask you would hand to a new teammate joining the project, so they understand the project without reading anything else.
  **Commit:** `discovery/teammate_onboarding.md`, open a pull request.


---

## 3 · Databases and Tables

Foundation link: Kudvenkat parts 1 to 2 (databases, tables). Note that Kudvenkat teaches SQL Server; the differences that matter are listed in `docs/09-resources.md`.

- [ ] **Task 6 - Create the database and schemas** (ID `S1.1`): In Snowflake, create the project database and three schemas named BRONZE, SILVER, and GOLD. Write down in one sentence what each schema will hold.
  **Commit:** `sql/s1/01_create_database.sql` plus `sql/s1/notes.md`, open a pull request.

- [ ] **Task 7 - Create the raw MCA table** (ID `S1.2`): Create the raw MCA table in BRONZE with one VARCHAR column per field in the RoC CSVs. Explain in one sentence why every column is VARCHAR at this stage.
  **Commit:** `sql/s1/02_create_raw_mca.sql`, update the pull request.

- [ ] **Task 8 - List the non-empty columns** (ID `S1.3`): Which columns in the raw MCA table must never be empty for a row to be a real company record? List them and explain why in one sentence each.
  **Commit:** append to `sql/s1/notes.md`, update the pull request.

---

## 4 · Python Basics: Files and Functions

- [ ] **Task 9 - Count rows in a CSV** (ID `P1.1`): Write a script that opens one RoC CSV file, counts the rows, and prints the count with the file name. Run it on three different RoC files.
  **Commit:** `python/p1/row_counter.py` plus output pasted in `python/p1/notes.md`, open a pull request.

- [ ] **Task 10 - Check the headers** (ID `P1.2`): Write a function that takes a file path and returns the column names from the CSV header line. Use it to verify two RoC files have identical headers. Report whether they match.
  **Commit:** `python/p1/header_check.py` plus result in notes, update the pull request.

- [ ] **Task 11 - Filter rows by state** (ID `P1.3`): Write a script that reads one raw CSV and writes a new CSV containing only rows where the state is a given value passed as text. Test it with "Kerala" on two files.
  **Commit:** `python/p1/state_filter.py`, update the pull request.

---

## End of week checklist

- [ ] Tasks 1–2 - discovery brief with open questions, in a pull request
- [ ] Task 3 - the one-page system map in `design/context_diagram.md`
- [ ] Tasks 4–5 - source summaries and the onboarding paragraph
- [ ] Tasks 6–8 - database, schemas, raw table, and the notes explaining both choices
- [ ] Tasks 9–11 - three scripts that run, with output pasted in notes
- [ ] At least one teammate's pull request reviewed with a real comment
- [ ] No data file, no credential, and no `.venv` anywhere in your commits

**If you are short on time, cut in this order:** Task 11 (P1.3), then Task 5 (B2.2). Never cut Tasks 1–2 (B1) or the notes files. The discovery brief is a milestone, and the written reasoning cannot be added back later.

Next: `week2/problem_statement.md`.
