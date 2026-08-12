# Student Guide

Welcome to Data Sprint 1. Read this guide any time you are unsure what to do next. It is your daily reference for how to work in this project.

## 1. Initial Setup: Forking and Cloning

You only need to do this step once at the very beginning of the project.

1. **Fork the Repository:** Go to the main repository page on GitHub. Click the "Fork" button in the top right corner. This creates your own copy of the project on your GitHub account.
2. **Clone to Your Computer:** Open your terminal and run this command, replacing `YOUR_USERNAME` with your actual GitHub username:
   `git clone https://github.com/YOUR_USERNAME/Data-Sprint-1.git`
3. **Set Up Your Git Config:** To make sure your work shows up as green squares on your GitHub profile graph, you must tell Git who you are. Run these two commands inside your cloned folder, using the exact email associated with your GitHub account:
   `git config user.name "Your Name"`
   `git config user.email "your.email@example.com"`
4. **Connect to the Upstream Repository:** You need a way to pull new changes from the main class repository into your fork. Run this command once:
   `git remote add upstream https://github.com/StartwithDot/Data-Sprint-1.git`

## 2. Finding Your Folder

You have been assigned a specific DE number by the program lead. 
Look inside the `students` folder. Find the folder that matches your number, for example `students/DE12`.
All of your individual practice work will happen inside this specific folder. Do not put your personal practice files anywhere else.

## 3. Finding Your Weekly Tasks

Tasks are grouped into a 10-week curriculum based on difficulty. Open your assigned folder and go to the current week (for example, `week1`). Inside, you will find a `problem_statement.md` file. That file contains the exact tasks you need to complete for that week. You can also view the full master task list in the `docs/task-list.md` document, but your weekly problem statement is what you should focus on.

## 4. The Daily Workflow

Every time you sit down to work, follow these exact steps:

1. **Pull the Latest Changes:** Always start by getting the newest updates from the main repository into your local clone. Run these commands:
   `git checkout main`
   `git pull upstream main`
2. **Do the Work:** Open your assigned student folder. Go into the correct week folder for the current assignment. Write your code or documentation there.
3. **Commit Your Work:** Save your changes in Git with a clear message explaining what you did.
4. **Push to Your Fork:** Send your saved commit up to your forked repository on GitHub.
5. **Open a Pull Request:** Go to GitHub and open a pull request from your fork into the main repository. 

## 5. One Task Equals One File Equals One Commit

This is a strict rule. Do not build one massive file over the whole week. 
When you finish a single task from the task list, save it in its own file. Make a single commit for just that one task. Then push it. This keeps your work organized and makes it easy for others to review.

## 6. Platform Rotation

Each week, a small group of students is chosen to work in the `platform` and `delivery` folders instead of their individual folders. 
If you are picked for the platform rotation team this week, your job is to build the real, shared version of the project. This work has stricter rules and automated checks. If you are on this team, you must read the `platform-and-cicd-guide.md` document before you start.

## 7. Getting Stuck

You will get stuck. That is normal.
When it happens, go to our Discord channel and ask for help. Ask for a nudge in the right direction, not for the final answer. Copying a final answer defeats the purpose of this training program. We are here to help you figure it out.

## 8. Your GitHub Contribution Graph

You might be wondering when your work counts towards the green squares on your GitHub profile.
Your commits count towards the graph only when they are merged into the main repository's default branch. Because you are working in a fork, simply pushing to your own fork will not turn your squares green immediately. As long as you follow the setup steps in section 1 and open a pull request, your work will be credited on your profile as soon as the core admin merges your pull request.

## 9. Our Data Approach: Kimball and Medallion

We are building a data platform using a Kimball star schema and a Medallion pipeline. The pipeline moves data through bronze, silver, and gold stages.

It is important to understand why the repository is split into two zones. 
The work you do in your individual folder is for practice and repetition. It allows you to learn the concepts safely. 
The work done in the `platform` folder is the single, real version of the pipeline. It is built collaboratively by the rotating team each week. 
This split exists so everyone gets to practice every skill individually, while still contributing to one shared, professional grade final product. Both areas matter, but they serve different purposes.
