#!/usr/bin/env python
import pika
import json  # Import json module for serialization
import os

def is_running_in_docker():
    return os.path.exists('/.dockerenv')

def push_notification(message_dict):
    # Set base URL based on environment
    if is_running_in_docker():
        RMQ_HOST = 'wheelsun_mq'
    else:
        RMQ_HOST = 'localhost'
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=RMQ_HOST))
    channel = connection.channel()

    channel.queue_declare(queue='notification_queue', durable=True)

    # Convert the dictionary to a JSON string
    message = json.dumps(message_dict)
    channel.basic_publish(
        exchange='',
        routing_key='notification_queue',
        body=message,  # Send the JSON string as the message body
        properties=pika.BasicProperties(
            delivery_mode=pika.DeliveryMode.Persistent
        ))
    print(f" [x] Sent {message}")  # Print the JSON string that was sent
    connection.close()
