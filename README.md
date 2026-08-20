# Data Sprint 1

**India Company Risk and Verification Data Platform · 10 weeks · Snowflake, dbt, Python, Airflow, Great Expectations, Metabase**

Welcome. This is the first project of the data engineering program. Over 10 weeks the cohort builds one real data platform together.

---

## Read these in this order

| # | File | When |
|---|---|---|
| 1 | `docs/00-START-HERE.md` | right now, before anything else |
| 2 | `docs/01-project-brief.md` | before week 1 begins |
| 3 | `docs/02-tools-setup.md` | before week 1 begins, with a terminal open |
| 4 | `docs/03-student-guide.md` | before your first commit, then whenever you forget a command |
| 5 | `students/DEx/week1/problem_statement.md` | when week 1 opens, and every week after |

Reference files, open them when something points you at them:

| File | Open it when |
|---|---|
| `docs/04-week-map.md` | you want to see the whole 10 weeks at once |
| `docs/05-task-list.md` | you want the full station-by-station task list |
| `docs/06-team-roles.md` | you want to know who reviews what and how rotations work |
| `docs/07-platform-and-cicd-guide.md` | you are on the platform rotation this week |
| `docs/08-glossary.md` | a document uses a word you do not know |
| `docs/09-resources.md` | you need the reading or video for this week's topic |
| `docs/10-troubleshooting.md` | Git, Snowflake, dbt, or Python breaks on you |
| `docs/platform-rotation-log.md` | you need to record your platform rotation turn |
| `CONTRIBUTING.md` | before your first pull request |

---

## What we are building, in four sentences

The client is a fintech due diligence company. Their analysts need to check any registered company in India: is it real and active, has it ever been in insolvency proceedings, and how does it compare to other companies in its state.

We bring four Indian public data sources into one platform to answer that: the MCA company registry, IBBI insolvency records, the MCA CDM statistics portal, and RBI policy rates. The platform refreshes on a schedule, keeps status history, and ends in a dashboard a non-technical analyst can use.

Full story, sources, and the reasoning behind every design choice: `docs/01-project-brief.md`.

---

## Two design words you will hear every week

* **Medallion pipeline** means data moves through three layers. **Bronze** holds it exactly as it arrived. **Silver** holds the cleaned version. **Gold** holds the final tables the dashboard uses.
* **Kimball star schema** is how we design those gold tables: fact tables for events, dimension tables for the things those events are about.

Both are explained in plain language in `docs/01-project-brief.md`, section 4, and defined in `docs/08-glossary.md`. You are not expected to know them yet.

---

## The 10 weeks at a glance

| Week | Theme | Stations | Milestone |
|---|---|---|---|
| 1 | Understand the ask, first tables, first Python | B1 B2 S1 P1 | Discovery Brief |
| 2 | Trust the data, join the data | S2 S3 P2 | — |
| 3 | Missing values, messy strings, first load | S4 S5 P3 | First Snowflake Load |
| 4 | Readable SQL and the agreed model | B3 S6 S7 P4 | Star Schema Design |
| 5 | Big files and real extractors | S8 P5 P6 P7 | — |
| 6 | Window functions and tests | S9 P8 P9 | Star Schema Design sign-off |
| 7 | History that survives: MERGE and SCD2 | S10 P10 P11 | — |
| 8 | The shared platform: stages, bronze, dbt staging | D1 D2 D3 D4 D5 | First Snowflake Load (shared) |
| 9 | Gold layer, SCD2 in dbt, quality gates | P12 D6 D7 D8 | SCD2 Build |
| 10 | Orchestrate, break, fix, present, hand over | B4 B5 B6 B7 B8 D9 D10 | Project Handover |

Week by week detail, including what you can do by the end of the week: `docs/04-week-map.md`.

---

## What is in each folder

| Folder | What it holds | Who writes in it |
|---|---|---|
| `students/DEx/weekY/` | One practice folder per cohort member, one subfolder per week | You, in your own folder only |
| `platform/` | The one real shared pipeline: raw, staging, marts, quality, orchestration, dbt | Only that week's platform rotation |
| `delivery/` | Shared outputs: discovery, design, dashboard, presentation | Only that week's platform rotation |
| `docs/` | Everything in the reading order above | Core admins, plus students when a task says so |
| `admin/` | A pointer only. No answer keys live in this repository. | Core admins |

---

## Your first hour

1. Read `docs/00-START-HERE.md` end to end. It is short.
2. Follow `docs/02-tools-setup.md` and get Git, Python, and a Snowflake login working.
3. Fork and clone this repository using `docs/03-student-guide.md`, section 1.
4. Find your own folder, for example `students/DE12/`, and open `week1/problem_statement.md`.
5. Post in the cohort Discord channel that you are set up, and say which DE number you are.

---

## Where to get help

Ask in the cohort Discord channel. Say what you were trying to do, what you tried, what happened, and paste the error. Ask for a hint, not for the finished answer.

Getting stuck is part of the work. Telling the group where you are stuck is the fastest way through it. If the problem looks like a tooling failure rather than a thinking failure, check `docs/10-troubleshooting.md` first.
