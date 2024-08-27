""" SQLAlchemy Parlamentar Model """

from typing import TYPE_CHECKING, List
from datetime import date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Date
from app import db

if TYPE_CHECKING:
    from .social_media import SocialMedia


class Parlamentar(db.Model):
    """Parlamentar Model"""

    first_name: Mapped[str] = mapped_column(String)
    last_name: Mapped[str] = mapped_column(String)
    mandate: Mapped[str] = mapped_column(String)
    dob: Mapped[date | None] = mapped_column(Date, nullable=True)
    social_media: Mapped[List["SocialMedia"]] = relationship(
        back_populates="parlamentar",
        cascade="all, delete",
        passive_deletes=True,
    )
