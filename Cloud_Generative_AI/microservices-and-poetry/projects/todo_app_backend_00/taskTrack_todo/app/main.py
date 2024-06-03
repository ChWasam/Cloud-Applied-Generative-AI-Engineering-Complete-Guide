from fastapi import FastAPI, Depends,HTTPException
from sqlmodel import SQLModel,Field, create_engine, Session, select
from app import settings
from typing import Annotated
from contextlib import asynccontextmanager

# *******************************************************************
# Quick summary

# Step-1: Create Database on Neon
# Step-2: Create .env file for environment variables
# Step-3: Create setting.py file for encrypting DatabaseURL
# Step-4: Create a Model
# Step-5: Create Engine
# Step-6: Create function for table creation
# Step-7: Create function for session management
# Step-8: Create contex manager for app lifespan
# Step-9: Create all endpoints of todo app

# *******************************************************************

#  Custom type create karna ka lia Annotated ka use karta han 

#  Lets make a data model yeh table create nahi kara ga 
#  table = True pass karna para ga agar ham chahta han kah yeh table bhi create kara 
#  Field() : Yeh e.g id ka name sa table me field create karta ha 
#  id is primary key ku kah filhal ak hi table ha 
#  primary key should be unique 
#  Foreign key aus waqt chahia ho ge jab ham banai ga user ka model 

#  Ab id ko bnana ha primary key 
#  aur wo unique bhi honi chahia
#  Agar user  sa  id lai to wo to asi id da sakta ha jo pehla nhi kisi na de ho 
#  Ham yeh chahta han db yeh khud create kara  
# is ka lia ham pehla id : int|None dana para ge. None ka matlab absence of data 
#  jab todo ko get kar kah  la kar ai ga aus case me id ho ga 
# Ku kah aus case me database na assign kia ho ga  
#  jab todo ko create kara ga to aus waqt none ho ga ku kah ham id to nahi da raha han


class Todo (SQLModel, table=True):
    id : int|None = Field(default=None, primary_key=True)
    # Yahan id optional ha 
    content: str = Field(index=True, min_length=3, max_length=54)
    # Index : Is column ko database me index kar da ge 
    # Faida yeh hota ha kha jab ham search karain ga apna task ko  
    # to database ko sara table scan nahi karna para ga 
    # data validation ka lia bhi use hota ha is lia min_length=3
    is_completed: bool = Field(default=False)
    #  Matlab jab bhi create karain ga task to default value False kar dya ha 

# *******************************************************************
#  Engine is one for whole application 

connection_string: str =str(settings.DATABASE_URL).replace("postgresql","postgresql+psycopg")
#  ku kah me is postgres ko psycopg ka sath use kar raha ho is lia replace kia ha 
#  kah mera communication is sa ho ge postgresql+psycopg 

#  Ab ham chahta han jo bhi hmari communication ho database ka sath wo encrypt ho kah jai 
#  so we will add secure socket layer(ssl)
engine = create_engine(connection_string, connect_args={"sslmode":"require"},pool_recycle=300,pool_size=10, echo=True)

#   Hamara jo engine ha wo connection pool banai ga 
#  wo ak connection hmara database ka sath nahi kara ga 
#   by default sqlslchemy me  jab app start ho ge to 5 connection establish karta ha 
#  lakin ham change kar sakta han pool_size=10 is tarha sa
#  matlab wo connection ka pool bna raha ha 

#  naya connection jab database ka sath bana ga to aus ka aupar time lagta ha 
#  wo time hamara waste ho raha ha 
#  jasa waiter ai ga order lai ga kitchen me jai ga aur wapis order lana chala jai ga 
#  yani connection standby ho ga 

#  pool_recycle : matlab kah 300 sec yani 5 min bad connection recycle ho jai 

# echo=True : matlab engine jitna bhi kam kar raha ho ga yeh mujha har step ka show kar dai ga kah yeh kam kia ha . Step wise sari cheezain terminal pa batai ga kah kya kya step perform hua han

# *******************************************************************

# ab jo model bnaya tha table ka isa create bhi karna ha 


def create_tables():
    SQLModel.metadata.create_all(engine)



# ham na ak engine create kia ha jo hmari application ke communication karwai ga db ka sath 
# Is engine ka use karta hua hamara tables database me create ho jai ga 
# *******************************************************************
#  Giving data to understand concept 

# todo1 : Todo = Todo(content="will go for swimming")  
# todo2 : Todo = Todo(content="Bring water")


# *******************************************************************

#  Session (Ak app me engine ak ho ga session different create ho ga)
#  session: separate session for each functionality/transaction
#  we will import  Session from sqlmodel

#  hamra har session engine ko use karta hua koi bhi functionality provide kara ga 

# session = Session(engine)

# *******************************************************************

# create todos in database

#  session overwrite sa bachna ka lia kahta ha kah jitna bhi kam mera sa karwana han wo mujha da do me ak hi bar kar do ga

# yeh in memory variable me store kar lata ha data 
# abhi direct commit nahi kara ga 
#  Like in git pehla ap add kar lata han commit bad me karta han

# session.add(todo1)
# session.add(todo2)
# print(f"Before Commit {todo1}")
#  Yahan todo ka andar value ha 
# session.commit()

# session.refresh(todo1)
# yeh hama database sa value la kar da ga jahan id  bhi assign ho chuki ha 

#  Commit sa todo table me create ho jai ga   
# print(f"After Commit {todo1}")
#  Yahan todo ka andar koi value nahi ha
# session.close()

#  Todo ke class as a table model use ho rahi ha wo hama yahan sa pta chal raha ha kah is ke basis pa tables  create ho raha han 


# *******************************************************************

#  Har transaction ka lia hama session required ha  
#  session ko  open karain ga aur close karain ga jab transacion complete ho jai ge 
#  Behtar yeh ha kah ham apna ak function bna lain 

#  We will use generator function here 
#  Dependency Injection 
def get_session():
    with Session(engine) as session:
        yield session 
# *******************************************************************
#  life span ka me function bnao ga is ka lia mujha context manager import karna para ga 
# from contextlib import asynccontextmanager
#  yeh context bnai ga app ka kah kis tarah sa chalna chahia 
#  Isa as a decorater use karo ga 
#  necha jo bhi function ho ga isa as a context create kar da ga 
# ab is ko async nahi bhi bnaya yeh async hi ho ga 
#  is me asi cheezain karain ga kah jab app start hoti ha to pehla yeh kam hona chahia 
# e.g  1) tables create hona chahia etc

#  app ke start pa sab sa pehla yeh kam hona chahia 
@asynccontextmanager
async def lifespan(app:FastAPI):
    # 1) tables create hona chahia
     print("Creating Tables")
     create_tables()
     print("Tables Created")
     yield
# yield pa  a kah ruk jai ga phir wahan pa baqi function hamari app ka cuncurrently perform ho ga 

# *******************************************************************


# Jab hamari app start hoti ha to wo khuch cheezo pa depend kar rahi hoti ha
# - Hama is ka lia ak context bnana para ga 
#  app ko title aur version bhi da sakta han 
app : FastAPI = FastAPI(lifespan=lifespan, title="TaskTrack todo app", version="1.0.0" )





# *******************************************************************

# In FastAPI, using async allows your application to handle multiple requests concurrently without blocking the execution of other requests. This improves the overall responsiveness and performance of your web application.

#  ab har method(get, del, post,put) ka lia session ka sara kam karna para ga 
#  Har transaction ka lia hama session required ha  
#  session ko  open karain ga aur close karain ga jab transaction complete ho jai ge 
#  Behtar yeh ha kah ham apna ak function bna lain 
@app.get("/")
async def root():
    return {"message":"Welcome to TaskTrack todo app"}

@app.post("/todos", response_model=Todo)
#  user sa ak todo ai ge aus ke type ho ge todo
#  Ab jo task user sa ai ge ham na isa create karna ha for that we need a session  
# ab yeh session get_session ka function me rakh lia 
#  Yahan ham dakh sakta han kah todo ke class as a data model bhi use ho rahi ha 

#  response_model=Todo : Is ka yeh matlab ha kah mujha jo response/todo return ho ge wo validate ho ge is datamodel sa 
# Agar ham user ka bnata to alag sa aus ka bhi model bna lata 
#  agar ham chahta han kah ham asa data model banai jis sa table na bana to ham  table=True nahi likhain ga 
async def create_todo(todo:Todo , session:Annotated[Session,Depends(get_session)]):
    # Keep in mind that from ui we wont allow user to give primary key. It will be generated by postgres. If we will also be allowed to give it manually then there is a chance that we may find conflict as the id might already exist
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return todo

@app.get("/todos",response_model=list[Todo])
async def get_all_todos(session:Annotated[Session,Depends(get_session)]):
    #  hama koi command dani para ge database ko orm ka through wo command jai ge 
    #  psycopg ausa sql ke query me convert kar kah database ko da ga  
    #  database ausa aus command ke base pa value return kar kah da dai ga 
    statement = select(Todo)
    # Todos ka table select karain 
    todos =  session.exec(statement).all()

    # todos = session.exec(select(Todo)).all()

    #  return ka datatype btana para ga datavalidation ka lia 
    #  ak sa zyada todos ai ge to wo list ke form me ai ge 
    if todos:
        return todos
    else:
        raise HTTPException(status_code=404 , detail=f"No task remaining")

@app.get("/todos/{id}", response_model=Todo)
async def get_single_todo(id:int, session:Annotated[Session,Depends(get_session)]):
    todo =  session.exec(select(Todo).where(Todo.id == id)).first()
    #  asal me yeh beshak single todo ha lakin yeh list ke form me ai ge 
    #  ham chahta han single object/ dictionary   me ai to .first() use karna ho ga 
    #  .first() =====>>>>>>>> Fetch the first object or None if no object is present.
    if todo:
        return todo
    else:
        raise HTTPException(status_code=404 , detail=f"No todo found with id: {id}")

@app.put("/todos/{id}", response_model= Todo)
#  put me complete data provide karna parta ha 
# Patch me jo data change karna chahta han sirf wohi provide karna chahta han  
async def update_todo(id:int, todo:Todo, session:Annotated[Session,Depends(get_session)]):
    existing_todo = session.exec(select(Todo).where(Todo.id==id)).first()
    if existing_todo:
        existing_todo.content = todo.content
        existing_todo.is_completed = todo.is_completed
        session.add(existing_todo)
        session.commit()
        session.refresh(existing_todo)
        return existing_todo
    else:
        raise HTTPException (status_code=404 , detail=f"No todo found with id: {id}")


@app.delete("/todos/{id}", response_model=dict)
async def delete_todo(id:int, session:Annotated[Session,Depends(get_session)]):
    todo = session.exec(select(Todo).where(Todo.id == id)).first()
    # todo = session.get(Todo, id)
    if todo:
        session.delete(todo)
        session.commit()
        #  no need to refresh this time as we don't need it in return 
        return {"message":"Task successfully deleted"}
    else:
        raise HTTPException (status_code=404 , detail=f"No todo found with id: {id}")
    


    


