from fastapi import FastAPI, Path
from enum import Enum
#test

app = FastAPI()

@app.get('/')
def index():
    return {'message': 'Hello World'}

@app.get('/blog')
def get_blog():
    return {'message': f'All Blogs Section'}

class BlogType(str, Enum):
    a = 'a'
    b = 'b'
    howto = 'howto'

@app.get('/blog/type/{temp}')
def get_blog_type(temp: str = Path(..., description="The type of the blog")):
    return {'message': f'Blog type of {temp}'}

@app.get('/blog/{id}') 
def get_blog(id: int):
    return {'message': f'blog with id of {id}'}