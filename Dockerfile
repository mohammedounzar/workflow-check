FROM python:3.13-slim

RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1

#CMD ["python", "main.py"]
# CMD is overridden by default when you pass arguments to docker run

ENTRYPOINT ["python", "main.py"]  
# ENTRYPOINT is not overridden by default when you pass arguments to docker run