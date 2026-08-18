# Data Sprint 1

Welcome. This is the first project of the DOTSET data engineering program.

Over 10 weeks we build one real data platform together. It brings four Indian public data sources into one place so a due diligence team can check any registered company in India: is it real and active, has it ever been in insolvency proceedings, and how does it compare to other companies in its state. The four sources are the MCA company registry, IBBI insolvency records, the MCA CDM statistics portal, and RBI policy rates.

Two design words you will hear all the time in this repo:

* **Medallion pipeline** means the data moves through three layers. Bronze holds the data exactly as it arrived. Silver holds the cleaned version. Gold holds the final tables the dashboard uses.
* **Kimball star schema** is how we design those gold tables: fact tables for events, dimension tables for the things those events are about.

Both are explained in plain language in `docs/project-brief.md`, section 4. You are not expected to know them yet.

## New here? Start in this order

1. `docs/student-guide.md` tells you how to set up Git, where your folder is, and what to do each day. Read this first.
2. `docs/project-brief.md` tells you what we are building and why. Read this second.
3. Your own weekly file at `students/DEx/weekY/problem_statement.md` has the tasks you actually do.
4. `CONTRIBUTING.md` has the short list of repo rules.

## What is in each folder

* **`students/`** holds one practice folder per cohort member. You work inside your own folder, for example `students/DE12/week1/`. This is your space to practice.
* **`platform/`** holds the real shared pipeline code. Only the students on that week's platform rotation work here.
* **`delivery/`** holds the shared outputs: discovery notes, design, dashboard, and the final presentation. Also built by the weekly rotation group.
* **`docs/`** holds the project documents listed above, plus the task list, team roles, and the platform rotation log.

## Where to get help

Ask in the cohort Discord channel. Ask for a hint, not for the finished answer. Getting stuck is part of the work, and telling the group where you are stuck is the fastest way through it.
