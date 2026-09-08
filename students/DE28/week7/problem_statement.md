# Week 7 — Extractors and the design sign-off

**Data Sprint 1 · Week 7 of 13 · Theme: get real data out of a PDF and a web page, then put what you learned back into the design**

Read this whole file before you start. Then work through the task groups in order.

---

## Before you start

Git commands: `docs/03-student-guide.md`. Client story and sources: `docs/01-project-brief.md`. Unknown word: `docs/08-glossary.md`. Broken tool: `docs/10-troubleshooting.md`. What a tool is for: `docs/11-tools-and-technology.md`. Each task names the exact file path to commit to, inside this same week folder.

---

## By the end of this week you can

- Pull real data out of a PDF and out of an HTML table
- Refactor three extractors behind one base class
- Write a specific, named risk your Python work creates for the design
- Update the pipeline flow diagram with what the real sources taught you

## The milestone this week

**P8 Star Schema Design, Python side.** The design agreed in weeks 4 and 5 must survive what the Python work now says can go wrong. If your extractor produces duplicate CINs or unparseable dates, the design has to handle it, and this is the week to say so.

---

## The week at a glance

| Step | LEARN | DO |
|---|---|---|
| **1** | Real Python OOP · `pdfplumber` README | Task 1 — the IBBI PDF extractor |
| **2** | Beautiful Soup quick start · Python `abc` module | Tasks 2–3 — CDM extractor, base class refactor |
| **3** | — | Task 4 — the design review paragraph |
| **4** | Re-read your week 4 pipeline flow diagram | Task 5 — the design review update |
| **5** | — | Cohort review: extractor demos, design review sign-off |

---

## 1 · Object Oriented Extractors

- [ ] **Task 1 — Write the IBBI PDF extractor** (ID `P7.1`): Write the IBBI PDF extractor: download the CIRP PDF, extract the table rows, validate each row with your P2 validator, and write one CSV to `data/raw/ibbi/` named with the quarter and pull date.
  **Commit:** `python/p7/ibbi_extractor.py` plus the first ten extracted rows in `python/p7/notes.md`, open a pull request.

- [ ] **Task 2 — Write the CDM portal extractor** (ID `P7.2`): Write the MCA CDM portal extractor: read the state statistics table from the web page, convert Indian number formats to plain numbers, and write one CSV to `data/raw/cdm/`.
  **Commit:** `python/p7/cdm_extractor.py` plus sample output, update the pull request.

- [ ] **Task 3 — Refactor behind one base class** (ID `P7.3`): Refactor all three extractors (RBI, IBBI, CDM) behind one abstract base class with a shared pull, validate, and save contract. Each source becomes a subclass. Write two sentences on what the refactor removed.
  **Commit:** `python/p7/extractors/` folder with the refactored code plus notes, update the pull request.

**On this group:** the PDF will not extract cleanly on the first attempt. Merged cells, headers repeating on every page, and numbers with commas are all normal. Fix the parsing, record what was wrong in notes, and keep the CSVs out of Git; only the code and the sample rows are committed.


---

## 2 · Design Review from the Python Side **[MILESTONE]**

- [ ] **Task 4 — Write the pipeline risk paragraph** (ID `P8.1`): Join the group design review. Bring one written paragraph: which part of the pipeline your Python work feeds, and what can go wrong in it that the design must survive.
  **Commit:** `design/pipeline_risk_notes.md`, open a pull request.

**On Task 4:** be specific. "The IBBI PDF can shift its column order between quarters, so the extractor must match on header text and not on position, and the fact table needs a load timestamp to tell two quarters apart" is a risk. "Data quality issues" is not.

---

## 3 · Design Review Update

- [ ] **Task 5 — Update the pipeline flow diagram** (ID `A3.1`): Update the pipeline flow diagram from week 4 with what the real extractors taught you: which source needs a browser download, which PDF columns shift between quarters, which number formats needed converting, and where the bronze load timestamp sits. Mark each change on the diagram and list, in notes, what changed and why.
  **Commit:** update `design/pipeline_flow.md` plus the change list in `design/pipeline_flow_notes.md`, open a pull request.

**On Task 5:** a diagram that is wrong is worse than no diagram, because nobody re-checks a picture. This is the first real check of whether the design survives contact with the data.

---

## End of week checklist

- [ ] Task 1 — the IBBI PDF extractor with the first ten rows in notes
- [ ] Tasks 2–3 — the CDM extractor and all three behind one base class, with what the refactor removed
- [ ] Task 4 — a specific, named risk your Python work creates for the design
- [ ] Task 5 — the pipeline flow diagram updated, with the change list in notes
- [ ] At least one teammate's pull request reviewed with a real comment
- [ ] No CSV, PDF, or ZIP anywhere in your commits

**If you are short on time, cut in this order:** Task 5 (A3.1), then Task 3 (P7.3). Never cut Task 1 (P7.1) or Task 4 (P8.1). The extractor is the hardest code in the sprint, and the design review is the milestone.

Next: `week8/problem_statement.md`.
