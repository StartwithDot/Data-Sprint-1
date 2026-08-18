# Team Roles

This document explains who does what across the cohort each week. It is a reference for both students and the program lead.

There are four positions in any given week. Three of them rotate, so everyone passes through them.

## Core admins

Core admins are the program instructors, and this role does not rotate. They have full write access to this repository, and they also hold a separate private repository with the answer keys.

They review all pull requests touching `platform/` and `delivery/`, run the end of week review calls, and spot check individual work.

## Weekly review lead (rotates, one student)

Each week one student becomes the review lead.

That student gets temporary write access to this repository for that week only. Their job is the first pass review of pull requests coming from individual practice folders. They work from a limited answer sheet that covers only that week, handed to them privately by a core admin before the week starts. They never receive the full project answer key.

Being review lead is a learning position, not an authority position. Reading other people's code and having to explain what is wrong with it teaches more than writing your own code does.

At the end of the week the access is removed and the next student takes over.

Note for admins: hand over the week's limited answer sheet before the week begins, and remove the previous lead's access at the same time.

## Weekly platform rotation group (rotates, 2 to 4 students)

Each week a small group works in the `platform` and `delivery` folders instead of their own practice folders. Their job is to build the real shared version of whatever the cohort just practiced.

The program lead picks this group. Everyone serves at least once during the project, and every turn is recorded in `docs/platform-rotation-log.md` with the component built and the pull request link. That log becomes proof of your contribution to a real shared pipeline, so keep it filled in.

If you are on this rotation, read `docs/platform-and-cicd-guide.md` before you start.

## Everyone else that week

If you are not the review lead and not on the platform group, you work in your own practice folder on that week's problem statement. Push to your fork, open pull requests, and review at least one teammate's pull request if you have time. Nobody is idle and nobody is waiting for a turn.

## We do not have fixed specialists

There is no "SQL person" and no "Python person" in this cohort. Every student is expected to touch every part of the stack, and the individual practice folders exist exactly so that everyone gets that practice.

The weekly rotation only decides who builds the shared platform that week. It never decides who is allowed to learn what.

## Merge policy

All merges into `main` use a normal merge commit or a rebase merge. We never squash.

Squashing would compress many commits into one and attribute the result to whoever merged it. That would erase individual authorship and take away the GitHub contribution history students are here to build.

## Discord notifications

You do not need to announce your work in chat. A GitHub webhook posts to the Discord channel automatically when a pull request is opened and when a merge happens.

Note for admins: to set this up, go to Repository Settings, then Webhooks, then Add webhook. Paste the Discord channel webhook URL with `/github` added at the end, set the content type to `application/json`, and choose either "Send me everything" or just the pull request and push events. Full steps are in the admin repository, in `guide/infrastructure-setup.md`.
