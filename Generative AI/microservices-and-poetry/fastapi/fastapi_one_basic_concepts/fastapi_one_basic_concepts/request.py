import requests
# from requests.models import Response
# from requests.structures import CaseInsensitiveDict

from fastapi import FastAPI

response: str  = requests.get("https://simple-books-api.glitch.me")
print(response)


app1 =  FastAPI()
@app1.get("/response")
def Urlresponse():
    return response

