# Platform and CI/CD Guide

This guide is for students picked for the weekly platform rotation. It explains how working in the shared `platform` and `delivery` folders is different from working in your own practice folder.

If you are not on the rotation this week, you do not need this guide yet. You will need it later, because everyone gets a turn.

## 1. What you are doing this week

The whole cohort has just practiced a set of skills in their own folders. Your job this week is to build the one real shared version of that work in the `platform` folder, and the shared outputs in the `delivery` folder.

Think of it like this. Everyone practices in a rehearsal room. Your week is the one on stage.

## 2. Why the rules are stricter here

A mistake in your own practice folder affects only your record, and that is fine, that is what practice is for.

A mistake in `platform` breaks the shared pipeline for all 15 to 30 people, and the shared pipeline is the thing we hand to the client at the end. So the code here gets reviewed by a core admin, not by the weekly student review lead, and it must pass automated checks first.

Being reviewed strictly is not a judgement on you. It is how real teams protect shared code.

## 3. The automated checks

CI stands for continuous integration. In practice it means: every time you open a pull request, GitHub automatically runs some checks on your code and shows a green tick or a red X. Your pull request cannot be merged until the ticks are green.

Two checks run on platform work.

**The linter.** A linter is a tool that reads your code and flags formatting and style problems, for example inconsistent SQL keyword casing or unused Python imports. We run `sqlfluff` for SQL and a Python style check. It catches the small stuff automatically so human reviewers can spend their time on the logic instead.

**The dbt check.** This one parses your dbt code to confirm it is structurally valid, for example that every model you reference actually exists. It is a parse only. It does not run your models against Snowflake, because running the full pipeline on every pull request would be slow and would burn warehouse credits. The full build runs after your code is merged into `main`.

## 4. What to do when a check fails

A red X is normal. It happens to everyone, including experienced engineers. Work through it in this order.

1. Click "Details" next to the failed check.
2. Read the log output from the bottom up. The real error is usually near the end.
3. Find the file name and line number in the message. The tool almost always tells you exactly where the problem is.
4. Fix it in your branch, commit, and push again.
5. The checks rerun by themselves on the same pull request. Wait for the result.

If you have read the log and still cannot tell what it wants, paste the last 20 lines into Discord and ask. Do not spend an hour stuck on a linting rule.

## 5. Where the checks apply

These checks only run when your pull request changes files inside `platform/` or `delivery/`. They never run on `students/` folders, so your practice work does not have to pass them.

## 6. Ground rules for platform code

Keep these in mind while you build, because they are the things reviewers will send back.

* **Respect the layers.** No business logic in bronze. Bronze is a faithful copy of what the source gave us. Cleaning belongs in silver, business shaping belongs in gold.
* **Make it rerunnable.** A script or model must produce the same result when run twice. No `DROP TABLE` as a way of cleaning up, no logic that duplicates rows on a second run. The word for this is idempotent, and it is one of the terms you will be asked to define at review time.
* **Match the agreed design.** Column and table names must follow the star schema the group signed off on. If you think a name is wrong, raise it in Discord and change the design deliberately, do not change it quietly in your pull request.
* **Never commit secrets or data files.** Credentials come from environment variables or GitHub secrets. Downloaded source files stay out of Git.
* **Write down what you did.** Update the relevant note or README in the same pull request, and add your row to `docs/platform-rotation-log.md`. The next rotation group depends on it.

## 7. If two of you touch the same file

Talk in Discord before you both push. Two pull requests editing the same dbt model will conflict, and a core admin will ask you to sort it out anyway. Deciding early takes two minutes. Deciding late costs a day.

---

## For admins: workflow files

The checks above come from three GitHub Actions workflow files in `.github/workflows/`.

* `lint.yml` runs the SQL and Python linters. Triggered on pull requests that touch `platform/`.
* `dbt-check.yml` runs the lightweight dbt parse. Triggered on pull requests that touch `platform/`.
* `dbt-build.yml` runs the full dbt build. Triggered when code touching `platform/` is merged into `main`.

## For admins: branch protection

Configure this in the repository settings before week 1.

1. Settings, then Branches.
2. Add a branch protection rule for `main`.
3. Enable "Require a pull request before merging".
4. Enable "Require approvals", set to at least 1.
5. Enable "Require status checks to pass before merging".
6. Add the lint and dbt check job names to the required checks list.

## For admins: GitHub secrets

The full dbt build needs Snowflake credentials, which must never sit in the repository. Add them as repository secrets.

1. Settings, then Secrets and variables, then Actions.
2. Click "New repository secret".
3. Add these, with the values for the restricted CI user:
   - `DBT_SNOWFLAKE_ACCOUNT`
   - `DBT_SNOWFLAKE_USER`
   - `DBT_SNOWFLAKE_PASSWORD`
   - `DBT_SNOWFLAKE_ROLE`
   - `DBT_SNOWFLAKE_WAREHOUSE`
   - `DBT_SNOWFLAKE_DATABASE`
   - `DBT_SNOWFLAKE_SCHEMA`
