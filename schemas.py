from pydantic import BaseModel

#SCHEMAS 

#user schemas or data validation
class UserBase(BaseModel):
    username: str
    email: str 
    password: str

class UserDisplay(BaseModel):
    id: int
    username: str
    email: str
    class Config():
        orm_mode = True
