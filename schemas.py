from pydantic import BaseModel
from typing import List

#SCHEMAS 

#RELATIONSHIP DISPLAY
class Article(BaseModel): # list to display on UserDisplay
    title: str
    content: str
    published: bool

    class Config():
        orm_mode = True

class User(BaseModel): # user display on ArticleDisplay
    id: int
    username: str
    email: str

    class Config():
        orm_mode = True

#user schemas or data validation
class UserBase(BaseModel):
    username: str
    email: str 
    password: str

class UserDisplay(BaseModel):
    id: int
    username: str
    email: str
    article: List[Article] = []

    class Config():
        orm_mode = True

class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    user_id: int

class ArticleDisplay(BaseModel):
    title: str
    content: str
    published: bool
    user: User

    class Config():
        orm_mode = True