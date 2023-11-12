from fastapi import APIRouter, Depends, HTTPException
from models import User
from pydantic_models import UserModel
from core.session import get_session
from sqlalchemy.orm import Session
from oauth.credential_handler import get_creds, SCOPES
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from routers import User as UserRouter
from pydantic_models import UserModel

router = APIRouter()


@router.get("/")
def auth(db: Session = Depends(get_session)):
    get_creds()
    creds = Credentials.from_authorized_user_file("core/token.json", SCOPES)
    user_info_service = build("oauth2", "v2", credentials=creds)
    user_info = user_info_service.userinfo().get().execute()
    try:
        UserRouter.get_by_id(id=user_info["id"], db=db)
    except:
        user_model = UserModel(
            id=user_info["id"],
            name=user_info["name"],
            email=user_info["email"],
            picture=user_info["picture"],
            role_id=1,
        )
        UserRouter.create_user(item=user_model, db=db)


@router.get("/test")
def test():
    creds = Credentials.from_authorized_user_file("core/token.json", SCOPES)
    user_info_service = build("oauth2", "v2", credentials=creds)
    user_info = user_info_service.userinfo().get().execute()
    print(user_info)
