# Curriculum Blueprint - The 13-Week Project Structure

**What this document is.** This is the skeleton of a project-based curriculum that runs for 13 weeks and is built around one real project the whole cohort builds together. It explains the structure - the repository layout, the weekly files, the task system, the milestones, the supporting documents - without referencing any specific subject. When you build a curriculum for a new subject, you keep this skeleton, fill in the subject's skills and source material, and adapt the optional parts.

> **How to use it:** read this once, then follow *Rebuilding this for a new subject* at the end. It lists everything you must produce, in order.

---

## 1. The one idea everything hangs on

This is not a list of topics taught week by week. It is **one real project that takes 13 weeks to build**, and every topic is learned because the project needs it.

- The client is fictional, but the source material is real and genuinely messy.
- The client's ask is vague on purpose. Turning it into a written brief is week 1.
- By week 13 there is a working product, reviewed, documented, and handed over - and every file in it is attributable to the person who wrote it.

Everything below exists to make one thing true: **skills are practised individually, then assembled into one shared product the whole cohort ships.**

---

## 2. The shape: one project, two zones, four tracks

**Two zones.** The repository has two zones with different jobs.

| Zone | Folder | Job |
|---|---|---|
| Individual practice | `students/` | every person practises every skill; mistakes are free |
| The shared product | `platform/` + `delivery/` | the one real version, built by a small rotating team; everyone depends on it |

The two-zone split means nobody is a fixed specialist: everyone touches everything in their own folder, and the rotation only decides who builds the shared product that week.

**Four tracks.** Every task belongs to one of four tracks. The tracks run in parallel, not one after another; a normal week touches two or three of them. That is deliberate: real work is never one skill at a time.

| Track | What it exists to teach |
|---|---|
| **Core** | the primary craft of the subject, practised on the real source material |
| **Tooling** | engineering habits: reading inputs reliably, validation, tests, error handling |
| **Product** | the shared product itself: its stages, its automated checks, its orchestration, its delivery |
| **Delivery** | writing, reviewing, presenting, handing over |

The track letter is the first letter of every task ID (see section 5). Name the tracks for your subject; the roles above are what matter, not the letters.

---

## 3. The 13-week arc

Thirteen weeks, four phases. The arc moves from understanding → individual craft → one shared product → handover.

| Weeks | Phase | What is happening |
|---|---|---|
| 1–4 | Foundations | Understand the client. First contact with the subject's core skills on real material. First end-to-end build - the first milestone. |
| 5–8 | Craft | Deeper skills, an agreed design, real (non-toy) builds, tests. The design gets signed off. |
| 9–11 | The shared product | The cohort stops practising separately and builds the one shared product: every stage, the checks, the automation. |
| 12–13 | Delivery | Automate and orchestrate, break it on purpose and fix it, present it, hand it over. |

Weeks get harder. The number of tasks per week varies - the original sprint ranges from **5 to 11 tasks in a week, 110 tasks in total** - and weeks are rebalanced whenever one becomes too heavy to finish honestly.

---

## 4. Milestones: the gates

A **milestone** is a small set of tasks marked `[MILESTONE]`. It is a gate: if the cohort is split across a gate, new work pauses until the group is back together, because everything after it depends on a shared decision or a shared deliverable.

Milestones sit at the points where the project changes shape:

| Week | Milestone | Why it is a gate |
|---|---|---|
| 1 | The Discovery Brief | the cohort must agree on what is being built before anyone builds it |
| 4 | The first end-to-end build | the first time the whole flow works, even roughly |
| 5 / 7 | The design agreed and signed off | everything after builds against one agreed design |
| 9 / 11 | The core requirement, built and rebuilt | the hardest logic, first by hand, then inside the shared product |
| 13 | The Project Handover | the product runs from a clean start, following only the written runbook |

Rules: milestone weeks are never the ones people skip, and the "never cut" tasks in every week file are always the milestone ones.

---

## 5. Tasks: numbering, stable IDs, commit paths

Every week file numbers its tasks **1 to N in working order** - the order you should actually do them. Separately, every task carries a **stable ID** that never changes once published:

```
<Track letter><Group number>.<Task number>     example:  A1.1, B3.2, C4.1
```

- The stable ID is what goes in commit messages and pull request titles, so anyone can find the task behind any commit.
- The week files track *working order* (Task 1…N); the task list (`docs/05-task-list.md`) tracks *IDs*.
- Each task names the **exact file path to commit to**, always inside the student's current week folder, and the path encodes the group - a task in group 3 of the core track commits under `core/c3/`.
- One task = one file = one commit. Never one giant file across a week.

---

## 6. The weekly rhythm

Every week has the same rhythm, so students always know where they are.

```
WEEK OPENS   the week's goal and roles are posted; everyone reads their own week file
DURING       work your own problem_statement.md, one task at a time,
             one commit per task, one pull request per task or per task group.
             Review at least one teammate's pull request.
WEEK CLOSES  cohort review: an architecture walkthrough, a terminology check,
             one honest failure story, and a preview of next week.
```

The expectation is about output, not hours: by the week's close the week's tasks are done, committed, and in pull requests. Every week file ends with an end-of-week checklist and a "if you are short on time, cut in this order" line, so a heavy week is survived honestly rather than half-finished silently.

---

## 7. Anatomy of a week file

Every week's `problem_statement.md` follows one skeleton. This is the template to reproduce for each week.

```markdown
# Week N - <short theme>

**<Project> · Week N of 13 · Theme: <one sentence>**

Read this whole file before you start. Then work through the task groups in order.

## Before you start
A pointer table: which support document to open for what
(the working loop, the client story, the glossary, the resources, troubleshooting, the tools).
Plus: how your tasks are numbered, and that each task names its exact commit path.

## By the end of this week you can
- a list of outcomes, written as things you can do, not topics you have seen

## The week at a glance
| Step | LEARN | DO |
| a table mapping each step to what to read or watch and which tasks to do with it

## 1 · <Task group name> [MILESTONE]
- [ ] **Task 1 - <short title>** (ID `X1.1`): <full instructions>
  **Commit:** `<exact path>`, open a pull request.
- [ ] **Task 2 - <short title>** (ID `X1.2`): ...
  **Commit:** ... update the pull request.

(Notes under the group: known traps, correctness checks, links forward to
later weeks that build on this. This is where the teaching lives.)

## 2 · <Task group name>
...

## End of week checklist
- [ ] every task ticked, each in its pull request
- [ ] at least one teammate's pull request reviewed with a real comment
- [ ] no source-material file, no secret, no environment folder in your commits

**If you are short on time, cut in this order:** <tasks>, then <tasks>. Never cut <the milestone tasks>.

Next: `weekN+1/problem_statement.md`.
```

Design details that matter:

- **"By the end of this week you can"** is written as outcomes, never as topics.
- **The glance table** pairs every reading or video with the exact tasks it feeds, so nobody reads on purpose.
- **Group headings** are simple names (for example "Reading the source material", "Validation and edge cases"), with `[MILESTONE]` where applicable. A group is a small set of related tasks - small enough to review in one sitting.
- **Notes under tasks** are a known trap, a correctness check, a "keep this for week N" link. These notes are what separate a project from a tutorial.
- **Foundation links** point backwards: "this week builds on your week N build/script/decision."
- **The cut line** is honest priorities, not permission to slack. Say what you cut, in the cohort channel.

---

## 8. The diagrams thread

Diagramming is woven through the sprint at five points, each one more detailed than the last. The first drawing is the whole project's table of contents; the last one is the architecture that gets handed over.

| Week | The drawing | Its job |
|---|---|---|
| 1 | the whole system on one page | a non-specialist can see what is being built |
| 4 | the flow, end to end | every hop from source to user, with the tool at each hop |
| 7 | the flow, updated with reality | what the real builds taught you, marked on the diagram |
| 9 | the full technical architecture | where every component and every automated check runs |
| 13 | the final architecture | the system exactly as it runs today, for the handover |

**The standard:** diagrams are written in Mermaid inside Markdown files and committed to Git. They render on the repository host, they are diffable in pull requests, and a reviewer can leave line-level comments on the change. Keep each one to a single page.

---

## 9. The repository layout

```text
<repo root>
├── README.md                  what the project is, the reading order, the 13 weeks at a glance
├── CONTRIBUTING.md            the rules of the repo: commit discipline, merge policy
├── .github/workflows/         automated checks (lint, build, tests) on every pull request
├── docs/                      everything in the reading order (section 10)
│   └── _week-templates/       the master week files, copied into every student folder
├── students/
│   └── <ID>/
│       └── week1…13/
│           └── problem_statement.md     one per week, per student
├── platform/                  the one real shared product (rotation only)
├── delivery/                  shared outputs: discovery, design, presentation, handover
└── admin/                     a pointer only - answer keys never live in this repository
```

**Always keep:** `README.md`, `CONTRIBUTING.md`, `docs/` with its reading order, `students/<ID>/week1…13/problem_statement.md`, `delivery/`, `admin/`.

**Adapt, don't copy:** `platform/` and the weekly rotation belong to subjects where the cohort ships one shared product - keep them when the subject has one, and write its rules in a dedicated guide. The original sprint's `platform/` holds the product's stages, its quality checks, its orchestration, and its build configuration; in a different subject the same folder holds whatever the shared product actually is. `docs/07-platform-and-cicd-guide.md` and `docs/platform-rotation-log.md` exist only because the rotation exists - drop them if you drop the rotation. The lint/CI files are whatever your subject's toolchain uses.

---

## 10. The documents, in reading order

The numbered `docs/` files are the spine of the experience. Keep the order; the numbering *is* the reading order.

| File | Its job | Opened |
|---|---|---|
| 00-START-HERE | the map: tracks, milestones, weekly rhythm, the rules that never bend, the week-1 checklist | first, before anything else |
| 01-project-brief | the client story, the source material, every design decision and the reason behind it | before week 1 |
| 02-tools-setup | install and configure every tool, accounts, logins - with a terminal open | before week 1 |
| 03-student-guide | fork, clone, commit, pull request; the working loop | before the first commit |
| 04-week-map | all 13 weeks on one page, with phases and milestones | to see where you are |
| 05-task-list | the complete task list, by track, with IDs and commit paths | to look ahead |
| 06-team-roles | who reviews what, how the rotation works, the merge policy | when roles matter |
| 07-platform-and-cicd-guide | the stricter rules for the shared product | when on rotation |
| 08-glossary | every word that appears in the documents, defined | whenever a word is unknown |
| 09-resources | the readings and videos, per week and per topic | whenever a task points at it |
| 10-troubleshooting | "this tool breaks like this" → the fix | when something breaks |
| 11-tools-and-technology | what each tool is for, and why it was chosen over the alternatives | when a tool is new |
| platform-rotation-log | who built what each week, with the pull request link | when a rotation turn ends |

Exactly one file per week sits outside `docs/`: the student's own `students/<ID>/weekY/problem_statement.md`. Everything else is reference - opened when a task points at it, never re-read cover to cover every week.

---

## 11. The working rules that make it work

1. **One task, one file, one commit.** The task tells you the exact path.
2. **Name the task ID** in the commit message and the pull request title.
3. **Stay in your own folder** unless you are on the rotation that week.
4. **Never squash merge** - it erases individual authorship, which is the record the cohort is building.
5. **No source-material files, no secrets** - raw downloads and credentials never enter the repository.
6. **Writing tasks are graded like code.** A good answer names the tradeoff, not just the fact.
7. **You will be asked "why", more than "what".** Every design choice has a reason and a rejected alternative.

---

## 12. Rebuilding this for a new subject

Follow this checklist. Do not reorder the steps - each one depends on the previous.

1. **Write the project brief.** The client story (vague on purpose), the source material (real, messy, specific), and the design decisions with reasons. This becomes `docs/01-project-brief.md`.
2. **Decide the tracks.** Use the four roles from section 2 as a checklist: core, tooling, product, delivery. Name them for the subject, assign a letter to each, and state the tracks in `docs/00-START-HERE.md`.
3. **Write the 13 week themes.** One short theme per week, inside the four-phase arc of section 3. A week's theme must be a thing you can *do* by the end of it.
4. **Choose the milestones.** The five gates from section 4, renamed for the project: the brief → the first end-to-end build → the design sign-off → the core requirement built and rebuilt → the handover. Mark them in the week map.
5. **Write the task list.** All tasks for all 13 weeks in one file, by track. Give every task a stable ID, a group, a short title, full instructions, and an exact commit path. Write the groups in the order students will meet them in the week files.
6. **Split the tasks into week files.** Each week gets: the glance table, the "by the end" outcomes, the groups with their notes, the checklist, the cut line, the next link. Keep the milestone tasks in the "never cut" position.
7. **Place the five diagram tasks** at weeks 1, 4, 7, 9, and 13, using the standard from section 8.
8. **Write the support documents.** START-HERE, tools-setup, student-guide, week-map, team-roles, glossary, resources, troubleshooting, tools-and-technology. These are not optional; the week files point at them constantly.
9. **Copy the week templates into every student folder** - one per student per week (30 students × 13 weeks in the original).
10. **Verify before publishing.** Task counts match between templates and the task list; IDs are unique; week numbers and `Next:` links are correct; cross-week references point at the right weeks; no leftover references to earlier versions.

Then the last sentence of every week file is always the same promise:

> Next: `weekN+1/problem_statement.md`.



