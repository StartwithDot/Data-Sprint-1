# Week 12 - Orchestrate, break, fix

**Data Sprint 1 · Week 12 of 13 · Theme: put a calendar on the pipeline, then break it on purpose and prove you can find it**

Read this whole file before you start. Then work through the task groups in order.

---

## Before you start

Platform rules before you touch `platform/`, `airflow/`, or `quality/`: `docs/07-platform-and-cicd-guide.md` and `docs/06-team-roles.md`. Git commands: `docs/03-student-guide.md`. Unknown word: `docs/08-glossary.md`. Broken tool: `docs/10-troubleshooting.md`. What a tool is for: `docs/11-tools-and-technology.md`.

---

## By the end of this week you can

- Write expectation suites and a gate that stops bad data before it reaches gold
- Orchestrate the monthly refresh so the gate stops the pipeline before gold is touched
- Review someone's work usefully, and fix your own in response to feedback
- Find an injected failure from evidence and write a blameless postmortem

---

## The week at a glance

| Step | LEARN | DO |
|---|---|---|
| **1** | Great Expectations "Getting Started" | Tasks 1–2 - raw suite, gold gate |
| **2** | Airflow "Core Concepts" | Tasks 3–4 - the monthly refresh DAG, the gate that stops it |
| **3** | - | Task 5 - GE versus dbt, in three sentences |
| **4** | Google SRE "Postmortem Culture" chapter | Tasks 6–9 - two reviews, one fix, the break-fix evidence trail, the postmortem |
| **5** | - | Cohort review: gold gate results, postmortem walkthrough |

---

## 1 · Quality Gates with Great Expectations

- [ ] **Task 1 - Write the raw expectations** (ID `D8.1`): Write expectation suites for the raw MCA files: CIN length, allowed status values, no fully empty rows, state names within the known list.
  **Commit:** `quality/expectations/mca_suite.json` (or the format your setup uses) plus a run report in `quality/notes.md`, open a pull request.

- [ ] **Task 2 - Write the gold gate** (ID `D8.2`): Write the gold layer gate: every CIN in fct_cirp_event must exist in dim_company, every end date must be after its start date, no overlapping version periods per company. Run it against the built marts and paste results.
  **Commit:** `quality/expectations/gold_suite.json` plus run report, update the pull request.

- [ ] **Task 3 - GE versus dbt** (ID `D8.3`): In three sentences, explain what Great Expectations catches that dbt tests do not, and why the project runs both.
  **Commit:** append to `quality/notes.md`, update the pull request.

**On Task 2:** the three checks are exactly the SCD2 correctness checks from week 9, now automated. That is the point: a rule you had to remember to run by hand is a rule that eventually does not get run.

**When an expectation fails, fix the data or the rule, never the threshold.** Loosening a check until it passes is the failure mode this group exists to teach you to avoid.


---

## 2 · Airflow Orchestration

- [ ] **Task 4 - Write the monthly refresh DAG** (ID `D9.1`): Write the monthly refresh DAG: snapshot preparation, bronze loads, dbt build, Great Expectations gate, with correct dependency order. Draw or describe the dependency graph in notes.
  **Commit:** `airflow/monthly_refresh_dag.py` plus `airflow/notes.md`, open a pull request.

- [ ] **Task 5 - Make the gate stop the pipeline** (ID `D9.2`): Add the failure behavior: the quality gate must stop the pipeline before gold tables are touched, and the failure must be visible in logs with the source file named.
  **Commit:** updated DAG plus a paste of a deliberate failure run in `airflow/notes.md`, update the pull request.

**On Task 5:** the deliberate failure run is the deliverable. A DAG that only has a green run proves the happy path, and the happy path was never in doubt. Show the gate stopping the pipeline with gold untouched.

---

## 3 · Peer Review

- [ ] **Task 6 - Review two pull requests** (ID `B4.1`): Review two pull requests from teammates. For each, leave at least one real comment: a question, a spotted mistake, or a suggested improvement. No "looks good" reviews.
  **Commit:** nothing new; paste the links to your two reviewed pull requests in `delivery/review_log.md` and open a pull request with that file.

- [ ] **Task 7 - Fix one piece of feedback** (ID `B4.2`): Fix one piece of review feedback you received on your own work, and reply to the reviewer explaining what you changed.
  **Commit:** the fix in its original folder, reference the original pull request in your new commit message.

---

## 4 · Break, Fix and Postmortem

- [ ] **Task 8 - Find the injected failure** (ID `B5.1`): The program leads will introduce a failure into the project data or pipeline. Find what broke, using logs, tests, and row counts. Write down the evidence trail that led you to the cause.
  **Commit:** `delivery/break_fix_notes.md`, open a pull request.

- [ ] **Task 9 - Write the postmortem** (ID `B5.2`): Write a one page postmortem: what broke, why it happened, how it was found, what was done to fix it, and what one change would stop it from happening again.
  **Commit:** `delivery/postmortem.md`, open a pull request.

**On Task 8:** write the trail as you go, including the wrong guesses. The order you checked things in is the part worth reviewing, and reconstructing it afterwards from memory produces fiction.

**On Task 9:** no names. "The load was not verified before the merge ran" is a system fault. "X forgot to check" is not a postmortem, it is blame, and it teaches nobody anything.

---

## End of week checklist

- [ ] Tasks 1–2 - raw suite and gold gate, with run results pasted
- [ ] Task 3 - the GE versus dbt answer
- [ ] Tasks 4–5 - the monthly refresh DAG with correct dependencies, and a failure run showing the gate stopping it
- [ ] Tasks 6–7 - two real reviews logged, and one piece of feedback fixed with a reply
- [ ] Tasks 8–9 - evidence trail including wrong guesses, and a blameless postmortem with one prevention
- [ ] Nothing secret, nothing large, nothing generated is in the repository

**If you are short on time, cut in this order:** Task 3 (D8.3), then Task 7 (B4.2), then Task 5's screenshot polish. Never cut Task 5 (D9.2), Task 8 (B5.1), or Task 9 (B5.2). The gate, the evidence trail, and the postmortem are the point of the week.

Next: `week13/problem_statement.md`.
