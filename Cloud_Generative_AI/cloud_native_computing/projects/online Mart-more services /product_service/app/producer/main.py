from sqlmodel import SQLModel,Field,create_engine,select, Session
from google.protobuf.json_format import MessageToDict
from fastapi import FastAPI,Depends,HTTPException
from app import settings
from contextlib import asynccontextmanager
from typing import Annotated
from aiokafka import AIOKafkaProducer , AIOKafkaConsumer
from aiokafka.admin import AIOKafkaAdminClient,NewTopic
from app import product_pb2
from app import settings
from app.consumer import main
import uuid 
from uuid import UUID 
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

# If the current attempt is the last one (else), the raise statement is executed.
# The raise statement re-raises the caught exception e.
# This means that after all retry attempts are exhausted, the function will raise the last encountered exception, propagating it to the caller.


# Creating topic from code 

async def create_topic ():
    admin_client = AIOKafkaAdminClient(
        bootstrap_servers= f"{settings.BOOTSTRAP_SERVER}"
    )
    await retry_async(admin_client.start)
    topic_list = [
        NewTopic(name=f"{settings.KAFKA_TOPIC}", num_partitions=2, replication_factor=1),
        NewTopic(name=f"{settings.KAFKA_TOPIC_GET}", num_partitions=2, replication_factor=1)
    ]
    try:
        await admin_client.create_topics(new_topics=topic_list, validate_only= False)
    except Exception as e:
        print ( {"error": e})
    finally:
        await admin_client.close()



async def consume_message_response():
    consumer = AIOKafkaConsumer(
    f"{settings.KAFKA_TOPIC_GET}",
    bootstrap_servers= f"{settings.BOOTSTRAP_SERVER}",
    group_id= f"{settings.KAFKA_CONSUMER_GROUP_ID_FOR_PRODUCT_GET}",
    auto_offset_reset='earliest'
    )
    await retry_async(consumer.start)
    try:
        async for msg in consumer:
            print(f"message from consumer : {msg}")
            try:
                new_msg = product_pb2.ProductList()
                #  yahan aupar bhi change karna para ga ku kah list ai ge to ProductList() likhna para ga ur agar Product ai ga to Product() likhna para ga
                new_msg.ParseFromString(msg.value)
                
                print(f"new_msg on producer side:{new_msg}")
                #  Ham yahan if else sa define kar sakt han kah  yeh kis ka lia msg aya ha
                return new_msg
            except Exception as e:
                print(f"Error Processing Message: {e} ")    
    finally:
        await consumer.stop()


class Product(SQLModel):
    # id : int|None = Field(default = None , primary_key= True)
    # product_id:UUID = Field(default_factory=uuid.uuid4, index=True)
    name:str = Field(index=True)
    description:str = Field(index=True)
    price:int = Field(index=True)
    is_available: bool = Field(default=True)

async def produce_message():
    producer = AIOKafkaProducer(bootstrap_servers= f"{settings.BOOTSTRAP_SERVER}")
    await retry_async(producer.start)
    try:
        yield producer
    finally:
        await producer.stop()

@asynccontextmanager
async def lifespan(app: FastAPI):
    main.create_table()
    await create_topic()
    loop = asyncio.get_event_loop()
    task = loop.create_task(main.consume_message_request())
    # task2 = loop.create_task(consume_message_response())
    try:
        yield
    finally:
        # for task in [task1,task2]:
        task.cancel()
        await task


# task.cancel(): This cancels the task that was created to consume messages.
# await task: This waits for the task to complete its cancellation.
# preferable to ensure proper task management and resource cleanup


#  Focus on the error given below 
# @asynccontextmanager
# async def lifespan(app:FastAPI):
#     main.create_table()
#     await create_topic()
#     asyncio.run(main.consume_message())  #  ERROR : asyncio.run() cannot be called from a running event loop
#     yield
#  ERROR : asyncio.run() cannot be called from a running event loop




app:FastAPI = FastAPI(lifespan=lifespan )
@app.get("/")
async def read_root():
    return {"Hello":"Product Service"}


@app.get("/products" ,response_model = dict)
async def get_all_products(producer:Annotated[AIOKafkaProducer,Depends(produce_message)]):
    product_proto = product_pb2.Product(option = product_pb2.SelectOption.GET_ALL)
    serialized_product = product_proto.SerializeToString()
    await producer.send_and_wait(f"{settings.KAFKA_TOPIC}",serialized_product)
    product_list_proto = await consume_message_response()
    return MessageToDict(product_list_proto)



@app.get("/products/{product_id}", response_model=dict)
async def get_a_product(product_id:UUID, producer:Annotated[AIOKafkaProducer,Depends(produce_message)]):
    product_proto = product_pb2.Product(product_id =str(product_id),  option = product_pb2.SelectOption.GET)
    serialized_product = product_proto.SerializeToString()
    await producer.send_and_wait(f"{settings.KAFKA_TOPIC}",serialized_product)
    product_proto = await consume_message_response()
    return MessageToDict(product_proto)






@app.post("/products", response_model=dict)
async  def add_product (product:Product , producer:Annotated[AIOKafkaProducer,Depends(produce_message)]):
    product_proto = product_pb2.Product(name = product.name, description = product.description , price = product.price , is_available = product.is_available, option = product_pb2.SelectOption.CREATE)
    serialized_product = product_proto.SerializeToString()
    await producer.send_and_wait(f"{settings.KAFKA_TOPIC}",serialized_product)
    return {f"product with name : {product.name} " : "added" }
#  Kafka ka topic me jo bhi data bhaja ga wo hamesha binary me jai ga 
#   Note : Serialization jasa marzi(json ya through protobuf ) karain lakin kafka ka broker me hamesha data binary form me jata ah 
#  jab json format me data bhaj raha han to wo binary me convert karna parta ha like b"hi"
#  lakin protobuf already searialize binary me karta ha is lia b likhna ke zarorat hi nahi ha 
# Topic data accept hi binary me karta ha 
#  json ka size zyada hota ha aur protobuf ka size kam hota ha  

#  operation type in protobuf. yeh is lia kia ha ku kah consumer ko to nahi pta kah aus na kya task perform karna ha 
#  ta ka tomic me clear ho kah yeh cheez create, update ya del ho rahi ha 

@app.put("/products/{product_id}", response_model=dict)
async  def update_product (product_id:UUID, product:Product , producer:Annotated[AIOKafkaProducer,Depends(produce_message)]):
    product_proto = product_pb2.Product(product_id= str(product_id), name = product.name, description = product.description ,price = product.price , is_available = product.is_available, option = product_pb2.SelectOption.UPDATE)
    serialized_product = product_proto.SerializeToString()
    await producer.send_and_wait(f"{settings.KAFKA_TOPIC}",serialized_product)
    return {f"product with product_id:{product_id}  ": {"Updated"}}


@app.delete("/products/{product_id}", response_model=dict)
async  def delete_product (product_id:UUID, producer:Annotated[AIOKafkaProducer,Depends(produce_message)]):
    product_proto = product_pb2.Product(product_id= str(product_id), option = product_pb2.SelectOption.DELETE)
    serialized_product = product_proto.SerializeToString()
    await producer.send_and_wait(f"{settings.KAFKA_TOPIC}",serialized_product)
    return {f"product with product_id:{product_id}  ": {"Deleted"}}



