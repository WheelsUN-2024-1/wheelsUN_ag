#!/usr/bin/env python
import pika
import time

def pop_notification():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='notification_queue', durable=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')


    def callback(ch, method, properties, body):
        print(f" [x] Received {body.decode()}")
        time.sleep(3)
        print(" [x] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)
        return body.decode()


    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='notification_queue', on_message_callback=callback)

    channel.start_consuming()