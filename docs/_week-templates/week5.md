# Week 5 — Big files and real extractors

**Data Sprint 1 · Week 5 of 10 · Theme: handle a file bigger than your laptop, then get data out of a PDF and a web page**

Read this whole file before you start. Then work through the stations in order.

---

## Before you start

Git commands: `docs/03-student-guide.md`. Client story and sources: `docs/01-project-brief.md`. Unknown word: `docs/08-glossary.md`. Broken tool: `docs/10-troubleshooting.md`. Each task names the exact file path to commit to, inside this same week folder.

---

## By the end of this week you can

- Explain why bronze is not normalized and gold is, in language a client would accept
- Stream a file too large to fit in memory, one row at a time
- Produce logs someone else could debug a failed run from
- Pull real data out of a PDF and out of an HTML table

## The thing to watch this week

**The state frequency map in P5.2.** It becomes the shared silver-layer cleaning rule in weeks 8 and 9. If your spellings are wrong or incomplete, the whole cohort's silver layer inherits it.

---

## The week at a glance

| Step | LEARN | DO |
|---|---|---|
| **1** | Kudvenkat parts 51 to 53 (normalization, pivot) | S8.1 S8.2 — normalization write-up, pivot |
| **2** | Real Python "Introduction to Python Generators" | P5.1 P5.2 P5.3 — generator, frequency map, memory explanation |
| **3** | Python `logging` HOWTO · `argparse` tutorial | P6.1 P6.2 — logging, CLI tool |
| **4** | Real Python OOP · `pdfplumber` README | P7.1 — the IBBI PDF extractor |
| **5** | Beautiful Soup quick start · Python `abc` module | P7.2 P7.3 — CDM extractor, base class refactor |
| **6** | — | Cohort review: extractor demos, state spelling reconciliation |

---

## Station S8: Normalization and Star Schema

Foundation link: Kudvenkat parts 51 to 53 (normalization, pivot).

- [ ] **S8.1** In three short paragraphs, explain: why the bronze layer is not normalized, why the gold layer is a denormalized star, and what problem each choice solves.
  **Commit:** `design/normalization_notes.md`, open a pull request.

- [ ] **S8.2** Pivot company counts so each state's row shows separate columns for Active, Strike Off, and Under Liquidation. Which state has the highest Strike Off column?
  **Commit:** `sql/s8/01_pivot_states.sql`, update the pull request.

---

## Station P5: Generators and Large File Handling

- [ ] **P5.1** Write a generator that yields one row at a time from a large RoC CSV without loading the whole file into memory. Use it to count rows and to count rows with empty capital fields, in one pass.
  **Commit:** `python/p5/row_generator.py` plus counts in `python/p5/notes.md`, open a pull request.

- [ ] **P5.2** Use the generator to build a state name frequency map for the largest RoC file: every distinct state spelling and its row count. This map will feed the silver layer cleaning rules.
  **Commit:** `python/p5/state_frequency.py` plus the top twenty entries in notes, update the pull request.

- [ ] **P5.3** In three sentences, explain why the generator version can handle a file larger than your laptop's memory while the P1 approach cannot.
  **Commit:** append to `python/p5/notes.md`, update the pull request.

**If your machine freezes or you see `MemoryError`,** you are still loading the whole file. That is the exact failure this station exists to fix; see `docs/10-troubleshooting.md`, Python section.

---

## Station P6: Logging and CLI Tools

- [ ] **P6.1** Replace every print call in your P4 and P5 scripts with proper logging: INFO for progress, WARNING for skipped rows, ERROR for failures. Logs must include timestamps.
  **Commit:** updated scripts in `python/p4/` and `python/p5/`, reference the original pull requests in the commit message.

- [ ] **P6.2** Turn the RBI download script into a command line tool: it must accept an output folder argument and a date argument, with helpful error messages for bad input.
  **Commit:** `python/p6/rbi_cli.py` plus example invocations in `python/p6/notes.md`, open a pull request.

**On P6.1:** the test of a log line is whether a teammate could find the failing row from it at 2am without your help. "Error" is not a log line. "WARNING row 41822 skipped, CIN length 19, file ROC_KERALA.csv" is.

---

## Station P7: OOP and Custom Extractors

- [ ] **P7.1** Write the IBBI PDF extractor: download the CIRP PDF, extract the table rows, validate each row with your P2 validator, and write one CSV to `data/raw/ibbi/` named with the quarter and pull date.
  **Commit:** `python/p7/ibbi_extractor.py` plus the first ten extracted rows in `python/p7/notes.md`, open a pull request.

- [ ] **P7.2** Write the MCA CDM portal extractor: read the state statistics table from the web page, convert Indian number formats to plain numbers, and write one CSV to `data/raw/cdm/`.
  **Commit:** `python/p7/cdm_extractor.py` plus sample output, update the pull request.

- [ ] **P7.3** Refactor all three extractors (RBI, IBBI, CDM) behind one abstract base class with a shared pull, validate, and save contract. Each source becomes a subclass. Write two sentences on what the refactor removed.
  **Commit:** `python/p7/extractors/` folder with the refactored code plus notes, update the pull request.

**On P7:** the PDF will not extract cleanly on the first attempt. Merged cells, headers repeating on every page, and numbers with commas are all normal. Fix the parsing, record what was wrong in notes, and keep the CSVs out of Git; only the code and the sample rows are committed.

---

## End of week checklist

- [ ] S8.1, S8.2 — the three-paragraph normalization write-up and the pivot with its answer
- [ ] P5.1, P5.2, P5.3 — generator, state frequency map with top twenty, memory explanation
- [ ] P6.1, P6.2 — logging with timestamps and levels, working CLI with example invocations
- [ ] P7.1, P7.2, P7.3 — two new extractors, all three behind one base class, and what the refactor removed
- [ ] At least one teammate's pull request reviewed with a real comment
- [ ] No CSV, PDF, or ZIP anywhere in your commits

**If you are short on time, cut in this order:** S8.2, then P7.3, then P6.2. Never cut P5.2 or P7.1. The frequency map and the PDF extractor are both inputs to week 8.

Next: `week6/problem_statement.md`.
