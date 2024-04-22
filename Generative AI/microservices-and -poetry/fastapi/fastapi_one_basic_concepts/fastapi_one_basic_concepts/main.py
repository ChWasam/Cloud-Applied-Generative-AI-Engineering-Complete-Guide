from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def greet():
    return "Hello World"

# path parameter API


#  validation nahi ha me yeh chahta ho sirf int hi pass kar sakain string acceptable nahi ho 
# def get_book_info(book_id:int):
#  Only integer is acceptable here  
@app.get("/books_id/{book_id}")
def get_book_id(book_id:int):
    return {"book_id " :book_id}

@app.get("/books_name/{book_name}")
def get_book_name(book_name:str):
    return {"book_name" : book_name}


@app.get("/file/{file_path:path}")
def file(file_path:str):
    return {"file":file_path}

# we can make multiple variables in one route
#  we can use them anywhere in that route 
@app.get("/{product_name}/product/{product_id}")
def product_info(product_name:str,product_id:int):
    return {
        "product_name":product_name,
        "prduct_id":product_id
    }
 

#  Query Parameters 

# starts with ?
# contains key value pair
# Seperated by &

# @app.get("/items")
# def items(q:int):
#     return {"q" : q}

# we can set by default value 

# @app.get("/items")
# def items(q:int = 1):
#     return {"q" : q}

# @app.get("/items")
# def items(q:int =12,skip:int = 0):
#     return {"q" : q,
#             "skip": skip}

# Use Case pagination

dumy_data = [{"item_name":"cake" },{"item_name":"Cake Rusk"},{"item_name":"cookies"}]

@app.get("/items")
def get_items(skip:int=0, limit:int=10):
    return dumy_data[skip:skip+limit]

@app.get("/books/{book_name}")
def books(book_name:str,q:str|None = None):
    if q:
        return{"book_name":book_name, "q":q }
    return{"book_name":book_name}

@app.get("/subjects/{subject_id}")
def subject(subject_id:str,q:str|None = None, short:bool = False):
    subject = {"subject_id":subject_id
               ,"description": "Book is Long"}
    if q:
        subject.update({"q":q})
    if short:
        subject.update({"description": "Book is short"})

    return subject

#  we can use True or true or on or yes
# @app get ("users/{user_id}/items/{item_id}")
# async def read_user_item(
# user_id: int, item_id: str, q: str | None = None, short: bool = False


    
    

        





















