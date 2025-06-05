# Dockerfile
FROM python:3.13-slim

# Install pika
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the test script
COPY test_rabbitmq.py /app/test_rabbitmq.py

# Set working directory
WORKDIR /app

# Run the script
CMD ["python", "test_rabbitmq.py"]
