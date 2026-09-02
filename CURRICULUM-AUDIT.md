# Data Sprint 1 — Tech Stack and Repository Audit

**Prepared for:** program leads and curriculum owners (not students).
**Date:** 2 September 2026.
**Scope:** every tool, workflow, config file, doc, and week template in this repository, plus the current free-tier terms of every external service in the stack.
**Ground rule honored:** this is a read-only audit. No existing file was modified. This document is the only addition to the repository. Every fix below is *described*, never applied.

---

## How to read this document

| Rating | Meaning |
|---|---|
| **P0** | Will break the sprint before or around weeks 4–5, or blocks an entire phase. Fix before week 1. |
| **P1** | Causes repeated student friction, or breaks in weeks 5–10 if left alone. Fix before the affected week. |
| **P2** | Polish. Improves the experience; nothing dies without it. |

Every finding names its evidence (file + section) so you can verify it in a minute. External facts carry a verification date; sources are listed in Appendix B.

---

## 0. Executive summary

The curriculum design itself is strong — the fork-plus-own-folder isolation, the practice-vs-platform two-zone split, milestone gates, per-week cut lists, and the no-squash merge policy are better than most commercial bootcamps. The risks below are almost entirely **operational**: things that break *around* the curriculum, not because of it.

| # | Finding | Severity | Evidence |
|---|---|---|---|
| 1 | Snowflake has no permanent free tier. A 30-day trial cannot cover a 70-day sprint, and one shared account for 15–30 students concentrates both the clock and the credit burn | **P0** | `docs/02-tools-setup.md` §5; week 10 D10.1 |
| 2 | All three GitHub Actions workflows are broken as committed: wrong dbt project dir, no `profiles.yml` anywhere, and a dbt-templating requirement the lint job cannot satisfy | **P0** | `.github/workflows/*`, `.sqlfluff`, `platform/dbt/dbt_project.yml` |
| 3 | `.gitignore` does not ignore `.venv/` although `02-tools-setup.md` §3 tells students it does, and does not ignore `*.zip` although CONTRIBUTING rule 6 bans them | **P0** | `.gitignore` (verified with `git check-ignore`) |
| 4 | Airflow and Metabase are "provided / hosted by the program" — the only stack items with no zero-cost hosting story, and nothing documents who runs them or how | **P0** | `docs/02-tools-setup.md` §8; week 10 B6 + D9 |
| 5 | Branch protection on GitHub Free works on **public repositories only** — the entire "nobody pushes to main" rule silently depends on repo visibility | **P1** | GitHub docs, verified 2 Sep 2026 |
| 6 | Government data sources block scripted access (mca.gov.in and data.gov.in returned HTTP 403 to this audit's fetches; an ibbi.gov.in publications URL 404s). Week 5's `requests` + Beautiful Soup extractors will hit this, and no offline fixtures exist | **P1** | week 5 P7, week 9 P12.1; live checks, 2 Sep 2026 |
| 7 | Nothing is version-pinned: no `requirements.txt`, unpinned CI installs, CI on Python 3.10 while docs demand 3.11+. Mid-sprint upstream releases will break students, tutorials, and CI in different ways | **P1** | `docs/02-tools-setup.md` §3; `.github/workflows/*` |
| 8 | Review bandwidth: one rotating student review lead cannot keep pace with ~25–30 continuously-updated pull requests per week plus their own full task load | **P1** | `docs/06-team-roles.md` |
| 9 | Week 8 and week 10 are overloaded: week 8 adds a brand-new tool (dbt) plus a process switch into the shared zone plus two milestones; week 10 adds two brand-new tools plus two milestones plus stakeholder delivery | **P1** | week 8 + week 10 templates |
| 10 | Missing hygiene files: no LICENSE, PR template, CODEOWNERS, `.env.example`, `.gitattributes`, setup-verification script, or test fixtures — each one costs support time in week 1 | **P2** | repo root listing |

**The single most important decision to make before week 1 is the Snowflake account strategy** (Section 1.1, and Fix 1 in Section 5). Everything else on this list is a file edit and an afternoon.

---

## 1. Critical loopholes & failure points

### 1.1 The Snowflake clock runs out in week 4–5 (P0)

**The arithmetic.** Snowflake's self-service trial is 30 days of usage (or $400 of credits, whichever comes first; no credit card at signup), and Snowflake has **no permanent free tier**. When a trial lapses, the account becomes read-only for a short grace period and is then deleted. This sprint is 10 weeks ≈ 70 days. The trial dies around **week 4–5** — before dbt (week 8), Great Expectations (week 9), Airflow and Metabase (week 10), and before the D10.1 handover milestone, which requires a live warehouse and a fresh schema on day ~70.

**Everything downstream is coupled to it:**

- Weeks 3–7: every SQL station and the P3, P11, and P12 milestones run in Snowflake.
- Week 8 onward: `dbt-build.yml` runs a full `dbt build` against Snowflake on every merge to `main`. The day the account dies, CI goes permanently red and *stays* red.
- Week 10 B6/D9/D10: dashboards, the DAG's real run, and the clean-checkout handover all need a live warehouse.

**Shared-account concentration.** `02-tools-setup.md` §5 hands every student the same account URL, a `STUDENT_ROLE`, and one shared `STUDENT_WH`. That makes three problems one:

1. **Credits.** An XS warehouse burns 1 credit per hour (Snowflake docs, verified 2 Sep 2026), and XS is the default size. Thirty students exploring, loading multi-GB RoC files into 30 personal schemas, running dbt builds and full refreshes all draw on one pool. Careful users can still exhaust $400 before day 30, and nobody is warned when it runs low, because no resource monitor is documented anywhere.
2. **Clock.** One account, one start date. The whole cohort hits the wall the same week, mid-milestone, with no partial credit.
3. **Concurrency.** A single XS warehouse serves a small number of concurrent queries. An evening lab with 15–30 simultaneous worksheets means queuing and timeouts, which beginners will read as "Snowflake is broken," not "I should retry."

Options are compared in Fix 1 (Section 5): a planned mid-sprint switch to a second trial account, per-student trial accounts, educator outreach to Snowflake, or a DuckDB bridge for weeks 1–6.

### 1.2 All three CI workflows are broken as committed — plus a fourth problem arriving in week 6 (P0)

The platform phase (weeks 8–10) depends on CI being green, and `07-platform-and-cicd-guide.md` tells admins to make the lint and dbt checks *required* under branch protection. As committed today, every workflow fails on its first real run:

**Bug A — wrong dbt project directory.** `dbt-check.yml` and `dbt-build.yml` run `dbt parse` / `dbt build` with `--project-dir platform/`, but the dbt project lives at `platform/dbt/dbt_project.yml`. dbt looks for `dbt_project.yml` *inside* the directory you give it; it does not search subdirectories. Both workflows die with "not a dbt project" before doing anything useful.

**Bug B — no `profiles.yml` exists anywhere.** `dbt_project.yml` declares `profile: 'default'`, and dbt needs a resolvable profile even to parse. The `DBT_SNOWFLAKE_*` repository secrets in `dbt-build.yml` do nothing by themselves — dbt never reads env vars with those names unless a committed `profiles.yml` maps them via `env_var()`. No such file exists in the repo, and the docs (correctly) tell students to keep their personal `profiles.yml` in `~/.dbt/` — which is useless to a CI runner.

**Bug C — the linter is configured for a templater it cannot load.** `.sqlfluff` sets `templater = dbt`, but `lint.yml` installs only `sqlfluff black flake8`. The dbt templater needs dbt installed (and a working profile) to render `.sql` files, so the first `.sql` file under `platform/` fails the lint job with a templater *error*, not a style error. Separately, `black` runs in CI on code no student is ever told to run locally — it appears in no doc, no install list, and no explanation.

**Bug D — week 6 asks 30 students to each commit a CI file at the repo root.** P9.3 says "Set up the tests to run automatically on every pull request. Commit: the CI configuration file at the repository root." Thirty students committing files into `.github/workflows/` at the same path is a guaranteed filename collision and merge-conflict pile-up — and every merged file becomes a *live* workflow that triggers on everyone's PRs. Either the task conflicts or it multiplies CI runs thirty-fold.

**Net effect:** from week 8, every platform PR is unmergeable (required checks that always fail), and from week 6 the workflow directory becomes a battleground. The first time the cohort meets CI — the moment the curriculum most needs it to feel trustworthy — it will feel arbitrary and broken.

---

### 1.3 `.gitignore` promises things it does not do (P0)

Verified with `git check-ignore` during this audit:

| Claim made in the docs | Reality |
|---|---|
| `02-tools-setup.md` §3: "`.venv/` is already in `.gitignore`" | **False.** No rule in `.gitignore` matches `.venv`. |
| CONTRIBUTING rule 6: "No downloaded CSV, ZIP, PDF, or Excel files" | `*.csv`, `*.pdf`, `*.xlsx` are ignored; **`*.zip` is not.** |
| Week 6 P9.2: fixtures are "allowed in Git" | Only true for plain-text fixtures; csv/pdf/xlsx fixtures are globally blocked. |

Why this is P0 and not trivia: week 1 has every student create `.venv` *inside the repo*, and the primary MCA download is literally "CSV per RoC, inside ZIP" (`09-resources.md`). One `git add .` from one student commits a 5,000-file, 100–300 MB virtual environment or a stack of government ZIPs. With 30 beginners over 10 weeks this is close to certain, and unwinding it from history requires admin surgery during the exact weeks nobody has slack. Week 1's checklist even says "no `.venv` anywhere in your commits" — the intent is right; the enforcement is missing.

A forward-looking variant of the same bug: `platform/dbt/dbt_project.yml` already configures `seed-paths: ["seeds"]`, and dbt seeds **are CSVs**. The first rotation that tries to commit a state-name mapping seed will find Git silently pretending not to see the file. The ignore rules need explicit allow-list exceptions before weeks 8–9 arrive.

### 1.4 "Provided by the program" is the only unpaid bill in the stack (P0)

`02-tools-setup.md` §8: Airflow is a "Provided environment; the program lead shares the URL," and Metabase is "Hosted by the program; you get a login." Every other tool in this sprint has a credible zero-cost story. These two do not, as of 2 Sep 2026:

- **Metabase Cloud** has no free plan — Starter is ~$100/month with a 14-day trial. The free path is the open-source edition, self-hosted (Docker image or JAR; modest RAM).
- **Astronomer (Astro)**, the natural "managed Airflow" answer, is usage-based from roughly $0.35/hour on its Developer plan — a trial, not a home.
- Free-tier PaaS options (Render, Fly, and friends) are too small for Airflow's scheduler + webserver + triggerer + worker set, and they spin down between requests.

None of this is fatal — running Airflow and Metabase as Docker containers on a machine the program already owns is genuinely free — but **nobody has been assigned this job**. It appears in no role in `06-team-roles.md`, no runbook, no admin guide in this repo. Week 10 (stations B6 and D9) depends on both environments in the final week, when there is zero slack left to procure, install, and debug them. An unowned, unpriced, deadline-critical dependency is a P0 regardless of how cheap the fix is.

### 1.5 Branch protection silently requires a public repo (P1)

GitHub's docs (verified 2 Sep 2026): "Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations." For **private** repositories, protection requires Pro/Team/Enterprise. CONTRIBUTING rule 3 — "nobody pushes straight to `main`; that branch is protected" — is therefore only true if `StartwithDot/Data-Sprint-1` is public, or someone pays.

Public visibility also happens to be what makes GitHub Actions free: unlimited standard-runner minutes for public repos, versus a metered monthly quota for private ones (~2,000 minutes/month on the Free plan, billed to the repository owner). This repo's three workflows, plus up to 30 student-created test workflows from week 6 P9.3, would drain a private repo's quota within weeks.

Two consequences to handle deliberately rather than accidentally:

- **Privacy.** A public repo publishes student names, emails, commit times, and work history. That is partly the point (the contribution graph), but say it out loud in week 0 and offer a professional-pseudonym option — any GitHub account's own graph shows merged commits, so the requirement survives a pseudonym.
- **Answer hygiene.** The answer keys already live in a separate private repository (`admin/README.md`) — good. Keep it that way; anything merged here is world-readable forever.

---

### 1.6 The data sources will fight the students (P1)

Live checks run during this audit (2 Sep 2026): the MCA CDM statistics page returned **HTTP 403** to a scripted request; a data.gov.in help page returned **403**; an ibbi.gov.in publications URL returned **404** (it has moved). Government portals in general, and mca.gov.in in particular, sit behind WAFs that tolerate browsers and reject `requests`. A human clicking around in week 1 will succeed; the week 5 P7.2 `requests` + Beautiful Soup extractor and the week 9 P12.1 snapshot prep may get 403'd with no code error to fix — the failure mode that frustrates beginners most, because the error is not theirs.

Compounding factors:

- **No offline fixtures.** Every task depends on live downloads. The one fixture pattern that exists (week 6 P9.2's "few lines of saved text") is the exception, not the rule.
- **PDF weight.** IBBI quarterly statistics PDFs run to hundreds of pages; `pdfplumber` table extraction on them is slow and memory-hungry on 8 GB laptops. Week 5's note "the PDF will not extract cleanly on the first attempt" is honest, but there is no fallback when the portal is down or the laptop chokes.
- **No mirror.** Nothing instructs the program lead to keep a known-good copy of every source file for the week it is needed.

### 1.7 Nothing is pinned, and the ground will move mid-sprint (P1)

There is no `requirements.txt`. Students install ad hoc (`02-tools-setup.md` §3 is one unpinned `pip install` line); CI installs unpinned `sqlfluff black flake8` and `dbt-snowflake`; CI runs Python 3.10 while the docs demand "3.11 or newer." Ten weeks is a long time to run unpinned:

- **dbt's docs site now defaults to the v2 (Fusion) release track**, which looks nothing like dbt Core 1.x. Students clicking through from `09-resources.md` will land in documentation for a product they are not using. They need to be told to switch the version selector to v1.
- **Airflow is at 3.3.x**; most books, courses, and half the internet still teach Airflow 2, whose installation and UI differ substantially.
- **Great Expectations is at 1.22** with an API completely different from 0.18 — and the 0.18 docs are still hosted, so search results mix eras freely. Week 9's `quality/expectations/mca_suite.json` framing hints at the 0.18-era filesystem workflow, which is not how GX Core 1.x works by default.
- **pydantic v1 vs v2** tutorials still circulate.
- **dbt's Python matrix** (verified 2 Sep 2026): Python 3.13 is supported only from dbt-core 1.11 onward, and 3.12 is the last universally safe version below that. "3.11 or newer" invites 3.13/3.14 installs that may or may not resolve depending on what pip picks that day.
- **Unpinned sqlfluff** ships new rules in minor releases. One upstream release mid-sprint and every pull request goes red for reasons no student caused.

### 1.8 Review bandwidth and merge-flow bottlenecks (P1)

- **Volume.** Roughly 25–30 students, each maintaining a continuously updated pull request per week, plus platform PRs from the rotation. `06-team-roles.md` assigns first-pass review to **one rotating student** who is also carrying that week's full task load, with core admins behind them. Expect multi-day merge latency precisely in weeks 3 and 8, when motivation matters most — the contribution-graph incentive makes students watch merge status like a stock ticker.
- **`docs/platform-rotation-log.md`** is a single shared table that rotation students append to — the classic conflict file. Frequency is low (2–4 rows a week), but each conflict lands on rotation newcomers inside the most visible file in the repo.
- **The 300-file template sync.** Every edit to a week template must be copied into all 30 `students/DEx/weekY/problem_statement.md` files. Mid-sprint template edits will also collide with any student PR that touched a problem statement they were told not to edit. The structure guarantees this toil; it should be scripted or generated, and template edits should be rare, announced, and timed to week boundaries.
- **Shared deliverable files.** `delivery/review_log.md`, `delivery/runbook.md`, and the root `README.md` (B8.2) are all single files that week 10 asks multiple students to write. Fine for a 2–4 person rotation, but the file-level coordination is unstated.

### 1.9 Windows and the hardware floor (P1)

Git Bash is prescribed (good), but: no `.gitattributes` exists, so Windows CRLF versus macOS LF will generate whole-file diff noise in shared files all sprint; PowerShell's execution policy blocks `.venv\Scripts\activate` for some students out of the box; and there is no stated hardware floor. 8 GB laptops will struggle to run VS Code + browser + Snowsight + `pdfplumber` on a 200-page PDF or a ~1 GB RoC CSV simultaneously (week 5's streaming lesson is the right medicine, but it arrives after the first freeze). Docker-based Airflow, if the local route is taken, wants ~4 GB of RAM by itself.

### 1.10 The handover milestone depends on five live systems at once (P1)

D10.1 — "clean checkout, fresh schema, only the runbook" — needs, simultaneously: a reachable GitHub repo, a **live Snowflake account** (finding 1.1), the **Airflow environment** (finding 1.4), **Metabase** (finding 1.4), and **all four government data sources** (finding 1.6). The sprint's self-declared "actual output" is thus its most failure-exposed deliverable: five independent single points of failure, three of them scheduled to be at their least reliable in week 10.

---

## 2. Free-tier compatibility matrix

All facts verified 2 Sep 2026. "Verdict" means *specifically over a 10-week cohort of 15–30 beginners on a zero budget* — a stricter test than "can one person try it for free."

| Tool / service | Free offering | Verdict over 10 weeks | What bites | Zero-cost workaround |
|---|---|---|---|---|
| Git | Free, local, forever | ✅ Safe | Nothing | — |
| GitHub accounts, forks, PRs | Free, unlimited | ✅ Safe | Nothing structural | — |
| GitHub Actions | Unlimited standard-runner minutes on **public** repos; metered quota (~2,000 min/mo) on private | ✅ Safe **if public** | A private repo would drain the quota in weeks; week 6 P9.3 multiplies workflows up to 30× | Keep the repo public; pin and cache pip installs; add `concurrency` with `cancel-in-progress` |
| Branch protection | Free plan: **public repos only** | ⚠️ Conditional | Silently absent on a private repo — the "protected branch" rule becomes a bluff | Public repo, or pay for Pro |
| Snowflake | 30-day trial, ~$400 credits, no credit card, **no permanent free tier** | ❌ **Breaks ~week 4–5** | The 30-day clock; one shared credit pool; single-warehouse queuing; CI and the handover are coupled to it | Planned second trial at week 7 (Fix 1); per-student trials for practice; educator outreach; DuckDB bridge for weeks 1–6 as last resort |
| dbt Core + dbt-snowflake | Open source, local, free | ✅ Safe | Version churn; docs site defaults to the v2 track; 3.13/3.14 Python edges | Pin in `requirements.txt`; "use the v1 docs" warning; Python 3.11–3.12 |
| Great Expectations (GX Core) | Open source, free | ✅ Safe (the tool) | 0.18 → 1.x API churn invalidates most tutorials; JSON-suite framing in week 9 is 0.18-era | Pin 1.x; teach only from the GX Core quickstart; provide a scaffold |
| Apache Airflow | Open source, free to self-host | ⚠️ **Hosting undefined** | "Provided environment" has no free managed tier; Astronomer is usage-based; Docker wants ~4 GB RAM | Local `airflow standalone` or Docker on a program-owned machine; document it and assign an owner (Fix 4) |
| Metabase | OSS free, unlimited users, self-hosted; Cloud Starter ~$100/mo with a 14-day trial only | ⚠️ **Hosting undefined** | No free cloud tier at all | Self-host OSS (Docker image or JAR) pointing at Snowflake |
| DBeaver Community | Free | ✅ Safe | — | — |
| VS Code + extensions | Free | ✅ Safe | — | — |
| Python stack (pandas, pydantic, requests, tenacity, pdfplumber, bs4, lxml, pytest, python-dotenv, snowflake-connector-python) | Free | ✅ Safe | Unpinned installs drift; 3.13/3.14 resolution edges; **tenacity is taught in week 4 but never appears in any install list** | Pinned `requirements.txt` (including tenacity); Python 3.11–3.12 |
| SQLFluff / flake8 / black | Free | ✅ Safe | New lint rules arrive in minor releases; black runs in CI but is taught nowhere | Pin all three; either teach black or remove it from CI |
| Discord + GitHub webhook | Free | ✅ Safe | — | — |
| data.gov.in (MCA master data) | Free downloads | ⚠️ Fragile | WAF 403s to scripts (observed this audit); large ZIPs; no SLA | Fixtures + instructor mirror + timeouts, retries, small pools |
| mca.gov.in CDM statistics | Free HTML tables | ⚠️ Fragile | HTTP 403 to scripts (observed this audit); periodic downtime | Same |
| ibbi.gov.in statistics | Free PDFs | ⚠️ Fragile | URL churn (a publications URL 404s today); very long PDFs | Fixtures; extract by page range; mirror |
| rbi.org.in data | Free CSVs | ✅ Most stable of the four | Rare downtime | Mirror anyway |

**Reading of the matrix:** the *software* is essentially all free — the risk concentrates in the *services*: one metered clock (Snowflake) and two unowned hosting promises (Airflow, Metabase). Those three rows are where the "100% free tier strategy" actually lives or dies.

---

## 3. Missing repository structure & files

Everything below is absent today (verified against the repo root and full file listing). Nothing here was created by this audit; these are descriptions for the program lead.

| Add this | What it is | Why it matters | Priority |
|---|---|---|---|
| `requirements.txt` | Pinned install list: the weeks 1–7 stack now, with commented week 8/9 sections for `dbt-snowflake` and `great-expectations` | Reproducibility across 30 machines and CI; today the install is ad hoc prose; **tenacity is assigned reading in week 4 but appears in no install list** | **P0** |
| `.gitignore` additions | `.venv/`, `venv/`, `*.zip`, `*.tar.gz`, plus allow-lists `!platform/dbt/seeds/**/*.csv` and `!test-fixtures/**` | Makes the documented promises true; prevents the virtualenv/ZIP catastrophe; unblocks dbt seeds and fixtures in weeks 6–9 | **P0** |
| `platform/dbt/profiles.yml` | A committed *template* that reads `env_var('DBT_SNOWFLAKE_ACCOUNT')` and friends, with no real values | Without it, `dbt parse`, `dbt build`, CI, and the sqlfluff dbt templater cannot run anywhere — for the rotation or for GitHub | **P0** |
| CI workflow corrections | `--project-dir platform/dbt --profiles-dir platform/dbt`; install dbt in the lint job (or set `templater = jinja`); pin sqlfluff/black/flake8; `python-version: '3.11'`; a `concurrency` block with `cancel-in-progress`; `workflow_dispatch` on dbt-build; harmless default env values for parse | Turns three always-red workflows into the teaching tool they are meant to be (details in Fix 2) | **P0** |
| Week 6 P9.3 redesign | One instructor-owned workflow that discovers and runs student tests under `students/**`, instead of 30 root-level CI files | Prevents workflow filename collisions and 30× CI multiplication | **P0** |
| `.env.example` | The seven `SNOWFLAKE_*` variable names from `02-tools-setup.md` §5 | Standard practice; prevents typos and "which variables?" questions; doubles as documentation | P1 |
| `.gitattributes` | `* text=auto` plus binary hints | Stops CRLF/LF whole-file diff noise between Windows and macOS students | P1 |
| `test-fixtures/` | Tiny sanitized HTML / PDF / CSV samples of each of the four sources, with the allow-list above | Week 5 and week 9 survive portal outages and 403s; enables offline tests | P1 |
| Starter/seed data plan | Instructor-provided: a prior-month MCA snapshot, a pre-extracted IBBI sample CSV, and a small already-loaded RoC table | Weeks 2–3 query "your loaded data," two monthly snapshots, and insolvency fields that per the curriculum's own timeline do not exist until weeks 3 and 5 (see §4) | P1 |
| `.github/PULL_REQUEST_TEMPLATE.md` | Task IDs, own-folder check, no-data/no-secrets checklist | Encodes the CONTRIBUTING rules where students actually look | P1 |
| `CODEOWNERS` | `platform/` and `delivery/` → core admins | Auto-routes shared-zone reviews; makes the branch-protection review requirement meaningful | P1 |
| `scripts/verify_setup.py` | One command checking git identity, Python version, venv, imports, `.env` keys, remotes | Converts the week 1 checklist into self-service pass/fail; saves hours of Discord triage | P1 |
| `platform/README.md` + a path decision | Reconcile the `quality/` and `airflow/` paths referenced by weeks 9–10 with the existing `platform/quality/` and `platform/orchestration/` | Week 9 and 10 commit paths point at directories that do not exist at the repo root | P2 |
| `LICENSE` | MIT (or a deliberate choice) | A public repo without a license is all-rights-reserved by default; students' code deserves clarity | P2 |
| `.editorconfig` | Consistent indentation and newlines across editors | Reduces diff noise and lint churn | P2 |
| `docker-compose.yml` (Airflow) + Metabase run notes | Only if the self-hosted route is chosen for week 10 | The "provided environment" needs a reproducible definition | P2 (P1 if that route is chosen) |
| `.pre-commit-config.yaml` | Optional local hooks (trailing whitespace, sqlfluff) | Catches lint errors before CI does | P2 |

Also missing but belonging to the **admin repository** rather than this one: a Snowflake resource-monitor alerting plan, the mid-sprint trial-migration runbook, GitHub secrets rotation steps, the Airflow/Metabase hosting runbook, and the Discord webhook setup (already referenced by `06-team-roles.md` as `guide/infrastructure-setup.md` — confirm it exists).

---

## 4. Week-by-week curriculum stress-test

Task and milestone counts below are counted directly from the week templates in `docs/_week-templates/`.

| Week | Tasks | Milestones | Brand-new tools | Load verdict |
|---|---|---|---|---|
| 1 | 10 | 1 (B1) | Git, GitHub, Python + venv, VS Code, Snowflake, forks/PRs — **six environments in one week** | Very heavy — but the weight is setup, not tasks |
| 2 | 11 | — | pydantic | Heavy **plus a data-availability gap** (below) |
| 3 | 12 | 1 (P3) | Stages, file formats, COPY INTO | Heavy but coherent |
| 4 | 12 | 1 (S7) | — (tenacity appears in the reading column) | Heavy |
| 5 | 10 | — | Generators, `logging`, `argparse`, OOP/ABCs, pdfplumber, Beautiful Soup | Heavy — five new concepts in one week |
| 6 | 8 | 1 (P8) | pytest, CI (currently broken — see 1.2 D) | **Lightest week — usable as a shock absorber** |
| 7 | 7 | 1 (S10) | Snowflake Python connector, thread pools | Moderate-heavy |
| 8 | 11 | 2 (D1, D4) | **dbt**, plus the process switch into `platform/` and CI gates | **Steepest cliff in the sprint** |
| 9 | 10 | 1 (P12) | Great Expectations | Heavy — two frameworks plus the hardest logic |
| 10 | 14 | 2 (B8, D10) | **Airflow + Metabase**, plus break/fix, presentation, handover | Overloaded as a single week |

### Week 1 — setup is a hidden seventh station

`02-tools-setup.md` opens with "budget two hours." For an absolute beginner on Windows the realistic range is four to eight (PATH checkboxes, token vs SSH choice, venv activation, Snowflake password change), and the week *also* carries 10 tasks and a milestone. **Adjustment:** run a "day 0" setup session before week 1, make `scripts/verify_setup.py` the exit ticket, and pair confident students with new ones for the first session.

### Weeks 2–3 — tasks reference data that does not exist yet

This is a sequencing flaw, not a workload flaw. S2.1 asks "how many [NULL CINs] did you find in your loaded data?" — but the first load milestone is week 3's P3, and the week 1 table is created empty. S3.3/S3.4 join IBBI insolvency rows to the MCA registry — but IBBI extraction is week 5 (P7.1). S3.5 and S4.3 compare "two monthly snapshots," which cannot exist two to three weeks into a 10-week program. The S5.4 recovery-rate task also needs insolvency amounts that arrive in week 5. **Adjustment:** provide a starter pack in week 1 — one small RoC CSV loaded during the week 1 Snowflake session, a pre-extracted IBBI sample CSV, and a prior-month MCA snapshot — and document where it lives; or move the affected tasks to the weeks where their data exists.

### Week 3 — heavy, but heavy in the right direction

Twelve tasks and one milestone, all pulling toward the P3 reconciliation discipline that everything later depends on. Keep it; just fix the data availability above or the reconciliation numbers are fiction.

### Week 5 — five new Python concepts in one week

Generators, logging, CLI tools, OOP with abstract base classes, and two new parsing libraries, for an audience that met type hints three weeks earlier. The template's own cut list implicitly admits the overload. **Adjustment:** move P7.3 (the ABC refactor) into week 6, and let week 6's pytest station test the extractors — the natural pairing that week 6 currently lacks.

### Week 6 — the lightest week; use it

Eight tasks, no heavy new tools. This is the natural place to absorb P7.3, and — once P9.3's CI task is redesigned — to pre-seed week 8 with a stretch task: install dbt, `dbt init`, run one toy model. Meeting dbt in week 6 halves the week 8 cliff.

### Week 7 → 8 — the steepest cliff

Week 8 adds dbt (Jinja, `ref()`, sources, tests, materializations, profiles.yml), the move into the shared `platform/` zone, CI gates (broken today — see 1.2), two milestones, and 11 tasks, immediately after week 7's own SCD2 milestone. **Adjustments:** pre-seed `platform/dbt/` with a working skeleton (sources declared, one finished staging model as the pattern, the rest as fill-in-the-blank); move D1 (the technical brief) into week 7's business-track slack; allow D5 to land mid-week-9 if needed.

### Week 9 — two frameworks plus the sprint's hardest logic

SCD2 *in dbt* and Great Expectations in the same week, with GX's 1.x API churn guaranteeing that half of every web search result is from the wrong era. **Adjustments:** pin the GX version and teach strictly from the GX Core quickstart (already the correct link in `09-resources.md`); pre-write the GX scaffold so students write expectations, not plumbing; state explicitly that 0.18-era `great_expectations.yml` / JSON-suite tutorials do not apply.

### Week 10 — two new tools, two milestones, and a client presentation

Fourteen tasks. Airflow and Metabase both land here for the first time, B5 depends on program leads injecting a failure, and B7/B8 are presentation and handover. **Adjustments:** move B6 (the Metabase dashboard) to week 9, where the gold tables it reads already exist; make D9.1's DAG *authoring* (file plus dependency sketch) a week 9 reading-and-sketch exercise so week 10 is about running, breaking, and handing over; and split the cut list into an explicit "minimum viable handover" tier versus "full delivery" — the current cut order already gestures at this.

---

## 5. Actionable fixes & resolution recommendations

Ordered by what unblocks the most, soonest. Each item is a *description* of the change for the program lead to make — nothing here has been applied.

### Fix 1 (P0) — decide the Snowflake account strategy now

Recommended: the **two-trial plan with a scripted reload.**

1. Weeks 1–7 run on trial account A, as today, but with guardrails: a resource monitor alerting at 50 / 80 / 100% of credits, XS warehouses only, 60-second auto-suspend, and the `LIMIT`-while-exploring rule already in `02-tools-setup.md`.
2. On the weekend of week 7, the program lead opens trial account B (a new email), recreates the users, `STUDENT_ROLE`, `STUDENT_WH`, the database, and the CI user.
3. Week 8's bronze loads — already rehearsed twice by then (P3 and D3) — reload into account B. Frame it explicitly in the week 8 file: *the warehouse is disposable; the repository is the source of truth.* That is a genuinely valuable data-engineering lesson disguised as disaster recovery.
4. Rotate the six GitHub secrets and each student's `SNOWFLAKE_ACCOUNT` value in `.env` (one variable). Write the procedure into the admin repo as the "mid-sprint migration runbook."
5. Alternative worth considering: per-student trial accounts for practice (own clock, own credits, no cross-talk) with one stable shared account reserved for `platform/` and CI. Cost: 30 signups to shepherd and more account-identifier confusion.
6. Last resort if trials cannot be secured at all: run weeks 1–6 SQL practice on DuckDB via DBeaver (free, permanent, no server) with a one-page dialect-differences note, and activate Snowflake in week 7. This changes the tool story, so prefer options 1–5 first.
7. In parallel, email Snowflake sales/education about academic terms. One email; sometimes yes.

### Fix 2 (P0) — repair CI before week 8, and dry-run it in week 2

1. Commit `platform/dbt/profiles.yml` referencing `env_var('DBT_SNOWFLAKE_*')` — template only, no real values (values come from local `.env` or GitHub secrets).
2. `dbt-check.yml`: `dbt parse --project-dir platform/dbt --profiles-dir platform/dbt`, with harmless default values for the env vars set in the workflow's `env:` block so profile resolution can never be the failure.
3. `dbt-build.yml`: the same directory flags; add a `concurrency` group with `cancel-in-progress: true`; add `workflow_dispatch` so credit-burning full builds are deliberate; keep secrets as the only source of real values.
4. `lint.yml`: either install `dbt-snowflake` in the lint job, or change `.sqlfluff` to `templater = jinja` (simpler for beginners, marginally less accurate linting); pin `sqlfluff`, `black`, and `flake8`; set `python-version: '3.11'`; decide black's fate — if it stays in CI, install it locally in `02-tools-setup.md` and explain it in `11-tools-and-technology.md`.
5. Redesign week 6 P9.3: replace "commit the CI configuration file at the repository root" with one instructor-owned workflow that discovers and runs student tests under `students/**` (or runs pytest path-filtered to the PR's changed files). One file, no collisions, no 30× multiplication.
6. Dry-run all three workflows on a scratch pull request in week 2 — when the rotation is small and the stakes are low, not in week 8.

### Fix 3 (P0) — make `.gitignore` match its own documentation

1. Add `.venv/`, `venv/`, `*.zip`, `*.tar.gz`.
2. Add the forward-looking allow-lists: `!platform/dbt/seeds/**/*.csv` and `!test-fixtures/**`.
3. Re-run `git check-ignore .venv` after the change and note the verification in the setup doc, so the doc's claim is true again.
4. Add a short "I already committed my `.venv` / a ZIP" recovery entry to `10-troubleshooting.md` (it already covers the secrets case; the data case is the common one).

### Fix 4 (P0) — assign and define the Airflow + Metabase hosting

1. Decide the route: program-machine Docker (recommended), per-student local, or demo-only-hosted.
2. Replace "Provided environment / hosted by the program" in `02-tools-setup.md` §8 with the actual mechanism: a URL, an owner, a restart procedure, and what students may and may not touch.
3. Name the owner in `06-team-roles.md` — a core admin; rotating students must not own production-shaped infrastructure.
4. If self-hosting: one `docker-compose.yml` (Airflow wants ~4 GB RAM; Metabase is modest), credentials via `.env`, and a five-line healthcheck in the runbook.

---

### Fix 5 (P1) — pin everything that moves

1. Create `requirements.txt` — including `tenacity`, which week 4 teaches but nobody installs — and have CI install from it. Version bumps become deliberate admin pull requests.
2. Pin Python to 3.11 or 3.12 in the docs *and* CI, per dbt's own compatibility matrix.
3. Add one warning box to `09-resources.md`: "dbt docs — switch the version selector to v1; Great Expectations — use only the GX Core (1.x) pages; Airflow — we use Airflow 3."

### Fix 6 (P1) — visibility, protection, and people

1. Confirm the repo is public; configure branch protection exactly as `07-platform-and-cicd-guide.md` describes; add CODEOWNERS.
2. Week 0 message: the repo is public; real names are a choice and pseudonyms are fine; contribution graphs work either way once PRs merge.
3. Review relief: make the "review at least one teammate's PR" checklist item a *formal approval* from week 1 (peer pairings), give the review lead a 48-hour merge SLA on practice PRs, and keep admin approval for `platform/` and `delivery/` only.
4. Split `docs/platform-rotation-log.md` into per-week files, or make it strictly append-only with a "never edit another row" rule, to defuse the shared-file conflict.

### Fix 7 (P1) — data resilience

1. Build `test-fixtures/` now: one small sanitized sample per source (HTML, PDF, CSV), with the `.gitignore` allow-list from Fix 3.
2. Keep an instructor mirror of each week's known-good source files (shared drive or pinned Discord message), refreshed weekly.
3. Require polite scraping in the extractor stations: realistic `User-Agent`, timeouts, tenacity backoff, small thread pools — week 7 P10.1 already says this; make it a checklist item in P7 too.
4. Say plainly in week 5: "if the portal blocks you today, use the fixture and note it — that is the professional response to an unreliable source, not a failure."

### Fix 8 (P1) — pacing adjustments (summary of §4)

- Week 0: setup session + `scripts/verify_setup.py` as the exit ticket.
- Weeks 1–2: instructor starter data (a loaded RoC table, a pre-extracted IBBI sample, a prior-month snapshot).
- Week 5 → 6: move P7.3 (ABC refactor) into week 6.
- Week 6: stretch task — install dbt, `dbt init`, one toy model (after the P9.3 fix).
- Week 7: absorb D1 (technical brief) from week 8.
- Week 8: dbt skeleton pre-seeded in `platform/dbt/`; D5 may slip to mid-week 9.
- Week 9: absorb B6 (Metabase) from week 10; D9.1 DAG sketch as reading; GX scaffold provided.
- Week 10: two-tier cut list — "minimum viable handover" versus "full delivery."

### Fix 9 (P2) — hygiene

LICENSE (MIT or a deliberate choice), `.editorconfig`, `.gitattributes`, the pull request template, optional pre-commit hooks, and generating `docs/05-task-list.md` from the week templates (or vice versa) so the 300-file student sync and the task list can never drift apart.

---

## Appendix A — what is already strong (do not change these)

- **Fork + own-folder isolation** is the right collaboration model for beginners: conflicts are structurally rare, and the practice-versus-platform two-zone split teaches the difference between rehearsal and production.
- The **no-squash merge policy** is correctly reasoned for contribution-graph attribution.
- **Milestones as cohort-wide gates**, per-week cut lists, and "say it out loud" review questions are unusually good pedagogy.
- `10-troubleshooting.md` anticipates the real errors beginners hit (auth, rebase, COPY INTO reconciliation, dbt profiles, silently-broken DAG imports).
- `09-resources.md` naming exact reading per station, plus the SQL Server → Snowflake difference table, prevents a whole class of confusion.
- Banning AI-generated deliverables while allowing AI for error explanation is the right line for a learning program.
- Week 7's "run the MERGE on a test copy first" and the three SCD2 correctness checks are exactly how professionals think about idempotence.

The audit above is about making the operational scaffolding as good as the pedagogy.

## Appendix B — research sources (all verified 2 September 2026)

- **GitHub Docs** — "About billing for GitHub Actions": public repos free on standard runners; private repos metered; Linux 2-core runner ≈ $0.006/min.
- **GitHub Docs** — "About protected branches": "Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations."
- **GitHub Docs** — "GitHub's plans": Actions usage free for public repos and self-hosted runners; private quota per plan.
- **Snowflake Docs** — "Overview of warehouses": X-Small = 1 credit/hour (Gen1); XS is the default warehouse size for `CREATE WAREHOUSE` and Snowsight.
- **Snowflake trial terms** — 30 days / $400 usage, no credit card, no permanent free tier, read-only grace period then account deletion: Snowflake's standard published trial terms; re-verify on the signup page the week an account is created.
- **dbt Docs** — Python compatibility matrix: current dbt-core 1.12; Python 3.13 supported from 1.11 (adapter-dependent); 3.12 the safe ceiling below that; docs site now defaults to the v2 (Fusion) release track.
- **Airflow Docs v3.3.1** — "Running Airflow in Docker" (multi-container compose stack, memory-hungry) and "Installation from PyPI" (constraints files required for reproducible pip installs).
- **Great Expectations Docs** — current version 1.22.0 with legacy 0.18.21 still hosted; GX Core is a pure Python library with a new API.
- **Metabase pricing page** — Open Source plan free with unlimited users (self-hosted); Cloud Starter ≈ $100/month with a 14-day trial; no free cloud tier.
- **Astronomer pricing page** — Astro Developer plan "try for free," deployments starting ≈ $0.35/hour; no permanent free tier.
- **Live probes during this audit** — mca.gov.in CDM statistics page → HTTP 403; data.gov.in help page → HTTP 403; ibbi.gov.in publications URL → HTTP 404.

## Appendix C — assumptions and limits of this audit

- The repository is assumed to be (or become) public at `github.com/StartwithDot/Data-Sprint-1`. If it is private, finding 1.5 escalates from conditional to immediate.
- Cohort size 15–30, per `07-platform-and-cicd-guide.md`; pull request volume estimates scale with that assumption.
- The Airflow/Metabase hosting plan was not discoverable from this repository; it is treated as undefined, which is itself the finding.
- CI workflow behavior (dbt's project-dir resolution, sqlfluff's dbt-templater requirements, profiles resolution) is assessed from tool documentation and static reading of the workflow files — no workflows were executed and nothing was modified during this audit.
- Free-tier terms are current as of 2 September 2026 and drift; re-verify Snowflake, Astronomer, and Metabase terms in the week each becomes load-bearing.
- Task counts are counted from `docs/_week-templates/week1.md` through `week10.md`, which at audit time were identical to all 300 student `problem_statement.md` files.
- This audit deliberately did not evaluate the *content difficulty* of the teaching material (whether Kudvenkat is the best SQL spine, whether the Kimball reading is right-sized) — only its operational and free-tier viability. The pedagogy questions deserve their own review by the curriculum owner.









