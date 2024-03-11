from fastapi import APIRouter, Depends, status
from schemas import UserBase, UserDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_user
from typing import List
from auth.oauth2 import oauth2_scheme, get_current_user

router = APIRouter(
    prefix='/user',
    tags=['user']
)

# Create User using a database / database model / schema
@router.post('/', response_model=UserDisplay)
async def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)

# Read All Users
@router.get('/', response_model=List[UserDisplay])
async def get_all_users(db: Session = Depends(get_db)):
    return db_user.get_all_users(db)

# Read a Single User
@router.get('/{id}', response_model=UserDisplay, status_code=status.HTTP_200_OK)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    return db_user.get_user(db, user_id)
    
# Update user
@router.put('/{id}/update')
async def update_user(user_id: int, request: UserBase, db: Session = Depends(get_db)):
    return db_user.update_user(db, user_id, request)

# Delete user
@router.delete('/{id}/delete', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int ,db: Session = Depends(get_db)):
    return db_user.delete_user(db, user_id)
    # algorithm for cascade. when the user associated with an article gets deleted
    
        
