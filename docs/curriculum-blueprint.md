# Curriculum Blueprint - A Project-Based Learning Structure

**What this document is.** A way to build a curriculum around one real project that the whole group creates together. It explains the parts - how the project drives the learning, how tasks are organised, how the repository can be laid out, what supporting documents are for - and, just as importantly, how to adapt each part to your own subject. Nothing here is fixed. The subject decides the length, the pace, the folders, and the documents. This file provides the thinking, not the prescription.

> **How to use it.** Read it once to understand the shape. Then use the checklist at the end to make the decisions for your own curriculum. Examples are marked *Example* - copy what fits, ignore the rest.

---

## 1. The idea everything hangs on

A project-based curriculum is not a list of topics taught in order. It is one real project that the whole group builds, and every topic is learned because the project needs it.

- The client is fictional, but the source material is real and genuinely messy.
- The client's ask is vague on purpose. Turning it into a written brief is the first task of the whole project.
- By the end there is a working product, reviewed, documented, and handed over - and every file in it is attributable to the person who wrote it.

Everything below exists to make one thing true: **skills are practised individually, then assembled into a finished whole.**

---

## 2. The shape: two zones and a few parallel tracks

### Two zones
Most subjects benefit from splitting the work into two zones with different jobs:

| Zone | Job |
|---|---|
| Individual practice | every person practises every skill; mistakes are free |
| The shared build | the one real version of the thing, assembled from everyone's practice; everyone depends on it |

*Example - a subject where each student ships their own artifact may have no shared build at all. Keep the practice zone, plus one shared place for outputs such as demos, reports, and presentations.* Whether you need a shared build is a decision, not a rule.

### Parallel tracks
Group the tasks into a small number of parallel tracks. The tracks run side by side - a single unit of work touches two or three of them, because real work is never one skill at a time.

A useful starting set of four:

| Track | What it exists to teach |
|---|---|
| Core | the primary craft of the subject, practised on the real source material |
| Tooling | engineering habits: reading inputs reliably, validation, tests, error handling |
| Product | the shared build itself: its stages, its checks, its automation, its delivery |
| Delivery | writing, reviewing, presenting, handing over |

Name the tracks for your subject; use two, three, or five if that fits better. What matters is that every task belongs to exactly one track, and the track letter is the first letter of the task's ID (section 5).

---

## 3. The arc: phases, not a fixed number of time-boxes

A project-based curriculum has a natural arc, but no natural length. The phases are the important part; how long each phase takes is your decision, based on the subject, the cohort, and the scope of the project.

| Phase | What happens |
|---|---|
| Understand | read the client and the material; write the brief; first contact with the core skills |
| Practice | deeper skills on real, messy material; the design is agreed and signed off |
| Build | the whole group assembles the real, shared, working thing |
| Deliver | automate and check it, break it on purpose and fix it, present it, hand it over |

*Example - a programme with a twelve-to-sixteen time-box project might spend roughly 30% on Understand, 30% on Practice, 25% on Build, and 15% on Deliver. A shorter project compresses; a longer one deepens. The exact split is the subject's decision.*

Rules of thumb, not laws:

- **The first phase must end with a written brief**, so the group agrees what it is building before anyone builds it.
- **The last phase must end with a handover**, so the project survives the people who built it.
- **Every phase must end with something real done** - a working piece, a signed-off design - never with "we covered the topics".
- If a phase grows heavier than the others, split it into more time-boxes. There is no required number.

---

## 4. Milestones: the gates

A **milestone** is a small set of tasks the whole group must arrive at together before anyone moves on, because everything after depends on a shared decision or a shared deliverable.

Useful positions, in order - rename and reposition them for your project:

| Position | Milestone | Why it is a gate |
|---|---|---|
| the start | the Discovery Brief | agree what is being built before building it |
| first completed build | the first end-to-end run | the whole flow works for the first time |
| mid-project | the design agreed and signed off | everything after builds against one agreed design |
| late project | the core requirement, built and rebuilt | the hardest part, first by hand, then in the real build |
| the end | the Project Handover | the product runs from a clean start, using only the written runbook |

Mark milestone groups clearly in the task list (for example with `[MILESTONE]`) and never put them in the "you can cut this if short on time" list.

---

## 5. Tasks: numbering, stable IDs, commit paths

- Each unit file numbers its tasks 1 to N in working order - the order they should be done.
- Each task also carries a **stable ID** that never changes once published: `<Track letter><Group number>.<Task number>` (example: `A1.1`).
- The stable ID goes in commit messages and pull request titles, so anyone can find the task behind any commit.
- Each task names the **exact file path** to commit to, and the path encodes its group.
- One task = one file = one commit.

The exact ID format is an example; the principle is the point - every piece of work is traceable to a task, and every task to a person.

---

## 6. The rhythm of a time-box

Every time-box (commonly called a week) follows the same rhythm, so the group always knows where it is.

```
OPENS    the goal and roles are posted; everyone reads the time-box file
DURING   work your own tasks: one task, one commit, one pull request.
         Review at least one teammate's pull request.
CLOSES   a short review: what got built, what failed, one lesson, a look ahead
```

The expectation is about output, not hours. Each time-box file ends with a checklist and an honest "if you are short on time, cut in this order" line, so a heavy time-box is survived honestly rather than half-finished silently.

---

## 7. Anatomy of a time-box file

The file that lists a time-box's tasks is the core of the experience. A skeleton to imitate:

```markdown
# Unit N - <short theme>

Read this whole file first. Then work through the task groups in order.

## Before you start
Which supporting documents to open, and how this unit's tasks are numbered.

## By the end of this unit you can
- outcomes, written as things you can do, not topics you have seen

## At a glance
| Step | LEARN | DO |
| each step maps what to read or watch to the tasks that use it

## 1 · <Task group name> [MILESTONE]
- [ ] **Task 1 - <short title>** (ID `X1.1`): <instructions>
  **Commit:** `<exact path>`, open a pull request.
- [ ] **Task 2 - <short title>** (ID `X1.2`): ...
  **Commit:** ... update the pull request.

(Notes under the group: known traps, checks that prove a task is right,
links to later units that build on this. The teaching lives in the notes.)

## End of unit checklist
- [ ] all tasks done and in pull requests
- [ ] at least one teammate's pull request reviewed

**If you are short on time, cut in this order:** <tasks>. Never cut <the milestone tasks>.

Next: `unitN+1`.
```

This is a shape to imitate, not a contract - adjust the headings and sections to your subject. The parts that carry the teaching are:

- **outcomes written as things you can do**, never as topics
- **the glance table**, pairing every reading with the tasks it feeds
- **notes under tasks** - a trap, a proof, a "keep this for later"
- **the cut line** - honest priorities, not permission to slack

---

## 8. Diagrams: the project's way of thinking

Drawing forces agreement, so diagramming belongs in any project curriculum. Place drawings at the points where the project changes shape:

| Position | Drawing | Job |
|---|---|---|
| the start | the whole system on one page | a non-specialist can see what is being built |
| the first build | the flow, end to end | every step from source to user, with what does each step |
| mid-project | the flow, updated with reality | what the real work taught you, marked on the diagram |
| before the final build | the technical architecture | where every component and every check lives |
| the handover | the final architecture | the system exactly as it runs, for whoever inherits it |

*Example standard:* diagrams written as Mermaid inside Markdown files and committed to the repository - they render, they are diffable in reviews, and reviewers can comment on specific lines. Use whatever tool your group can review in the same way. Keep each drawing to one page.

---

## 9. The repository layout

The layout is a decision, not a mandate. A minimal starting point that works for almost any subject:

```text
<repo root>
├── README.md              what the project is and how to get started
├── CONTRIBUTING.md        the rules of the repo: commits, reviews, merging
├── work/                  per-person practice: one folder per person, one per time-box
└── shared/                the things everyone needs: the brief, the design, the product
```

Common additions, used when they fit:

| Folder | When it fits | What it holds |
|---|---|---|
| `docs/` | always, in some form | the supporting documents (section 10) |
| the shared build folder (name it for your subject) | when the group ships one shared product | the real build, with its own rules |
| `delivery/` | always, in some form | shared outputs: brief, design, presentation, handover |
| `admin/` | when answer keys exist | pointers only - keys never live in the repository |

Whatever folders you choose, never lose these two things: **one place where each person practises**, and **one place where the group's real outputs live**. Everything else is judgement.

---

## 10. The supporting documents: roles, not a fixed list

The documents folder exists to answer the questions people actually ask. Do not copy a fixed list from anywhere; start from the *roles* and keep the documents your subject needs. A typical set:

| Role | Answers the question | Example file |
|---|---|---|
| the map | what is this whole thing, and where do I start | START-HERE |
| the brief | what are we building, for whom, and why | project brief |
| the setup guide | install everything before day one | tools-setup |
| the working guide | fork, clone, commit, pull request | student guide |
| the overview | where are we in the project | project map |
| the task list | every task in the project, by track | task list |
| the roles | who reviews what, how roles rotate | team roles |
| the glossary | what does this word mean | glossary |
| the resources | what do I read or watch this time-box | resources |
| the troubleshooting | this tool broke like this - what now | troubleshooting |
| the tools guide | what is this tool for and why this one | tools and technology |

Keep the role, choose your own names, numbering, and order - and merge or drop roles your subject does not need (a subject with one tool needs no tools guide). The only rule: every document the time-box files point at must exist, and every student must know which document answers which kind of question.

---

## 11. Working rules that make it work

1. **One task, one file, one commit.** The task tells you the exact path.
2. **Name the task ID** in the commit message and the pull request title.
3. **Stay in your own work folder** unless you are on the shared build this time-box.
4. **Never squash merge** - it erases individual authorship, which is the record the group is building.
5. **No source-material files, no secrets** - raw downloads and credentials never enter the repository.
6. **Writing tasks are graded like code.** A good answer names the tradeoff, not just the fact.
7. **You will be asked "why" more than "what".** Every design choice has a reason and a rejected alternative.

---

## 12. Building the curriculum for your subject

A sequence of decisions, in the order they depend on each other.

1. **Choose the project.** The client story, the real source material, and the scope. A project too big to finish is as bad as one too small to learn from.
2. **Choose the length.** The number of time-boxes is your call. Divide the project across the four phases of section 3.
3. **Choose the tracks.** Two to five parallel tracks, each with a letter and a one-line purpose.
4. **Choose the milestones.** The five gate positions of section 4, renamed and placed where they fit.
5. **Write the task list.** Every task, by track, with a stable ID, a group, a short title, instructions, and a commit path. Write the groups in the order students will meet them.
6. **Split the tasks into time-box files.** Each file gets: the glance table, the outcomes, the groups with their notes, the checklist, the cut line, the next link. Milestone tasks always in the "never cut" position.
7. **Place the diagram tasks** at the points where the project changes shape (section 8).
8. **Write the supporting documents.** Start from the roles in section 10, keep only what this subject needs, and make every pointer from the time-box files resolve.
9. **Create the folders and copy the time-box templates into each person's folder.**
10. **Verify before publishing.** Task counts match between templates and the task list; IDs are unique; cross-references point at the right units; no leftovers from earlier drafts.

And the final sentence of every time-box file is the promise that keeps the group moving:

> Next: `unitN+1`.
