from fastapi import APIRouter,status,Depends,HTTPException
from .. import database,schemas,models
from sqlalchemy.orm import Session
from ..repository import user

get_db=database.get_db

router=APIRouter(
    tags=['Users'],
    prefix='/user'
)

@router.post('/',status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(request: schemas.User,db:Session=Depends(get_db)):
    return user.create(request,db)
    

@router.get('/{id}',response_model=schemas.ShowUser)
def get_user(id:int,db:Session=Depends(get_db)):
    return user.show(id,db)
    