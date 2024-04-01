#!/usr/bin/env python
import pika
import json  # Import json module for serialization

def push_notification(message_dict):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
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
