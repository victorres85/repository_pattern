""" Social Media Schemas """

from typing import Optional, List, Annotated, TYPE_CHECKING, Dict
from pydantic import BaseModel, Field, BeforeValidator
from .helpers import (
    parse_date_to_str,
    parse_str_to_int,
    ensure_lowercase,
    split_links,
    join_links,
)

if TYPE_CHECKING:
    from .parlamentar_schema import ParlamentarFilter


class SocialMediaBase(BaseModel):
    """Base Model for SocialMedia"""

    venue: Annotated[str, BeforeValidator(ensure_lowercase)] = Field(
        description="Social Media Platform"
    )
    handle: str = Field(description="Social Media Handle")
    followers_count: Annotated[int, BeforeValidator(parse_str_to_int)] = Field(
        None, description="Total number of followers"
    )
    description: Optional[str] = Field(
        None, description="Social Media Description"
    )
    links: Annotated[Optional[List[str]], BeforeValidator(split_links)] = Field(
        [], description="Social Media Urls separeted by comma"
    )


class SocialMediaCreate(SocialMediaBase):
    """Social Media Create Schema"""

    pass


class SocialMediaUpdate(SocialMediaBase):
    """Social Media Update Schema"""

    id: int
    venue: Annotated[Optional[str], BeforeValidator(ensure_lowercase)] = None
    handle: Optional[str] = None


class SocialMediaResponse(SocialMediaBase):
    """Social Media Response Schema"""

    id: int
    links: Annotated[Optional[str], BeforeValidator(join_links)] = ""
    added: Annotated[Optional[str], BeforeValidator(parse_date_to_str)] = Field(
        None,
        description="Date parlamentar social-media account has been added to the system in YYYY-MM-DD format",
    )
    updated: Annotated[Optional[str], BeforeValidator(parse_date_to_str)] = (
        Field(
            None,
            description="Date parlamentar social-media account has been updated to the system in YYYY-MM-DD format",
        )
    )

    posts: Optional[List[Dict]] = []
    social_media: Optional[List[Dict]] = []


class SocialMediaFilter(BaseModel):
    """Social Media Filter Schema"""

    venue: Annotated[Optional[str], BeforeValidator(ensure_lowercase)] = Field(
        description="Social Media Platform"
    )
    handle: Optional[str]
    followers_count: Annotated[
        Optional[int | str], BeforeValidator(parse_str_to_int)
    ] = Field(None, description="Total number of followers")
    description: Optional[str] = Field(
        None, description="Social Media Description"
    )
    parlamentar: Optional["ParlamentarFilter"] = Field(None)


class SocialMediaGet(BaseModel):
    """Social Media Get Schema"""

    id: Annotated[int | str, BeforeValidator(parse_str_to_int)] = Field(
        None, description="Social Media id"
    )
