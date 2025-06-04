# test_rabbitmq.py
import pika
import os
import sys
import time

host = os.getenv("RABBITMQ_HOST", "localhost")
port = int(os.getenv("RABBITMQ_PORT", 5672))
username = os.getenv("RABBITMQ_USER", "guest")
password = os.getenv("RABBITMQ_PASS", "guest")

credentials = pika.PlainCredentials(username, password)
parameters = pika.ConnectionParameters(host, port, '/', credentials)

print(f"Trying to connect to RabbitMQ at {host}:{port}...")

try:
    connection = pika.BlockingConnection(parameters)
    connection.close()
    print("✅ Successfully connected to RabbitMQ")
    sys.exit(0)
except Exception as e:
    print(f"❌ Failed to connect: {e}")
    sys.exit(1)
