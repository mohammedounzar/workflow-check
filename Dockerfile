FROM python:3.10-slim

ARG SHEET_ID
ARG GOOGLE_CREDS_JSON

ENV SHEET_ID=${SHEET_ID}
ENV GOOGLE_CREDS_JSON=${GOOGLE_CREDS_JSON}
ENV WORKFLOW_STATUS=${VALIDATION_OUTCOME}
ENV PR_NUMBER=${PR_NUMBER}

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip && pip install gspread oauth2client

CMD ["python", "main.py"]
