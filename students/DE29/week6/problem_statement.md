# Week 6 - Big files and cleaner tooling

**Data Sprint 1 · Week 6 of 13 · Theme: handle a file bigger than your laptop, then make code a teammate can debug**

Read this whole file before you start. Then work through the task groups in order.

---

## Before you start

Git commands: `docs/03-student-guide.md`. Client story and sources: `docs/01-project-brief.md`. Unknown word: `docs/08-glossary.md`. Broken tool: `docs/10-troubleshooting.md`. What a tool is for: `docs/11-tools-and-technology.md`. Each task names the exact file path to commit to, inside this same week folder.

---

## By the end of this week you can

- Explain why bronze is not normalized and gold is, in language a client would accept
- Stream a file too large to fit in memory, one row at a time
- Produce logs someone else could debug a failed run from

## The thing to watch this week

**The state frequency map in Task 4 (P5.2).** It becomes the shared silver-layer cleaning rule in week 10. If your spellings are wrong or incomplete, the whole cohort's silver layer inherits it.

---

## The week at a glance

| Step | LEARN | DO |
|---|---|---|
| **1** | Kudvenkat parts 51 to 53 (normalization, pivot) | Tasks 1–2 - normalization write-up, pivot |
| **2** | Real Python "Introduction to Python Generators" | Tasks 3–5 - generator, frequency map, memory explanation |
| **3** | Python `logging` HOWTO · `argparse` tutorial | Tasks 6–7 - logging, CLI tool |
| **4** | - | Cohort review: state spelling reconciliation |

---

## 1 · Normalization

Foundation link: Kudvenkat parts 51 to 53 (normalization, pivot).

- [ ] **Task 1 - Explain the layer choices** (ID `S8.1`): In three short paragraphs, explain: why the bronze layer is not normalized, why the gold layer is a denormalized star, and what problem each choice solves.
  **Commit:** `design/normalization_notes.md`, open a pull request.

- [ ] **Task 2 - Pivot company counts by state** (ID `S8.2`): Pivot company counts so each state's row shows separate columns for Active, Strike Off, and Under Liquidation. Which state has the highest Strike Off column?
  **Commit:** `sql/s8/01_pivot_states.sql`, update the pull request.

---

## 2 · Generators and Large Files

- [ ] **Task 3 - Write a row generator** (ID `P5.1`): Write a generator that yields one row at a time from a large RoC CSV without loading the whole file into memory. Use it to count rows and to count rows with empty capital fields, in one pass.
  **Commit:** `python/p5/row_generator.py` plus counts in `python/p5/notes.md`, open a pull request.

- [ ] **Task 4 - Build the state frequency map** (ID `P5.2`): Use the generator to build a state name frequency map for the largest RoC file: every distinct state spelling and its row count. This map will feed the silver layer cleaning rules.
  **Commit:** `python/p5/state_frequency.py` plus the top twenty entries in notes, update the pull request.

- [ ] **Task 5 - Explain the memory win** (ID `P5.3`): In three sentences, explain why the generator version can handle a file larger than your laptop's memory while the P1 approach cannot.
  **Commit:** append to `python/p5/notes.md`, update the pull request.

**If your machine freezes or you see `MemoryError`**, you are still loading the whole file. That is the exact failure this group exists to fix; see `docs/10-troubleshooting.md`, Python section.

---

## 3 · Logging and Command Line Tools

- [ ] **Task 6 - Replace prints with logging** (ID `P6.1`): Replace every print call in your P4 and P5 scripts with proper logging: INFO for progress, WARNING for skipped rows, ERROR for failures. Logs must include timestamps.
  **Commit:** updated scripts in `python/p4/` and `python/p5/`, reference the original pull requests in the commit message.

- [ ] **Task 7 - Make the RBI download a CLI tool** (ID `P6.2`): Turn the RBI download script into a command line tool: it must accept an output folder argument and a date argument, with helpful error messages for bad input.
  **Commit:** `python/p6/rbi_cli.py` plus example invocations in `python/p6/notes.md`, open a pull request.

**On Task 6:** the test of a log line is whether a teammate could find the failing row from it at 2am without your help. "Error" is not a log line. "WARNING row 41822 skipped, CIN length 19, file ROC_KERALA.csv" is.

---

## End of week checklist

- [ ] Tasks 1–2 - the three-paragraph normalization write-up and the pivot with its answer
- [ ] Tasks 3–5 - generator, state frequency map with top twenty, memory explanation
- [ ] Tasks 6–7 - logging with timestamps and levels, working CLI with example invocations
- [ ] At least one teammate's pull request reviewed with a real comment
- [ ] No CSV, PDF, or ZIP anywhere in your commits

**If you are short on time, cut in this order:** Task 2 (S8.2), then Task 7 (P6.2). Never cut Task 4 (P5.2). The frequency map feeds week 10's silver cleaning rules.

Next: `week7/problem_statement.md`.
