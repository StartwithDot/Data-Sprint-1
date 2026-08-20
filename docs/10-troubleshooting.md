# Troubleshooting

**Open this when a tool breaks and the error means nothing to you.** Find your symptom, apply the fix, and if it still fails, post in Discord with the exact command and the exact error.

Everything here is a tooling failure, not a thinking failure. Nothing in this file gives away an answer to a task.

---

## How to ask for help so you get help fast

Post four things, in this order:

1. What you were trying to do, in one line.
2. The exact command you ran, in a code block.
3. The exact error, in a code block, including the last ten lines.
4. What you already tried.

Screenshots of terminals are hard to read and impossible to search. Paste text.

---

## Git

### `fatal: not a git repository`

You are in the wrong folder. `cd` into the cloned repository. `pwd` tells you where you are, `ls` shows whether you can see `README.md` and `students/`.

### Push rejected: `Authentication failed`

GitHub does not accept your account password from the command line.

- Using HTTPS: generate a personal access token with the `repo` scope and paste that when asked for a password. See `02-tools-setup.md`, section 2.
- Using SSH: check `ssh -T git@github.com` greets you by username.

### Push rejected: `Updates were rejected because the remote contains work that you do not have`

Someone else pushed since you last pulled.

```bash
git fetch upstream
git rebase upstream/main
# fix any conflicts, then:
git push --force-with-lease
```

Use `--force-with-lease`, never plain `--force`. It refuses to overwrite work you have not seen.

### Merge conflict

Git stopped because two changes touch the same lines. The file now contains markers:

```
<<<<<<< HEAD
your version
=======
their version
>>>>>>> upstream/main
```

1. Open the file, decide what the correct final content is, delete all three marker lines.
2. `git add path/to/file`
3. `git rebase --continue` (or `git commit` if you were merging)
4. `git push --force-with-lease`

To abandon the attempt and get back to where you were: `git rebase --abort`.

Ask for a review if the conflict is in `platform/`. Never resolve a shared-zone conflict by deleting someone else's work.

### I committed a data file or a password

**Stop. Do not push.** If you have not pushed yet:

```bash
git rm --cached path/to/file
git commit --amend
```

If you already pushed, say so in Discord immediately and name the file. If it was a credential, assume it is compromised and rotate it. Removing a secret from history requires an admin, and pretending it did not happen is the only unforgivable version of this mistake.

### My commits do not show on my GitHub contribution graph

The commit email does not match a verified email on your GitHub account.

```bash
git log -1 --format='%an %ae'
git config --global user.email "your.github.email@example.com"
```

Future commits will count. Earlier ones can be fixed by an admin if it matters.

### `Please tell me who you are`

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### CI is red on my pull request and I cannot tell why

Open the pull request, click **Details** next to the failing check, then click the failing step. Read the *first* error, not the last one; later errors are usually consequences.

The most common causes: trailing whitespace, a missing final newline, tabs instead of spaces, uppercase or lowercase keyword style, or a file in a folder CI lints (`platform/`, `delivery/`) that is not formatted. Run the linter locally first:

```bash
sqlfluff lint path/to/file.sql
flake8 path/to/file.py
```

---

## Python

### `command not found: python` on macOS or Linux

Use `python3`. On Windows use `python`.

### `python` opens the Microsoft Store on Windows

Python is not on PATH. Reinstall from `python.org` and tick **Add python.exe to PATH** on the first screen.

### `ModuleNotFoundError: No module named 'pandas'`

Either the virtual environment is not active, or the package was installed into a different Python.

```bash
source .venv/bin/activate      # macOS / Linux
.venv\Scripts\activate         # Windows
which python                   # should be inside .venv
pip install pandas
```

You must re-run the activate line in every new terminal.

### `pip: command not found`

```bash
python3 -m pip install --upgrade pip
```

Then use `python3 -m pip install ...` if plain `pip` still fails.

### `UnicodeDecodeError` when reading a CSV

Indian government CSVs are frequently not UTF-8.

```python
open(path, encoding="utf-8-sig")     # strips a byte order mark
open(path, encoding="latin-1")       # last resort, never fails, may mangle characters
```

Record which encoding each file needed in your notes. Station D2 asks for it.

### `SSLError` or `CertificateError` downloading from a government site

Some government hosts have a broken certificate chain. Do not blanket-disable verification. First try a session with a proper user agent and a retry. If it still fails, note it in your notes file and raise it in Discord: the fix belongs in the shared extractor, not in your script.

### The script hangs forever on a download

You did not pass a timeout. Every network call in this project needs one:

```python
requests.get(url, timeout=30)
```

A hang with no timeout is why station P4 exists.

### `MemoryError`, or the machine freezes reading a big file

You loaded the whole file into memory. This is exactly what station P5 fixes: read it with a generator, one row at a time, and never hold the whole file.

### pytest says `no tests ran`

pytest only collects files named `test_*.py` and functions named `test_*`. Check both, and run from the repository root.

---

## Snowflake

### `Object does not exist, or operation cannot be performed`

Nine times out of ten this is context, not permissions. Set all four:

```sql
USE ROLE STUDENT_ROLE;
USE WAREHOUSE STUDENT_WH;
USE DATABASE DOTSET_DB;
USE SCHEMA YOUR_SCHEMA;
```

Then check the name really exists: `SHOW TABLES LIKE 'RAW_MCA%';`

### `Insufficient privileges to operate on schema`

You are trying to write outside your own schema, or the role is wrong. Run `SELECT CURRENT_ROLE();`. If you genuinely need access to a shared object, ask in Discord rather than trying other roles.

### The query runs forever

Check the warehouse is not suspended, and check you did not write `SELECT *` against 31 lakh rows. Add `LIMIT 100` while exploring. Cancel a runaway query from the Query History page.

### `COPY INTO` loaded 0 rows

In order of likelihood:

1. The stage path is wrong. `LIST @your_stage;` and read the exact file names.
2. The file format skips the wrong number of header lines.
3. The files were already loaded once, and Snowflake is skipping them by load metadata. `COPY INTO ... FORCE = TRUE` reloads, but understand *why* before you use it, and never use `FORCE` to paper over a duplicate problem.

### `COPY INTO` loaded fewer rows than the file has

That is a real finding, not necessarily a bug. Reconcile it: `ON_ERROR` may be skipping bad rows, the file may have blank trailing lines, or a quoted field may contain a newline. Use the `VALIDATE` function or `ON_ERROR = 'CONTINUE'` plus the copy history to see which rows were rejected, then write the explanation. A difference you cannot explain fails the milestone; a difference you can explain passes it.

### `Numeric value 'xx' is not recognized`

You are casting text to a number and one row is not a number. This is the reason bronze columns are VARCHAR. Cast in staging, using `TRY_TO_NUMBER` and `TRY_TO_DATE`, which return NULL instead of failing the whole statement.

### `PUT` does not work in the web UI

`PUT` is a client-side command. It runs from SnowSQL, the Python connector, or VS Code with the Snowflake extension, not from a browser worksheet.

### I dropped something I should not have

Say so immediately in Discord. Snowflake has Time Travel:

```sql
UNDROP TABLE my_table;
```

Speed matters, and hiding it is worse than the drop.

---

## dbt

### `Could not find profile named 'x'`

`profiles.yml` is missing or in the wrong place. It belongs in `~/.dbt/profiles.yml`, and the profile name must match the `profile:` value in `dbt_project.yml`. **Never commit `profiles.yml`.**

### `Database Error ... Object does not exist` on a source

Check `sources.yml` names the database and schema exactly as Snowflake has them, and that you referenced it with `{{ source('name', 'table') }}` rather than a hardcoded name.

### `Compilation Error: dbt found two models with the same name`

Model file names must be unique across the whole project, not just per folder. Rename one.

### `dbt run` succeeds but the table is empty

The model compiled to a `SELECT` that returns nothing. Run the compiled SQL directly: `target/compiled/...` holds the exact statement dbt executed. Nine times out of ten a `WHERE` clause is filtering on a column that is NULL in bronze.

### A dbt test fails and I do not know which rows

```bash
dbt test --store-failures
```

Then query the failures table dbt created. Reading the failing rows is faster than guessing.

---

## Great Expectations and Airflow

### The expectation suite passes locally but fails in the pipeline

The pipeline is pointing at a different schema. Check the environment variables the run used, then compare row counts in both schemas.

### An Airflow task is stuck in `queued`

No worker slot is free, or the DAG is paused. Unpause the DAG, check the scheduler is running, and check whether an earlier run is still holding the slot.

### An Airflow task fails but the log is empty

Look at the *task instance* log, not the DAG log, and check the correct try number. If the log genuinely does not exist, the task never started: that is a scheduler or dependency problem, not a code problem.

### My DAG does not appear in the UI

A Python import error in the DAG file. Airflow shows nothing rather than a broken DAG. Run `python your_dag.py` locally; an import error will print.

---

## When the answer is not here

Post in Discord using the four-part format at the top of this file. If the problem is in the shared zone, tag that week's platform rotation and the review lead, because your local fix may be someone else's blocker.

If a problem happens to three or more people, it stops being a personal problem and becomes a documentation bug. Say so, and it gets added to this file.
