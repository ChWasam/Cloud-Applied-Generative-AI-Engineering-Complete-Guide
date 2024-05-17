from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root ():
    return {"Welcome ":"Ali here "}
@app.get("/userinfo")
def user_info ():
    return {"name" : "wasam",
            "rollno":"160898"}


