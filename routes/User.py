from fastapi import APIRouter, Depends
from models import User, UserModel
from session import get_session
from sqlalchemy.orm import Session

router = APIRouter()

@router.post('/user/create')
def create_user(item: UserModel,  db: Session = Depends(get_session)):
    user = User(
        name=item.name,
        password=item.password,
        email=item.email,
        jwt_token=item.jwt_token,
        role_id=item.role_id,
        )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user