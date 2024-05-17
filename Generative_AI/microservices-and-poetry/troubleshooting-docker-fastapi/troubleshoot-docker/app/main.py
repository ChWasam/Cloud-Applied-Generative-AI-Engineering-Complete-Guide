from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def greet ():
    return {"Hello":"Welcome to my kingdom"}

@app.get("/family")
def family_name ():
    return {"Family":"Chaudhry"}

