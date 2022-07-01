"""Module class of kibernum patent"""
from pydantic import BaseModel
from typing import Union


#Token models
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Union[str, None] = None