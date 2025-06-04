# Dockerfile
FROM python:3.13-slim

# Install pika
RUN pip install --no-cache-dir pika

# Copy the test script
COPY test_rabbitmq.py /app/test_rabbitmq.py

# Set working directory
WORKDIR /app

# Run the script
CMD ["python", "test_rabbitmq.py"]
