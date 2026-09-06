from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator

from .models import ReportStatus
from .toronto import CRIME_CATEGORIES, TORONTO_BOUNDS


class CrimeReportBase(BaseModel):
    title: str = Field(min_length=3, max_length=120)
    description: str = Field(min_length=10, max_length=2000)
    category: str
    neighbourhood: str = Field(min_length=2, max_length=80)
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    reporter_name: Optional[str] = Field(default=None, max_length=80)

    @field_validator("category")
    @classmethod
    def category_must_be_known(cls, value: str) -> str:
        if value not in CRIME_CATEGORIES:
            raise ValueError(
                f"category must be one of: {', '.join(CRIME_CATEGORIES)}"
            )
        return value

    @field_validator("latitude")
    @classmethod
    def latitude_within_toronto(cls, value: Optional[float]) -> Optional[float]:
        if value is None:
            return value
        if not (TORONTO_BOUNDS["min_lat"] <= value <= TORONTO_BOUNDS["max_lat"]):
            raise ValueError("latitude must fall within the City of Toronto")
        return value

    @field_validator("longitude")
    @classmethod
    def longitude_within_toronto(cls, value: Optional[float]) -> Optional[float]:
        if value is None:
            return value
        if not (TORONTO_BOUNDS["min_lng"] <= value <= TORONTO_BOUNDS["max_lng"]):
            raise ValueError("longitude must fall within the City of Toronto")
        return value


class CrimeReportCreate(CrimeReportBase):
    pass


class CrimeReportUpdate(BaseModel):
    status: ReportStatus


class CrimeReportOut(CrimeReportBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    status: ReportStatus
    created_at: datetime
