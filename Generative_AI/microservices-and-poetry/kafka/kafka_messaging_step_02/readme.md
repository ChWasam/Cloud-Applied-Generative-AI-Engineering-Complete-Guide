# 02_kafka_messaging

# Understanding concepts related to Python for this code

### Understanding Yield

- Generators are functions that produce a sequence of values on demand.
- They use the yield keyword to pause execution and return a value.
- When next() is called on a generator object, it resumes execution from the last yield statement and produces the next value.

```
async def get_kafka_producer():
    producer = AIOKafkaProducer(bootstrap_servers='broker:19092')
    await producer.start()
    try:
        yield producer
    finally:
        await producer.stop()
```

##### This line (yield producer) is the crux of the function. It uses the yield keyword, a special construct in Python's asynchronous programming model. When this function is called, it pauses execution at this point and returns the producer object to the caller. The caller can then use the producer to send messages to Kafka.Importantly, when the caller is done using the producer, it resumes the execution of get_kafka_producer() at this point (after the yield statement).

### Understanding asyncio

#### What is asyncio?

- asyncio is a library to write concurrent code using the async and await syntax. It's particularly useful for I/O-bound tasks, such as network operations, file I/O, or database operations, where you spend a lot of time waiting for something to happen.

Key Concepts

- Coroutine: A coroutine is a function that can pause its execution and return control to the event loop, allowing other tasks to run.
- Event Loop: The event loop is responsible for executing coroutines, handling events, and switching between tasks.
- Tasks: Tasks wrap coroutines and schedule them to run on the event loop.

c

#### Running Multiple Coroutines Concurrently

```

import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

async def say_hi():
    print("Hi")
    await asyncio.sleep(1)
    print("There")

async def main():
    await asyncio.gather(say_hello(), say_hi())

asyncio.run(main())


```

#### Explanation

- asyncio.gather(say_hello(), say_hi()): Runs say_hello and say_hi concurrently.
- Both coroutines will pause at await asyncio.sleep(1) and resume after 1 second.

#### Creating Tasks

asyncio.create_task allows you to create tasks that run concurrently:

```

import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

async def say_hi():
    print("Hi")
    await asyncio.sleep(1)
    print("There")

async def main():
    task1 = asyncio.create_task(say_hello())
    task2 = asyncio.create_task(say_hi())

    await task1
    await task2

asyncio.run(main())


```

#### Explanation

- asyncio.create_task(say_hello()): Schedules say_hello to run concurrently.
- await task1 and await task2: Waits for both tasks to complete.

#### Try to understand this code

```
import asyncio

async def make_lemonade(order):
 # Simulate making lemonade (wait 2 seconds)
 import time
 await asyncio.sleep(2)
 print(f"Here is your {order} lemonade!")

async def take_order_async():
 print("Customer arrives!")
 order = input("What size lemonade would you like? (small, medium, large): ")
 # Make lemonade asynchronously (without blocking)
 await make_lemonade(order)

async def main():
 # Serve multiple customers concurrently
 tasks = [take_order_async() for _ in range(3)]
 await asyncio.gather(*tasks)

asyncio.run(main())
```

# What is an Event Loop?
It runs in a loop and continuously checks for tasks that are ready to execute, runs them, and then waits for more tasks.

## asyncio.get_event_loop()
asyncio.get_event_loop() is a function provided by the asyncio module to get the current event loop object.
```
import asyncio

async def say_hello():
    print("Hello")

# Get the current event loop
loop = asyncio.get_event_loop()

# Schedule the coroutine to be run on the loop
loop.run_until_complete(say_hello())

```

### What Does asyncio.get_event_loop() Do?
* Retrieve the Current Event Loop:
asyncio.get_event_loop() returns the current event loop for the current OS thread.
If there is no current event loop set for the current OS thread, it creates a new event loop and sets it as the current event loop.

* Run Until Complete:
loop.run_until_complete(say_hello()) runs the say_hello coroutine until it completes.
The event loop executes the coroutine and manages the asynchronous operations.

### Modern Approach: asyncio.run()
```
import asyncio

async def say_hello():
    print("Hello")

# Run the coroutine using asyncio.run
asyncio.run(say_hello())

```




# AIOKafka

### AIOKafkaProducer

AIOKafkaProducer is a high-level, asynchronous message producer.

Example of AIOKafkaProducer usage:

```
from aiokafka import AIOKafkaProducer

# Kafka Producer as a dependency
async def get_kafka_producer():
    producer = AIOKafkaProducer(bootstrap_servers='broker:19092')
    await producer.start()
    try:
        # Produce message
        await producer.send_and_wait("my_topic", b"Super message")
    finally:
        await producer.stop()
```

### AIOKafkaConsumer

AIOKafkaConsumer is a high-level, asynchronous message consumer. It interacts with the assigned Kafka Group Coordinator node to allow multiple consumers to load balance consumption of topics (requires kafka >= 0.9.0.0).

Example of AIOKafkaConsumer usage:

```
from aiokafka import AIOKafkaConsumer
import asyncio

async def consume_messages():
    consumer = AIOKafkaConsumer(
        'my_topic', 'my_other_topic',
        bootstrap_servers='localhost:9092',
        group_id="my-group")
    # Get cluster layout and join group `my-group`
    await consumer.start()
    try:
        # Consume messages
        async for msg in consumer:
            print("consumed: ", msg.topic, msg.partition, msg.offset,
                  msg.key, msg.value, msg.timestamp)
    finally:
        # Will leave consumer group; perform autocommit if enabled.
        await consumer.stop()

asyncio.create_task(consume_messages())
```

https://github.com/aio-libs/aiokafka
