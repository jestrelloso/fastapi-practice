from sqlalchemy.orm import Session
from schemas import UserBase
from db.models import DbUser
from db.hash import Hash
from fastapi import status, HTTPException

#FUNCTIONALITY TO WRITE TO DATABASE

# create a user
def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        username = request.username,
        email = request.email,
        password = Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# get all users
def get_all_users(db: Session):
    user = db.query(DbUser).all()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return user

# get a single user
def get_user(db: Session, user_id: int) -> DbUser:
    user = db.query(DbUser).filter(DbUser.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return user

# update a single user
def update_user(db: Session, user_id: int, request:UserBase):
    user = db.query(DbUser).filter(DbUser.id==user_id)
    user.update({
        DbUser.username: request.username,
        DbUser.email: request.email,
        DbUser.password: Hash.bcrypt(request.password)
    })
    db.commit()
    return {'message': "User updated"}

# delete a user
def delete_user(db: Session, user_id: int):
    user = db.query(DbUser).filter(DbUser.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    db.delete(user)
    db.commit()

