# Week 13 — Present and hand over

**Data Sprint 1 · Week 13 of 13 · Theme: make the work visible to the client, then hand it to a stranger**

Read this whole file before you start. Then work through the task groups in order.

---

## Before you start

Platform rules before you touch `platform/`, `airflow/`, `quality/`, or `delivery/`: `docs/07-platform-and-cicd-guide.md` and `docs/06-team-roles.md`. Git commands: `docs/03-student-guide.md`. Unknown word: `docs/08-glossary.md`. Broken tool: `docs/10-troubleshooting.md`. What a tool is for: `docs/11-tools-and-technology.md`.

This is the heaviest week of the sprint. Read the whole file before you start, and plan the order you will work in.

---

## By the end of this week you can

- Build a dashboard a non-technical analyst can read without you next to them
- Present to a client with zero tool names, including what the platform cannot tell them
- Draw the final architecture diagram for the handover
- Hand over a pipeline someone else can run from a clean checkout

## The milestones this week

**B8 Project Handover** and **D10 Project Handover.** D10.1 is the real test: a clean checkout, a fresh schema, and only the runbook to guide you. Every gap you find is a gap you fix.

---

## The week at a glance

| Step | LEARN | DO |
|---|---|---|
| **1** | Metabase docs on dashboards | Tasks 1–2 — four views, plain language labels |
| **2** | — | Tasks 3–4 — the presentation script, the Q&A log |
| **3** | Re-read your week 1 system map and week 9 architecture diagram | Task 5 — the final architecture |
| **4** | — | Tasks 6–9 — runbook, final README, clean run, archive |
| **5** | — | Final review: client presentation, handover walkthrough |

---

## 1 · Dashboard

- [ ] **Task 1 — Build the dashboard** (ID `B6.1`): Build a dashboard in Metabase on top of the gold tables with at least these four views: company status counts by state, insolvency events by quarter, capital distribution by business activity, and a company search that shows current status plus status history.
  **Commit:** export or screenshot the dashboard definition into `dashboard/dashboard_definition.md` with a short description of each view, open a pull request.

- [ ] **Task 2 — Write the plain language labels** (ID `B6.2`): Write the plain language label and one sentence explanation for each dashboard view, as it should appear to a non technical analyst.
  **Commit:** append to `dashboard/dashboard_definition.md`, update the pull request.

**On Task 1:** the company search view is where the client sees the whole sprint's SCD2 work pay off. Current status plus the history that led to it, in one place, is the whole point of the project.

**Build on gold tables only.** A dashboard reaching into bronze or silver breaks the layer contract you wrote in week 11, and it breaks quietly.


---

## 2 · Stakeholder Delivery

- [ ] **Task 3 — Write the presentation script** (ID `B7.1`): Write a five minute stakeholder presentation script. It must contain zero tool names. It must say what the data shows, what the client should do with it, and what the platform cannot tell them.
  **Commit:** `delivery/presentation_script.md`, open a pull request.

- [ ] **Task 4 — Rehearse and log the hard questions** (ID `B7.2`): Present to a peer playing the client. Record their three hardest questions and your answers, or "I did not know" where true.
  **Commit:** `delivery/qa_log.md`, open a pull request.

**On Task 3:** the limits section is the part that earns trust. Unmatched CINs, a state whose data is thin, a source that updates quarterly and not monthly — say it plainly. A client who discovers a limit after the handover stops believing the rest.

---

## 3 · Final Architecture for Handover

- [ ] **Task 5 — Draw the final architecture** (ID `A4.1`): Draw the final architecture for the handover: the end-to-end pipeline exactly as it runs today — sources, extractors, stages, bronze, silver, gold, the quality gate, Airflow, the dashboard — plus the final star schema. Start from your week 1 system map and your week 9 architecture diagram and update them with everything that changed since.
  **Commit:** `design/final_architecture.md` (embed the diagram), then embed it in `delivery/runbook.md` and `/README.md`.

**On Task 5:** the diagrams must match what the code actually does. If the runbook and the diagram disagree, a stranger will trust whichever one happens to be right on the day — and you will not know which that is.

---

## 4 · Project Handover **[MILESTONE]**

- [ ] **Task 6 — Write the runbook** (ID `B8.1`): Write the runbook: how to refresh each data source, what to check when a run fails, who to contact for what, and where every piece of documentation lives.
  **Commit:** `delivery/runbook.md`, open a pull request.

- [ ] **Task 7 — Write the final README** (ID `B8.2`): Write the final README for the repository root, so a stranger can understand what this project is, how it is structured, and how to run it.
  **Commit:** `/README.md`, open a pull request.

- [ ] **Task 8 — Run the clean handover test** (ID `D10.1`): Run the full pipeline from a clean checkout on a fresh Snowflake schema, following only the runbook. Record every place the runbook was unclear or wrong, and fix it.
  **Commit:** updated `delivery/runbook.md` plus `delivery/clean_run_log.md`, open a pull request.

- [ ] **Task 9 — Archive the project** (ID `D10.2`): Archive the project: final README, all documentation linked, every pull request merged or explicitly closed with a reason.
  **Commit:** final state of the repository, final pull request titled "Project handover".

**On Task 8:** follow the runbook literally, including the steps you know by heart. Every time you use knowledge that is in your head and not in the file, that is a gap, and it goes in the log before you fix it.

---

## End of week checklist

- [ ] Tasks 1–2 — four views on gold tables, each with a plain language label and explanation
- [ ] Tasks 3–4 — a script with zero tool names and a real limits section, plus three hard questions logged
- [ ] Task 5 — the final architecture and schema diagram, embedded in the runbook and the final README
- [ ] Tasks 6–7 — the runbook and the final root README
- [ ] Tasks 8–9 — clean run log with every runbook gap fixed, and the handover pull request
- [ ] Nothing secret, nothing large, nothing generated is in the repository

**If you are short on time, cut in this order:** Task 2 (B6.2), then Task 4 (B7.2), then Task 5's polish. Never cut Tasks 6, 8, or 9 (B8.1, D10.1, D10.2). The handover is the sprint's actual output.

---

## When this sprint is finished

Read `docs/00-START-HERE.md` once more, the section on what happens after week 13. Then re-read your own week 1 discovery brief. The gap between what you thought the work was in week 1 and what you now know it is, is the thing you carry into Sprint 2.
