FROM python:3.13-slim

RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1

#CMD
ENTRYPOINT ["python", "main.py"] 
