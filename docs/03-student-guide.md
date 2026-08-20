# Student Guide

Welcome to Data Sprint 1. Read this guide any time you are unsure what to do next. It is your reference for how to work in this project.

If you have never used Git or GitHub before, do not worry. Follow the steps in order and ask in Discord the moment a command does not do what this guide says it should.

## 1. One time setup: fork, clone, configure

You only do this once, at the very start of the project.

**Step 1. Fork the repository.**
Open the main repository page on GitHub. Click the "Fork" button in the top right. A fork is your own copy of the project under your GitHub account. You can change your copy freely without affecting anyone else.

**Step 2. Clone your fork to your computer.**
Cloning means downloading your copy so you can work on it locally. Open your terminal and run this, replacing `YOUR_USERNAME` with your GitHub username:

```
git clone https://github.com/YOUR_USERNAME/Data-Sprint-1.git
cd Data-Sprint-1
```

**Step 3. Tell Git who you are.**
Your commits only count on your GitHub contribution graph if the email in your commits matches the email on your GitHub account. Run these inside the cloned folder:

```
git config user.name "Your Name"
git config user.email "your.email@example.com"
```

Use the exact email your GitHub account uses. If you are not sure, check GitHub Settings, then Emails.

**Step 4. Connect to the main class repository.**
Your fork will fall behind as the class repository gets new work. We add a second remote called `upstream` so you can pull those updates later. A remote is just a nickname for a repository address. Run this once:

```
git remote add upstream https://github.com/StartwithDot/Data-Sprint-1.git
```

Check that both remotes exist:

```
git remote -v
```

You should see `origin` pointing at your fork and `upstream` pointing at the class repository.

## 2. Finding your folder

The program lead gives you a DE number, for example DE12.

Open the `students` folder and find the folder with your number, for example `students/DE12`. Inside it you will find one folder per week.

All of your individual practice work goes inside your own folder. Do not put practice files anywhere else in the repository, because that makes review harder for everyone.

## 3. Finding your weekly tasks

The project runs for 10 weeks and the tasks get harder each week.

Open your folder, then the current week folder, for example `students/DE12/week1`. Inside you will find a file named `problem_statement.md`. That file has the exact tasks for that week. Each task has an ID like `S1.2` or `P1.3`, tells you what to produce, and tells you the exact file path to commit it to.

The full list of every task in the project is in `docs/05-task-list.md` if you want to see what is coming. Your weekly `problem_statement.md` is the one you actually work from.

## 4. The working loop

Every time you sit down to work, follow these steps.

**Step 1. Get the newest class changes.**

```
git checkout main
git pull upstream main
```

**Step 2. Do the work.**
Open your own student folder, go into the current week folder, and write your code or notes there.

**Step 3. Commit your work.**
A commit is a saved checkpoint with a message explaining what you did.

```
git add students/DE12/week1/sql/s1/01_create_database.sql
git commit -m "S1.1 create bronze silver gold schemas"
```

Write commit messages that name the task, like the example above. "update" and "fix" tell a reviewer nothing.

**Step 4. Push to your fork.**

```
git push origin main
```

**Step 5. Open a pull request.**
A pull request, often called a PR, is a request to add your work into the class repository. Go to your fork on GitHub, click "Contribute", then "Open pull request", and write one or two lines saying which task IDs the PR covers. A reviewer will read it and either merge it or leave comments asking for changes.

If a reviewer leaves comments, fix the code in the same folder, commit again, and push again. The pull request updates by itself. You do not open a new one.

## 5. One task, one file, one commit

This is a strict rule.

Do not build one giant file across the whole week. When you finish a single task, put it in its own file, make one commit for just that task, and push it.

Small commits are easier to review, easier to fix, and they show a clear record of your work. Your weekly `problem_statement.md` already tells you which file path each task belongs in, so follow those paths exactly.

## 6. Platform rotation

Each week the program lead picks a small group of students to work in the `platform` and `delivery` folders instead of their own practice folders.

If you are picked, your job that week is to build the real shared version of the thing the whole cohort just practiced. This work has stricter rules and automated checks. Before you start, read `docs/07-platform-and-cicd-guide.md`.

Everyone gets a turn during the project. The turns are recorded in `docs/platform-rotation-log.md`.

## 7. When you get stuck

You will get stuck. Everyone does. It is part of the work, not a sign that you are behind.

When it happens, post in the Discord channel. Say what you were trying to do, what you tried, and what happened instead, and paste the error message. Ask for a hint that points you in the right direction, not for the finished answer. Copying a finished answer skips the learning, which is the only thing this program is for.

## 8. Your GitHub contribution graph

Your commits turn the squares green on your GitHub profile only after they are merged into the class repository's default branch.

Pushing to your own fork does not do it on its own. So do the setup in section 1 correctly, especially the email, and always finish your work with a pull request. Once a core admin merges it, the contribution shows up on your profile.

## 9. Why the repository has two zones

We are building a data platform using a Medallion pipeline (bronze, silver, gold) and a Kimball star schema. Both are explained in plain language in `docs/01-project-brief.md`, section 4.

The repository is split into two zones on purpose.

Your individual folder is for practice and repetition. You try every skill yourself, and a mistake there costs nothing.

The `platform` folder is the one real version of the pipeline. It is built by the rotating team each week, and everyone depends on it working.

This split means every person gets to practice every skill, while the cohort still ships one shared product that is good enough to show an employer. Both zones matter. They just have different jobs.
