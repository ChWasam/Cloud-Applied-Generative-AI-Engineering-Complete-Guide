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
 





