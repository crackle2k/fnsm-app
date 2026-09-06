from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from . import crud, schemas
from .database import Base, engine, get_db
from .seed import seed_if_empty
from .toronto import CRIME_CATEGORIES, TORONTO_NEIGHBOURHOODS

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FNSM API",
    description="Friendly Neighbourhood Spider-Man API — crime reporting for Toronto.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup() -> None:
    db = next(get_db())
    try:
        seed_if_empty(db)
    finally:
        db.close()


@app.get("/api/health")
def health_check() -> dict:
    return {"status": "ok", "city": "Toronto"}


@app.get("/api/neighbourhoods")
def list_neighbourhoods() -> list[str]:
    return TORONTO_NEIGHBOURHOODS


@app.get("/api/categories")
def list_categories() -> list[str]:
    return CRIME_CATEGORIES


@app.get("/api/crimes", response_model=list[schemas.CrimeReportOut])
def list_crimes(
    neighbourhood: str | None = None,
    category: str | None = None,
    limit: int = 100,
    offset: int = 0,
    db: Session = Depends(get_db),
):
    return crud.list_crime_reports(
        db, neighbourhood=neighbourhood, category=category, limit=limit, offset=offset
    )


@app.post("/api/crimes", response_model=schemas.CrimeReportOut, status_code=201)
def report_crime(report: schemas.CrimeReportCreate, db: Session = Depends(get_db)):
    return crud.create_crime_report(db, report)


@app.get("/api/crimes/{report_id}", response_model=schemas.CrimeReportOut)
def get_crime(report_id: int, db: Session = Depends(get_db)):
    db_report = crud.get_crime_report(db, report_id)
    if db_report is None:
        raise HTTPException(status_code=404, detail="Crime report not found")
    return db_report


@app.patch("/api/crimes/{report_id}", response_model=schemas.CrimeReportOut)
def update_crime_status(
    report_id: int, update: schemas.CrimeReportUpdate, db: Session = Depends(get_db)
):
    db_report = crud.update_crime_report_status(db, report_id, update.status)
    if db_report is None:
        raise HTTPException(status_code=404, detail="Crime report not found")
    return db_report
