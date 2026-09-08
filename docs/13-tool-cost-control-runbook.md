# Snowflake and Tool Cost-Control Runbook

**Prepared for:** every student, on the day they create their Snowflake account (week 1 setup). Team Leads should read §7 before the sprint starts.
**Date:** 8 September 2026.
**Ground rule honored:** read-only. This is a new file; nothing existing was modified.
**Related:** `02-tools-setup.md` (account creation), `12-discord-cohort-learning-design.md` (learning design), `CURRICULUM-AUDIT.md` (the original Snowflake risk finding, corrected - see below).

---

## 0. Why this runbook exists

Every student creates their **own** Snowflake account via the student signup link (`https://signup.snowflake.com/?trial=student`): **120 days of access, $400 of credits, no credit card.** That fixes the audit's worst finding - there is no shared account, no shared clock, and no 30-day cliff in the middle of a 70-day sprint.

But a fresh account has **no cost-saving configuration**, and Snowflake will happily let a beginner burn $400 in a bad night. The math below shows why $400 is genuinely generous **if** the account is configured on day 0 - and this runbook makes the account sprint-proof in about ten minutes, with SQL you paste once and a 30-second weekly check.

**The core idea: on this sprint, credits are lost to misconfiguration, not to studying.** Guard against the five failure modes in §2 and the budget is effectively unlimited.

---

## 1. Account facts (read once, on signup day)

| Dimension | Fact | Note |
|---|---|---|
| Duration | **120 days** (student trial) | Standard non-student trials are 30 days - use the student link, not the generic one. Sprint = 70 days, so the account outlives the sprint by ~7 weeks **if created at week-1 setup**. Do not create it months early. |
| Credits | **$400 of usage** | One pool for warehouse compute, cloud services, and serverless features. Not a monthly allowance - a total. |
| Credit card | **Not required** | **Never add one.** If credits run out, the account stops - that is the desired failure mode. A card converts a hard stop into a real bill. |
| Edition | Standard | Everything this sprint needs (warehouses, stages, resource monitors, `ACCOUNT_USAGE`) is included. |
| Region | Pick the one nearest you (Asia-Pacific Singapore/Mumbai for the cohort) | Same credit price in every region for the same cloud; nearer = lower latency only. |
| Users | You are the only user, with `ACCOUNTADMIN` | That is why the day-0 script below works - you already hold the privileges. |

**Verification note:** the student signup page is JavaScript-rendered and returns 404 to scripted fetches; the 120-day/$400 terms come from the program lead. Confirm the banner text on the day you sign up, and note the expiry date in your notes file.

---

## 2. How credits are actually spent

### 2.1 Warehouse compute - the part you control

An X-Small warehouse costs **1 credit per hour**, billed per second of use with a **60-second minimum each time it starts**. Sizes double from there:

| Size | Credits/hour | One night left running (~10 h) |
|---|---|---|
| **X-Small** | **1** | 10 credits (2.5% of budget - fine) |
| Small | 2 | 20 credits |
| Medium | 4 | 40 credits |
| Large | 8 | 80 credits |
| X-Large | 16 | 160 credits |
| 2X-Large | 32 | **320 credits - 80% of your budget in one night** |

With `AUTO_SUSPEND = 60` and `AUTO_RESUME = TRUE`, the warehouse shuts down one minute after your last query and wakes when the next one arrives. A student querying an hour a day uses roughly **10-14 credits/week ≈ 100-140 credits over the whole sprint** - about a third of the budget, with ~3× headroom. This is why §3 exists: the settings matter more than your behavior.

### 2.2 The invisible spend - and why the monitor cannot stop it

Resource monitors suspend **warehouse compute only**. Two categories sit outside them:

- **Cloud services** - the Snowflake-side layer (metadata, parsing, `SHOW` commands, result serving). On Standard editions, daily cloud-services usage above 10% of daily warehouse compute is billed from your credit pool. At this sprint's scale it is small - but it is nonzero, and it is why the weekly check (§4) reports it separately.
- **Serverless features** - automatic clustering, search optimization, materialized-view maintenance, Snowpipe, serverless tasks, dynamic tables. **None of these are needed anywhere in this sprint.** Each one consumes credits continuously once enabled, and a resource monitor will not suspend them. The rule is therefore "never turn them on" (§5), not "monitor them."

### 2.3 What you can safely ignore at this scale

Storage (a few GB ≈ cents), Time Travel (leave the default 1-day retention), fail-safe, and the **result cache - which is free and your friend**: re-running an identical query returns the cached result at zero warehouse cost. Developing a query by re-running it costs nothing after the first run.

### 2.4 Warehouse type

Keep the default (Standard/Gen1) compute. Gen2 warehouses bill roughly **1.35× credits/hour** (AWS) for faster hardware that MB-scale student data cannot use. Do not switch.

---

## 3. Day-0 setup - the ten-minute script

**Where:** Snowsight → Worksheets → new worksheet → paste → **Run All**, top to bottom. Replace `<YOUR_USERNAME>` with your login (uppercased, in double quotes if it contains special characters). You hold `ACCOUNTADMIN` because you are the account's only user.

```sql
-- 0. Make sure you are the admin (you are, on a trial account)
USE ROLE ACCOUNTADMIN;

-- 1. Kill runaway queries before they burn credits.
--    Default statement timeout is 172800 seconds (2 days). 15 minutes is the
--    right ceiling for anything in this sprint. Queued queries die after 5 min.
ALTER ACCOUNT SET STATEMENT_TIMEOUT_IN_SECONDS = 900;
ALTER ACCOUNT SET STATEMENT_QUEUED_TIMEOUT_IN_SECONDS = 300;

-- 2. One warehouse, right-sized, self-suspending. This is your only warehouse.
CREATE WAREHOUSE IF NOT EXISTS SPRINT_WH
  WAREHOUSE_SIZE = XSMALL
  AUTO_SUSPEND = 60            -- suspend 60 seconds after the last query
  AUTO_RESUME = TRUE           -- ...and wake up automatically when needed
  INITIALLY_SUSPENDED = TRUE
  STATEMENT_TIMEOUT_IN_SECONDS = 900
  STATEMENT_QUEUED_TIMEOUT_IN_SECONDS = 300
  COMMENT = 'Sprint warehouse - do not resize, do not disable auto-suspend';

-- 3. Make it your default, so worksheets and connectors never spawn surprises
ALTER USER <YOUR_USERNAME> SET DEFAULT_WAREHOUSE = SPRINT_WH;

-- 4. Show every warehouse on the account. If anything other than SPRINT_WH
--    exists, drop it:  DROP WAREHOUSE <name>;
SHOW WAREHOUSES;

-- 5. The hard ceiling: a resource monitor that suspends the warehouse at 75%
--    of a 100-credit monthly quota, and kills running statements at 100%.
--    100 credits/month x 3 sprint months = 300 < 400. The monitor is the
--    seatbelt, not the budget.
CREATE RESOURCE MONITOR SPRINT_BUDGET WITH
  CREDIT_QUOTA = 100
  FREQUENCY = MONTHLY
  START_TIMESTAMP = IMMEDIATELY
  TRIGGERS ON 75 PERCENT DO SUSPEND
             ON 100 PERCENT DO SUSPEND_IMMEDIATE;

-- 6. Attach the monitor to the warehouse
ALTER WAREHOUSE SPRINT_WH SET RESOURCE_MONITOR = SPRINT_BUDGET;
```

**What each guardrail buys you:**

| Setting | What it prevents |
|---|---|
| `STATEMENT_TIMEOUT_IN_SECONDS = 900` | A cross-join or `SELECT *` written by a tired student at 1am runs 15 minutes max instead of all night. Settable at account/user/session/warehouse level; when set at more than one level, the lowest non-zero value wins - you set both, so you are safe everywhere. |
| `AUTO_SUSPEND = 60` + `AUTO_RESUME = TRUE` | The classic beginner loss: leaving a worksheet tab open with auto-suspend disabled. Snowflake's own best-practice pairing. |
| `WAREHOUSE_SIZE = XSMALL` | Every task in this sprint (bronze loads of MB-scale files, dbt models on thousands of rows) fits in XS with room to spare. Slow means your SQL needs work - which is the lesson, not a hardware problem. |
| `SPRINT_BUDGET` monitor at 75/100 | Even if everything else fails, the warehouse physically stops at 75 credits in a month. `SUSPEND` lets pending statements finish; `SUSPEND_IMMEDIATE` kills them. You get an email/notification only if you also configure notifications - skip that; the weekly check in §4 replaces it. |

**Verify it worked** (run in the same worksheet):

```sql
SHOW WAREHOUSES;              -- exactly one row: SPRINT_WH, size X-Small,
                              -- auto_suspend 60, auto_resume true,
                              -- resource_monitor SPRINT_BUDGET
SHOW RESOURCE MONITORS;       -- SPRINT_BUDGET, credit_quota 100, monthly
```

Two honest limitations, so nothing surprises you later: a monitor suspends the **warehouse** - cloud-services and serverless spend continues (§2.2, which is why §5 exists); and if the monitor suspends your warehouse mid-week, queries resume it automatically only if the monitor has not hit a suspend trigger again in the new month.

---

## 4. The weekly 30-second check

Save this as a worksheet named `BUDGET CHECK` and run it every Monday (with the mission drop). It reads only `ACCOUNT_USAGE` views - free to query, and they cost no warehouse credits to speak of at this size.

```sql
-- Credits burned in the last 7 days, split by type.
-- Healthy: < 15 credits/week, all of it COMPUTE.
SELECT DATE_TRUNC('day', start_time) AS day,
       SUM(credits_used_compute)      AS compute_credits,
       SUM(credits_used_cloud_services) AS cloud_services_credits
FROM SNOWFLAKE.ACCOUNT_USAGE.METERING_HISTORY
WHERE start_time >= DATEADD('day', -7, CURRENT_TIMESTAMP())
GROUP BY 1
ORDER BY 1;

-- Per-warehouse daily burn, last 30 days.
-- Healthy: one warehouse, one bar per day, nothing on no-work days.
SELECT DATE_TRUNC('day', start_time) AS day,
       warehouse_name,
       SUM(credits_used) AS credits
FROM SNOWFLAKE.ACCOUNT_USAGE.WAREHOUSE_METERING_HISTORY
WHERE start_time >= DATEADD('day', -30, CURRENT_TIMESTAMP())
GROUP BY 1, 2
ORDER BY 1;

-- Any query that ran longer than 10 minutes last week (runaway suspects)
SELECT query_id,
       warehouse_name,
       TOTAL_ELAPSED_TIME/1000 AS seconds,
       LEFT(query_text, 80)    AS query_head
FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY
WHERE start_time >= DATEADD('day', -7, CURRENT_TIMESTAMP())
  AND TOTAL_ELAPSED_TIME > 600000
ORDER BY TOTAL_ELAPSED_TIME DESC
LIMIT 10;

-- Monitor status: how much of the monthly 100-credit quota is used
SHOW RESOURCE MONITORS;
```

Notes:

- `ACCOUNT_USAGE` views lag (up to ~45 minutes for metering, hours for some views). For a same-hour number, use the Information Schema instead: `SELECT * FROM TABLE(INFORMATION_SCHEMA.METERING_HISTORY(DATEADD('day',-1,CURRENT_TIMESTAMP()), CURRENT_TIMESTAMP()));`
- The headline number - **remaining free credits** - is visible without SQL: Snowsight → **Admin → Cost Management**. Check it whenever you are in the UI anyway.
- If compute credits ever exceed ~15/week on this sprint, something from §5 happened. The `QUERY_HISTORY` query above names the culprit.

---

## 5. The never-do list - what actually kills student accounts

| # | Never | Why |
|---|---|---|
| 1 | **Never add a payment card, and never accept a conversion to On-Demand** | The hard stop when credits end is the feature that makes this safe. A card turns "account stops" into "card is charged." |
| 2 | **Never disable auto-suspend or set it to 0** | An idle-but-resumed XS warehouse bills 24 credits/day; a 2XL bills 768/day. This one setting is the difference between 3× headroom and a dead account. |
| 3 | **Never resize above X-Small** | No task in this sprint needs it. Slow = fix the SQL (that is the curriculum). |
| 4 | **Never enable: Search Optimization, Automatic Clustering, Materialized Views, Dynamic Tables, Snowpipe, serverless Tasks, Cortex/ML functions** | All burn serverless credits that resource monitors **cannot** suspend (§2.2). None are needed for this project. |
| 5 | **Never create a second warehouse** "to try something" | One account, one warehouse. `SHOW WAREHOUSES` in the weekly check enforces this. |
| 6 | **Never enable multi-cluster** | `MAX_CLUSTER_COUNT` stays 1. Multi-cluster is for hundreds of concurrent users. |
| 7 | **Never sign up for marketplace paid listings or cross-cloud sharing** | These bill directly against the trial's credit pool. |
| 8 | **Never switch warehouse type to Gen2** | ~1.35× credits/hour for hardware MB-scale data cannot use (§2.4). |

---

## 6. What happens at the limit - and the exit plan

**If credits hit $400 first:** compute suspends and the account is effectively unusable until converted to paid (**never convert**). With the day-0 settings this should not happen - the monitor already failed you safe at 100 credits/month, and §4's weekly check would have shown the burn weeks earlier. If a monitor suspension was *legitimate* (a genuinely heavy month), investigate with §4 first, then adjust the quota deliberately: `ALTER RESOURCE MONITOR SPRINT_BUDGET SET CREDIT_QUOTA = 150;` - a decision, not an accident.

**If day 120 arrives first:** the account is disabled (Snowflake's published trial behavior: a grace period, then removal). With week-1 signup, day 120 lands ~7 weeks **after** the sprint ends - outside the program entirely. Do not cycle new trial accounts to extend free usage; that violates Snowflake's terms and teaches the wrong professional habit. One account per student; treat day 120 as the end.

**The exit plan is already the curriculum.** Everything needed to rebuild the platform lives in git: extractors, DDL, dbt models, and the week-10 runbook - the handover milestone literally rehearses a clean rebuild on a fresh schema. The only things not in git are the raw source files (banned by repo rule 5), which stay on your machine. **A fresh account + the repo + your local raw files = a full bronze reload in about an hour.** For portfolios after the sprint: the repo, screenshots, and the generated dbt docs site outlive the account and are what interviewers actually look at.

---

## 7. Every other tool in the stack - the $0 guardrails

Snowflake is the only tool in this project with a metered trial behind it. Everything else is either free software or a free tier - each with exactly **one** way it can start costing money. Know the one way; avoid it.

| Tool | Free basis | The one way it starts costing money | Guardrail |
|---|---|---|---|
| **GitHub** (repo, PRs, reviews) | Free plan: unlimited public repos; Actions free on public repos with standard runners; branch protection works on public repos | The repo going **private** (Actions drops to the 2,000 min/month Free quota - enough for this project, but tighter) or using larger/paid runners | Keep the repo public; check Settings → General → Danger Zone if anyone suggests changing visibility |
| **GitHub Student Pack** (optional) | Free for verified students; includes Pro perks while enrolled | Nothing - it is free | Apply at education.github.com with college ID; no card required |
| **Python + venv** | Free, open-source | Nothing | Pin versions (audit finding 7) so pip never surprises you |
| **pytest, tenacity, pandas, pdfplumber, bs4** | Free libraries | Nothing | - |
| **dbt Core** | Free, open-source, runs locally against your Snowflake account | Nothing | This is why the repo uses Core, not Cloud |
| **dbt Cloud** (optional - not required by this repo) | Free Developer plan (1 seat, monthly build allowance) | Starting a **Team/Enterprise trial**, which converts to a paid subscription | If you use it at all, pick the free **Developer** plan explicitly at signup; never enter a card |
| **Great Expectations (GX Core)** | Free library | GX Cloud (managed) - not needed | Local library only |
| **SQL Server Express** (weeks 2-4 SQL practice) | Free local edition (compute and 10 GB database caps - far above sprint needs) | Azure SQL / any hosted SQL | Local install only |
| **Docker Desktop** | Free for personal and educational use (paid only for larger organizations) | Corporate use at a company above the size threshold - not students | If its license ever concerns you: Podman, Colima, or Rancher Desktop are free drop-ins |
| **Airflow** | Free, open-source; run via the official Docker Compose stack locally | **Astronomer or any managed Airflow** - no permanent free tier, deployments ≈ $0.35/hour | Never sign up for a managed deployment. Local Compose only. Budget ~4-8 GB RAM for the stack; close other apps |
| **Metabase** | **Open Source edition** is free, self-hosted, unlimited users | **Metabase Cloud** - Starter is ≈ $100/month after a 14-day trial | Never start the Cloud trial. Week 10's dashboard runs on the local OSS edition (jar or container) |
| **VS Code, Git** | Free | Nothing | - |
| **Discord + XP machinery** | Free at any cohort scale; XP computable by a free GitHub Action + webhooks (see `12-discord-cohort-learning-design.md` §6.8) | A premium XP bot tier, or a hosted custom bot | Use a free-tier bot, a self-hosted open-source bot on a Lead's machine, or the bot-free Action approach |
| **Snowflake University, dbt Learn, all resources in doc 12 §8** | Free | Nothing | Verify links weekly (doc 12 §8.3) |

**The pattern across the whole stack:** free software run locally, or free tiers on public repos. The money traps are all *trials of managed services* - dbt Cloud Team, Metabase Cloud, Astronomer, any "free trial" credit card form. If a signup ever asks for a card and Snowflake's student link did not, stop and ask in `#discussion`.

---

## 8. One-page checklist (pin this in Discord `#learning-resources`)

**On signup day:**
- [ ] Account created via the **student** link - 120 days, $400, **no card**
- [ ] Region = nearest (Asia-Pacific Singapore/Mumbai for the cohort)
- [ ] Day-0 script (§3) run; `<YOUR_USERNAME>` replaced
- [ ] `SHOW WAREHOUSES` shows exactly one: `SPRINT_WH`, X-Small, auto_suspend 60, monitor `SPRINT_BUDGET`
- [ ] Expiry date (signup + 120 days) written in my notes file

**Every Monday:**
- [ ] `BUDGET CHECK` worksheet run (§4) - under ~15 credits/week, all compute

**Always:**
- [ ] Never-do list (§5) read once - especially: no card, no resize, no serverless features
- [ ] Raw source files stay local (never committed - repo rule 5)
- [ ] No cloud trials for dbt / Metabase / Airflow - local and open-source only

---

## 9. Sources and verification

- **Snowflake student trial terms (120 days / $400 / no card):** provided by the program lead via `https://signup.snowflake.com/?trial=student`. The page is JavaScript-rendered and returned 404 to this document's automated fetches on 8 Sep 2026 - **confirm the banner on signup day**. Standard trial terms (30 days / $400, read-only grace then removal) per Snowflake's published trial terms as cited in `CURRICULUM-AUDIT.md` Appendix B.
- **Snowflake Docs - "Cost controls for warehouses"** (fetched 8 Sep 2026): `STATEMENT_TIMEOUT_IN_SECONDS` and `STATEMENT_QUEUED_TIMEOUT_IN_SECONDS` settable at account/user/session/warehouse, lowest non-zero value enforced; auto-suspend + auto-resume as the recommended pairing; `SHOW WAREHOUSES` hygiene queries for warehouses without auto-suspend, without auto-resume, or without a monitor; resource monitors suspend warehouses at credit thresholds and **do not cover cloud services or serverless** features.
- **Snowflake Docs - "Working with resource monitors"** (fetched earlier this week): created by `ACCOUNTADMIN` (or a role granted the privilege); `CREDIT_QUOTA` + `FREQUENCY`; trigger thresholds with `NOTIFY` / `SUSPEND` / `SUSPEND_IMMEDIATE`; account-level and warehouse-level monitors stack (whichever limit hits first suspends); `SHOW RESOURCE MONITORS` reports quota usage.
- **Snowflake Docs - parameters reference** (fetched 8 Sep 2026): parameter hierarchy (account → user → session → object) and the three parameter types.
- **Snowflake Docs - "Overview of warehouses"** (via the audit, 2 Sep 2026): X-Small = 1 credit/hour, sizes double from there; XS is the default warehouse size; per-second billing with 60-second minimum.
- **ACCOUNT_USAGE views** (`METERING_HISTORY` with `credits_used` / `credits_used_compute` / `credits_used_cloud_services`; `WAREHOUSE_METERING_HISTORY`; `QUERY_HISTORY` with `TOTAL_ELAPSED_TIME` in milliseconds): per Snowflake Docs, with the known latency caveats stated in §4.
- **Gen2 warehouse multiplier (~1.35× on AWS):** Snowflake pricing/docs; stated as approximate - the guardrail is simply "keep the default type."
- **dbt Cloud free Developer plan (1 seat) and free dbt Learn Fundamentals:** verified 8 Sep 2026.
- **Metabase (OSS free / Cloud Starter ≈ $100/month after 14-day trial), Astronomer (no permanent free tier, ≈ $0.35/hour), Docker Desktop (free for personal/education), GitHub Actions (free on public repos) and branch protection (public-repo-only on Free):** carried from `CURRICULUM-AUDIT.md` Appendix B, verified 2 Sep 2026.

## 10. Assumptions

- One account per student, created at week-1 setup per `02-tools-setup.md`; cohort 15-30.
- Sprint data volumes are MB-scale (four Indian government sources, monthly snapshots). The credit math in §2 and the monitor quota in §3 assume this; anyone loading GB-scale data should revisit §2.1 before touching anything else.
- The weekly check's "under ~15 credits/week" healthy reading assumes the week 1-6 pattern (SQL practice is on local SQL Server; Snowflake becomes load-bearing from week 7's connector and week 8's bronze loads). Weeks 8-10 running dbt and monthly refreshes may legitimately push higher - that is why the monitor is 100/month, not 15/week.
- This runbook configures **your own account only**; it modifies nothing in the repository, no shared infrastructure, and no existing files.

