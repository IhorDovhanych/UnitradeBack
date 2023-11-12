from fastapi import APIRouter, Depends
from models import Role
from pydantic_models import RoleModel
from core.session import get_session
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/get_all")
def get_all(db: Session = Depends(get_session)):
    roles = db.query(Role).all()
    return roles

@router.post("/create")
def create_user(item: RoleModel, db: Session = Depends(get_session)):
    role = Role(name=item.name)
    db.add(role)
    db.commit()
    db.refresh(role)
    return role
