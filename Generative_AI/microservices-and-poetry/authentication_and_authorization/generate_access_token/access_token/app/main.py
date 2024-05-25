from fastapi import FastAPI,Depends,HTTPException
from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer
from jose import jwt, JWTError
from datetime import datetime, timedelta
from typing import Annotated

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

ALGORITHM:str = "HS256"
SECRET_KEY:str = "A Secure Secret Key"
def generate_access_token(subject:str , expire_delta:timedelta ):
    expire = datetime.utcnow() + expire_delta 
    to_encode = {"exp" : expire , "sub": subject}
    access_token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return access_token

app = FastAPI()

@app.get("/")
def root():
    return {"Generate":"Access_token"}

@app.get("/get_acess_token")
def getting_acess_token(name:str):
    expiry_time = timedelta(minutes=2)
    access_token = generate_access_token(subject = name , expire_delta = expiry_time )
    return {"access_token": access_token}

def decode_token(token:str):
    decode_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return decode_token

@app.get("/decode_token")
def decoding_token(token:str):
    try:
        decode_result = decode_token(token = str(token))
        return decode_result
    except JWTError as e:
        return  {"error":str(e)}


dummy_database: dict[str,dict[str,str]] = {
    "wasamChaudhry":{
        "name":"Chaudhry Wasam Ur Rehman",
        "username":"wasamChaudhry",
        "email":"ch.wasam@gmail.com",
        "password":"wasam223344"
    },
    "aliwali":{
        "name":"Chaudhry Ali Raza",
        "username":"aliwali",
        "email":"aliwali@gmail.com",
        "password":"ali223344"
    }
}


@app.post("/login")
def login(login_credentials:Annotated[OAuth2PasswordRequestForm,Depends(OAuth2PasswordRequestForm)]):
    username_verified = dummy_database.get(login_credentials.username)
    if not username_verified:
        raise HTTPException(status_code=400 , detail=" Incorrect Username")
    password_verified = username_verified["password"] == login_credentials.password
    if not password_verified:
        raise HTTPException(status_code=400, detail="Incorrect Password")
    expiry_time = timedelta(minutes=1)
    access_token = generate_access_token(subject = username_verified["username"], expire_delta = expiry_time )
    return {"access_token": access_token, "token_type":"bearer", "expire_in" : expiry_time.total_seconds()}
# One that returns the list of all users
@app.get("/users")
def all_users(token:Annotated[str,Depends(oauth2_scheme)]):
    return dummy_database

# Other that takes access_token and return user all details
@app.get("/users/me")
def getting_user(token:Annotated[str ,Depends(oauth2_scheme)]):
    token = str(token)
    try:
        getting_back_user = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        user_detail = dummy_database.get(getting_back_user["sub"])
        return user_detail
    except JWTError as e:
        return {"error": str(e)}
