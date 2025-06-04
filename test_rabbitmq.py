# test_rabbitmq.py
import pika
import os
import sys
import ssl

host = os.getenv("RABBITMQ_HOST", "localhost")
port = int(os.getenv("RABBITMQ_PORT", 5671))  # AMQPS default port
username = os.getenv("RABBITMQ_USER", "guest")
password = os.getenv("RABBITMQ_PASS", "guest")

# Create SSL context
context = ssl.create_default_context()

credentials = pika.PlainCredentials(username, password)

ssl_options = pika.SSLOptions(context, host)

parameters = pika.ConnectionParameters(
    host=host,
    port=port,
    virtual_host='/',
    credentials=credentials,
    ssl_options=ssl_options
)

print(f"Trying to connect to RabbitMQ via AMQPS at {host}:{port}...")

try:
    connection = pika.BlockingConnection(parameters)
    connection.close()
    print("✅ Successfully connected to RabbitMQ via AMQPS")
    sys.exit(0)
except Exception as e:
    print(f"❌ Failed to connect: {e}")
    sys.exit(1)
