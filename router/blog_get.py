from fastapi import APIRouter, status , Path, Response, Depends
from enum import Enum
from typing import Optional
from router.blog_post import required_functionality

router = APIRouter(
    prefix = '/blog',
    tags = ['blog']
)

# @router.get('')
# def get_all_blogs():
#     return {'message': f'All Blogs Section'}

@router.get('/all',
        summary='retrieves all blog',
        description='endpoint for retrieving all blogs in the db',
        response_description='The list of all available blogs')
def get_all_blogs(page=1, page_size: Optional[int] = None, req_param: dict=Depends(required_functionality)):
    return {'message': f'All {page_size} blogs on page {page}', 'req':req_param}

# @router.get('/blog/{page}')
# def get_blog(page,  page_size: Optional[int] = None):
#     return {'message': f'All {page_size} blogs on page {page}'}

class BlogType(str, Enum):
    a = 'a'
    b = 'b'
    howto = 'howto'

@router.get('/type/{type}')
def get_blog_type(type: BlogType):
    return {'message': f'Blog type of {type.value}'}

@router.get('/{id}/comments/{comment_id}', tags=['comment'])
def get_comment(id: int, comment_id: int, valid: bool=True, username: Optional[str]=None):
    """
    Retrieving a comment of a blog

    - **id** mandatory path parameter 
    """
    return {'message:': f'Blog {id}, Comment {comment_id}, Valid {valid}, Username {username}'}

@router.get('/{id}', status_code=status.HTTP_200_OK) 
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'message': f'blog with id of {id} not found'}
    else:
        return {'message': f'blog with id of {id}'}
