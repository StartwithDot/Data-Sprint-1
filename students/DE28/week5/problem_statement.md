# Week 5 Tasks

> **Before you start:** the setup steps and daily Git commands are in `docs/student-guide.md`. The client story and the four data sources are in `docs/project-brief.md`. Each task below tells you the exact file path to commit to, and that path sits inside this same week folder.

## Station S8: Normalization and Star Schema

Foundation link: Kudvenkat parts 51 to 53 (normalization, pivot).

- [ ] **S8.1** In three short paragraphs, explain: why the bronze layer is not normalized, why the gold layer is a denormalized star, and what problem each choice solves.
  **Commit:** `design/normalization_notes.md`, open a pull request.

- [ ] **S8.2** Pivot company counts so each state's row shows separate columns for Active, Strike Off, and Under Liquidation. Which state has the highest Strike Off column?
  **Commit:** `sql/s8/01_pivot_states.sql`, update the pull request.

## Station P5: Generators and Large File Handling

- [ ] **P5.1** Write a generator that yields one row at a time from a large RoC CSV without loading the whole file into memory. Use it to count rows and to count rows with empty capital fields, in one pass.
  **Commit:** `python/p5/row_generator.py` plus counts in `python/p5/notes.md`, open a pull request.

- [ ] **P5.2** Use the generator to build a state name frequency map for the largest RoC file: every distinct state spelling and its row count. This map will feed the silver layer cleaning rules.
  **Commit:** `python/p5/state_frequency.py` plus the top twenty entries in notes, update the pull request.

- [ ] **P5.3** In three sentences, explain why the generator version can handle a file larger than your laptop's memory while the P1 approach cannot.
  **Commit:** append to `python/p5/notes.md`, update the pull request.

## Station P6: Logging and CLI Tools

- [ ] **P6.1** Replace every print call in your P4 and P5 scripts with proper logging: INFO for progress, WARNING for skipped rows, ERROR for failures. Logs must include timestamps.
  **Commit:** updated scripts in `python/p4/` and `python/p5/`, reference the original pull requests in the commit message.

- [ ] **P6.2** Turn the RBI download script into a command line tool: it must accept an output folder argument and a date argument, with helpful error messages for bad input.
  **Commit:** `python/p6/rbi_cli.py` plus example invocations in `python/p6/notes.md`, open a pull request.

## Station P7: OOP and Custom Extractors

- [ ] **P7.1** Write the IBBI PDF extractor: download the CIRP PDF, extract the table rows, validate each row with your P2 validator, and write one CSV to `data/raw/ibbi/` named with the quarter and pull date.
  **Commit:** `python/p7/ibbi_extractor.py` plus the first ten extracted rows in `python/p7/notes.md`, open a pull request.

- [ ] **P7.2** Write the MCA CDM portal extractor: read the state statistics table from the web page, convert Indian number formats to plain numbers, and write one CSV to `data/raw/cdm/`.
  **Commit:** `python/p7/cdm_extractor.py` plus sample output, update the pull request.

- [ ] **P7.3** Refactor all three extractors (RBI, IBBI, CDM) behind one abstract base class with a shared pull, validate, and save contract. Each source becomes a subclass. Write two sentences on what the refactor removed.
  **Commit:** `python/p7/extractors/` folder with the refactored code plus notes, update the pull request.

