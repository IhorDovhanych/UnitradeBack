from fastapi import Response, HTTPException, status

from models import Report


class ReportsController:
    @staticmethod
    async def get_reports(page, limit, db):
        reports = (
            db.query(Report)
            .limit(limit)
            .offset(page * limit)
            .all()
        )

        return {"response": reports}

    @staticmethod
    async def get_report(id, db):
        report = (
            db.query(Report)
            .filter(Report.id == id)
            .first()
        )

        if report is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Report with such id not found")
        else:
            return {"response": report}

    @staticmethod
    async def create_report(item, db):
        report = Report(**item.dict())
        db.add(report)
        db.commit()

        return Response("Successfully created", 201)

    @staticmethod
    async def update_report(id, item, db):
        report = db.query(Report).filter(Report.id == id)
        if report.first() is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Report with such id not found")
        else:
            report.update(item.dict())
            db.commit()

        return Response("Successfully updated", 200)

    @staticmethod
    async def delete_report(id, db):
        report = db.query(Report).get(id)
        if report is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post with such id not found")
        else:
            db.delete(report)
            db.commit()

        return Response("Successfully deleted", 200)
