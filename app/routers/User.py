from fastapi import APIRouter, Depends, HTTPException, Request
from models import User
from pydantic_models import UserModel
from core.session import get_session
from sqlalchemy.orm import Session
from elastic.controllers import DocumentsController

router = APIRouter()


@router.get("/get_all")
def get_all(db: Session = Depends(get_session)):
    users = db.query(User).all()
    if users is None:
        raise HTTPException(status_code=404, detail="No users in database")
    return [
        {
            "id": str(user.id),
            "name": user.name,
            "email": user.email,
            "role_id": user.role_id,
            "picture": user.picture,
        }
        for user in users
    ]


@router.get("/get_by_id/{id}")
def get_by_id(id: int, db: Session = Depends(get_session)):
    user = db.query(User).filter(User.id == id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {
        "id": str(user.id),
        "name": user.name,
        "email": user.email,
        "role_id": user.role_id,
        "picture": user.picture,
    }


@router.post("/create")
async def create_user(
    req: Request, item: UserModel, db: Session = Depends(get_session)
):
    user = User(
        id=item.id,
        name=item.name,
        email=item.email,
        role_id=item.role_id,
        picture=item.picture,
    )
    if user is None:
        raise HTTPException(status_code=400, detail="Wrong details")
    # * Add to Elastic
    await DocumentsController.create_document(
        req,
        "users",
        {
            "user_id": str(item.id),
            "name": item.name,
            "email": item.email,
            "role_id": item.role_id,
            "picture": item.picture,
        },
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.put("/update/{id}")
async def update_user(
    req: Request, id: int, item: UserModel, db: Session = Depends(get_session)
):
    user = db.query(User).filter(User.id == id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    for key, value in item.dict().items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)
    # * Update Elastic
    await DocumentsController.update_document(
        req,
        "users",
        str(id),
        {
            "name": item.name,
            "email": item.email,
            "role_id": item.role_id,
            "picture": item.picture,
        },
    )

    return user


@router.delete("/delete/{id}")
async def delete_user(req: Request, id: int, db: Session = Depends(get_session)):
    user = db.query(User).filter(User.id == id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    # * Delete from Elastic
    user_id = await DocumentsController.search_document_by_field_with_id(
        req, "users", "user_id", str(id)
    )
    await DocumentsController.delete_document(req, "users", str(user_id))

    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}
