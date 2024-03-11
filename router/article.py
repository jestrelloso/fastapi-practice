from fastapi import APIRouter, Depends, status, HTTPException
from schemas import ArticleBase, ArticleDisplay, UserBase
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_article
from typing import List
from auth.oauth2 import oauth2_scheme, get_current_user

router = APIRouter(
    prefix='/article',
    tags=['article']
)

# Create Article using a database / database model / schema
@router.post('/', response_model=ArticleDisplay)
async def create_article(request: ArticleBase, db: Session = Depends(get_db)):
    return db_article.create_article(db, request)

# Read All Articles
@router.get('/', response_model=List[ArticleDisplay])
async def get_all_articles(db: Session = Depends(get_db)):
    return db_article.get_all_articles(db)

# Read a Single Article
@router.get('/{id}',  status_code=status.HTTP_200_OK) #response_model=ArticleDisplay)
async def get_article(article_id: int, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    print(current_user)
    return {
        'data' : db_article.get_article(db, article_id),
        'current_user': current_user
    }

# update a single article
@router.put('/{id}/update')
async def update_article(article_id: int, request: ArticleBase, db: Session = Depends(get_db)):
    return db_article.update_article(db, article_id, request)

#delete a single article
@router.delete('/{id}/delete', status_code=status.HTTP_204_NO_CONTENT)
async def delete_article(article_id: int, db: Session = Depends(get_db)):
    return db_article.delete_article(db, article_id)