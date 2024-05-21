from fastapi import FastAPI
from jose import jwt, JWTError
from datetime import datetime, timedelta

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
    decode_result = decode_token(token = str(token))
    return decode_result






