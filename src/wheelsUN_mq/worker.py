import asyncio
import aio_pika
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def is_running_in_docker():
    return os.path.exists('/.dockerenv')

async def on_message(message: aio_pika.IncomingMessage):
    async with message.process():
        logger.info(f" [x] Received {message.body.decode()}")
        # Simulate some processing
        await asyncio.sleep(3)
        logger.info(" [x] Done")

async def connect_to_rabbitmq():
    RMQ_HOST = '34.41.172.204'
    retry_count = 0
    max_retries = 10  # Increase retries for more robustness

    while retry_count < max_retries:
        try:
            logger.info(f"Connecting to RabbitMQ at {RMQ_HOST}...")
            connection = await aio_pika.connect_robust(
                host=RMQ_HOST,
                port=5672,
            )
            logger.info("Connected to RabbitMQ")
            return connection
        except aio_pika.exceptions.AMQPConnectionError as e:
            retry_count += 1
            logger.error(f"Connection attempt {retry_count}/{max_retries} failed: {e}")
            await asyncio.sleep(5)
    
    logger.error("Failed to connect to RabbitMQ after multiple attempts")
    raise aio_pika.exceptions.AMQPConnectionError("Could not connect to RabbitMQ")

async def main():
    try:
        connection = await connect_to_rabbitmq()

        # Creating a channel
        channel = await connection.channel()

        # Declare the queue
        queue = await channel.declare_queue(
            "notification_queue", durable=True
        )

        # Setting up consumer
        await queue.consume(on_message)

        logger.info(" [*] Waiting for messages. To exit press CTRL+C")
        await asyncio.Future()  # Run forever
    except Exception as e:
        logger.error(f"Failed to start worker: {e}")

if __name__ == "__main__":
    asyncio.run(main())
