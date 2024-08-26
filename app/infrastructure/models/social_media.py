from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey
from app import db


if TYPE_CHECKING:
    from .post import Post
    from .parlamentar import Parlamentar


class SocialMedia(db.Model):
    """Social Media Model"""

    venue: Mapped[str] = mapped_column(String)
    handle: Mapped[str] = mapped_column(String)
    followers_count: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(String)
    links: Mapped[str] = mapped_column(String)
    posts: Mapped["Post"] = relationship(
        "Post", back_populates="social_media", cascade="all, delete", passive_deletes=True
    )
    parlamentar_id = mapped_column(ForeignKey("parlamentar.id", ondelete="CASCADE"))
    parlamentar: Mapped["Parlamentar"] = relationship(
        "Parlamentar", back_populates="social_media", cascade="all, delete"
    )
