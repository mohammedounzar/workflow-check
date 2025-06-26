FROM python:3.10-slim

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip && pip install gspread oauth2client python-dotenv

CMD ["python", "main.py"]
