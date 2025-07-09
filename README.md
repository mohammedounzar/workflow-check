# Setup

## 📌 Project Overview

This project automates the update of a Google Spreadsheet using data from a GitHub Actions workflow. It pushes CI/CD workflow statuses, test results, and error messages directly to a Google Sheet—removing the need for manual reporting and improving visibility for your team.

---

## 🛠 Prerequisites

- A Google Cloud Platform (GCP) project
- A Google Sheet (for reporting)
- A GitHub repository with CI/CD workflows
- Docker installed (for running the updater)
- Basic knowledge of GitHub Actions

---

## 🔐 Step 1: Google Sheets API Setup

1. Visit [Google Cloud Console](https://console.cloud.google.com/).
2. Create or select a project.
3. Go to **APIs & Services → Library**.
4. Enable the **Google Sheets API**.
5. Go to **APIs & Services → Credentials**.
6. Click **Create Credentials → Service Account**.
7. Finish the setup, then:
   - Go to the **Keys** tab
   - Click **Add Key → Create new key → JSON**
   - Download the JSON file (this is your credentials file)

---

## 📄 Step 2: Share the Spreadsheet

1. Open your spreadsheet in Google Sheets.
2. Click **Share**.
3. Use the email from your service account JSON (ends in `@<project>.iam.gserviceaccount.com`) and give it **Editor** access.

---

## 🔑 Step 3: Add GitHub Secrets

In your GitHub repo:

1. Go to **Settings → Secrets and variables → Actions**.
2. Add the following secrets:
   - `GOOGLE_CREDENTIALS`: Content of your service account JSON
   - `SHEET_ID`: The ID from your Google Sheets URL
   - `GH_AUTH_TOKEN`: A GitHub token with the right permissions

---

## 🧪 Step 4: Update GitHub Workflow

Add the following steps to your GitHub Actions workflow:

### 1. Extract Error Messages

```yaml
- name: Extract Result Message
  run: |
    {
      echo "ERROR_MSG<<EOF"
      grep "Error in" validate_output.txt || echo "No error message"
      echo "EOF"
    } >> $GITHUB_ENV

### 2. Clone the Updater Repo

```yaml
- name: Clone Spreadsheet Updater Repo
  run: git clone https://github.com/mohammedounzar/workflow-check.git

### 3. Build & Run Docker Container

```yaml
- name: UPDATE Sprint spreadsheet using Docker
  env:
    GOOGLE_CREDENTIALS: ${{ secrets.GOOGLE_CREDENTIALS }}
    SHEET_ID: ${{ secrets.SHEET_ID }}
    PR_NUMBER: ${{ env.PR_NUMBER }}
    VALIDATION_STATUS: ${{ steps.validation.outcome }}
    ERROR_MSG: ${{ env.ERROR_MSG || 'No error message' }}
    GITHUB_TOKEN: ${{ secrets.GH_AUTH_TOKEN }}
  run: |
    echo "$GOOGLE_CREDENTIALS" > /tmp/service_account.json

    docker build -t update-sheet-app -f workflow-check/Dockerfile workflow-check

    docker run --rm \
      -e SHEET_ID="$SHEET_ID" \
      -e VALIDATION_STATUS="$VALIDATION_STATUS" \
      -e PR_NUMBER="$PR_NUMBER" \
      -e ERROR_MSG="$ERROR_MSG" \
      -e GITHUB_TOKEN="$GITHUB_TOKEN" \
      -v /tmp/service_account.json:/app/service_account.json \
      update-sheet-app

## Result

Once configured, your GitHub workflow will automatically:

1. Log validation status

2. Extract any error messages

3. Update the corresponding row in your sprint Google Sheet
