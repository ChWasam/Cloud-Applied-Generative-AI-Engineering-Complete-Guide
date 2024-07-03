from sqlmodel import SQLModel,Field,create_engine,select, Session
from fastapi import FastAPI,Depends,HTTPException
from app import settings
from contextlib import asynccontextmanager
from aiokafka import AIOKafkaConsumer,AIOKafkaProducer
from typing import Annotated 
from app import product_pb2
from app import settings
import asyncio
import logging
import psycopg
import uuid
from uuid import UUID

# Retry utility
async def retry_async(func, retries=5, delay=2, *args, **kwargs):
    for attempt in range(retries):
        try:
            print("retry")
            return await func(*args, **kwargs)
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                await asyncio.sleep(delay)
            else:
                raise

# Configure the logger 
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

class Product(SQLModel, table=True):
    id : int|None = Field(default = None , primary_key= True)
    product_id:UUID = Field(default_factory=uuid.uuid4, index=True)
    name:str = Field(index=True)
    description:str = Field(index=True)
    price:int = Field(index=True)
    is_available: bool = Field(default=True)


connection_string:str = str(settings.DATABASE_URL).replace("postgresql","postgresql+psycopg")

engine = create_engine(connection_string , pool_recycle=300 , pool_size=10 , echo=True)

def create_table():
    SQLModel.metadata.create_all(engine)

# def get_session():
#     with Session(engine) as session:
#      yield session


# @asynccontextmanager
# async def lifespan():   
#    create_table()
#    loop = asyncio.get_event_loop()
#    task = loop.create_task(consume_message())
#    yield
#    task.cancel()
#    await task


# writing Consumer code 
async def consume_message_request():
    consumer = AIOKafkaConsumer(
        f"{settings.KAFKA_TOPIC}",
        bootstrap_servers= f"{settings.BOOTSTRAP_SERVER}",
        group_id= f"{settings.KAFKA_CONSUMER_GROUP_ID_FOR_PRODUCT}",
        auto_offset_reset='earliest'
    )
    await retry_async(consumer.start)
    try:
        async for msg in consumer:
            print(f"message from consumer : {msg}")
            try:
                new_msg = product_pb2.Product()
                new_msg.ParseFromString(msg.value)
                print(f"new_msg:{new_msg}")
                if new_msg.option == product_pb2.SelectOption.GET_ALL:
                    with Session(engine) as session:
                        products_list_from_db = session.exec(select(Product)).all()
                        print(f"List of products from database:{products_list_from_db} ")
                        product_list_proto = product_pb2.ProductList()
                        for product in products_list_from_db:
                            product_proto = product_pb2.Product(
                                id=product.id,
                                product_id=str(product.product_id),
                                name=product.name,
                                description=product.description,
                                price=product.price,
                                is_available=product.is_available,
                            )
                            product_list_proto.products.append(product_proto)
                        print(f"List of products in proto :{product_list_proto} ")
                        producer = AIOKafkaProducer(bootstrap_servers= f"{settings.BOOTSTRAP_SERVER}")
                        await retry_async(producer.start)
                        try:
                            serialized_product_list = product_list_proto.SerializeToString()
                            await producer.send_and_wait(f"{settings.KAFKA_TOPIC_GET}", serialized_product_list)
                        finally:
                            await producer.stop()
                        print(f"List of products sent back from database: {product_list_proto} ")
                elif new_msg.option == product_pb2.SelectOption.GET:
                    msg_to_db = Product(product_id = new_msg.product_id)
                    with Session(engine) as session:
                        product = session.exec(select(Product).where(Product.product_id == msg_to_db.product_id)).first()
                        print(f"product from database:{product}")
                        product_proto = product_pb2.Product(
                            id=product.id,
                            product_id=str(product.product_id),
                            name=product.name,
                            description=product.description,
                            price=product.price,
                            is_available=product.is_available,
                        )
                        print(f"Product in proto :{product_proto} ")
                        producer = AIOKafkaProducer(bootstrap_servers= f"{settings.BOOTSTRAP_SERVER}")
                        await retry_async(producer.start)
                        try:
                            serialized_product = product_proto.SerializeToString()
                            await producer.send_and_wait(f"{settings.KAFKA_TOPIC_GET}", serialized_product)
                        finally:
                            await producer.stop()
                        print(f"product sent back from database: {product_proto} ")
                elif new_msg.option == product_pb2.SelectOption.CREATE:
                    msg_to_db = Product(name = new_msg.name,description = new_msg.description, price = new_msg.price , is_available = new_msg.is_available )
                    print(f"msg_to_db:{msg_to_db}")
                    with Session(engine) as session:
                        session.add(msg_to_db)
                        session.commit()
                        print(f"Product Added to database:{msg_to_db} ")
                elif new_msg.option == product_pb2.SelectOption.UPDATE:
                    msg_to_db = Product(product_id = new_msg.product_id, name = new_msg.name, description = new_msg.description, price = new_msg.price , is_available = new_msg.is_available)
                    with Session(engine) as session:
                        current_product = session.exec(select(Product).where(Product.product_id == msg_to_db.product_id)).first()
                        if current_product:
                            current_product.name = msg_to_db.name
                            current_product.description = msg_to_db.description
                            current_product.price = msg_to_db.price
                            current_product.is_available = msg_to_db.is_available
                            session.add(current_product)
                            session.commit()
                            # session.refresh(current_product)
                            print(f"Product Updated in database:{msg_to_db} ")
                        else:
                            # raise HTTPException(status_code=400,detail=f"No Product with id :{id} is found !")
                           print(f"No Product with product_id :{msg_to_db.product_id} is  found !")
                elif new_msg.option == product_pb2.SelectOption.DELETE:
                    msg_to_db = Product(product_id = new_msg.product_id)
                    with Session(engine) as session:
                        current_product = session.exec(select(Product).where(Product.product_id == msg_to_db.product_id)).first()
                        if current_product:
                            print(f"current_product :{current_product} is  found ! ")
                            session.delete(current_product)
                            session.commit()
                        else:
                            # raise HTTPException(status_code=400, detail=f"No Product with id :{id} is found !")
                            print(f"No Product with id :{msg_to_db.product_id} is  found ! ")
            except Exception as e:
                print(f"Error Processing Message: {e} ")    
    finally:
        await consumer.stop()




# app:FastAPI = FastAPI(lifespan=lifespan)
# @app.get("/")
# async def read_root():
#     return {"Hello":"Consumer Service to update Database"}




# @app.post("/products", response_model = Product)
# async def add_product(product:Product, session:Annotated[Session,Depends(get_session)]):
#    session.add(product)
#    session.commit()
#    session.refresh(product)
#    return product
#     # Keep in mind that from ui we wont allow user to give primary key. It will be generated by postgres. If we will also be allowed to give it manually then there is a chance that we may find conflict as the id might already exist

# @app.get("/products", response_model=list[Product])
# async def get_all_products(session:Annotated[Session,Depends(get_session)]):
#     products = session.exec(select(Product)).all()
#     return products


# @app.get("/products/{id}", response_model=Product)
# async def get_a_product(id:int, session:Annotated[Session,Depends(get_session)]):
#     product = session.exec(select(Product).where(Product.id == id)).first()
#     if product:
#         return product
#     else:
#         raise HTTPException(status_code=400, detail=f"No Product with id :{id} is found !")
    
# @app.put("/products/{id}",response_model=Product)
# async def update_a_product(id:int, product: Product, session:Annotated[Session,Depends(get_session)]):
#     current_product = session.exec(select(Product).where(Product.id == id)).first()
#     if current_product:
#         current_product.name = product.name
#         current_product.price = product.price
#         current_product.is_available = product.is_available
#         session.add(current_product)
#         session.commit()
#         session.refresh(current_product)
#         return(current_product)
#     else:
#         raise HTTPException(status_code=400,detail=f"No Product with id :{id} is found !")

# @app.delete("/products/{id}",response_model=dict)
# async def del_a_product(id:int , session:Annotated[Session,Depends(get_session)]):
#     product = session.exec(select(Product).where(Product.id == id)).first()
#     if product:
#         session.delete(product)
#         session.commit()
#         return {f"{id}":"Deleted"}
#     else:
#         raise HTTPException(status_code=400, detail=f"No Product with id :{id} is found !")


