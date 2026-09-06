from typing import Optional

from sqlalchemy import select
from sqlalchemy.orm import Session

from . import models, schemas


def create_crime_report(db: Session, report: schemas.CrimeReportCreate) -> models.CrimeReport:
    db_report = models.CrimeReport(**report.model_dump())
    db.add(db_report)
    db.commit()
    db.refresh(db_report)
    return db_report


def get_crime_report(db: Session, report_id: int) -> Optional[models.CrimeReport]:
    return db.get(models.CrimeReport, report_id)


def list_crime_reports(
    db: Session,
    neighbourhood: Optional[str] = None,
    category: Optional[str] = None,
    limit: int = 100,
    offset: int = 0,
) -> list[models.CrimeReport]:
    stmt = select(models.CrimeReport).order_by(models.CrimeReport.created_at.desc())
    if neighbourhood:
        stmt = stmt.where(models.CrimeReport.neighbourhood == neighbourhood)
    if category:
        stmt = stmt.where(models.CrimeReport.category == category)
    stmt = stmt.offset(offset).limit(limit)
    return list(db.execute(stmt).scalars().all())


def update_crime_report_status(
    db: Session, report_id: int, status: models.ReportStatus
) -> Optional[models.CrimeReport]:
    db_report = get_crime_report(db, report_id)
    if db_report is None:
        return None
    db_report.status = status
    db.commit()
    db.refresh(db_report)
    return db_report
