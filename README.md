# Data Sprint 1

**India Company Risk and Verification Data Platform · 13 weeks · Snowflake, dbt, Python, Airflow, Great Expectations, Metabase**

Welcome. This is the first project of the data engineering program. Over 13 weeks the cohort builds one real data platform together.

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
| `docs/04-week-map.md` | you want to see the whole 13 weeks at once |
| `docs/05-task-list.md` | you want the full task list |
| `docs/06-team-roles.md` | you want to know who reviews what and how rotations work |
| `docs/07-platform-and-cicd-guide.md` | you are on the platform rotation this week |
| `docs/08-glossary.md` | a document uses a word you do not know |
| `docs/09-resources.md` | you need the reading or video for this week's topic |
| `docs/10-troubleshooting.md` | Git, Snowflake, dbt, or Python breaks on you |
| `docs/11-tools-and-technology.md` | you want to know what a tool is for and why we chose it |
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

## The 13 weeks at a glance

| Week | Theme | Task groups | Milestone |
|---|---|---|---|
| 1 | Understand the ask, first tables, first Python | Discovery Brief · System Map · Source Summaries · Databases and Tables · Python Basics | Discovery Brief |
| 2 | Trust the data, join the data | Data Integrity · Queries and Joins · Type Hints and Validation | - |
| 3 | Missing values, messy strings | Missing Values · SQL Functions | - |
| 4 | First load, and the design begins | First Snowflake Load · Design Record · Pipeline Flow Diagram | First Snowflake Load |
| 5 | Readable SQL and the agreed model | Views and CTEs · Star Schema Design · Retry Logic | Star Schema Design |
| 6 | Big files and cleaner tooling | Normalization · Generators · Logging and CLI | - |
| 7 | Extractors and the design sign-off | Object Oriented Extractors · Design Review · Design Review Update | Star Schema Design sign-off |
| 8 | Window functions and tests | Window Functions · Testing with pytest | - |
| 9 | History that survives | SCD2 · Parallel Downloads · Python + Snowflake · Technical Brief | SCD2 Build |
| 10 | The shared platform: stages, bronze, dbt staging | Stages · Bronze Loads · Teach-Back · dbt Staging Models | First Snowflake Load (shared) |
| 11 | Gold layer and the monthly refresh | Layer Contracts · Gold Layer with dbt · Monthly Refresh | The Monthly Refresh |
| 12 | Orchestrate, break, fix | Quality Gates · Airflow · Peer Review · Break and Fix | - |
| 13 | Present and hand over | Dashboard · Stakeholder Delivery · Final Architecture · Handover | Project Handover |

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
