from fastapi import APIRouter, Depends, HTTPException
from models import User, UserModel
from session import get_session
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/get_all")
def get_all(db: Session = Depends(get_session)):
    users = db.query(User).all()
    if users is None:
        raise HTTPException(status_code=404, detail="No users in database")
    return users

@router.get("/get_by_id/{id}")
def get_by_id(id: int, db: Session = Depends(get_session)):
    user = db.query(User).filter(User.id == id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/create")
def create_user(item: UserModel, db: Session = Depends(get_session)):
    user = User(
        name=item.name,
        password=item.password,
        email=item.email,
        jwt_token=item.jwt_token,
        role_id=item.role_id,
    )
    if user is None:
        raise HTTPException(status_code=400, detail="Wrond details")
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.put("/update/{id}")
def update_user(id: int, item: UserModel, db: Session = Depends(get_session)):
    user = db.query(User).filter(User.id == id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    for key, value in item.dict().items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)
    return user
