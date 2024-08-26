# """ Base Model """

# from datetime import date
# from typing import List
# from sqlalchemy.orm import Mapped, mapped_column, relationship
# from sqlalchemy import Integer, String, ForeignKey, Date
# from app import db


# class Parlamentar(db.Model):
#     """Parlamentar Model"""

#     id: Mapped[int]
#     first_name: Mapped[str] = mapped_column(String)
#     last_name: Mapped[str] = mapped_column(String)
#     mandate: Mapped[str] = mapped_column(String)
#     dob: Mapped[date] = mapped_column(Date)
#     posts: Mapped[List] = relationship(back_populates="parlamentar", cascade="all, delete", passive_deletes=True)
#     social_media: Mapped[List] = relationship(back_populates="parlamentar", cascade="all, delete", passive_deletes=True)


# class SocialMedia(db.Model):
#     """Social Media Model"""

#     venue: Mapped[str] = mapped_column(String)
#     handle: Mapped[str] = mapped_column(String)
#     followers_count: Mapped[int] = mapped_column(Integer)
#     description: Mapped[str] = mapped_column(String)
#     links: Mapped[str] = mapped_column(String)
#     post_id = mapped_column(ForeignKey("post.id", ondelete="CASCADE"))
#     post: Mapped["Post"] = relationship(
#         "Post", back_populates="social_media", cascade="all, delete", passive_deletes=True
#     )
#     parlamentar_id = mapped_column(ForeignKey("parlamentar.id", ondelete="CASCADE"))
#     parlamentar: Mapped["Parlamentar"] = relationship(
#         "Parlamentar", back_populates="social_media", cascade="all, delete"
#     )


# class Post(db.Model):
#     """Post Model"""

#     url: Mapped[str] = mapped_column()
#     media: Mapped[str] = mapped_column()
#     views_count: Mapped[int] = mapped_column()
#     comments_count: Mapped[int] = mapped_column()
#     reposts_count: Mapped[int] = mapped_column()
#     likes_count: Mapped[int] = mapped_column()
#     content: Mapped[str] = mapped_column()
#     contain_fake_news: Mapped[bool] = mapped_column()
#     social_media_id: Mapped[int] = mapped_column(ForeignKey("social_media.id", ondelete="CASCADE"))
#     social_media: Mapped["SocialMedia"] = relationship("SocialMedia", back_populates="posts")
#     parlamentar_id: Mapped[int] = mapped_column(ForeignKey("parlamentar.id", ondelete="CASCADE"))
#     parlamentar: Mapped["Parlamentar"] = relationship("Parlamentar", back_populates="posts")
#     post_date: Mapped[str] = mapped_column()
