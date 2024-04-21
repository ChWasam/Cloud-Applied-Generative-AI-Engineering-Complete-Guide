from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def greet():
    return "Hello World"

# path parameter API

@app.get("/books/{book_name}")
def get_book_info(book_name:str):
    return {"message":f"you requested information about {book_name}"}

