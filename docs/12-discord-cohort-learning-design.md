# Discord Cohort and Learning Design Review

**Prepared for:** program leads and Team Leads (not students).
**Date:** 8 September 2026.
**Scope:** the DOTSET Discord server architecture as described by the program lead, the sprint's learning design (`docs/00-START-HERE.md` through `docs/11-tools-and-technology.md`), and how the two systems connect. This document assumes the reader has `CURRICULUM-AUDIT.md` nearby; it builds on it rather than repeating it.
**Ground rule honored:** still read-only. This file and `13-tool-cost-control-runbook.md` are the only additions to the repository. No existing file was modified.

---

## 0. Executive summary

**Is the Discord + cohort arrangement on the right path? Yes.** The architecture — XP only from three earning channels, a 1-3-7 spaced-repetition loop, daily streaks, automated GitHub tracking, a freeze mechanic with a recovery room instead of expulsion, read-only information channels, and weekly mission drops — matches what learning-science research actually supports better than most commercial bootcamp designs. The pedagogy and the accountability system reinforce each other instead of fighting.

It is **calibrated wrong in five places**, all fixable with rule changes and channel setup, none requiring paid tools:

| # | Problem | Section |
|---|---|---|
| 1 | The XP ladder is arithmetically impossible at the top: an honest, maximal 10-week run earns roughly **1,300-1,400 XP**, but `@L4` needs 3,500 and `@L5` (labeled "Track completion milestone") needs 7,000 | §4 |
| 2 | The freeze mechanic is loss aversion without a safety valve; the first freeze window closes exactly during the hardest onboarding weeks, which is where beginners churn | §5 |
| 3 | The channel topology will drown at 30 students: one `#discussion` channel, one announce-only integrations feed at 60-90 posts/day, and no surface for PR review requests or data-source status | §6 |
| 4 | The sprint **is** heavy — 105 tasks over 70 days, four tracks in parallel from week 1, eleven load-bearing tools, milestone spikes in weeks 8 and 10 — sustainable only with an explicit week 0, a default "core path", and week 8/10 relief | §7 |
| 5 | The resource strategy is repo-only: good content exists in `09-resources.md` but there is no beginner video spine for Python, nothing is pre-loaded into Discord, and students will be searching at midnight | §8 |

Plus one **correction** to the earlier audit: the Snowflake risk is smaller than assessed, because each student creates their own student-trial account (120 days, $400 credits). See §1 and `13-tool-cost-control-runbook.md`.

---

## 1. Corrections to CURRICULUM-AUDIT.md

The program lead supplied two facts that change audit finding 1. This section records the corrections; the audit file itself is intentionally untouched (read-only rule).

| Audit finding | Was | Now | Residual risk | Handled by |
|---|---|---|---|---|
| Finding 1 (P0): "Snowflake has no permanent free tier; a 30-day trial cannot cover a 70-day sprint; one shared account concentrates the clock and the credit burn" | P0 — will break the sprint around weeks 4-5 | **Downgraded to P1.** Each student creates their own account via the student signup link (`https://signup.snowflake.com/?trial=student`): **120 days** of access and **$400 credits**, no credit card. 120 days covers a 70-day sprint with ~7 weeks of margin. Per-student accounts also eliminate the shared-warehouse queuing and single-clock concerns | Brand-new accounts have **no cost-saving configuration** — Snowflake's defaults will not stop a student from burning the whole budget in a bad week. Every student needs the day-0 setup script | `13-tool-cost-control-runbook.md` (new) |

Everything else in the audit stands: the broken CI workflows, the `.gitignore` contradictions, the unowned Airflow/Metabase hosting, the 403/404 government data sources, the unpinned versions, the review-bandwidth math, and the week 8/10 overload findings are all unchanged by per-student Snowflake accounts.

**Verification note:** the student signup page is JavaScript-rendered and returns 404 to scripted fetches, so the 120-day/$400 terms could not be independently re-verified by tooling. They come from the program lead. Snowflake's standard non-student trial is 30 days / $400; the student variant's distinguishing feature is the longer clock. Confirm the banner text on the day accounts are created.

---

## 2. Is the Discord + cohort arrangement on the right path?

### 2.1 What the design gets right (keep all of this)

| Mechanism | Why it works | Evidence it is wired correctly |
|---|---|---|
| XP only from three channels (recap 4, integrations 3, streak 5), **0 XP everywhere else** | Aligns rewards with learning behaviors and kills the message-spam incentive that ruins most Discord learning servers | Channel table: 0 XP on `#public-chat`, `#discussion`, `#gmcm`, and every community channel |
| The 1-3-7 loop | A real expanding spaced-retrieval schedule (see §3.2) — not a sticker version of one | Day 1 study, Day 3 handwritten recap upload, Day 7 live recall in voice |
| Daily streak posts | Habit formation needs a daily cue-routine-reward loop in a stable context | `#guild-streak`, 5 XP |
| `#frozen-chamber` | Accountability without expulsion — there is a documented way back, which most programs never build | Freeze rules in the lifecycle description |
| Read-only information channels | Single source of truth; announcements cannot be buried by chat | `#announcements`, `#rules`, `#roles`, `#youtube-videos` |
| Automated GitHub feed | Proof-of-work from the environment, not screenshots or trust | `#integrations`, announce-only, webhook-driven |
| Monday mission drops | Cohort pacing with shared deadlines creates a goal gradient and syncs the 1-3-7 loop to the week | Weekly sprint cadence |
| Day-7 recall in voice calls | Retrieval practice in front of peers plus the teaching effect — the strongest single consolidation event available | "Live review of concepts during cohort voice calls" |
| Level roles | Visible progression; the progress principle (Amabile) is the most reliable motivator in knowledge work | L1-L5 ladder |

### 2.2 The six design risks (detailed in later sections)

1. **The XP ladder's top is unreachable in one sprint** (§4) — and `@L5` is labeled "Track completion milestone", which promises something the arithmetic cannot deliver.
2. **The freeze mechanic's first enforcement window closes during onboarding** (§5) — missing weeks 1-2 is the most likely beginner failure mode, and freezing a beginner during week 3 is where cohorts lose people permanently.
3. **One `#discussion` channel for 30 students is a scroll-wall** (§6) — questions get asked five times, answers get lost, and helpers burn out.
4. **Peer help earns 0 XP** (§4.4) — the single most valuable learning behavior in the server (explaining to others) is the one the reward system ignores.
5. **The integrations feed will bury itself** (§6) — 30 students × 2-3 webhook events/day = 60-90 posts/day in an announce-only channel nobody can search usefully by week 3.
6. **The XP bot is the accountability backbone but has no owner or budget** (§6.8) — free options exist, but the choice must be made before week 1, because if XP silently stops being awarded, the entire status system loses credibility mid-sprint.

---

## 3. The learning science underneath

### 3.1 Neuroplasticity, stated honestly

The program asked for "the best possible learning method through cognitive psychology, implementing neuroplasticity." Here is the honest version, because the dishonest version (brain-training apps, "hack your brain" content) wastes exactly the time this sprint does not have.

Adult learning runs on five levers, all of which the sprint already touches:

1. **Attention.** Plasticity in adults is attention-gated: structural change in the cortex happens for what you attend to, while distracted exposure produces little. Practically: focused blocks with one screen and no task-switching. Task-switching costs are measurable (commonly cited at 20+ minutes to fully refocus after an interruption) and every context switch during a focused block deletes part of the encoding.
2. **Retrieval, not review.** Re-reading notes feels like learning and produces almost nothing; pulling knowledge out of memory from a prompt is what strengthens the trace (the testing effect, Roediger & Karpicke 2006). The sprint's Day-3 recap and Day-7 recall are retrieval; a student who "reviews" by re-reading Day 1 notes on Day 3 has converted the exercise back into review.
3. **Spacing.** Memory consolidates between exposures, and expanding intervals (1 day → 3 days → 7 days) beat equal intervals and beat massed practice (Cepeda et al. 2006). The 1-3-7 loop is a legitimate expanding schedule.
4. **Sleep.** Consolidation of the day's encoding happens during sleep; an all-nighter before a deadline deletes most of the previous day's learning. This is the cheapest performance lever in the entire program and belongs in the rules channel.
5. **Repeated use in varied contexts.** Myelination of a circuit comes from repeated, correct use — which is why the sprint's four interleaved tracks (SQL, Python, platform, delivery) beat "finish all SQL, then all Python": the same skill resurfaces in a different context each week, which is interleaving, and interleaving produces better retention at the cost of feeling harder (Rohrer & Taylor 2007).

The one-sentence version for students: **attend fully, retrieve often, space it out, sleep on it, and expect it to feel hard — the difficulty is the signal that consolidation is happening, not a sign of failure.**

### 3.2 Element-by-element audit of the cohort's mechanics

| Cohort mechanic | Cognitive-science principle | Verdict | Tune |
|---|---|---|---|
| 1-3-7 loop (learn → recap → mastery) | Spacing effect + testing effect; 1→3→7 is a proper expanding interval set | **Keep** | Add a Day-30 touchpoint: the week-10 review should explicitly re-test week 1-3 concepts from memory |
| Day-1 handwritten notes | Encoding effort; longhand note-taking outperforms laptop note-taking for conceptual recall (Mueller & Oppenheimer 2014, with later partial replications — directionally solid, effect size modest) | **Keep** | Tell students notes are only allowed to be *prompts*, not transcripts — notes that contain everything prevent retrieval |
| Day-3 recap photo upload | Retrieval at ~48h, near the steep part of the forgetting curve | **Keep** | The recap must be written **from memory first**, then checked against Day-1 notes — otherwise it is copying, not retrieval |
| Day-7 live recall in voice | Generation effect + teaching effect; the strongest consolidation event in the week | **Keep** | Make cold-calling safe: opt-in rotation, no ranking, no leaderboard of who answered best — test anxiety impairs retrieval (Yerkes-Dodson) |
| Daily streak post | Habit formation: stable cue (same channel, same time) → routine → reward (XP + visible streak) | **Keep** | Require a two-line format ("yesterday I did / today I will") — implementation intentions, not one-word posts |
| Four interleaved tracks | Interleaving beats blocked practice for long-term retention but feels worse during learning | **Keep** | Say this out loud in week 1: "this will feel harder than one-subject-at-a-time, and that is the method working" — otherwise students conclude they are failing |
| Messy real data, week-10 failure injection | Desirable difficulties (Bjork): conditions that slow learning during acquisition and double retention | **Keep** | This is the sprint's main differentiator from tutorial-following; do not smooth it away when students complain |
| "Why" grading + say-it-out-loud defense | Elaborative interrogation + retrieval in front of others | **Keep** | Already correctly designed in `00-START-HERE.md` §8 |
| Per-week cut lists ("if you are short on time, cut in this order") | Cognitive-load management; protects intrinsic load by shedding extraneous scope | **Keep, promote** | Make the cut list the *default* path, not the emergency path (§7.4) |
| XP + level roles | Progress principle (Amabile): visible small wins are the strongest motivator in knowledge work | **Keep** | Fix the arithmetic (§4); keep XP non-material — never exchangeable for anything, to avoid the over-justification effect (extrinsic rewards that feel controlling erode intrinsic motivation; Deci & Ryan) |
| Freeze mechanic | Loss aversion (Kahneman & Tversky): strong short-term motivator with a dropout cliff at the moment of loss | **Redesign** | See §5 — keep the mechanic, soften the cliff |

### 3.3 The student-facing protocol (ready to pin in `#learning-resources`)

A one-page study protocol that operationalizes §3.1-3.2, written for students:

1. **Work in 45/15 blocks.** One task, one tab, notifications off. 45 minutes of full attention, then a real 15-minute break (walking, not scrolling). Two blocks beat a distracted four-hour session.
2. **Same time, same place, daily.** Context is a retrieval cue; a stable study context makes starting cheaper every week. This is what the streak post is actually for.
3. **Close the notebook, then write the recap.** Day-3 summaries are written from memory first, then corrected against Day-1 notes. The corrections are the learning.
4. **Sleep is a study technique.** The day's encoding consolidates overnight. Cutting sleep to finish a task trades the learning the task was supposed to produce.
5. **Explain one thing per week to someone else.** The Day-7 call is this; volunteer before being asked — the explainer consolidates more than the listener.
6. **When it feels hard, that is the method.** Interleaving, retrieval, and messy data all feel worse than tutorials and all produce more durable engineers. Struggling for 20 minutes before asking is not wasted time; it is the workout.
7. **Ask with evidence.** "It doesn't work" is not a question; "here is the command, the error, and what I tried" is. The evidence-gathering is itself debugging practice.

---

## 4. XP economy audit — the arithmetic

### 4.1 Inputs (all from the repo's own rules)

- 10 weeks = 70 days.
- **105 tasks** per student (unique task IDs counted across `docs/_week-templates/week1.md`-`week10.md`): 10, 11, 12, 13, 10, 8, 8, 11, 10, 14 per week.
- Repo rules: one commit per task, one pull request per task or per station, task ID named in commit and PR title.
- Webhook reality: a task typically produces 2-3 events in `#integrations` (push, PR opened, PR merged) at **3 XP each**.

### 4.2 The math

| Source | Calculation | Max over the sprint |
|---|---|---|
| Streak (`#guild-streak`, 5 XP/day) | 70 days × 5 | **350** (requires posting every single day, weekends included) |
| Recap (`#1-3-7-recap`, 4 XP/upload) | 10-20 uploads × 4 | **40-80** |
| Integrations (3 XP/event) | 105 tasks × 2-3 events × 3 | **630-945** |
| **Honest ceiling (maximal student, every day, every event)** | | **≈ 1,020-1,375** |
| **Typical consistent student** (5-day weeks, PR-per-station) | | **≈ 900-1,100** |
| **Student completing ~half the sprint** | | **≈ 400-500** |

### 4.3 Ladder verdict

| Role | Threshold | Reachable? | When |
|---|---|---|---|
| `@L2-Intern` | 500 XP | **Yes** | Week 5-6 for a consistent student |
| `@L3-Junior Engineer` | 1,500 XP | **No** — above the honest ceiling of ~1,375; only reachable by inflating webhook events (micro-commits), which the rules should not reward | — |
| `@L4-Software Analyst` | 3,500 XP | **No** — ~2.5× the ceiling | — |
| `@L5-Software Engineer` | 7,000 XP | **No** — ~5× the ceiling, yet labeled **"Track completion milestone"** | — |

This is the single most important calibration problem in the server: a student who does **every task, every day, for ten straight weeks** tops out below L3, while the server tells them L5 is the "track completion milestone."

### 4.4 Three fixes (pick one, before week 1)

1. **Recommended: relabel the ladder as a multi-sprint career path.** DOTSET runs Data Engineering, Cyber Security, and Full Stack tracks; XP presumably persists across sprints. Keep 500/1,500/3,500/7,000 as the long-horizon ladder, drop the "Track completion milestone" label from L5, and add a **per-sprint finish line** — e.g., a "Sprint Graduate" badge at ~1,000-1,100 XP, which is exactly what a consistent, honest 10-week run produces. The sprint then has a reachable finish line *and* the server keeps its long ladder.
2. **Rebalance per sprint:** 400 / 900 / 1,100 (L2 week 4-5, L3 week 8, L4 at graduation). Keeps everything reachable in one sprint.
3. **Raise XP weights** (e.g., 10 XP per task). *Not recommended* — it amplifies the farming vectors in §4.5.

### 4.5 Farming vectors and guardrails

| Vector | Exploit | Guardrail |
|---|---|---|
| Per-event integration XP | 20 micro-commits = 20 feed posts = 60 XP without finishing a task | Award integration XP **per merged PR** (dedupe push/PR events), or cap integration XP per day (e.g., 15/day). The repo already mandates task IDs in commit messages — the bot can award once per unique task ID, which makes the XP rules and the repo rules enforce each other |
| One-word streak posts | "gm" × 70 = 350 XP for zero learning | The two-line format from §3.2 (done / next) — leads spot-check |
| Recap photo spam | Uploading 5 photos per week | One qualifying upload per 1-3-7 cycle; extra photos welcome, no XP |
| Peer help = 0 XP | The most valuable behavior in the server is unrewarded | Do **not** add XP to help channels (it recreates the spam problem). Use non-XP recognition instead: a weekly "reviewer of the week" ping by Team Leads in `#community-updates`. Recognition preserves relatedness (the strongest retention predictor in cohort programs) without a spam incentive |

---

## 5. Freeze mechanic redesign — loss aversion without the cliff

### 5.1 What the current design gets right

- The trigger is **automatic and objective** (2 consecutive missed weeks), not a mood.
- The frozen student keeps a documented path back (`#frozen-chamber` + `@Team-Leader` tag) — recovery, not expulsion.
- Two weeks of tolerance matches the reality that one bad week is recoverable.

### 5.2 The three risks

1. **The first freeze window closes during onboarding.** A student who misses weeks 1-2 — the hardest weeks, when git friction is at its worst — gets frozen at the start of week 3, exactly when they needed momentum. This is the highest-churn moment in any cohort.
2. **Freeze is a public status.** Being visibly frozen in a small community is a shame event; loss aversion cuts both ways — it motivates briefly, then produces avoidance (silent leaving) rather than recovery.
3. **The backlog is what froze them, and the recovery path asks them to backfill it.** If the unfreeze rule is perceived as "submit everything you missed," the backlog that caused the freeze becomes the barrier to unfreezing.

### 5.3 Five rule changes (no code required)

1. **Streak shield:** each student gets one pre-declared skip per sprint, posted in advance in `#guild-streak` ("shielding this Saturday, exam"). A planned absence is not a failure; this keeps the habit honest instead of teaching students to disappear quietly.
2. **Freeze quietly, unfreeze loudly.** No public freeze announcements — DM plus `#frozen-chamber` access only. Unfreezes *are* celebrated publicly in `#community-updates` ("comeback of the week"). Loss aversion resolves into pride instead of shame.
3. **Re-entry is a checklist, not a debt.** The unfreeze rule should be: "do the missed week's **cut list** only, skip everything else, you're active." Never require 100% backfill.
4. **Manual override for weeks 1-2.** During onboarding only, a missed week triggers a warning DM from the Team Lead instead of a freeze. Freezes start being automatic from week 3.
5. **Freeze decisions get data.** A free GitHub Action (public repo, so Actions are free) can compile a weekly per-student merged-PR count and post it to a private leads channel. The freeze trigger becomes a query, not a scroll through `#integrations`.

---

## 6. Channel architecture — gaps and fixes for a 30-student cohort

All fixes use free Discord features. Discord itself has no meaningful free-tier risk at this scale — the only cost vectors are premium bots or a hosted custom bot (§6.8).

| # | Current | Problem at 30 students | Fix |
|---|---|---|---|
| 6.1 | `#discussion` (single text channel) | 30 students × daily debugging = a scroll-wall; the same question gets asked 5 times; answers are unfindable by week 3 | Convert to a **Forum channel** with one thread per task ID (`S3.2`, `P7.3`...). Mark-solved support, searchable, and "search before asking" becomes a teachable skill instead of a scolding |
| 6.2 | `#integrations` (announce-only feed) | 60-90 webhook posts/day bury everything, including the milestones | Keep announce-only, but add a pinned **weekly merge digest** (a free GitHub Action posts "this week: 214 merges, top reviewers, milestone status" every Sunday). Humans read the digest; the bot reads the feed |
| 6.3 | No surface for PR review requests | Reviewing is a repo requirement, but there is nowhere to ask "review my PR #142" — requests will leak into `#discussion` | Add a review-request **post format in the forum** (or its own sub-channel): `[task ID] [PR link] [what to check]`. Reviewers pick from the board — this also distributes the review load the audit's finding 8 flagged |
| 6.4 | No wins channel | The progress principle needs visible small wins; `#community-updates` is official-only | Add `#wins` (text, 0 XP): first green CI, first merged PR, the SCD2 proof. Leads seed it in week 1 so students know it is for them |
| 6.5 | No data-source status channel | The audit proved government sources 403/404 intermittently; in week 5 every student will rediscover this alone, at night | Add `#data-source-status` (text, 0 XP) with a pinned status table: source / works / blocked / workaround / mirror link. One student's 403 becomes the whole cohort's known issue within minutes |
| 6.6 | `#1-3-7-recap` unstructured photos | 30 photos/week of handwritten notes are unsearchable and unverifiable | Filename convention `DE##_W#_D3_topic`, plus a pinned rubric: legible, dated, from memory, at least 5 lines. Spot-check ~25% (not all 30) — the recap's value is the retrieval act, which cannot be faked by the uploader without defeating itself |
| 6.7 | Voice calls unscheduled/uncaptured | Day-7 mastery depends on attendance; there is no visible time or record | Post the weekly office-hours time in `#announcements`; record calls (with consent) and index them in `#youtube-videos` with a 3-line summary each |
| 6.8 | XP awarding machinery unspecified | XP is the accountability backbone; if it silently stops, the whole status system loses credibility mid-sprint | Decide **before week 1**, in this order of preference: (a) a leveling bot whose XP module is on a free tier (verify current terms at setup — leveling modules are commonly premium, e.g., MEE6's), (b) a self-hosted open-source leveling bot on a Team Lead's machine ($0), or (c) cleanest: no always-on bot at all — a scheduled GitHub Action + Discord webhook that computes XP from merged PRs and streak/recap posts and updates a leaderboard message. Whatever is chosen: one named owner in `06-team-roles.md` terms |

**One structural recommendation that cuts across all of the above:** the mission drop each Monday in `#weekly-missions` should be a **pinned message per week** containing: the week's goal, the three resource links (§8), the new tool if any, the office-hours time, and the cut list. One message, pinned, never edited after posting — the Discord-native equivalent of the repo's week file, so students never have to leave Discord to know what to do today.

---

## 7. Is the sprint overwhelming? The honest verdict

### 7.1 The numbers

| Dimension | Count | Source |
|---|---|---|
| Tasks per student | **105** (10, 11, 12, 13, 10, 8, 8, 11, 10, 14 by week) | week templates |
| Tracks running in parallel | 4, from week 1 | `00-START-HERE.md` §3 |
| Load-bearing tools | **11**: Git/GitHub, Python, SQL, SQL Server (local, weeks 2-4), Snowflake (weeks 7+), pytest, dbt, Great Expectations, Airflow, Docker, Metabase | `11-tools-and-technology.md` |
| Milestone gates | Discovery Brief (W1), First Load (W3), Star Schema Design (W4, sign-off W6), SCD2 Build (W7 SQL / W9 dbt), First Snowflake Load (W8), Handover (W10) | `04-week-map.md` |
| Process rituals per student per week | ~5-7 commits + PRs, 1+ review, 5-7 streak posts, 1-2 recap photos, 1 voice call | repo rules + server rules |

### 7.2 Estimated hours (engineering estimate, not a measurement)

Beginners average roughly 1.5-2.5 hours per task (Python and platform tasks at the high end, business-writing tasks at the low end): **105 × ~2h ≈ 200 hours ≈ 20 hours/week** for the full path. Process overhead (git friction, PR etiquette, Discord rituals) adds 15-20% in weeks 1-2, where beginners pay a 3× tax on every git operation that an experienced user pays once.

**Verdict: the full path is too heavy for a part-time beginner cohort.** 20 hours/week is a part-time job on top of whatever life the student already has, sustained for 10 consecutive weeks with milestone spikes. The curriculum's *content* is right-sized; its *volume* is not, **unless** three things happen (§7.4). The cut lists in each week file are the designed pressure valve — but they are framed as emergency measures, and beginners will not use them because using one feels like failing. That framing is the problem, not the tasks.

### 7.3 Week-by-week difficulty curve

| Week | Tasks | New things introduced | Load | Verdict |
|---|---|---|---|---|
| 1 | 10 | Git, fork/PR flow, Discord rituals, discovery writing — **all at once** | Process spike | **Danger zone** — the highest beginner-quit window in the program |
| 2 | 11 | SQL ramp + Python ramp | Heavy but focused | Watch |
| 3 | 12 | First end-to-end load, milestone | All tools come together first time | Watch |
| 4 | 13 | Peak task count so far + star schema milestone | Conceptual + volume peak | Watch |
| 5 | 10 | Three new Python patterns (generators, logging/CLI, OOP) + the 403-blocked-source risk | Conceptually dense | Watch |
| 6 | 8 | pytest only | **Lightest week** | Green — use it (see §7.4 fix 5) |
| 7 | 8 | Snowflake connector, concurrency, first real Snowflake usage | Tool switch | Watch |
| 8 | 11 | **dbt + the move into the shared `platform/` zone + two milestones** | Spike | **Danger zone** |
| 9 | 10 | dbt marts + SCD2 + Great Expectations + Kimball | Densest concepts, but no new tool | Watch |
| 10 | 14 | **Airflow + Metabase + two milestones + stakeholder delivery** | Highest task count + two new tools | **Danger zone** |

### 7.4 Pacing adjustments (concrete, mostly cost-free)

1. **Add week 0 (2-3 days before week 1).** Accounts created, a no-stakes git drill (fork, 5 commits, 1 PR to a sandbox repo), Discord rituals rehearsed, Python warmup started. This removes the week-1 process spike — week 1's actual content (discovery writing) is then learnable. This is the single highest-return fix in this document, and it costs two days.
2. **Make the cut list the default, not the emergency.** Publish two paths openly: **core path** (~12 hours/week, reaches every milestone, uses each week's cut list) and **full path** (~20 hours/week). Students choose weekly, switching is normal, and neither is shameful. Autonomy and competence — the two needs self-determination theory says motivation is built from — both require the choice to be real.
3. **Week 8 relief.** The audit already requires fixing the broken CI before week 8; extend that work one step: leads merge a working `platform/dbt` skeleton before the week opens, so students write models and tests, not scaffold and debug tooling, during the week they also switch zones and hit two milestones.
4. **Week 10 relief.** Airflow and Metabase both arriving in the final week, with two milestones, is the worst overload in the sprint. Either (a) leads provide pre-running local containers (this is the same fix as audit P0-4) so students write the DAG and the dashboard, not the infrastructure; or (b) move B6 Metabase to week 9 as a preview. Failing both: convert B5 break-fix into a lead-run failure demo + student postmortem.
5. **Label week 6 "catch-up week."** It is already the lightest (8 tasks, one new skill). Officially frame the surplus as time to finish weeks 4-5 stragglers. Framed as bonus time, it is a gift; framed as remedial time, it is an admission of failure. Same content, different dropout rate.

### 7.5 What NOT to cut (protects the psychology)

The messy real data, the "why" questions, the review requirement, the 1-3-7 loop, and the week-10 failure injection. These five are the desirable difficulties the whole design is built on; every one of them feels like friction in week N and is the reason graduates can interview credibly in week 11.

---

## 8. The resource problem — pre-load everything

### 8.1 What exists and what is missing

The repo is not actually resource-empty: `09-resources.md` is a genuinely good, week-mapped, station-referenced list. But three gaps remain:

1. **Python has no beginner video spine.** SQL has one (the Kudvenkat course); Python's entries are all docs and articles. Absolute beginners learn code better watch-first than read-first — a docs-only Python path in weeks 2-5 is the steepest avoidable curve in the sprint. This is the "apart from SQL there are no Python resources" feeling, and it is correct as felt even though a curated Python *reading* list exists.
2. **The list lives in the repo, not in Discord.** Students live in Discord; the resources are a `git pull` and four clicks away, and nothing is pinned in `#learning-resources` week by week.
3. **The platform tools have no resources at all** — dbt has dbt Learn listed (good), but Airflow, Docker, Metabase, and Great Expectations have no curated entry, and those all land in weeks 8-10, when time pressure is worst.

**Answer to "can we learn this from free public resources?": yes — every single topic in this sprint has a free, high-quality resource.** The risk is not availability; it is **search-time waste and quality variance at 11pm before a deadline**. A beginner searching "learn airflow" gets a mix of vendor marketing, outdated Airflow 1.x tutorials, and paid course ads. Pre-loading the pack below removes that entirely.

### 8.2 The pre-curated free pack (load into `#learning-resources` as pinned weekly messages **before week 1**)

One pinned message per week, posted each Monday with the mission drop: "Week N pack: watch X, read Y, sandbox Z." The repo stays the source of truth; Discord pins carry the top three items only.

| When | For | Resource (all free) | Exact portion | Time |
|---|---|---|---|---|
| Week 0 | Git survival | GitHub Skills — "Introduction to GitHub" (skills.github.com) | Whole course | ~1 h |
| Week 0 | Git mental model | Learn Git Branching (learngitbranching.js.org) | Levels 1-3 | ~2 h |
| Week 0 | Fork/PR loop | freeCodeCamp "Git and GitHub for Beginners" (YouTube) | First 45 minutes only | 45 m |
| Weeks 1-5 | **Python spine — pick one and finish it** | **CS50P — Harvard's Introduction to Programming with Python** (free on YouTube/edX audit) | Lectures 0-6 roughly track P1-P4 territory | ~2 h/week |
| or | Python spine (gentler) | Python for Everybody — py4e.com (Dr. Chuck) | Chapters 1-5, 10 | ~2 h/week |
| or | Python spine (faster) | Corey Schafer's Python Beginner Playlist (YouTube) | First ~10 videos | ~2 h/week |
| Weeks 1-2 | Zero-setup Python fallback | Kaggle Learn "Python" micro-course (browser sandbox) | For students whose local install is still broken — never block on environment | ~4 h |
| Weeks 2-3 | Files, CSV, functions | Automate the Boring Stuff (automatetheboringstuff.com, free online) | Chapters 6-9 | ~4 h |
| Week 5 | OOP | Corey Schafer OOP series (YouTube) | Videos 1-4 | ~1 h |
| Week 6 | pytest | freeCodeCamp pytest course (YouTube) **or** the Real Python article already in `09-resources.md` | First half | ~2 h |
| Week 7 | Snowflake connector | Snowflake University (learn.snowflake.com — free) Python connector hands-on lab | Lab only | ~1 h |
| Weeks 7-8 | Snowflake fundamentals + **cost sense** | Snowflake University Hands-on Essentials badge courses + the resource-monitor course | Assign alongside the day-0 runbook in `13-tool-cost-control-runbook.md` | ~2 h |
| Week 8 | dbt | dbt Learn — "dbt Fundamentals" (free; already in `09-resources.md`) | Modules 1-3 for week 8; snapshots module for week 9 | ~3 h |
| Week 9 | Great Expectations | GX docs "Getting Started" tutorial | Quickstart only | ~1 h |
| Week 9 | Kimball | The two Kimball articles already in `09-resources.md` | Both | ~1 h |
| Week 10 | Airflow | Airflow docs "Core Concepts" + Astronomer's free learning guides/videos (free content — **do not** sign up for a paid deployment) | Concepts + one example DAG | ~2 h |
| Week 10 | Docker | Docker's official "Get Started" workshop + Play with Docker sandbox | First two sections | ~1.5 h |
| Week 10 | Metabase | Metabase "Learn" + docs Getting Started (OSS edition) | Getting started + basics tour | ~1 h |

### 8.3 Maintenance rules (cheap, and they prevent the 11pm panic)

1. **Verify every link the week before it is needed.** Link rot is real, and this sprint's government data sources already 403 intermittently (audit finding 6). The `#data-source-status` channel (§6.5) is the live early-warning system.
2. **Pin per week, never one giant list.** A 60-link pinned message is where motivation goes to die; three items per week gets done.
3. **Never send students to search.** The moment a student has to search is the moment they meet a 2021 tutorial for the wrong tool version (audit finding 7 makes this a real risk — pin versions in the resource message).

---

## 9. Pre-sprint setup checklist for Team Leads (the two weeks before day 0)

**Decisions (make these first):**
- [ ] XP ladder policy chosen (§4.4 — recommended: multi-sprint ladder + ~1,100 XP "Sprint Graduate" badge)
- [ ] XP machinery chosen and owned (§6.8 — bot, self-hosted bot, or GitHub-Action-computed XP; one named owner)
- [ ] Core path vs full path published (§7.4 fix 2)
- [ ] Week 0 dates set (§7.4 fix 1)
- [ ] Week 10 relief option chosen (§7.4 fix 4)

**Discord build-out:**
- [ ] `#discussion` converted to a forum channel; review-request post format published
- [ ] `#wins` and `#data-source-status` channels created; status table pinned; wins seeded by leads
- [ ] `#1-3-7-recap` rubric + filename convention pinned
- [ ] Weekly merge-digest action wired to `#integrations`
- [ ] Mission-drop pin template created (goal / resources / new tool / office hours / cut list)
- [ ] Voice call schedule posted in `#announcements`; recording + consent policy decided
- [ ] `#roles` updated: streak shield rule, freeze rules per §5, ladder relabel per §4.4

**Repo and tools (from the audit — still outstanding):**
- [ ] CI workflows repaired (audit P0-2), `.gitignore` fixed (audit P0-3), Airflow/Metabase plan owned (audit P0-4)
- [ ] `13-tool-cost-control-runbook.md` linked in `#learning-resources` and assigned as week-1 reading alongside Snowflake signup
- [ ] Week 0-10 resource packs pinned (§8.2)

---

## 10. Sources and verification notes

- **Snowflake student trial (120 days / $400 / no card):** provided by the program lead via `https://signup.snowflake.com/?trial=student`; the page is JavaScript-rendered and returned 404 to scripted fetches on 8 Sep 2026 — confirm at signup. Standard trial: 30 days / $400. Full cost-control detail: `13-tool-cost-control-runbook.md` §9.
- **Snowflake docs (fetched 8 Sep 2026):** "Cost controls for warehouses" (statement timeouts settable at account/user/session/warehouse, lowest non-zero wins; auto-suspend/auto-resume pairing; resource monitors suspend at thresholds and cover neither cloud services nor serverless features; `SHOW WAREHOUSES` hygiene queries). "Working with resource monitors" (ACCOUNTADMIN creation, credit quota + frequency, trigger thresholds and actions). ACCOUNT_USAGE views (`METERING_HISTORY`, `WAREHOUSE_METERING_HISTORY`, `QUERY_HISTORY`).
- **Free-tier facts carried over from `CURRICULUM-AUDIT.md` Appendix B (verified 2 Sep 2026):** GitHub Actions free on public repos; branch protection public-repo-only on Free; dbt Learn Fundamentals free; Snowflake University free; Metabase OSS free / Cloud ≈ $100/mo after 14-day trial; Astronomer no permanent free tier; Docker Desktop free for personal/education use.
- **dbt Cloud free Developer plan (1 seat):** verified 8 Sep 2026 — relevant only if anyone opts into Cloud; the repo uses dbt Core.
- **Cognitive-science claims (standard, replicated literature; deliberately no pop-neuroscience):** spacing effect and expanding intervals (Cepeda et al. 2006); testing effect (Roediger & Karpicke 2006); desirable difficulties (Bjork); interleaving (Rohrer & Taylor 2007); longhand note-taking (Mueller & Oppenheimer 2014, partial replications since — stated as directional); progress principle (Amabile); self-determination theory and the over-justification effect (Deci & Ryan); loss aversion (Kahneman & Tversky); Yerkes-Dodson arousal/performance. Task-switching cost (Gloria Mark's research) cited as commonly-measured, not exact.
- **Not independently verified (flagged for lead verification at setup):** current free-tier terms of specific Discord XP bots (MEE6/Arcane-class leveling modules — pricing changes frequently); this document's §6.8 deliberately offers a bot-free option so the program does not depend on any bot's pricing.

## 11. Assumptions and limits

- Cohort size 15-30 (per `07-platform-and-cicd-guide.md`); Discord architecture and XP weights exactly as provided by the program lead on 8 Sep 2026.
- One mission drop and one 1-3-7 cycle per week per student. If classes run more often than weekly, §4's recap math (40-80 XP) rises and the L3 verdict moves from "unreachable" to "barely reachable" — the L4/L5 conclusions do not change.
- Task counts were counted from the week templates, which matched all 300 student files at audit time (2 Sep 2026).
- Hours estimates (§7.2) are engineering estimates, not measurements. Calibrate after week 2 using actual PR timestamps; the weekly per-student PR digest (§5.3 fix 5) produces exactly this data.
- This document and `13-tool-cost-control-runbook.md` are the only files added; nothing existing was modified. Every recommendation here is a rule change, a channel change, or a new-file change — none requires editing the existing curriculum.

