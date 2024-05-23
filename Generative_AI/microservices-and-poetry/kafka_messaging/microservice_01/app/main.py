# main.py
from contextlib import asynccontextmanager
from typing import Union, Optional, Annotated
from app import settings
from sqlmodel import Field, Session, SQLModel, create_engine, select, Sequence
from fastapi import FastAPI, Depends
from typing import AsyncGenerator

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
            "url": "http://0.0.0.0:8000", # ADD NGROK URL Here Before Creating GPT Action
            "description": "Development Server"
        }
        ])

@app.get("/")
def read_product():
    return {"test":"product"}

@app.post("/create_order")
def create_order(order:Order):
    return {
        "id" : 1 ,
        "username": "wasam" ,
        "product_id": 1,
        "product_name": "Laptop",
        "product_price": 200
    }



