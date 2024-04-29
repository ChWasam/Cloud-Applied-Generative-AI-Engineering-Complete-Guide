#  This is just to understand the complete code 


from typing import Annotated

from fastapi import Depends, FastAPI

app = FastAPI()


async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}

#  jo  cheez bhi ap smajhta han kah  aus code ko bar bar likhna ke zarorat ho ge 
#  database sa connection ya authentication etc khuch bhi ho sakta ha 
#  Ausa ak bar likh lain 
# Aus logic ya aus funtionality ko ak function ka andar likhain  

#  We can pass classes as dependencies also 


#  Yeh jo items aur users wali api ha yeh depend kar rahi ha common_parameters is ka aupr 
#  Jab bhi yeh api hit ho ge pehla yeh function chala ga phiur api ka code chala ga 
@app.get("/items/")
async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
    return commons["skip"]


@app.get("/users/")
async def read_users(commons : dict = Depends(common_parameters)):
    return commons


#  Dependency Injection 
#  Apni API's ko kisi function ka aupar depend karna is ko kahta han dependencies
#  why it is usedul ?
#  API's have share logic (Ham one time isa  define kar dain ga aur tamam API's ka aupar isa apply kar dai ga )
#  Share database connection (Matlab one time database bna dain ga aur ausa bhi share kar dain ga tamam API's ka sath )
#  Enforce security, authentication, role requirements, etc. and many other things 