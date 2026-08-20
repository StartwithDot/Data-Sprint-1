# Start Here

**Read this before anything else. It takes ten minutes and it saves you a week.**

If you have never used Git, never touched a cloud database, and never written a data pipeline, you are in the right place. Nothing in this sprint assumes prior experience. It assumes you will follow the order.

---

## 1. What this sprint is

Ten weeks. One real data platform, built by the whole cohort together, for a client who exists on paper but whose data is completely real.

The client is a fintech due diligence company. Their analysts check Indian companies before a lender or a buyer trusts them. Today they do it by hand, one company at a time, across two government websites and a spreadsheet. We build them one platform instead.

By week 10 there is a pipeline that refreshes on a schedule, a set of tested tables, and a dashboard a non-technical person can use. Every part of it is in this repository, reviewed, and attributable to whoever wrote it.

---

## 2. Read in this order

| # | File | When | Why |
|---|---|---|---|
| 1 | `00-START-HERE.md` | now | The map. This file. |
| 2 | `01-project-brief.md` | before week 1 begins | What we are building and why. The client story, the four data sources, the design decisions. |
| 3 | `02-tools-setup.md` | before week 1 begins | Git, Python, Snowflake, VS Code, and the accounts you need. Do it with a terminal open. |
| 4 | `03-student-guide.md` | before your first commit | Fork, clone, commit, pull request. The working loop. |
| 5 | `students/DEx/week1/problem_statement.md` | when week 1 opens | Your actual tasks. |

Then, every week, you open exactly one file: that week's `problem_statement.md` in your own folder.

Everything else is reference. You open it when a task points you at it:

| File | Open it when |
|---|---|
| `04-week-map.md` | you want to see all 10 weeks and what each one gives you |
| `05-task-list.md` | you want the complete station-by-station list |
| `06-team-roles.md` | you want to know who reviews your work and how rotations work |
| `07-platform-and-cicd-guide.md` | you have been picked for the platform rotation |
| `08-glossary.md` | a word appears that you do not know |
| `09-resources.md` | you need this week's reading or video |
| `10-troubleshooting.md` | a tool breaks and the error means nothing to you |
| `../CONTRIBUTING.md` | before your first pull request |

---

## 3. The four tracks

Every task in this sprint belongs to one of four tracks. The track letter is the first letter of the task ID, so `S3.2` is a SQL task and `P7.1` is a Python task.

| Letter | Track | What it teaches |
|---|---|---|
| **B** | Business and Delivery | Turning a vague client ask into a written brief, reviewing other people's work, presenting to a non-technical stakeholder, handing a project over |
| **S** | SQL and Data Modeling | Databases, tables, constraints, joins, NULL handling, functions, views, CTEs, window functions, MERGE, star schema design |
| **P** | Python | Files and functions, validation, retries, generators, logging, CLI tools, classes, tests, concurrency, the Snowflake connector |
| **D** | Data Platform | Snowflake stages, bronze loads, dbt staging and marts, Great Expectations, Airflow, the clean run and handover |

The tracks run in parallel, not one after another. In a normal week you touch two or three of them. That is deliberate: real data work is never one skill at a time.

---

## 4. Stations and milestones

A **station** is a small group of related tasks with one theme, for example `Station S1: Databases and Tables`. Stations are numbered inside each track: S1 through S10, P1 through P12, B1 through B8, D1 through D10.

A **milestone station** is a checkpoint the whole cohort must reach before anyone moves far past it, because the next stations depend on a shared decision. There are five:

| Milestone | Around | Why it gates everyone |
|---|---|---|
| Discovery Brief | week 1 | Building the wrong thing perfectly is the most expensive mistake in data work |
| First Snowflake Load | weeks 3 and 8 | Everyone must be able to move a file into the warehouse and prove the row counts match |
| Star Schema Design | weeks 4 and 6 | Table and column names must be agreed before anyone builds the gold layer |
| SCD2 Build | weeks 7 and 9 | The history logic is the client's core requirement and the hardest code in the project |
| Project Handover | week 10 | The pipeline must run from a clean checkout using only the runbook |

When the cohort is split across a milestone, new station work stops until the group catches up. That is not a punishment. It is how a team avoids building two incompatible halves of one platform.

---

## 5. Two zones in this repository

This is the single most important thing to understand about how the repo is laid out.

```
Data-Sprint-1/
├── students/DE1 … DE30/        ← PRACTICE ZONE. Your own folder. Mistakes cost nothing.
│   └── week1 … week10/
│       └── problem_statement.md
│
├── platform/                    ← SHARED ZONE. The one real pipeline. Stricter rules.
│   ├── raw/  staging/  marts/  quality/  orchestration/  dbt/
│
├── delivery/                    ← SHARED ZONE. discovery/ design/ dashboard/ presentation/
│
└── docs/                        ← Everything you read
```

**Practice zone.** You work in `students/DEx/weekY/`. You try every skill yourself. If you break something, you broke your own copy, and that is exactly what the zone is for.

**Shared zone.** `platform/` and `delivery/` hold the one real version. A small rotating group builds there each week. Mistakes there block the whole cohort, so that code gets automated checks and a core admin review.

Everyone gets a turn in the shared zone. See `06-team-roles.md`.

---

## 6. Your week, every week

```
WEEK OPENS   The week's goal is posted in Discord. Roles for the week are named.
DURING       You work your own problem_statement.md, one task at a time,
             one commit per task, one pull request per task or per station.
             You review at least one teammate's pull request.
WEEK CLOSES  Cohort review: architecture walkthrough, terminology check,
             one failure story, preview of next week.
```

The expectation is about output, not hours: by the time the week closes, the tasks in your week file are done, committed, and in pull requests. Each week file ends with an end of week checklist and a "if you are short on time, cut in this order" line. Use them honestly.


---

## 7. The five rules that never bend

1. **One task, one file, one commit.** Never build one giant file across a week. The task tells you the exact path.
2. **Name the task ID.** In the commit message and the pull request title. `S1.2 create raw MCA table`, not `update`.
3. **Stay in your own folder** unless you are on the platform rotation this week.
4. **Never squash merge.** Squashing collapses everyone's commits into one and erases individual authorship, which is the record you are here to build.
5. **No data files, no secrets.** No downloaded CSV, ZIP, PDF, or Excel. No passwords, no `profiles.yml`. Check `.gitignore` first, ask in Discord if unsure.

The full rule list is `../CONTRIBUTING.md`. The commands are `03-student-guide.md`.

---

## 8. How writing tasks are graded

Several tasks ask for a short explanation in a notes file rather than code. Those are graded exactly like code.

A good answer names the tradeoff. "We use VARCHAR in bronze" is a fact. "We use VARCHAR in bronze because a typed column would reject the whole file when one row has a bad date, and losing the file is worse than storing a bad value we can find later" is an answer.

You will be asked to say these out loud at the cohort review, from memory. Write them in your own words for that reason, not because copying is against the rules.

---

## 9. Before week 1 opens

- [ ] `01-project-brief.md` read end to end
- [ ] `02-tools-setup.md` completed: Git configured, Python 3.11+, VS Code, Snowflake login working
- [ ] Repository forked and cloned, `upstream` remote added (`03-student-guide.md`, section 1)
- [ ] You know your DE number and have found `students/DEx/week1/problem_statement.md`
- [ ] You have opened data.gov.in once and found the Company Master Data catalog page
- [ ] You have joined the cohort Discord channel and said hello with your DE number

Then open `students/DEx/week1/problem_statement.md`.

---

## 10. What will be hard, and it is meant to be

**The client ask is vague on purpose.** "We want to check companies faster" is not a specification. Week 1 is about turning it into something answerable. If you start writing SQL on the start you will build the wrong thing.

**The data is genuinely messy.** State names spelled four ways. Dates in three formats. Capital amounts with commas and currency symbols. One source only exists inside a PDF. Another only exists as an HTML table. This is not a teaching simplification of real data; it is real data.

**Something will break in week 10 on purpose.** A failure will be injected into the data or the pipeline. You will find it using logs, tests, and row counts, and write a postmortem about it.

**You will be asked "why" more than "what".** Every design choice in this project has a reason and an alternative that was rejected. Knowing the reason is the difference between a data engineer and someone who copied a tutorial.

---

Next: `01-project-brief.md`.
