# Platform and CI/CD Guide

This guide is for students who have been chosen for the weekly platform rotation. It explains how working in the shared `platform` folder is different from working in your individual practice folder.

## 1. Stricter Rules for Platform Work

When you work in your individual folder, it is for your own practice and learning. If you make a mistake there, it only affects your own record. 
The `platform` folder is different. It is the one real, shared version of our data pipeline that the entire cohort relies on. Because a mistake here affects everyone, the code is reviewed much more strictly before it is allowed in.

## 2. Automated Checks

To keep the platform code high quality, we use automated checks that run every time you open a pull request. These checks must pass before your code can be merged.

### The Linter
A linter is a tool that automatically reads your code to check for formatting mistakes and messy style. We run a linter on every pull request to check SQL formatting (using sqlfluff) and Python style. It catches these small style issues automatically so human reviewers do not have to waste time looking for them.

### The dbt Check
We also run a dbt check on your code. This check is a lightweight parse step, not a full build. Running the entire pipeline against our live Snowflake data warehouse on every single pull request would be slow and would waste expensive warehouse credits. Instead, this automated check only makes sure your dbt code is structurally correct. A full build against the warehouse only happens after your code is merged into the main branch.

## 3. The Scope of These Checks

These automated checks only run when you change files inside the `platform` folder. They will never run on the code in your individual student folder. Your practice work does not need to pass these strict automated gates.

## 4. What to Do If a Check Fails

If you open a pull request and see a red "X" telling you a check failed, do not panic. 
1. Click on the details of the failed check to read the text output.
2. The output will tell you exactly which line of code failed and why.
3. Go back to your code, fix the issue, and commit your changes.
4. Push your changes to your fork again. The automated checks will automatically rerun on your pull request.

## 5. Setting Up the Automated Workflows (For Admins)

The automated checks described above are controlled by three GitHub Actions workflow files located in the `.github/workflows/` folder:

* `lint.yml`: Runs the SQL and Python linters. It is triggered only on pull requests that touch the `platform/` folder.
* `dbt-check.yml`: Runs the lightweight dbt compile step. It is triggered only on pull requests that touch the `platform/` folder.
* `dbt-build.yml`: Runs the full dbt build. It is triggered only when code touching the `platform/` folder is merged into the main branch.

## 6. Setting Up Branch Protection (For Admins)

To enforce these rules, the program lead must configure the repository settings on GitHub:
1. Go to Settings > Branches.
2. Add a branch protection rule for the `main` branch.
3. Check "Require a pull request before merging".
4. Check "Require approvals" (set to at least 1).
5. Check "Require status checks to pass before merging".
6. Add the names of the linting and dbt check jobs to the required list.

## 7. Setting Up GitHub Secrets (For Admins)

The full dbt build relies on Snowflake credentials that must be kept secret. The program lead must add these secrets before the build workflow can run:
1. Go to Repository Settings > Secrets and variables > Actions.
2. Click "New repository secret".
3. Add the following secrets with their correct Snowflake values:
   - `DBT_SNOWFLAKE_ACCOUNT`
   - `DBT_SNOWFLAKE_USER`
   - `DBT_SNOWFLAKE_PASSWORD`
   - `DBT_SNOWFLAKE_ROLE`
   - `DBT_SNOWFLAKE_WAREHOUSE`
   - `DBT_SNOWFLAKE_DATABASE`
   - `DBT_SNOWFLAKE_SCHEMA`
