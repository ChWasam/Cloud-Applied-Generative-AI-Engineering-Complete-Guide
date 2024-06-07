from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"Home":"Welcome to HomeScreen"}
@app.get("/username")
def username():
    return {"Username":"Chaudhry Wasam Ur Rehman"}

@app.get("/email")
def email():
    return {"Email":"ch.wasam@gmail.com"}



