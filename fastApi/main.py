from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app= FastAPI()


@app.get('/')
def index():
    return {'data':{'name': 'raj'}}


@app.get('/blog')

def index(limit=10,published: bool=True,sort:Optional[str]=None):
    if(published):
        return {'data':f'{limit} published blog from db {sort}'}
    else :
        return {'data':f'{limit} blog from db'}


@app.get('/about')

def about():
    return {'data':{'fgg':'about page'}}




@app.get('/blog/{id}')

def show(id: int):
    return {'data':id}


@app.get('/blog/{id}/comments')

def comments(id):
    return {'data':{'1','2'}}


class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]=None
    


@app.post('/blog')
def create_blog(blog: Blog):
    return {'data':f'Blog is created with title as {blog.title}'} 


# if __name__ == '__main__':
#     uvicorn.run(app,host='127.0.0.1',port=9000)