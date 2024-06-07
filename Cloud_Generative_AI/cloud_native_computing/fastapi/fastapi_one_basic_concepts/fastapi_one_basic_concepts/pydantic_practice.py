# from datetime import datetime
# from typing import Tuple
# from pydantic import BaseModel

# class Checking(BaseModel):
#     time_stamp: datetime
#     dimentons: Tuple[int,int]

# m = Checking(time_stamp='2020-01-02T03:04:05Z', dimentons=['10', '20'])
# print(repr(m.time_stamp))
# print(m.time_stamp)
# print(m.dimentons)

# 888888888888888888888888888888888888888888888888888888888888888888888888888888888



# from datetime import datetime
# from pydantic import BaseModel,PositiveInt

# class User(BaseModel):
#     id: int 
#     name:str
#     user_ts: datetime
#     hobbies: dict[ str , PositiveInt]

# data:dict = {
#     "id" : 12 ,
#     "name" : "Wasam",
#     "user_ts": "2016-03-24 04:05" ,
#     "hobbies": {
#         "cricket" : 12,
#         "footbal" : 15,
#         "hicking" :20,
#     }
# }
# user1: User = User(**data)

# print(user1.hobbies)
# print(user1.model_dump())



# 888888888888888888888888888888888888888888888888888888888888888888888888888888888

# from datetime import datetime
# from pydantic import BaseModel,PositiveInt,ValidationError

# class User(BaseModel):
#     id: int 
#     name:str
#     user_ts: datetime
#     hobbies: dict[ str , PositiveInt]

# data:dict = {
#     "id" : "Wasam" ,
#     "name" : "Wasam",
#     "hobbies": {
#     }
# }


# try:
#     user1: User = User(**data)
# except ValidationError as e:
#     print(e.errors())

# print(user1.hobbies)
# print(user1.model_dump())



# 888888888888888888888888888888888888888888888888888888888888888888888888888888888
#  validator has been depricated 
#  Use field_validator instead of validator 

from pydantic import BaseModel,field_validator, EmailStr
from typing import Any
class User(BaseModel):
    id : int
    email: EmailStr

    @field_validator('id')
    def validate_id(cls, id:int):
        if id <= 0:
            raise ValueError(f"Id must be positive: {id}")
        return id
    
# validator must be written inside the class

user = User(id = 1234, email = "ch.wasam@gmai.com" )

user_json_str: str = user.model_dump_json()
print(user_json_str, type(user_json_str))
user_obj: User = user.model_validate_json(user_json_str)
print (user_obj)

# 888888888888888888888888888888888888888888888888888888888888888888888888888888888
