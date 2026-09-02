# Tools and Technology

**What every tool in this project is, what job it does for us, and why we chose it. Read it once in week 1 for the map, then again each time a new tool arrives.**

`02-tools-setup.md` tells you how to install all of this. This file tells you why each piece exists. If a task ever feels like busywork, come back here: every tool in the stack is paying off a real problem this project actually has.

You do not need to memorize this file. But you will be asked "why this tool" at cohort reviews, and the answers below are the honest ones.

---

## 1. The whole stack in one table

| Tool | Its one job | Arrives |
|---|---|---|
| Git | Remember every change to every file, and who made it | week 1 |
| GitHub | Host the shared repository; pull requests and reviews | week 1 |
| Python 3.11 or newer | Write the code that gets data out of files, PDFs, and web pages | week 1 |
| VS Code | Edit SQL, Python, and Markdown in one place | week 1 |
| Snowflake | The cloud data warehouse: where the data lives, where SQL runs | week 1 |
| pydantic | Check each record against written rules before we trust it | week 2 |
| Snowflake stages and `COPY INTO` | The door files pass through to land in bronze | week 3 |
| requests | Download files and web pages over the internet | week 4 |
| tenacity | Retry a failed download instead of crashing | week 4 |
| pdfplumber | Pull tables out of the IBBI PDF | week 5 |
| Beautiful Soup | Pull tables out of the MCA CDM web pages | week 5 |
| pytest | Run automated tests on our own code | week 6 |
| snowflake-connector-python | Let Python talk to Snowflake | week 7 |
| Environment variables and `python-dotenv` | Keep credentials out of the code | set up week 1, load-bearing from week 7 |
| GitHub Actions | Run lint and dbt checks on every pull request | week 8 |
| dbt Core | Turn our cleaning SQL into tested, ordered, documented models | week 8 |
| Great Expectations | Check the data itself against written rules, and stop bad data | week 9 |
| Apache Airflow | Run the whole pipeline on a calendar, in the right order | week 10 |
| Metabase | Turn the gold tables into charts an analyst can use | week 10 |
| SQLFluff and flake8 | Lint SQL and Python so reviewers see logic, not formatting | set up week 1, enforced from week 8 |
| DBeaver *(optional)* | A desktop SQL client, if you prefer it to the Snowflake web UI | any time |
| Markdown | The format almost every file in this repository is written in | everywhere |

If you can explain that table in your own words, you can answer most of the "why" questions a reviewer will ever ask you.

---

## 2. How the tools fit together

The stack splits into three groups, and each group answers a different question.

* **The pipeline tools** hold and move the data: Python and its libraries, Snowflake, dbt, Great Expectations, Metabase.
* **The record tools** hold and protect the code: Git, GitHub, GitHub Actions.
* **The workbench tools** are what you personally write with: VS Code, SQLFluff, flake8, Markdown.

Here is the journey, in the order the data actually travels.

1. Four Indian public sources publish on their own schedules: the MCA registry as CSV files inside ZIPs, IBBI insolvency records as PDF, MCA CDM statistics as HTML tables, RBI policy rates as CSV.
2. Python extractors pull each source apart. `requests` fetches, `tenacity` retries when a government site times out, `pdfplumber` and Beautiful Soup read the PDF and the web pages, and pydantic checks every row before it is saved as a clean dated CSV.
3. Files land in Snowflake stages, and `COPY INTO` loads them into bronze: raw, everything as text, file name and load timestamp on every row.
4. dbt staging models clean bronze into silver. dbt marts shape silver into the gold star schema. dbt tests check the structure, and dbt snapshots keep the status history.
5. Great Expectations stands in front of gold. If the data breaks a written rule, the run stops before anything is published.
6. Metabase reads only gold and draws the dashboard the client's analysts use.
7. Airflow runs steps 2 to 6 on a calendar, records what happened at every step, and tells us the moment something fails.

The whole time, every piece of code lives in Git on GitHub. Every change arrives as a pull request. GitHub Actions lints and parses it, a teammate reviews it, and only then does it merge.

In one sentence: the data flows downhill from bronze to silver to gold, the code flows through review, and Airflow is the clock that makes both repeat every month.

---

## 3. Git and GitHub — the project's memory

### Git

**What it is.** Version control. It records every change to every file, who made it, when, and why.

**What it does for us.** Every task in this sprint ends in a commit. That is not ceremony. With 30 people building one platform, "who changed what, and what did they change it from" is the difference between a project and a pile of files. The commit history is also the work record you show people afterwards.

**Why we chose it.** It is the industry standard for version control, it is what every employer uses, and there is no real alternative left. The interesting question is not "Git or something else" but "commit properly or not", which is why the commit message rules in `../CONTRIBUTING.md` are as strict as the code rules.

**Arrives** in week 1 and never leaves.

### GitHub

**What it is.** The website that hosts the shared repository.

**What it does for us.** Forks, branches, pull requests, reviews, the contribution graph. The whole working loop in `03-student-guide.md` happens on GitHub. Code review is not a checkbox here: it is how the cohort catches mistakes and spreads knowledge.

**Why we chose it.** Same reason as Git: it is the standard, and the pull request habit is directly the job skill.

### GitHub Actions

**What it is.** The automation that runs inside GitHub. CI, continuous integration: every time you open a pull request, checks run automatically and show a green tick or a red X.

**What it does for us.** Three workflow files live in `.github/workflows/`. `lint.yml` runs SQLFluff and flake8, `dbt-check.yml` parses the dbt project to confirm it is structurally valid, and `dbt-build.yml` runs the full dbt build after a change is merged into `main`.

**Why we chose it.** Human reviewers should spend their attention on logic, not on spacing and keyword casing. A machine checks the small stuff every single time and never gets tired. Full detail is in `07-platform-and-cicd-guide.md`.

**Arrives** in week 8, when work moves into the shared `platform/` folder. Practice work in your own folder is not checked by CI; shared work is.

---

## 4. Python — the project's hands

### Python 3.11 or newer

**What it is.** A general purpose programming language.

**What it does for us.** Three of our four sources cannot be loaded by hand at all. The IBBI data only exists inside a PDF, the MCA CDM numbers only exist inside web pages, and the RBI files have quirks that no `COPY INTO` survives untouched. Python is where every extractor, validator, and load-checking script lives.

**Why we chose it.** These jobs cannot be done in SQL, and Python has the best libraries for files, PDFs, and web pages. It is also the most common language in data engineering, so every hour spent here transfers.

### pydantic

**What it is.** A library where you describe what a valid record looks like as a small class, then hand it records to check.

**What it does for us.** Every extracted row is checked against declared rules, like "CIN is 21 characters" and "the date parses", before it is allowed into a file. The same validator is reused by every extractor instead of each script growing its own pile of `if` statements.

**Why we chose it.** The client's core demand is trust. Rules written once as code behave identically every run; rules re-implemented by hand in five scripts drift apart silently.

**Arrives** in week 2, station P2.

### requests

**What it is.** The standard Python library for downloading things over the internet.

**What it does for us.** It fetches the RBI file, the IBBI PDF, and the CDM web pages, so the pipeline downloads data instead of a person clicking Save As.

**Why we chose it.** A step a human must click is a step that does not happen at 2 am when the monthly refresh runs.

**Arrives** in week 4, station P4.

### tenacity

**What it is.** A retry library. It runs a failed function again, with a wait that doubles each time.

**What it does for us.** Government websites time out. Downloads stop halfway. A retry wrapper tries again instead of crashing the whole run.

**Why we chose it.** Without retries, the pipeline breaks every few runs and nobody knows why. With them, one bad attempt is a warning in the log and the next attempt usually succeeds.

**Arrives** in week 4, station P4.

### pdfplumber

**What it is.** A library that reads PDF files and pulls tables out of them.

**What it does for us.** The IBBI insolvency data is published as a PDF: text laid out like a printed page, with no CSV download and no API. `pdfplumber` finds the table in the page and hands us rows.

**Why we chose it.** The alternative is a human retyping numbers from a PDF every quarter, which is slow, unattributable, and quietly wrong.

**Arrives** in week 5, station P7.

### Beautiful Soup

**What it is.** A library that reads HTML, the language web pages are written in, and lets you find tables and rows in it.

**What it does for us.** The MCA CDM statistics exist only as tables on web pages. Beautiful Soup finds the table and walks its rows, and the extractor converts Indian number formats to plain numbers.

**Why we chose it.** Same reason as pdfplumber: the data exists, but only inside a format meant for reading, not for data work.

**Arrives** in week 5, station P7.

### pytest

**What it is.** The standard Python testing framework.

**What it does for us.** Small tests that check our own code, especially the validators that guard what reaches the client-facing tables. They run offline, in seconds, on every change.

**Why we chose it.** "I ran it once and it worked" is not a guarantee. A test suite is the same check, run by a machine, forever. Mistakes get caught before review, not after the client sees them.

**Arrives** in week 6, station P9.

### snowflake-connector-python

**What it is.** Snowflake's official library for running SQL from Python.

**What it does for us.** The pipeline can load files, run row count checks, and compare source counts against loaded counts without a human pasting queries into a web page.

**Why we chose it.** Orchestration in week 10 needs every step callable as code. If Python cannot talk to Snowflake, Airflow can only watch.

**Arrives** in week 7, station P11.

### Environment variables and `python-dotenv`

**What it is.** A way for code to read credentials from outside itself. The values live in a `.env` file on your machine, which `.gitignore` excludes, and the code reads them at runtime.

**What it does for us.** No password, account, or token ever appears in a commit. This rule is absolute in this repository and is enforced by review.

**Why we chose it.** A secret committed to Git is leaked the moment it is pushed, even if you delete it in the next commit, because history keeps it. `.env` keeps secrets in exactly one place: your machine, never the repository.

**Set up** in week 1 during tools setup; becomes load-bearing in week 7, station P11.

### A note on pandas

`pandas` is installed in your environment, and it is a fine tool for exploring data interactively. But the sprint deliberately teaches the `csv` module and generators first, because pandas loads whole files into memory and hides the mechanics. Week 5 is about handling a file bigger than your laptop's memory, and that lesson is worth more than the one-liner. Use pandas to look; build with the streaming habits the tasks teach.

---

## 5. Snowflake — the warehouse

**What it is.** A cloud data warehouse. Storage and compute are separate: the data sits in one place, and you spin up compute, called a warehouse, only when you run something.

**What it does for us.** All data lands here and all SQL runs here. The project database holds three schemas, BRONZE, SILVER, and GOLD, one per layer of the medallion pipeline. Internal stages are the holding area where files wait before `COPY INTO` loads them into bronze tables.

**Why we chose it.** The cohort already learned SQL on Snowflake in the foundation month, so there is nothing new to install or administer, and it handles the registry's roughly 31 lakh rows without any server setup. Snowflake's `ON_ERROR` options on `COPY INTO` also let one bad row be flagged rather than rejecting a whole file, which matters with data this messy. And the warehouse auto-suspends, which keeps the shared account's credits from burning while nobody is querying.

**DBeaver** is an optional desktop SQL client. Some people prefer it to the Snowflake web UI. Neither choice is wrong.

**Arrives** in week 1, and the first real load milestone lands in week 3.

---

## 6. dbt Core — the transformation layer

**What it is.** A tool where every transformation is one SQL `SELECT` in one file, called a model. dbt works out what depends on what, creates the tables and views in the right order, and runs tests alongside them.

**What it does for us.** Staging models clean bronze into silver: correct types, cleaned state names, parsed dates. Marts build the gold star schema. Tests declare expectations like unique and not null on columns, and relationships from facts to dimensions. Snapshots keep the slowly changing history of company status. And dbt documents itself: it draws the map of how every table was built.

**Why we chose it.** The alternative is a folder of numbered SQL scripts that somebody must run in exactly the right order, every month, forever. That works once and rots quickly. dbt keeps every step in version control, so every change to the logic is a pull request a teammate reads before it merges. We use **dbt Core**, the free command line version, not dbt Cloud: it runs locally and in CI, which is all we need.

**Arrives** in week 8, station D5, and carries weeks 8 and 9.

---

## 7. Great Expectations — the quality gate

**What it is.** A data validation tool. You write expectations, which are plain rules about the data's content, then run the data against them.

**What it does for us.** Two jobs. Expectation suites on the raw MCA files: CIN length, allowed status values, no fully empty rows, state names within the known list. And the gate in front of gold: every CIN in the insolvency fact must exist in the company dimension, end dates after start dates, no overlapping version periods. If a rule breaks, the run stops before anything is published.

**Why we chose it.** The client asked for a platform they can trust, and trust needs automated proof, not promises. You may ask why we run both dbt tests and Great Expectations: dbt tests check a model's structure, like uniqueness and relationships, while Great Expectations checks the data's content against business rules and can stop the pipeline. Station D8.3 makes you write down the difference yourself.

**Arrives** in week 9, station D8.

---

## 8. Apache Airflow — the scheduler

**What it is.** An orchestrator. You describe a pipeline as a DAG, a directed acyclic graph, which is just "this step, then that step, never in a loop", and Airflow runs it on a schedule.

**What it does for us.** The monthly refresh: run the extractors, load bronze, run the dbt build, run the quality gate, in the right order, with retries and a record of every step's status. When week 10's injected failure arrives, the run history is how you find where it broke.

**Why we chose it.** Once the pipeline works by hand, it must run by calendar, because the sources refresh monthly whether or not anyone clicks anything. Airflow is also the most widely used orchestrator in industry, so it is the most useful first one to learn.

**Arrives** in week 10, station D9. The program provides the environment; you write the DAG.

---

## 9. Metabase — the window the client looks through

**What it is.** An open source dashboard tool that connects to a database and turns tables into charts and filters.

**What it does for us.** Four views on the gold tables: company status counts by state, insolvency events by quarter, capital distribution by business activity, and a company search showing current status plus status history. An analyst uses these without ever knowing what dbt or bronze is.

**Why we chose it.** The client's analyst is not a data engineer, and the deliverable is something they can use directly. Metabase is free, open source, and learnable in days. It points only at gold, the one layer clean enough to show, never at raw.

**Arrives** in week 10, station B6.

---

## 10. The workbench: VS Code, SQLFluff, flake8, Markdown

**VS Code** is the editor: one place for SQL, Python, and Markdown, with a terminal built in. Use something else if you already love it, but the docs here assume VS Code.

**SQLFluff** lints SQL, and **flake8** lints Python. A linter reads your code and flags style problems, like inconsistent keyword casing or unused imports, before a human ever sees it. They are configured in `.sqlfluff` and `.flake8` at the repository root, so the whole cohort writes in one style. That matters more than it sounds: when 30 people's code looks the same, reviewers read the logic instead of the formatting.

**Markdown** is the format nearly every file in this repository is written in, including this one. In this project, writing is not an afterthought to the code: the discovery brief, the design decisions, the runbook, and every notes file are deliverables. Markdown keeps them in Git, under review, versioned exactly like SQL and Python.

---

## 11. What we deliberately did not use

Every tool above was chosen over something. The rejected alternatives teach the reasoning as much as the choices do.

| Rejected | Why it was rejected |
|---|---|
| Spreadsheets | Fine for looking at a hundred rows. They break at lakhs of rows, keep no review trail, and cannot be tested. |
| Manual downloads and copy-paste | Not repeatable, not attributable, and silently different every month. The whole pipeline exists to replace this. |
| Hand-run SQL scripts in a folder | Someone must run 14 scripts in exactly the right order every month, forever. Nobody does that reliably. That is what dbt and Airflow are for. |
| Stored procedures in the warehouse | The logic hides inside the database, out of Git, out of review, invisible to CI. dbt keeps SQL in files where review can reach it. |
| cron and shell scripts | A calendar with no run history, no visibility of where it failed, and no retries. Airflow is the calendar plus the record. |
| dbt Cloud | A paid UI around a tool we can run for free on the command line and in CI. |
| A big data engine, like Spark | Our data is lakhs of rows, not billions. The cluster complexity would buy us nothing here. |
| pandas as the default | One-line loads hide the memory mechanics that week 5 exists to teach. |

---

## 12. Where to read more

| You want | Go to |
|---|---|
| How to install any of this | `02-tools-setup.md` |
| The client story and why the platform exists | `01-project-brief.md` |
| The shorter version of this story, in business terms | `01-project-brief.md`, section 5 |
| A one line definition of any term above | `08-glossary.md` |
| The exact reading or video for a tool, week by week | `09-resources.md` |
| What to do when one of these tools breaks | `10-troubleshooting.md` |

