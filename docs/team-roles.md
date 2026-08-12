# Team Roles

This document explains who does what across the entire cohort. It is a reference for both students and the program lead.

## Core Admins

Core admins are permanent roles held by the program instructors. They have full write access to this main repository. They also have access to the separate private repository that contains the answer key. Core admins are responsible for leading final review calls and performing quality spot checks on all work.

## Weekly Rotating Review Lead

Each week, one student is chosen to be the review lead. This student is given temporary write access to the main repository for that week only. 
Their job is to do the first pass review of all pull requests coming from the individual student practice folders. They will use a limited answer sheet provided by a core admin just for that specific week. They do not get the full project answer key. When the week ends, their write access is removed and a new student takes over.

## Weekly Platform Rotation Group

Each week, a group of 2 to 4 students is assigned to work in the `platform` and `delivery` folders. 
Their job is to build the real, shared version of the concept the whole cohort just practiced. The program lead decides who is in this group each week. 
We keep a simple list in `platform-rotation-log.md` to record who worked on what part of the platform and when. By the end of the project, everyone will have at least one real platform contribution logged there.

## All Other Students

If you are not the review lead or on the platform team this week, you are focused entirely on your own individual practice folder. You will contribute by pushing work to your fork and opening pull requests. Everyone will be picked for the rotating roles at some point during the life of the project.

## No Fixed Specialists

This project does not use fixed specialist teams. Every student is expected to learn every part of the data stack. You will do this through the work in your individual folder. The weekly rotation only decides who is building the shared platform that week. It does not limit who is allowed to learn what.

## Merge Policy

When it is time to merge a pull request into the `main` branch, we follow a strict rule. All merges must use a regular merge commit or a rebase merge. We never use squash and merge. This ensures that the original student authorship is preserved and their GitHub contribution graph accurately reflects their real work.

## Discord Notifications

You do not need to manually announce your work in chat. A GitHub webhook is connected directly to our Discord channel. It posts an automatic message every time a pull request is opened and every time a merge happens.
