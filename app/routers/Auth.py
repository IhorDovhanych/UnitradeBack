import json
import os
from fastapi import APIRouter, Depends, HTTPException, Request
from pydantic_models import UserModel
from core.session import get_session
from sqlalchemy.orm import Session
from auth.credential_handler import get_creds
from googleapiclient.discovery import build
from routers import User as UserRouter
from pydantic_models import UserModel
import google.auth.transport.requests


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = (
    "D:\\Projects\\UnitradeBack\\app\\auth\\unitrade-404519-22f4096c1235.json"
)

router = APIRouter()


@router.get("/")
async def auth(req: Request, db: Session = Depends(get_session),):
    creds = get_creds()
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
        await UserRouter.create_user(req, item=user_model, db=db)
    return {
        "token": creds.token,
        "refresh_token": creds.refresh_token,
        "expiry": creds.expiry,
    }


@router.get("/login")
def login(google_token: str, db: Session = Depends(get_session)):
    creds = get_creds_login(token=google_token)
    user_info_service = build("oauth2", "v2", credentials=creds)
    user_info = user_info_service.userinfo().get().execute()
    try:
        user = UserRouter.get_by_id(id=user_info["id"], db=db)
        return {"login_status": True}
    except:
        raise HTTPException(status_code=401, detail="Invalid Google Token")


@router.get("/refresh_token")
def refresh_google_token(token: str, db: Session = Depends(get_session)):
    new_creds = refresh_token(refresh_token=token)
    if new_creds is None:
        raise HTTPException(status_code=401, detail="Invalid Refresh Token")
    return {
        "token": new_creds["token"],
        "refresh_token": new_creds["refresh_token"],
        "expiry": new_creds["expiry"],
    }


from google.oauth2.credentials import Credentials


def get_creds_login(token: str):
    return Credentials(token)


def refresh_token(refresh_token):
    with open("auth/creds.json") as f:
        creds_data = json.load(f)

    creds = Credentials(
        token=None,
        refresh_token=refresh_token,
        token_uri="https://oauth2.googleapis.com/token",
        client_id=creds_data["installed"]["client_id"],
        client_secret=creds_data["installed"]["client_secret"],
    )
    creds.refresh(google.auth.transport.requests.Request())
    return {
        "token": creds.token,
        "refresh_token": creds.refresh_token,
        "expiry": creds.expiry,
    }
