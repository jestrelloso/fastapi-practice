from sqlalchemy.orm import Session
from schemas import ArticleBase
from exceptions import StoryException
from db.models import DbArticle
from fastapi import status, HTTPException

#FUNCTIONALITY TO WRITE, READ, UPDATE AND DELETE TO DATABASE

# create an article
def create_article(db: Session, request: ArticleBase):
    if request.content.startswith('Once upon a time'):
        raise StoryException('Stories not allowed!')
    new_article = DbArticle(
        title = request.title,
        content = request.content,
        published = request.published,
        user_id = request.user_id
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article

# get all articles
def get_all_articles(db: Session):
    article = db.query(DbArticle).all()
    if article is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return article

# get a single article
def get_article(db: Session, article_id: int):
    article = db.query(DbArticle).filter(DbArticle.id == article_id).first()
    if article is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'Article with id {article_id} not found')
    return article

# update a single article
def update_article(db: Session, article_id: int, request: ArticleBase):
    article = db.query(DbArticle).filter(DbArticle.id == article_id)
    if article is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'Article with id {article_id} not found')
    article.update({
        DbArticle.title: request.title,
        DbArticle.content: request.content,
        DbArticle.published: request.published,
        DbArticle.user_id: request.user_id
    })
    db.commit()
    return {'message': 'Article Updated!'}

# delete a single user
def delete_article(db: Session, article_id: int):
    article = db.query(DbArticle).filter(DbArticle.id == article_id).first()
    if article is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'Article with id {article_id} not found')
    db.delete(article)
    db.commit()
