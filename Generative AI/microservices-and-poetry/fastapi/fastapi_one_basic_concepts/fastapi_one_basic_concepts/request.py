# Import both pakages requests and types-requests



import requests
from requests.models import Response
from requests.structures import CaseInsensitiveDict
from fastapi import FastAPI

response: Response  = requests.get("https://simple-books-api.glitch.me")

json_obj: dict = response.json()

status_code:int = response.status_code

text :str = response.text

headers : CaseInsensitiveDict = response.headers
# yeh jo header ha yeh server ka response ka ha 
#  server ka aupar yeh time hua ha 
# server ke tamam info
#  client sa bhi ak header ke info jati ha e.g browser konsa ha aur ip address konsa ha






# print(type(request))


app =  FastAPI()
@app.get("/response")
def Urlresponse():
    return json_obj
#  yahan agar response ko direct return karain  ga to nahi ho ga 
#  json me convert karna zarori ha 

@app.get("/status_code")
def successfull ():
    return status_code

@app.get("/text")
def text_response ():
    return text

@app.get("/headers")
def headers_response ():
    return headers




