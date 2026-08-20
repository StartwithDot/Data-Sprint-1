# Tools Setup

**Do this before when week 1 opens, with a terminal open. Budget two hours.**

Everything here is free. If any step asks for a credit card, stop and ask in Discord before entering one.

Work through the sections in order. Each one ends with a **check it worked** command. Do not move on until that command gives the expected output.

---

## What you are installing and why

| Tool | What it is | Why this sprint needs it |
|---|---|---|
| Git | Version control. Tracks every change to every file. | Every task ends in a commit. This is also the record employers see. |
| A GitHub account | Where the shared repository lives | Pull requests, reviews, and your contribution graph |
| Python 3.11 or newer | Programming language | Three of the four data sources cannot be loaded without code |
| VS Code | Code editor | SQL, Python, and Markdown in one place, with a terminal built in |
| Snowflake | Cloud data warehouse | The platform lives here. All SQL runs here. |
| DBeaver *(optional)* | Desktop SQL client | Useful if you prefer a desktop tool to the Snowflake web UI |
| dbt Core | Transformation tool | Weeks 8 onward. Installed when you get there, listed here so you know it is coming. |

---

## 1. Git

### macOS

```bash
git --version
```

If that prints a version, you already have it. If it prints nothing or offers to install developer tools, accept, or install with Homebrew:

```bash
brew install git
```

### Windows

Download Git for Windows from `git-scm.com/download/win` and run the installer. Accept the defaults, except: when it asks about the default editor, pick VS Code if you have it, otherwise leave Vim. When it asks about the default branch name, choose **main**.

Use **Git Bash** (installed with it) as your terminal for the rest of this sprint. The commands in our docs are written for it.

### Linux

```bash
sudo apt update && sudo apt install git    # Debian / Ubuntu
sudo dnf install git                       # Fedora
```

### Configure it, once

Your commits only count on your GitHub contribution graph if the email in your commits matches an email on your GitHub account.

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
git config --global init.defaultBranch main
git config --global pull.rebase false
```

**Check it worked**

```bash
git config --global --list
```

You should see your name, your email, `init.defaultbranch=main`.

---

## 2. GitHub account

1. Create an account at `github.com` if you do not have one.
2. Settings → Emails: confirm the email you just put in Git config is listed and verified.
3. Settings → Profile: put your real name. This repository becomes something you show people.

### Authentication for pushing

GitHub does not accept your account password from the command line. Pick one:

**Option A, HTTPS with a personal access token (simplest).**
Settings → Developer settings → Personal access tokens → Tokens (classic) → Generate new token. Tick the `repo` scope. Copy the token somewhere safe; GitHub shows it once. When Git asks for a password, paste the token.

**Option B, SSH key (nicer long term).**

```bash
ssh-keygen -t ed25519 -C "your.email@example.com"
cat ~/.ssh/id_ed25519.pub
```

Copy the whole output, then GitHub → Settings → SSH and GPG keys → New SSH key → paste.

**Check it worked**

```bash
ssh -T git@github.com     # Option B: should greet you by username
```

For Option A you will find out at your first `git push`.

---

## 3. Python

You need Python **3.11 or newer**.

```bash
python3 --version
```

If it is missing or older:

- **macOS:** `brew install python@3.12`
- **Windows:** install from `python.org/downloads`, and **tick "Add python.exe to PATH"** on the first installer screen. This one checkbox causes most Windows setup problems in week 1.
- **Linux:** `sudo apt install python3 python3-pip python3-venv`

### Create the virtual environment you will use all sprint

A virtual environment is a private copy of Python for one project, so installing a library for this sprint cannot break anything else on your machine.

```bash
cd path/to/Data-Sprint-1      # after you clone in step 6
python3 -m venv .venv
source .venv/bin/activate     # macOS / Linux
.venv\Scripts\activate        # Windows PowerShell
```

Your prompt now starts with `(.venv)`. You need to run the `activate` line again in every new terminal.

Install what week 1 to week 7 need:

```bash
pip install --upgrade pip
pip install pandas pydantic requests pdfplumber beautifulsoup4 lxml pytest python-dotenv snowflake-connector-python
```

**Check it worked**

```bash
python -c "import pandas, pydantic, requests, pdfplumber, bs4, snowflake.connector; print('all imports fine')"
```

`.venv/` is already in `.gitignore`. Never commit it.

---

## 4. VS Code

Install from `code.visualstudio.com`, then add these extensions (Extensions panel, search by name):

| Extension | Why |
|---|---|
| Python (Microsoft) | Running and debugging Python |
| Jupyter (Microsoft) | Only if you like notebooks for exploring; committed work stays as `.py` and `.sql` |
| SQLFluff | The same SQL linter that CI runs, so you see problems before you push |
| Markdown All in One | The notes and answers you write are all Markdown |
| GitLens *(optional)* | Makes Git history readable |

Two settings worth changing now: turn on **Format on Save**, and set **Files: Insert Final Newline**. Both prevent noisy diffs in review.

---

## 5. Snowflake

Snowflake is the cloud data warehouse where all the data lives and all the SQL runs.

The program lead gives you: an **account URL**, a **username**, a **first-time password**, a **role** (usually `STUDENT_ROLE`), a **warehouse** (usually `STUDENT_WH`), and a **database**.

1. Open the account URL in a browser and sign in.
2. Change your password when prompted.
3. Open a new worksheet and run:

```sql
SELECT CURRENT_USER(), CURRENT_ROLE(), CURRENT_WAREHOUSE(), CURRENT_DATABASE();
```

**Check it worked:** four values come back and none of them are NULL. If the warehouse is NULL, run `USE WAREHOUSE STUDENT_WH;` and try again.

### Rules that keep the shared account alive

- **Suspend when done.** The warehouse auto-suspends, but do not leave a giant query running when you close your laptop.
- **`LIMIT` while exploring.** The registry has roughly 31 lakh rows. `SELECT *` with no limit is slow and burns shared credits.
- **Work in your own schema** when a task does not say otherwise. Do not drop or overwrite anything you did not create.
- **Never put your password in a file.** Not in SQL, not in Python, not in a notes file. Credentials go in environment variables. Station P11 teaches this properly.

### Environment variables for Python later

Create a file called `.env` in the repo root, and confirm `.env` is in `.gitignore` before you save anything in it:

```
SNOWFLAKE_ACCOUNT=your_account_identifier
SNOWFLAKE_USER=your_user
SNOWFLAKE_PASSWORD=your_password
SNOWFLAKE_ROLE=STUDENT_ROLE
SNOWFLAKE_WAREHOUSE=STUDENT_WH
SNOWFLAKE_DATABASE=your_database
```

---

## 6. Fork and clone the repository

Full explanation of every command is in `03-student-guide.md`, section 1. The short version:

```bash
# 1. Fork on GitHub: open the class repository, click Fork, top right.
# 2. Clone your fork:
git clone https://github.com/YOUR_USERNAME/Data-Sprint-1.git
cd Data-Sprint-1

# 3. Add the class repository as a second remote called upstream:
git remote add upstream https://github.com/StartwithDot/Data-Sprint-1.git
git remote -v
```

**Check it worked:** `git remote -v` shows `origin` pointing at your fork and `upstream` pointing at the class repository.

---

## 7. Data folders on your machine

Downloaded source files never go into Git. They live in a local folder that `.gitignore` already excludes:

```bash
mkdir -p data/raw/mca data/raw/ibbi data/raw/cdm data/raw/rbi
```

**Check it worked**

```bash
git status
```

`data/` must not appear in the output. If it does, stop and ask in Discord before committing anything.

---

## 8. Tools that arrive later in the sprint

Do not install these now. They are listed so nothing surprises you, and each is installed in the week that needs it.

| Tool | Arrives | Install then with |
|---|---|---|
| dbt Core with the Snowflake adapter | week 8, station D5 | `pip install dbt-snowflake` |
| Great Expectations | week 9, station D8 | `pip install great_expectations` |
| Apache Airflow | week 10, station D9 | Provided environment; the program lead shares the URL |
| Metabase | week 10, station B6 | Hosted by the program; you get a login |

---

## 9. Setup checklist

- [ ] `git config --global --list` shows your name and your GitHub-verified email
- [ ] GitHub account exists, and pushing works with a token or an SSH key
- [ ] `python3 --version` is 3.11 or newer
- [ ] `.venv` created and activated, and the import check passes
- [ ] VS Code installed with the Python and SQLFluff extensions
- [ ] Snowflake login works and `SELECT CURRENT_USER()` returns a value
- [ ] Repository forked, cloned, and `upstream` remote added
- [ ] `data/raw/...` folders created locally and invisible to `git status`
- [ ] `.env` created, and `.env` confirmed present in `.gitignore`

If something on this list will not work after two honest attempts, post in Discord with the exact command you ran and the exact error. Setup problems are the single most common reason a student loses week 1, and they are the fastest thing for someone else to fix.

---

Next: `03-student-guide.md`.
