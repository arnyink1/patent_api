"""Module class of kibernum patent"""
from pydantic import BaseModel
from typing import Union
from datetime import datetime



#Token models
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Union[str, None] = None


#Patent Model
class Patent(BaseModel):
    id:int
    patent:str
    create_date:datetime = datetime.now()


#Login model
class Login(BaseModel):
    username:str
    password:str
