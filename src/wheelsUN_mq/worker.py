import asyncio
import aio_pika
import os

def is_running_in_docker():
    return os.path.exists('/.dockerenv')

async def on_message(message: aio_pika.IncomingMessage):
    async with message.process():
        print(f" [x] Received {message.body.decode()}")
        # Simulate some processing
        await asyncio.sleep(3)
        print(" [x] Done")

async def main():
    if is_running_in_docker():
        RMQ_HOST = 'wheelsun_mq'
    else:
        RMQ_HOST = 'localhost'
    # Connect to RabbitMQ
    connection = await aio_pika.connect_robust(
        host=RMQ_HOST,
        port=5672,  # default port for RabbitMQ
    )

    # Creating a channel
    channel = await connection.channel()

    # Declare the queue
    queue = await channel.declare_queue(
        "notification_queue", durable=True
    )

    # Setting up consumer
    await queue.consume(on_message)

    print(" [*] Waiting for messages. To exit press CTRL+C")
    await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())