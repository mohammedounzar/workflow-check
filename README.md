# 📝 Workflow-Check: Google Sheets Updater for GitHub Actions

Automate the update of a Google Spreadsheet with your CI/CD workflow results, PR numbers, and error messages—directly from GitHub Actions. No more manual reporting!

---

## 🚀 Features

- **Automatic Google Sheet updates** after each workflow run
- **Pull Request info extraction** (ticket number, release name)
- **Error message logging** from your workflow
- **Dockerized** for easy integration in CI/CD
- **Secure**: uses GitHub Secrets and Google Service Account

---

## 📦 Project Structure

```
.
├── Dockerfile
├── extract_ticket_and_sheet.py
├── import_sheet.py
├── main.py
├── requirements.txt
├── update_sheet.py
└── README.md
```

---

## 🛠 Prerequisites

- Google Cloud Platform project with Sheets API enabled
- Google Sheet (shared with your service account)
- GitHub repository with Actions workflows
- Docker installed

---

## 🔐 Google Sheets API Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com/).
2. Create/select a project.
3. Enable the **Google Sheets API**.
4. Create a **Service Account** and download the JSON key.
5. Share your Google Sheet with the service account email (Editor access).

---

## 🔑 GitHub Secrets

In your GitHub repo, add these secrets:

- `GOOGLE_CREDENTIALS`: Content of your service account JSON
- `SHEET_ID`: Your Google Sheet ID (from the URL)
- `GH_AUTH_TOKEN`: GitHub token with repo access

---

## ⚙️ Usage in GitHub Actions

Add these steps to your workflow:

### 1. Extract Error Messages

```yaml
- name: Extract Result Message
  run: |
    {
      echo "ERROR_MSG<<EOF"
      grep "Error in" validate_output.txt || echo "No error message"
      echo "EOF"
    } >> $GITHUB_ENV
```

### 2. Clone the Updater Repo

```yaml
- name: Clone Spreadsheet Updater Repo
  run: git clone https://github.com/mohammedounzar/workflow-check.git
```

### 3. Build & Run Docker Container

```yaml
- name: Update Sprint Spreadsheet
  env:
    GOOGLE_CREDENTIALS: ${{ secrets.GOOGLE_CREDENTIALS }}
    SHEET_ID: ${{ secrets.SHEET_ID }}
    PR_NUMBER: ${{ env.PR_NUMBER }}
    VALIDATION_STATUS: ${{ steps.validation.outcome }}
    ERROR_MSG: ${{ env.ERROR_MSG || 'No error message' }}
    GITHUB_TOKEN: ${{ secrets.GH_AUTH_TOKEN }}
    REPO_NAME: ${{ github.event.repository.name }}
    REPO_OWNER: ${{ github.repository_owner }}
  run: |
    echo "$GOOGLE_CREDENTIALS" > /tmp/service_account.json

    docker build -t update-sheet-app -f workflow-check/Dockerfile workflow-check

    docker run --rm \
      -e SHEET_ID="$SHEET_ID" \
      -e VALIDATION_STATUS="$VALIDATION_STATUS" \
      -e PR_NUMBER="$PR_NUMBER" \
      -e ERROR_MSG="$ERROR_MSG" \
      -e GITHUB_TOKEN="$GITHUB_TOKEN" \
      -e REPO_NAME="$REPO_NAME" \
      -e REPO_OWNER="$REPO_OWNER" \
      -v /tmp/service_account.json:/app/service_account.json \
      update-sheet-app
```

---

## 🧩 How It Works

1. **Extracts** ticket number and release name from the latest PR commit.
2. **Finds** the correct worksheet in your Google Sheet.
3. **Updates** the row for the ticket with PR number, status, and error message.

---

## 🧪 Local Testing

Install dependencies:

```sh
pip install -r requirements.txt
```

Run manually:

```sh
export SHEET_ID=...
export VALIDATION_STATUS=success
export ERROR_MSG="No error"
export PR_NUMBER=123
export REPO_NAME=your-repo
export REPO_OWNER=your-org
export GITHUB_TOKEN=ghp_...
python main.py
```

---