""" Parlamentar Schemas """

from datetime import date
from abc import ABC
from typing import Optional, Annotated, List, Dict
from pydantic import BaseModel, Field, BeforeValidator
from .helpers import (
    parse_str_to_date,
    parse_date_to_str,
    ensure_lowercase,
    parse_str_to_int,
)


class ModelInterface(BaseModel, ABC):
    """Interface for Models"""


class ParlamentarBase(BaseModel):
    """Base Model for Parlamentar"""

    first_name: Annotated[str, BeforeValidator(ensure_lowercase)] = Field(
        description="First name of the parlamentar"
    )
    last_name: Annotated[str, BeforeValidator(ensure_lowercase)] = Field(
        description="Last name of the parlamentar"
    )
    mandate: Annotated[str, BeforeValidator(ensure_lowercase)] = Field(
        description="Mandate type of the parlamentar"
    )
    dob: Annotated[Optional[date], BeforeValidator(parse_str_to_date)] = Field(
        None,
        description="Date of birth of the parlamentar",
    )


class ParlamentarCreate(ParlamentarBase):
    """Parlamentar Create Schema"""

    pass


class ParlamentarUpdate(ParlamentarBase):
    """Parlamentar Update Schema"""

    id: int
    first_name: Annotated[Optional[str], BeforeValidator(ensure_lowercase)] = (
        Field(None, description="First name of the parlamentar")
    )
    last_name: Annotated[Optional[str], BeforeValidator(ensure_lowercase)] = (
        Field(None, description="Last name of the parlamentar")
    )
    mandate: Annotated[Optional[str], BeforeValidator(ensure_lowercase)] = (
        Field(None, description="Mandate type of the parlamentar")
    )


class ParlamentarResponse(BaseModel):
    """Parlamentar Response Schema"""

    id: int
    first_name: str
    last_name: str
    mandate: Optional[str] = None
    dob: Annotated[Optional[str], BeforeValidator(parse_date_to_str)] = Field(
        None,
        description="Date of birth of the parlamentar",
    )
    added: Annotated[str, BeforeValidator(parse_date_to_str)] = Field(
        None,
        description="Date post account has been added to the system",
    )
    updated: Annotated[str, BeforeValidator(parse_date_to_str)] = Field(
        None,
        description="Date post account has been updated to the system",
    )

    posts: Optional[List[Dict]] = [{}]
    social_media: Optional[List[Dict]] = [{}]


class ParlamentarFilter(BaseModel):
    """Parlamentar Filter Schema"""

    first_name: Annotated[Optional[str], BeforeValidator(ensure_lowercase)] = (
        Field(None, description="First name of the parlamentar")
    )
    last_name: Annotated[Optional[str], BeforeValidator(ensure_lowercase)] = (
        Field(None, description="Last name of the parlamentar")
    )
    mandate: Annotated[Optional[str], BeforeValidator(ensure_lowercase)] = (
        Field(None, description="Mandate type of the parlamentar")
    )
    dob: Annotated[Optional[date], BeforeValidator(parse_str_to_date)] = Field(
        None,
        description="Date of birth of the parlamentar",
    )
    page: Annotated[Optional[int], BeforeValidator(parse_str_to_int)] = Field(
        1, description="Page number for pagination"
    )
    limit: Annotated[Optional[int], BeforeValidator(parse_str_to_int)] = Field(
        10, description="Number of records per page"
    )


class ParlamentarGet(BaseModel):
    """Parlamentar Get Schema"""

    id: Annotated[int, BeforeValidator(parse_str_to_int)] = Field(
        description="Parlamentar id"
    )
