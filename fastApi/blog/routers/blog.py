from fastapi import APIRouter,Depends,status,HTTPException,Response
from .. import schemas,database,models,oauth2
from typing import List
from sqlalchemy.orm import Session
from ..repository import blog


get_db=database.get_db
router=APIRouter(
    tags=['Blogs'],
    prefix='/blog'
)



@router.get('/',response_model=List[schemas.ShowBlog])
def all(db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.get_all(db)



@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=schemas.ShowBlog)
def show(id,response:Response,db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    breakpoint()
    return blog.show(id,db,response)


@router.post('/',status_code=status.HTTP_201_CREATED)
def create(request:schemas.Blog,db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.create(db,request)


@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request:schemas.Blog, db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.update(id,db,request)



@router.delete('/{id}',status_code=status.HTTP_200_OK)
def destroy(id:int,db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.destroy(id,db)
