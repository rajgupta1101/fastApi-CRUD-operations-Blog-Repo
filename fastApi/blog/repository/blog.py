from sqlalchemy.orm import Session
from .. import models,schemas
from fastapi import HTTPException,status

def get_all(db:Session):
    blogs=db.query(models.Blog).all()
    return blogs
    
    
def create(db:Session,request:schemas.Blog):
    new_blog=models.Blog(title=request.title,body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(id:int,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog not found with {id} id ")
    blog.delete(synchronize_session=False)
    db.commit()
    return {'data':'detele successfully'}

def update(id:int,db:Session,request:schemas.Blog):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog not found with {id} id ")

    blog.update(request.model_dump())
    db.commit()
    return 'updated'

def show(id:int,db:Session,response):
    breakpoint()
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        # raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog not fount with id {id}")
        response.status_code=status.HTTP_404_NOT_FOUND
        return {'detail':f"blog not fount with id {id}"}
    return blog