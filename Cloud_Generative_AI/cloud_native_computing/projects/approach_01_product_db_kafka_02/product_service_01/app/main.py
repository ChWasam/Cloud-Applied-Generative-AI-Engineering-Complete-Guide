from sqlmodel import SQLModel,Field,create_engine,select, Session
from fastapi import FastAPI,Depends,HTTPException
from app import settings
from contextlib import asynccontextmanager
from typing import Annotated
from aiokafka import AIOKafkaProducer 
from aiokafka.admin import AIOKafkaAdminClient,NewTopic
from app import product_pb2
from app import settings
import asyncio
import psycopg


# Retry utility
async def retry_async(func, retries=5, delay=2, *args, **kwargs):
    for attempt in range(retries):
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                await asyncio.sleep(delay)
            else:
                raise


# Creating topic from code 

async def create_topic ():
    admin_client = AIOKafkaAdminClient(
        bootstrap_servers= f"{settings.BOOTSTRAP_SERVER}"
    )
    await retry_async(admin_client.start)
    topic_list = [NewTopic(name=f"{settings.KAFKA_TOPIC}", num_partitions=2, replication_factor=1)]
    try:
        await admin_client.create_topics(new_topics=topic_list, validate_only= False)
    except Exception as e:
        print ( {"error": e})
    finally:
        await admin_client.close()


class Product(SQLModel):
    # id : int|None = Field(default = None , primary_key= True)
    name:str = Field(index=True)
    price:int = Field(index=True)
    is_available: bool = Field(default=True)

async def produce_message ():
    producer = AIOKafkaProducer(bootstrap_servers= f"{settings.BOOTSTRAP_SERVER}")

    await retry_async(producer.start)
    try:
        yield producer
    finally:
        await producer.stop()


@asynccontextmanager
async def lifespan(app:FastAPI):
   await create_topic()
   yield

app:FastAPI = FastAPI(lifespan=lifespan)

@app.get("/")
async def read_root():
    return {"Hello":"Product Service"}

@app.post("/products", response_model=dict)
async  def add_product (product:Product , producer:Annotated[AIOKafkaProducer,Depends(produce_message)]):
    product_proto = product_pb2.Product(name = product.name, price = product.price , is_available = product.is_available, option = product_pb2.SelectOption.CREATE)
    serialized_product = product_proto.SerializeToString()
    await producer.send_and_wait(f"{settings.KAFKA_TOPIC}",serialized_product)
    return {f"product with name : {product.name}  " : "added" }
#  Kafka ka topic me jo bhi data bhaja ga wo hamesha binary me jai ga 
#   Note : Serialization jasa marzi(json ya through protobuf ) karain lakin kafka ka broker me hamesha data binary form me jata ah 
#  jab json format me data bhaj raha han to wo binary me convert karna parta ha like b"hi"
#  lakin protobuf already searialize binary me karta ha is lia b likhna ke zarorat hi nahi ha 
# Topic data accept hi binary me karta ha 
#  json ka size zyada hota ha aur protobuf ka size kam hota ha  

#  operation type in protobuf. yeh is lia kia ha ku kah consumer ko to nahi pta kah aus na kya task perform karna ha 
#  ta ka tomic me clear ho kah yeh cheez create, update ya del ho rahi ha 

@app.put("/products/{id}", response_model=dict )
async  def update_product (id:int, product:Product , producer:Annotated[AIOKafkaProducer,Depends(produce_message)]):
    product_proto = product_pb2.Product(id= id, name = product.name, price = product.price , is_available = product.is_available, option = product_pb2.SelectOption.UPDATE)
    serialized_product = product_proto.SerializeToString()
    await producer.send_and_wait(f"{settings.KAFKA_TOPIC}",serialized_product)
    return {f"product with id:{id}  ": {"Updated"}}


@app.delete("/products/{id}", response_model=dict)
async  def delete_product (id:int, producer:Annotated[AIOKafkaProducer,Depends(produce_message)]):
    product_proto = product_pb2.Product(id= id, option = product_pb2.SelectOption.DELETE)
    serialized_product = product_proto.SerializeToString()
    await producer.send_and_wait(f"{settings.KAFKA_TOPIC}",serialized_product)
    return {f"product with id:{id}  ": {"Deleted"}}



