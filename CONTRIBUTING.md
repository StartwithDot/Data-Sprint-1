# Contributing to Data Sprint 1

These are the repo rules, kept short on purpose. The full daily workflow with commands is in `docs/student-guide.md`.

## The rules

1. **One task, one commit.** Each commit should contain the files for a single task from your weekly problem statement, nothing else.
2. **Stay in your own folder.** Unless you are on this week's platform rotation, only commit files inside your own `students/DEx/` folder.
3. **Everything goes through a pull request.** Nobody pushes straight to `main`. That branch is protected, so a direct push will be rejected.
4. **Name your task IDs.** Put the task ID in the commit message and in the pull request title, for example `S1.2 create raw MCA table`. It makes review much faster.
5. **Never use squash and merge.** Use a normal merge commit or a rebase merge. Squashing would collapse everyone's commits into one and wipe out individual authorship, which affects your GitHub contribution graph.
6. **Do not commit data files or secrets.** No downloaded CSV, ZIP, PDF, or Excel files. No passwords, no Snowflake credentials, no `profiles.yml`. Check `.gitignore` before you add files, and if you are unsure, ask in Discord first.
7. **Answer the "why" questions in writing.** Several tasks ask for a short explanation in a notes file. Those are graded like code. Write them in your own words.

## If your pull request gets comments

Fix the code in the same branch, commit again, and push again. The existing pull request updates automatically. Do not open a second one for the same task.

## If a check fails

Automated checks only run on the `platform/` and `delivery/` folders. If you are on the platform rotation and see a red X, read `docs/platform-and-cicd-guide.md`, section 4. It explains how to read the failure and fix it.
