# Use official Python 3.11 slim image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements file first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all your project files into the container
COPY . .

# Make sure Python outputs are immediately flushed (good for logs)
ENV PYTHONUNBUFFERED=1

# Command to run your script
CMD ["python", "main.py"]
