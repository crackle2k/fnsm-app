from sqlalchemy.orm import Session

from . import models

SAMPLE_REPORTS = [
    {
        "title": "Break-in at Kensington Market storefront",
        "description": "Front window smashed overnight, cash register disturbed.",
        "category": "break_and_enter",
        "neighbourhood": "Kensington-Chinatown",
        "latitude": 43.6547,
        "longitude": -79.4005,
        "reporter_name": "Anonymous",
    },
    {
        "title": "Bike stolen outside Distillery District",
        "description": "Locked bike cut and taken near Mill St entrance.",
        "category": "theft",
        "neighbourhood": "Distillery District",
        "latitude": 43.6503,
        "longitude": -79.3596,
        "reporter_name": "J. Parker",
    },
    {
        "title": "Vehicle break-in on Liberty Village street parking",
        "description": "Passenger window smashed, glovebox rifled through.",
        "category": "auto_theft",
        "neighbourhood": "Liberty Village",
        "latitude": 43.6373,
        "longitude": -79.4201,
        "reporter_name": None,
    },
]


def seed_if_empty(db: Session) -> None:
    existing = db.query(models.CrimeReport).first()
    if existing is not None:
        return
    for payload in SAMPLE_REPORTS:
        db.add(models.CrimeReport(**payload))
    db.commit()
