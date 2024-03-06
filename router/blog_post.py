from fastapi import APIRouter, Query, Body
from pydantic import BaseModel
from typing import Optional, List


router = APIRouter(
    prefix = '/blog',
    tags = ['blog']
)

class BlogModel(BaseModel):
    title: str
    content: str
    comment_count: int
    published: Optional[bool]

@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int=1):
    return {
        'id': id,
        'data': blog,
        'version': version,
    }

@router.post('/new/{id}/comment')
def create_comment(blog: BlogModel, id: int, 
        comment_id: int = Query(None,
            title="id of the comment",
            description="some random desc for comment_id"
        ),
        content: str = Body('tests'),
        version: List[str]=Query(None)
    ):
    return {
        'Blog' : blog,
        'id': id,
        'comment_id': comment_id,
        'content': content
    }

def required_functionality():
    return {"message": "Learning Fastapi is important"}