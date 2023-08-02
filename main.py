from fastapi import FastAPI
from blog_type import BlogType

app = FastAPI()

@app.get('/')
def index():
    return {'message': 'Hello world!'}

@app.get('/blog/all')
def get_all_blogs():
    return  { 'message': 'All blogs provided'}

@app.get('/blog/type/{type}')
def get_blog_type(type: BlogType):
    return { 'message': f'Blog type {type}'}

@app.get('/blog/{id}')
def get_blog(id: int):
    return {'message': f'Blog with id {id}'}

