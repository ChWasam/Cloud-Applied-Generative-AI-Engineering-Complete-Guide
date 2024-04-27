from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def welcome ():
    return {"Welcome Message ":"Hi, Wasam here"}

