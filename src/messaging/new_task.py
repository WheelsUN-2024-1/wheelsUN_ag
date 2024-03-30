#!/usr/bin/env python
import pika
import sys

def push_notification(message):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='notification_queue', durable=True)

    #message = dict
    channel.basic_publish(
        exchange='',
        routing_key='notification_queue',
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=pika.DeliveryMode.Persistent
        ))
    print(f" [x] Sent {message}")
    connection.close()