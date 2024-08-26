""" Post Schemas """

from datetime import date
from typing import Optional, Annotated, List, TYPE_CHECKING
from pydantic import BaseModel, Field, BeforeValidator
from .helpers import parse_date_to_str, parse_str_to_date, parse_str_to_int, parse_bool


if TYPE_CHECKING:
    from .parlamentar_schema import ParlamentarResponse
    from .social_media_schema import SocialMediaResponse


class PostBase(BaseModel):
    """Base Model for Post"""

    url: str = Field(description="Post url")
    media: Optional[str] = Field(None, description="Post Media url")
    views_count: Annotated[Optional[int], BeforeValidator(parse_str_to_int)] = Field(
        None, description="Post Views Count"
    )
    comments_count: Annotated[Optional[int], BeforeValidator(parse_str_to_int)] = Field(
        None, description="Post Comments Count"
    )
    reposts_count: Annotated[Optional[int], BeforeValidator(parse_str_to_int)] = Field(
        None, description="Post Reposts Count"
    )
    likes_count: Annotated[Optional[int], BeforeValidator(parse_str_to_int)] = Field(
        None, description="Post Likes Count"
    )
    content: Optional[str] = Field(None, description="Post Content")
    contain_fake_news: Annotated[Optional[bool], BeforeValidator(parse_bool)] = Field(
        None, description="Does Post Contain Fake News"
    )
    published_on: Annotated[date, BeforeValidator(parse_str_to_date)] = Field(
        description="Date in which post has been published in YYYY-MM-DD format"
    )


class PostCreate(PostBase):
    """Post Create Schema"""

    pass


class PostUpdate(PostBase):
    """Post Update Schema"""

    url: Optional[str] = None


class PostResponse(PostBase):
    """Post Response Schema"""

    id: int
    views_count: Optional[int] = Field(None, description="Post Views Count")
    comments_count: Optional[int] = Field(None, description="Post Comments Count")
    reposts_count: Optional[int] = Field(None, description="Post Reposts Count")
    likes_count: Optional[int] = Field(None, description="Post Likes Count")
    content: Optional[str] = Field(None, description="Post Content")
    contain_fake_news: Optional[bool] = Field(None, description="Does Post Contain Fake News")
    published_on: Annotated[str, BeforeValidator(parse_date_to_str)] = Field(
        None, description="Date in which post has been published in YYYY-MM-DD format"
    )
    added: Annotated[str, BeforeValidator(parse_date_to_str)] = Field(
        None, description="Date parlamentar post account has been added to the system in YYYY-MM-DD format"
    )
    updated: Annotated[str, BeforeValidator(parse_date_to_str)] = Field(
        None, description="Date parlamentar post account has been updated to the system in YYYY-MM-DD format"
    )

    parlamentar: Optional[List["ParlamentarResponse"]] = []
    social_media: Optional[List["SocialMediaResponse"]] = []


class PostFilter(PostBase):
    """Post Filter Schema"""

    url: Optional[str] = None
    page: Annotated[Optional[int], BeforeValidator(parse_str_to_int)] = Field(1, description="Post Views Count")
    limit: Annotated[Optional[int], BeforeValidator(parse_str_to_int)] = Field(10, description="Post Views Count")


class PostGet(BaseModel):
    """Post Get Schema"""

    id: Annotated[int, BeforeValidator(parse_str_to_int)] = Field(None, description="Post id")
