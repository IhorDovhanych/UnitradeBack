from fastapi import APIRouter, Depends
from models import Role, RoleModel
from session import get_session
from sqlalchemy.orm import Session

router = APIRouter()

@router.post('/role/create')
def create_user(item: RoleModel,  db: Session = Depends(get_session)):
    role = Role(name=item.name)
    db.add(role)
    db.commit()
    db.refresh(role)
    return role