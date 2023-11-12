from fastapi import APIRouter, Depends, UploadFile, Query
from sqlalchemy.orm import Session

from models import PostModel
# from controllers import PostController
from session import get_session

ReportsRouter = APIRouter(prefix="/api/reports", tags=["Reports API"])


@ReportsRouter.get("/")
async def get_reports():
    pass


@ReportsRouter.get("/{id}")
async def get_report():
    pass


@ReportsRouter.post("/create")
async def create_report():
    pass


@ReportsRouter.put("/update/{id}")
async def update_post():
    pass


@ReportsRouter.delete("/delete/{id}")
async def delete_post():
    pass
