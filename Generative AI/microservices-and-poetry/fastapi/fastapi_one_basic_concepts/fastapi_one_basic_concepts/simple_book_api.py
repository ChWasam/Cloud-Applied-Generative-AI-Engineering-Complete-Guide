import requests

from requests.models import Response
from requests.structures import CaseInsensitiveDict
from fastapi import FastAPI

data_authorization = {
   "clientName": "ALI87",
   "clientEmail": "ali87@example.com"
}
data_order = {
  "bookId": 3,
  "customerName": "wasam"
}

update_order = {
  "customerName": "John"
}


accessToken : str | None = None 
orderId : str | None = None 
authorization_request : Response|None = None
order_subittion_request: Response|None = None

def get_accessToken() -> str :
    authorization_request: Response = requests.post("https://simple-books-api.glitch.me/api-clients/", json = data_authorization)
    json_authorization_request: dict  = authorization_request.json()
    accessToken: str = json_authorization_request["accessToken"]
    return accessToken

def get_orderid() -> str:
    headers: dict = {"Authorization": f"Bearer "+f"{accessToken}"}
    order_subittion_request: Response  = requests.post("https://simple-books-api.glitch.me/orders/",headers = headers , json = data_order) 
    json_order_subittion_request: dict = order_subittion_request.json()
    orderId : str = json_order_subittion_request["orderId"]
    return orderId
def get_all_orders() -> dict:
    headers: dict = {"Authorization": f"Bearer "+f"{accessToken}"}
    response_getting_orders : Response  = requests.get("https://simple-books-api.glitch.me/orders/",headers = headers ) 
    json_response_getting_all_orders: dict = response_getting_orders.json()
    return json_response_getting_all_orders
def get_an_order() -> dict:
    headers: dict = {"Authorization": f"Bearer "+f"{accessToken}"}
    response_getting_an_order : Response  = requests.get(f"https://simple-books-api.glitch.me/orders/"+f"{orderId}",headers = headers ) 
    json_response_getting_an_order: dict = response_getting_an_order.json()
    return  json_response_getting_an_order

def update_an_order() -> int:
    headers: dict = {"Authorization": f"Bearer "+f"{accessToken}"}
    update_an_order: Response  = requests.patch(f"https://simple-books-api.glitch.me/orders/"+f"{orderId}",headers = headers , json = update_order) 
    status_code_update_an_order: int = update_an_order.status_code
    return status_code_update_an_order

def delete_an_order() -> int:
    headers: dict = {"Authorization": f"Bearer "+f"{accessToken}"}
    delete_an_order: Response  = requests.delete(f"https://simple-books-api.glitch.me/orders/"+f"{orderId}",headers = headers) 
    status_code_delete_an_order: int = delete_an_order.status_code
    return status_code_delete_an_order

if accessToken == None :
    accessToken = get_accessToken()

app = FastAPI()
@app.get("/authorization")
async def authorization() -> str|None:
    return accessToken

@app.get("/submitanorder")
async def submit_an_order() -> str|None:
    return get_orderid()

@app.get("/getallorders")
async def get_orders() -> dict:
    return get_all_orders()

@app.get("/getanorder")
async def get_any_order() -> dict:
    return get_an_order()

@app.get("/updateanorder")
async def updateorder() -> int:
    return update_an_order()

@app.get("/deleteanorder")
async def delete_order() -> int:
    return delete_an_order()
    




     