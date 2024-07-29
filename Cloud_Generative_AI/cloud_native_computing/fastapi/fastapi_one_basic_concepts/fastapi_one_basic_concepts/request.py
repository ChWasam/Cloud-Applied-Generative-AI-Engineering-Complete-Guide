# Import both pakages requests and types-requests



import requests
# used for typing
#  used for response
from requests.models import Response  

#  used for headers
from requests.structures import CaseInsensitiveDict

from fastapi import FastAPI

# 1
# response: Response  = requests.get("https://simple-books-api.glitch.me")
# 2
# response: Response  = requests.get("https://simple-books-api.glitch.me/books")
# 3
# response: Response  = requests.get("https://simple-books-api.glitch.me/books/3")
# 4 query parameters
# response: Response  = requests.get("https://simple-books-api.glitch.me/books?type=fiction&&limit=2")
# 5
response: Response  = requests.get("https://simple-books-api.glitch.me/books/3")


#  Jo bhi secret info hoti ha wo client sa header ka zariya server ko bhajain ga 
#  header me jo bhi info bhajain ga wo encrypt ho ge 
#  Encrypt hona ka bad server pa jati ha 
# aur phir server  pa jana ka bad decrypt hoti ha 



json_obj: dict = response.json()

status_code:int = response.status_code

text :str = response.text
#  Agar json me response na ho to phir text sa xlient pa show kar sakta han 

headers : CaseInsensitiveDict = response.headers
# yeh jo header ha yeh server ka response ka ha 
#  server ka aupar yeh time hua ha 
# server ke tamam info
#  client sa bhi ak header ke info jati ha e.g browser konsa ha aur ip address konsa ha

# process and method of encryption 

# Authorization: Bearer <YOUR TOKEN>
# headers : dict = {"Authorization" : "Bearer e232c09f3d1fcb27eac378535450bfd1ac489b607390938ec395b7aa1d5d151f"}






# print(type(request))


app =  FastAPI()
@app.get("/json_response")
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




