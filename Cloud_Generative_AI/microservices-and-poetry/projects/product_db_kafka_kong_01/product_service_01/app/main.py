from sqlmodel import SQLModel,Field,create_engine,select, Session
from fastapi import FastAPI,Depends,HTTPException
from app import settings
from contextlib import asynccontextmanager
from typing import Annotated

class Product(SQLModel, table=True):
    id : int|None = Field(default = None , primary_key= True )
    name:str = Field(index=True)
    price:int = Field(index=True)
    is_available: bool = Field(default=True)

connection_string:str = str(settings.DATABASE_URL).replace("postgresql","postgresql+psycopg")
print(connection_string)
engine = create_engine(connection_string , pool_recycle=300 , pool_size=10 , echo=True)

def create_table():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
     yield session

@asynccontextmanager
async def lifespan(app:FastAPI):
   create_table()
   yield

app:FastAPI = FastAPI(lifespan=lifespan)

@app.get("/")
async def read_root():
    return {"Hello":"Product Service"}

@app.post("/products", response_model = Product)
async def add_product(product:Product, session:Annotated[Session,Depends(get_session)]):
   session.add(product)
   session.commit()
   session.refresh(product)
   return product
    # Keep in mind that from ui we wont allow user to give primary key. It will be generated by postgres. If we will also be allowed to give it manually then there is a chance that we may find conflict as the id might already exist

@app.get("/products", response_model=list[Product])
async def get_all_products(session:Annotated[Session,Depends(get_session)]):
    products = session.exec(select(Product)).all()
    return products


@app.get("/products/{id}", response_model=Product)
async def get_a_product(id:int, session:Annotated[Session,Depends(get_session)]):
    product = session.exec(select(Product).where(Product.id == id)).first()
    if product:
        return product
    else:
        raise HTTPException(status_code=400, detail=f"No Product with id :{id} is found !")
    
@app.put("/products/{id}",response_model=Product)
async def update_a_product(id:int, product: Product, session:Annotated[Session,Depends(get_session)]):
    current_product = session.exec(select(Product).where(Product.id == id)).first()
    if current_product:
        current_product.name = product.name
        current_product.price = product.price
        current_product.is_available = product.is_available
        session.add(current_product)
        session.commit()
        session.refresh(current_product)
        return(current_product)
    else:
        raise HTTPException(status_code=400,detail=f"No Product with id :{id} is found !")

@app.delete("/products/{id}",response_model=dict)
async def del_a_product(id:int , session:Annotated[Session,Depends(get_session)]):
    product = session.exec(select(Product).where(Product.id == id)).first()
    if product:
        session.delete(product)
        session.commit()
        return {f"{id}":"Deleted"}
    else:
        raise HTTPException(status_code=400, detail=f"No Product with id :{id} is found !")


