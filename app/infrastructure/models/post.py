from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey, Boolean
from app import db

if TYPE_CHECKING:
    from .social_media import SocialMedia


class Post(db.Model):
    """Post Model"""

    url: Mapped[str] = mapped_column(String)
    media: Mapped[str] = mapped_column(String)
    views_count: Mapped[int] = mapped_column(Integer)
    comments_count: Mapped[int] = mapped_column(Integer)
    reposts_count: Mapped[int] = mapped_column(Integer)
    likes_count: Mapped[int] = mapped_column(Integer)
    content: Mapped[str] = mapped_column(String)
    contain_fake_news: Mapped[bool] = mapped_column(Boolean)
    social_media_id: Mapped[int] = mapped_column(
        ForeignKey("social_media.id", ondelete="CASCADE")
    )
    social_media: Mapped["SocialMedia"] = relationship(
        "SocialMedia", back_populates="posts", cascade="all, delete"
    )
    post_date: Mapped[str] = mapped_column(String)
