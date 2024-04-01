import asyncio
import aio_pika

async def on_message(message: aio_pika.IncomingMessage):
    async with message.process():
        print(f" [x] Received {message.body.decode()}")
        # Simulate some processing
        await asyncio.sleep(3)
        print(" [x] Done")

async def main():
    # Connect to RabbitMQ
    connection = await aio_pika.connect_robust(
        host="localhost",
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