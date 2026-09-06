import enum
from datetime import datetime, timezone

from sqlalchemy import DateTime, Enum, Float, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base
from .toronto import CRIME_CATEGORIES


class ReportStatus(str, enum.Enum):
    reported = "reported"
    under_review = "under_review"
    resolved = "resolved"


CrimeCategory = enum.Enum("CrimeCategory", {name: name for name in CRIME_CATEGORIES})


class CrimeReport(Base):
    __tablename__ = "crime_reports"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(120), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    category: Mapped[str] = mapped_column(
        Enum(CrimeCategory, native_enum=False, length=32), nullable=False
    )
    neighbourhood: Mapped[str] = mapped_column(String(80), nullable=False, index=True)
    latitude: Mapped[float | None] = mapped_column(Float, nullable=True)
    longitude: Mapped[float | None] = mapped_column(Float, nullable=True)
    reporter_name: Mapped[str | None] = mapped_column(String(80), nullable=True)
    status: Mapped[str] = mapped_column(
        Enum(ReportStatus, native_enum=False, length=32),
        nullable=False,
        default=ReportStatus.reported,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=lambda: datetime.now(timezone.utc)
    )
