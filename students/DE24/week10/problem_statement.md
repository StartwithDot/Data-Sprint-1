# Week 10 — Break it, explain it, hand it over

**Data Sprint 1 · Week 10 of 10 · Theme: prove the pipeline survives failure, then hand it to a stranger**

Read this whole file before you start. Then work through the stations in order.

---

## Before you start

Platform rules before you touch `platform/`, `airflow/`, or `quality/`: `docs/07-platform-and-cicd-guide.md` and `docs/06-team-roles.md`. Git commands: `docs/03-student-guide.md`. Unknown word: `docs/08-glossary.md`. Broken tool: `docs/10-troubleshooting.md`.

This is the heaviest week of the sprint. Read the whole file before you start, and plan the order you will work in.

---

## By the end of this week you can

- Diagnose a failure you did not cause, from logs, tests, and row counts
- Write a postmortem that blames the system and not a person
- Build a dashboard a non-technical analyst can read without you next to them
- Present to a client with zero tool names, including what the platform cannot tell them
- Orchestrate the monthly refresh so the quality gate stops it before gold is touched
- Hand over a pipeline someone else can run from a clean checkout

## The milestones this week

**B8 Project Handover** and **D10 Project Handover.** D10.1 is the real test: a clean checkout, a fresh schema, and only the runbook to guide you. Every gap you find is a gap you fix.

---

## The week at a glance

| Step | LEARN | DO |
|---|---|---|
| **1** | Airflow "Core Concepts" | D9.1 — the monthly refresh DAG |
| **2** | Airflow on failure handling and retries | D9.2 B4.1 — the gate that stops the pipeline, two reviews |
| **3** | Google SRE "Postmortem Culture" chapter | B5.1 B5.2 B4.2 — the injected failure, postmortem, your fix |
| **4** | Metabase docs on dashboards | B6.1 B6.2 — four views, plain language labels |
| **5** | — | B7.1 B7.2 B8.1 B8.2 D10.1 D10.2 — presentation, runbook, clean run, archive |
| **6** | — | Final review: client presentation, handover walkthrough |

---

## Station B4: Build, PR and Peer Review

- [ ] **B4.1** Review two pull requests from teammates. For each, leave at least one real comment: a question, a spotted mistake, or a suggested improvement. No "looks good" reviews.
  **Commit:** nothing new; paste the links to your two reviewed pull requests in `delivery/review_log.md` and open a pull request with that file.

- [ ] **B4.2** Fix one piece of review feedback you received on your own work, and reply to the reviewer explaining what you changed.
  **Commit:** the fix in its original folder, reference the original pull request in your new commit message.

---

## Station B5: Break and Fix, Postmortem

- [ ] **B5.1** The program leads will introduce a failure into the project data or pipeline. Find what broke, using logs, tests, and row counts. Write down the evidence trail that led you to the cause.
  **Commit:** `delivery/break_fix_notes.md`, open a pull request.

- [ ] **B5.2** Write a one page postmortem: what broke, why it happened, how it was found, what was done to fix it, and what one change would stop it from happening again.
  **Commit:** `delivery/postmortem.md`, open a pull request.

**On B5.1:** write the trail as you go, including the wrong guesses. The order you checked things in is the part worth reviewing, and reconstructing it afterwards from memory produces fiction.

**On B5.2:** no names. "The load was not verified before the merge ran" is a system fault. "X forgot to check" is not a postmortem, it is blame, and it teaches nobody anything.

---

## Station B6: Metabase Dashboard

- [ ] **B6.1** Build a dashboard in Metabase on top of the gold tables with at least these four views: company status counts by state, insolvency events by quarter, capital distribution by business activity, and a company search that shows current status plus status history.
  **Commit:** export or screenshot the dashboard definition into `dashboard/dashboard_definition.md` with a short description of each view, open a pull request.

- [ ] **B6.2** Write the plain language label and one sentence explanation for each dashboard view, as it should appear to a non technical analyst.
  **Commit:** append to `dashboard/dashboard_definition.md`, update the pull request.

**On B6.1:** the company search view is where the client sees ten weeks of SCD2 work pay off. Current status plus the history that led to it, in one place, is the whole point of the sprint.

**Build on gold tables only.** A dashboard reaching into bronze or silver breaks the layer contract you wrote in week 9, and it breaks quietly.

---

## Station B7: Stakeholder Delivery

- [ ] **B7.1** Write a five minute stakeholder presentation script. It must contain zero tool names. It must say what the data shows, what the client should do with it, and what the platform cannot tell them.
  **Commit:** `delivery/presentation_script.md`, open a pull request.

- [ ] **B7.2** Present to a peer playing the client. Record their three hardest questions and your answers, or "I did not know" where true.
  **Commit:** `delivery/qa_log.md`, open a pull request.

**On B7.1:** the limits section is the part that earns trust. Unmatched CINs, a state whose data is thin, a source that updates quarterly and not monthly — say it plainly. A client who discovers a limit after the handover stops believing the rest.

---

## Station B8: Project Handover **[MILESTONE]**

- [ ] **B8.1** Write the runbook: how to refresh each data source, what to check when a run fails, who to contact for what, and where every piece of documentation lives.
  **Commit:** `delivery/runbook.md`, open a pull request.

- [ ] **B8.2** Write the final README for the repository root, so a stranger can understand what this project is, how it is structured, and how to run it.
  **Commit:** `/README.md`, open a pull request.

---

## Station D9: Airflow Orchestration

- [ ] **D9.1** Write the monthly refresh DAG: snapshot preparation, bronze loads, dbt build, Great Expectations gate, with correct dependency order. Draw or describe the dependency graph in notes.
  **Commit:** `airflow/monthly_refresh_dag.py` plus `airflow/notes.md`, open a pull request.

- [ ] **D9.2** Add the failure behavior: the quality gate must stop the pipeline before gold tables are touched, and the failure must be visible in logs with the source file named.
  **Commit:** updated DAG plus a paste of a deliberate failure run in `airflow/notes.md`, update the pull request.

**On D9.2:** the deliberate failure run is the deliverable. A DAG that only has a green run proves the happy path, and the happy path was never in doubt. Show the gate stopping the pipeline with gold untouched.

---

## Station D10: Project Handover **[MILESTONE]**

- [ ] **D10.1** Run the full pipeline from a clean checkout on a fresh Snowflake schema, following only the runbook. Record every place the runbook was unclear or wrong, and fix it.
  **Commit:** updated `delivery/runbook.md` plus `delivery/clean_run_log.md`, open a pull request.

- [ ] **D10.2** Archive the project: final README, all documentation linked, every pull request merged or explicitly closed with a reason.
  **Commit:** final state of the repository, final pull request titled "Project handover".

**On D10.1:** follow the runbook literally, including the steps you know by heart. Every time you use knowledge that is in your head and not in the file, that is a gap, and it goes in the log before you fix it.

---

## End of week checklist

- [ ] B4.1, B4.2 — two real reviews logged, and one piece of feedback fixed with a reply
- [ ] B5.1, B5.2 — evidence trail including wrong guesses, and a blameless postmortem with one prevention
- [ ] B6.1, B6.2 — four views on gold tables, each with a plain language label and explanation
- [ ] B7.1, B7.2 — a script with zero tool names and a real limits section, plus three hard questions logged
- [ ] B8.1, B8.2 — runbook and final root README
- [ ] D9.1, D9.2 — DAG with correct dependencies, and a failure run showing the gate stopping it
- [ ] D10.1, D10.2 — clean run log with every runbook gap fixed, and the handover pull request
- [ ] Nothing secret, nothing large, nothing generated is in the repository

**If you are short on time, cut in this order:** B6.2, then B4.2, then D9.2's screenshot polish. Never cut B8.1, D10.1, or B5.2. The handover is the sprint's actual output.

---

## When this sprint is finished

Read `docs/00-START-HERE.md` once more, the section on what happens after week 10. Then re-read your own week 1 discovery brief. The gap between what you thought the work was in week 1 and what you now know it is, is the thing you carry into Sprint 2.
