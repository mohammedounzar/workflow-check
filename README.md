# PR Monitoring

This project monitors GitHub Pull Requests (PRs) for a specified repository and updates a Google Sheet with the status of each PR's workflow.

## Features

- Fetches PRs from a GitHub repository.
- Checks the status of the latest workflow for each PR.
- Updates a Google Sheet with the PR status automatically.
- Runs continuously with a configurable interval.

## Requirements

- Python 3.11
- Google Service Account credentials (`service_account.json`)
- A Google Sheet with columns: `PR Number`, `Status automatique`
- GitHub personal access token

## Setup

1. **Clone the repository** and navigate to the project directory.

2. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

3. **Configure environment variables** in a `.env` file:
   ```
   SHEET_ID=your_google_sheet_id
   GITHUB_TOKEN=your_github_token
   REPO_OWNER=your_github_username_or_org
   REPO_NAME=your_repository_name
   ```

4. **Add your Google service account credentials** as `service_account.json` in the project root.

5. **Run the application**:
   ```sh
   python main.py
   ```

## Docker

You can run the project in a Docker container:

```sh
docker build -t pr-monitoring .
docker-compose up
```

## File Structure

- `main.py` - Main loop for monitoring and updating the sheet.
- `import_sheet.py` - Imports data from the Google Sheet.
- `update_sheet.py` - Updates the Google Sheet with workflow statuses.
- `workflow_status.py` - Fetches workflow status from GitHub.
- `requirements.txt` - Python dependencies.
- `Dockerfile` & `docker-compose.yaml` - Docker configuration.

## License

This project is for internal use.