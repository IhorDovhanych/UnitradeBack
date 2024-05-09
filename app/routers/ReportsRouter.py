from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from models import ReportModel
from controllers import ReportsController
from core.session import get_session

router = APIRouter()


@router.get("/")
async def get_reports(page: int = 0, limit: int = 10, db: Session = Depends(get_session)):
    return await ReportsController.get_reports(page, limit, db)


@router.get("/{id}")
async def get_report(id: int, db: Session = Depends(get_session)):
    return await ReportsController.get_report(id, db)


@router.post("/create")
async def create_report(item: ReportModel = Depends(), db: Session = Depends(get_session)):
    return await ReportsController.create_report(item, db)


@router.put("/update/{id}")
async def update_report(id: int, item: ReportModel, db: Session = Depends(get_session)):
    return await ReportsController.update_report(id, item, db)


@router.delete("/delete/{id}")
async def delete_report(id: int, db: Session = Depends(get_session)):
    return await ReportsController.delete_report(id, db)
