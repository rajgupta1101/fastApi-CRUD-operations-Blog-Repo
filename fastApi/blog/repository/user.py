from .. import schemas,models
from sqlalchemy.orm import Session
from ..hashing import Hash
from fastapi import HTTPException,status



def create(request:schemas.User,db:Session):
    # new_user=models.User(**request.model_dump())
    new_user=models.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def show(id,db):
    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user not found with {id} id ")
    return user