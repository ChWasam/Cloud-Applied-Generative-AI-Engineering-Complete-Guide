# main.py
from contextlib import asynccontextmanager
from typing import Union, Optional, Annotated
from app import settings
from sqlmodel import Field, Session, SQLModel, create_engine, select, Sequence
from fastapi import FastAPI, Depends
from typing import AsyncGenerator
from aiokafka import AIOKafkaProducer , AIOKafkaConsumer
import json

class Order(SQLModel):
    id: Optional[int] = Field(default=None)
    username: str
    product_id: int
    product_name: str
    product_price: int


@asynccontextmanager
async def lifespan(app: FastAPI)-> AsyncGenerator[None, None]:
    print("Call kafka consumer...")
    # Initial class call for event service
    yield


app = FastAPI(lifespan=lifespan, title="Product Service with Kafka ", 
    version="0.0.1",
    servers=[
        {
            "url": "http://127.0.0.1:8000", # ADD NGROK URL Here Before Creating GPT Action
            "description": "Development Server"
        }
        ])


@app.get("/")
def read_product():
    return {"test":"product"}

@app.post("/create_order")
async def create_order(order:Order):
    producer = AIOKafkaProducer(bootstrap_servers = f"{settings.BOOTSTRAP_SERVER}")
    # ho sakta ha order buffer form me ho 
    #  Agar wo buffer form me ho to wo khatam ho jai 

     # Convert the Order object to a dictionary and then serialize it to JSON
    order_dict = order.dict()

    #  now a bytes-like object is required, not 'dict'
    order_json = json.dumps(order_dict).encode("utf-8")
    #  encode("utf-8") yeh is lia add kia kah agar koi buffering a rahi ho ge to wo khatam ho jai ge
    print("order_json")
    print(order_json) 
    await producer.start()
    try:
        # Produce message
        await producer.send_and_wait(settings.KAFKA_ORDER_TOPIC, order_json)
        #  yahan order json me ai ga aur is order ko ham na json dumb kar kah call kia ha 
    finally:
        # Wait for all pending messages to be delivered or expire.
        await producer.stop()

    return order_dict 


@app.get("/read_order")
async def read_order():
    consumer = AIOKafkaConsumer(f"{settings.KAFKA_ORDER_TOPIC}",bootstrap_servers = f"{settings.BOOTSTRAP_SERVER}", group_id = f"{settings.KAFKA_CONSUMER_GROUP_ID_FOR_PRODUCT}")

    await consumer.start()
    try:
        # Consume messages
        async for msg in consumer:
            print("consumed: ", msg.topic, msg.partition, msg.offset,
                  msg.key, msg.value, msg.timestamp)
       
    finally:
        # Wait for all pending messages to be delivered or expire.
        await consumer.stop()

    return {"consumer":"Done"}

