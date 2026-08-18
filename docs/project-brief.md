# DOTSET Project 1: Project Brief
## India Company Risk and Verification Data Platform

---

## 1. The client and the business need

Our client is a fintech due diligence company. Due diligence means checking a business before trusting it. Their customers are lenders, banks, and procurement teams. Before a customer lends money to a company, or buys from a company, or signs a contract with a company, they want to know three things.

First, is this company really registered and still active. Second, has this company ever been in financial trouble, like bankruptcy proceedings. Third, how does this company compare to others in its state and industry.

Today the client checks these things by hand. An analyst visits the Ministry of Corporate Affairs website. The analyst searches for one company at a time. The analyst checks the Insolvency and Bankruptcy Board website separately. The analyst copies numbers into a spreadsheet. This is slow. It does not scale. When two analysts check the same company on different days, they can get different answers, because the source data keeps changing.

The client is asking for one reliable data platform. They want every registered company in India in one place. They want insolvency events attached to the right companies. They want state level context attached. They want the history kept, so they can answer not just "what is this company's status today" but "what was this company's status three months ago". They want the whole thing to refresh on a regular schedule. And they want a dashboard at the end that a non technical person can use.

Our cohort plays the role of the data engineering team hired to build this.

---

## 2. The data we will use

We use four real public data sources. All four are published by Indian government bodies. All four are free.

### 2.1 MCA Company Master Data

**What it is.** The Ministry of Corporate Affairs, called MCA, is the government body that registers every company in India. Every company gets a 21 character identification number called a CIN, which stands for Corporate Identity Number. The MCA publishes a master list of all registered companies on data.gov.in, India's open government data platform.

**What is in it.** For each company: the CIN, the company name, the registration date, the current status (Active, Strike Off, Under Liquidation, Dormant, and others), the company class and category, the authorized capital, the paid up capital, the registered state, the Registrar of Companies office, the main business activity, and the registered office address.

**Why it matters to the client.** This is the core of the platform. It answers the first question: is this company real and what is its status. The registry holds roughly 31 lakh companies in total, of which roughly 20 lakh are active.

**How it arrives.** As roughly 20 to 25 separate ZIP files. Each ZIP covers one Registrar of Companies office, called an RoC. Inside each ZIP is one CSV file. CSV means comma separated values, a plain text table format. The files arrive with messy details: state names written differently across files, dates in different formats, capital amounts with commas and currency symbols mixed in. Each update is a full fresh snapshot of the whole registry, published roughly monthly.

**How to get it, step by step.**

1. Open a browser and go to data.gov.in.
2. Search for "Company Master Data" in the dataset search box.
3. Open the catalog page for the Company Master Data dataset from the Ministry of Corporate Affairs.
4. You will see a list of downloadable files, one per RoC region.
5. Download each ZIP file into a folder on your computer named `data/raw/mca/`.
6. Unzip each file. Keep the original ZIPs too.
7. Write down the date you downloaded them in a notes file. This matters because the data is a snapshot, and you must always know which snapshot you are holding.

### 2.2 IBBI Insolvency Records

**What it is.** The Insolvency and Bankruptcy Board of India, called IBBI, is the government body that oversees bankruptcy proceedings. When a company cannot pay its debts, it can enter a legal process called the Corporate Insolvency Resolution Process, called CIRP. The IBBI publishes lists of companies going through this process.

**What is in it.** For each case: the CIN of the company, the company name, which court bench is handling it, the date the process started, the date of the court order, and financial details like the total claims admitted and the amounts recovered.

**Why it matters to the client.** This answers the second question: has this company been in serious financial trouble. A company in insolvency proceedings is a high risk company to lend to. This is the most important risk signal in the whole platform. Because each row carries a CIN, we can attach each insolvency event to the right company in the MCA registry.

**How it arrives.** As PDF files on the IBBI website, published roughly every quarter. A PDF is a document format made for reading, not for data work. The table of companies is inside the PDF as text laid out like a printed page. There is no CSV download and no download API. We must write a small Python program to read the PDF and pull the table out into a CSV file.

**How to get it, step by step.**

1. Open a browser and go to ibbi.gov.in.
2. Look for the publications or "What's New" section of the site.
3. Find the most recent publication listing companies under the Corporate Insolvency Resolution Process.
4. Download the PDF file into a folder named `data/raw/ibbi/`.
5. Record the publication date and the exact file name in your notes file.
6. Do not try to edit or convert the PDF by hand. The extraction will be done later by a Python script, so the process is repeatable.

### 2.3 MCA Corporate Data Management Portal

**What it is.** The MCA runs a public analytics portal at mcacdm.nic.in. It shows summary statistics about companies in India: how many active companies each state has, how company counts are split across industries, how capital is distributed, and filing trends over the years.

**What is in it.** Tables and charts on web pages. For example, a table with one row per state showing the number of active companies in that state.

**Why it matters to the client.** This answers the third question: how does this company compare to its surroundings. Knowing that a company is registered in Kerala is more useful when you also know how many active companies Kerala has and which industries dominate there. It gives every company record an economic backdrop.

**How it arrives.** As HTML tables on web pages. HTML is the language web pages are written in. There is no download button and no data file. We must write a small Python program that reads the web page and pulls the numbers out of the tables.

**How to get it, step by step.**

1. Open a browser and go to mcacdm.nic.in.
2. Look at the state wise distribution table and the activity wise tables on the page.
3. Note which tables you need and what columns they have.
4. Do not copy the numbers by hand into a spreadsheet. The extraction will be done later by a Python script that reads the page directly, so the process can be repeated when the portal updates.
5. Record the date you viewed the portal in your notes file.

### 2.4 RBI Policy Rate Data

**What it is.** The Reserve Bank of India, called RBI, is India's central bank. It sets the repo rate, which is the interest rate at which it lends to banks. This rate shapes borrowing costs across the whole economy. The RBI publishes its data through a portal called the Database on the Indian Economy, called DBIE, at dbie.rbi.org.in.

**What is in it.** Time series data. A time series is a list of values over time. Here it is the policy interest rates with the dates each rate took effect.

**Why it matters to the client.** This is light background context only. It lets the platform answer questions like "what was the repo rate when this company was incorporated". It is not company level data, so we use it as supporting context, not as a core part of the risk model.

**How it arrives.** As downloadable Excel or CSV files from the DBIE portal. The files need light cleaning: merged cells in Excel, percentage symbols attached to numbers, and dates in Indian formats.

**How to get it, step by step.**

1. Open a browser and go to dbie.rbi.org.in.
2. Navigate to the statistics section and find the key policy rates series.
3. Download the file in CSV format if offered, otherwise Excel format.
4. Save it into a folder named `data/raw/rbi/`.
5. Record the download date and the exact series name in your notes file.

### 2.5 An honest note on what these sources feel like

None of these four sources arrives as one clean file. This is normal. Real company data lakes look like this too. Files arrive from different publishers, at different times, in different formats, with different naming habits. Learning to handle exactly this mess, in a controlled and repeatable way, is the main skill this project teaches.

---

## 3. The plan of action

The project follows a published learning roadmap with four parallel tracks: SQL and Data Modeling, Python, Data Platform, and Business and Delivery. Each track is a sequence of stations. Some stations are milestones, which are points where the whole group must reach before anyone moves on. Here is the plan, station by station, always with the business reason first.

**Before anything else, we need a Discovery Brief.** This is a milestone. The client gave us a short, slightly vague request, the way real clients do. We must write back a one page brief that says what we are building, what questions are still open, and what "done" looks like. We do this first because building the wrong thing perfectly is the most expensive mistake in data work.

**Next we need to understand databases and tables, because** the final product lives in a database. The client's questions, like "which companies are active in Kerala", are answered by querying tables. If we do not know what a database, a schema, and a table are, nothing else can start.

**Next we need constraints and data integrity, because** the client must be able to trust the data. A company record without a CIN is useless. We need to know which rules the database enforces and which rules we must enforce ourselves.

**Next we need SELECT, GROUP BY, and joins, because** the client's real questions combine tables. "How many active companies does each state have" needs grouping. "Which companies in the insolvency list also appear in the registry" needs a join on CIN. These three SQL skills answer most of the client's everyday questions.

**Next we need NULL handling and set operations, because** real registry data has missing values. A missing capital value must stay missing. Turning it into zero would lie to the client. Set operations let us answer questions like "which companies were active last month but not this month", which is exactly how struck off companies are detected.

**Next we need string, date, and math functions, because** the raw data is messy. State names are written in different ways. Dates arrive in different formats. Recovery rates in the insolvency data must be computed from claim and recovery amounts. These functions are the cleaning tools.

**Next we need views and CTEs, because** our queries are getting long. A CTE, which means common table expression, lets us build a query in readable steps. Readable steps are easier to check and easier to hand over.

**Next we need Python basics, files, and functions, because** three of our four sources cannot be loaded by hand. The IBBI data is inside a PDF. The MCA portal data is inside a web page. The RBI file has merged cells. Only code can extract these repeatably.

**Next we need type hints and data validation, because** extracted data must be checked before it enters the platform. If the PDF reader produces garbage on one page, we want a loud error at extraction time, not a silent wrong number in the client's dashboard three weeks later.

**Then we reach the First Snowflake Load milestone.** Every track meets here. The MCA registry files land in Snowflake for the first time. Snowflake is the cloud database where the whole platform lives. This is the moment the project stops being theory and starts being real.

**Next we need Snowflake fundamentals and stages, because** files must land somewhere before they can be loaded into tables. A stage is Snowflake's holding area for files. Understanding stages is what makes the first load possible instead of magical.

**Next we need the raw layer load for all sources, because** the client needs all four sources in one place, not just the registry. Every source lands exactly as it arrived, before any cleaning. Keeping an untouched raw copy is how we prove later that we never invented or lost data.

**Next we need retry logic and context managers in Python, because** government websites fail. Downloads stop halfway. Pages time out. A retry wrapper tries again instead of crashing. A context manager closes files and connections safely even when something fails. Without these, the pipeline breaks every few runs and nobody knows why.

**Next we need generators and large file handling, because** some registry files are large. A generator processes a file one line at a time instead of loading the whole file into memory. This is how we inspect big files on ordinary laptops.

**Next we need dbt staging models, because** raw data must be cleaned before anyone uses it. dbt is the tool that organizes our cleaning SQL into tested, documented, reviewable steps. Staging models are the first cleaning layer: correct types, clean state names, parsed dates.

**Next we need logging and CLI tools, because** the pipeline will soon run on a schedule. When a scheduled run fails at night, the logs are the only witness. And scripts must accept arguments like which month to load, so the same script works for every month without being edited.

**Next we need OOP and custom extractors, because** we now have three working extraction scripts that look very similar. Object oriented programming lets us write the shared pattern once and reuse it. This is the moment the scripts become a small, maintainable system instead of three copies.

**Then we reach the Star Schema Design milestone.** Every track meets here. Before building the final layer, the whole group agrees on the design: which tables are facts, which are dimensions, and what grain each one has. Grain means exactly what one row represents. Getting the grain right is the single most important modeling decision in the project.

**Next we need normalization and star schema knowledge, because** we must explain why the final design looks the way it does. The raw layer is intentionally unnormalized. The final layer is intentionally denormalized into a star. Knowing why both choices are correct is what separates a data engineer from someone copying patterns.

**Next we need the Medallion plus Kimball design step, because** we must turn the agreed design into a real plan: bronze for raw data, silver for cleaned data, gold for the business ready star schema. These terms are explained in section 4 below.

**Next we need dbt marts for the gold layer and SCD2, because** this is where the client's core requirement lives. SCD2, explained in section 4, is the technique that remembers what a company's status was at any point in the past.

**Next we need window functions and MERGE, because** SCD2 is built with them. Window functions compare this month's snapshot to last month's. MERGE applies the changes: update what changed, insert what is new, close what expired. These are the two most advanced SQL skills in the project, and they arrive exactly when the build needs them.

**Next we need testing with pytest, because** Python code that extracts client facing data must be tested. A test is a small piece of code that checks another piece of code. Tests run automatically on every change, so mistakes are caught before review, not after the client sees them.

**Next we need Great Expectations, because** the client asked for a platform they can trust. Great Expectations is a tool that checks data against written rules, like "every CIN must be 21 characters" or "every company in the insolvency fact must exist in the registry". These checks run automatically on every pipeline run. Trust is not a feeling. Trust is a test suite.

**Next we need concurrency and parallel downloads, because** downloading 20 plus registry files one by one is slow. Doing it in parallel is fast. We learn this late on purpose, after the slow correct version already works, so speed never comes at the cost of correctness.

**Next we need the Snowflake Python connector and Airflow orchestration, because** the whole pipeline must run on a schedule without human clicks. The connector lets Python talk to Snowflake. Airflow is the scheduler that runs every step in the right order and records what happened.

**Next we need the Break and Fix step, because** real pipelines break. At this point the program leads will deliberately break something in the data, the way a real source system would. We must find what broke, fix it, and write a short postmortem: what happened, why, and what would prevent it next time.

**Next we need the Metabase dashboard, because** the client is not a data engineer. Metabase turns the gold tables into charts and filters a business person can use directly: company status by state, insolvency events over time, capital distributions.

**Then Stakeholder Delivery.** We present the platform to the client in business language. Not "here are our dbt models" but "here is what this tells you about the companies you check, and here is what you should do with it".

**Finally, the Project Handover milestone.** The client gets the dashboard, the pipeline, the documentation, and the runbook. Everything is in the shared repository, reviewed, tested, and explained. The project is done when someone else could maintain it without us.

---

## 4. The modeling decision, in plain language

The client needs one thing more than anything else: reliable history. A company that is Active today may have been Under Liquidation four months ago. A due diligence check that only knows today's status is dangerous, because a company can look healthy today right after emerging from serious trouble.

To serve that need, the project uses two design choices that work together.

**Choice one: Medallion architecture.** This is a way of organizing the pipeline in three layers. The bronze layer holds the data exactly as it arrived, untouched. The silver layer holds cleaned and standardized data: correct types, consistent state names, parsed dates, validated CINs. The gold layer holds the business ready tables that the dashboard and the analysts actually use. This layering means we can always retrace our steps. If a number in the gold layer looks wrong, we can check it against silver, and silver against bronze, all the way back to the file the government published.

**Choice two: Kimball star schema.** This is a way of designing the gold layer's tables. There are fact tables, which hold events and measurements, and dimension tables, which hold the things those events are about. In our project, the main fact table holds insolvency events: one row per company per insolvency case, with dates and amounts. The main dimension table is dim_company: one row per company per version of that company, holding its name, status, capital, address, state, and business activity.

Inside dim_company we use a technique called SCD Type 2. SCD means slowly changing dimension. Type 2 means: when a tracked value changes, we do not overwrite the old row. We close it with an end date and open a new row with a start date. So the table can answer both "what is this company's status now" and "what was it on any past date". We track status, capital, and address this way, because those genuinely change in the monthly registry snapshots, and the client needs the history. We do not track the company name or registration date this way, because those do not change.

We deliberately do not use a more complex modeling approach called Data Vault. Data Vault is designed for very large organizations with many changing source systems. Our project has four stable sources and one clear history requirement. The simpler design does the job, and the simpler design is the one beginners can reason about.

---

## 5. The technology stack, in plain language

**Snowflake.** This is the cloud database where all the data lives and all the heavy computing happens. We chose it because the cohort already learned SQL on Snowflake during the foundation month, and because it handles large files well without any server setup.

**dbt.** This is the tool that organizes all the transformation SQL, the cleaning and reshaping steps between bronze and gold. It keeps every step in version control, runs tests on the data, and draws a map of how every table was built. We chose it because it makes review and teamwork possible: every change is a pull request a teammate reads before it merges.

**Python.** This is the programming language we use for the three messy sources: reading the IBBI PDF, reading the MCA portal web pages, and cleaning the RBI files. We chose it because these jobs cannot be done in SQL, and Python has the best libraries for them.

**Git and GitHub.** Git tracks every change to every file. GitHub hosts the shared repository where the team's work comes together. Every task in this project ends in a commit or a pull request. This is how we build review habits and a visible work history from day one.

**Apache Airflow.** This is the scheduler. Once the pipeline works by hand, Airflow runs it on a calendar: check for the new monthly registry snapshot, run the extractors, run the dbt build, run the quality checks. We chose it because it is the most widely used orchestrator in industry, so it is the most useful first one to learn.

**Great Expectations.** This is the data quality tool. It checks the loaded data against written rules before the data is allowed into the gold layer. We chose it because the client's core demand is trust, and trust needs automated proof, not promises.

**Metabase.** This is the dashboard tool. It connects to Snowflake and lets us build charts and filters that non technical people can use. We chose it because it is free, open source, and simple enough to learn in days.

---

## 6. What the client gets at the end

The final deliverable has three parts.

First, a working data pipeline. It refreshes the registry monthly, the insolvency data quarterly, and the context sources on their own schedules. Every run is logged, checked, and reproducible. If a source publishes a bad file, the pipeline stops and says so, instead of quietly loading wrong data.

Second, a set of gold layer tables the client can query directly: the company dimension with full status history, the insolvency event facts, the state level context. These tables are documented, tested, and stable.

Third, a Metabase dashboard for everyday use. A due diligence analyst can search a company, see its current status, see its status history, see any insolvency events, and see how it compares to its state and industry. That is the product the client asked for on day one, and every station on the roadmap exists to make it trustworthy.

---

*This document explains the why. The task by task list is in `docs/task-list.md`, and your week is pulled out for you in `students/DEx/weekY/problem_statement.md`. Reviewer answer keys live in the private admin repository.*
