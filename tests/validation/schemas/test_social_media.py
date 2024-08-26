""" Test Social Media Schemas """

import json
from datetime import date
from pydantic import ValidationError
import pytest
from app.validation.schemas import social_media_schema as sms

ADDED_DATE = date(2024, 8, 8)
ADDED_STR = "2024-08-08"
UPDATED_DATE = date(2024, 8, 9)
UPDATED_STR = "2024-08-09"
DOB_DATE = date(2024, 8, 7)
DOB_STR = "2024-08-07"


payload_error = {
    "no_first_name": {
        "last_name": "RICK",
        "mandate": "senador",
        "dob": "1985-06-17",
    },
    "no_last_name": {
        "first_name": "ALAN",
        "mandate": "senador",
        "dob": "1985-06-17",
    },
    "no_mandate": {
        "first_name": "ALAN",
        "last_name": "RICK",
        "dob": "1985-06-17",
    },
    "wrong_date_format_DD-MM-YYYY": {
        "first_name": "ALAN",
        "last_name": "RICK",
        "mandate": "senador",
        "dob": "17-06-1985",
    },
    "wrong_date_format_YYYY,MM,DD": {
        "first_name": "ALAN",
        "last_name": "RICK",
        "mandate": "senador",
        "dob": "1985,06,17",
    },
    "wrong_date_format_YY-MM-DD": {
        "first_name": "ALAN",
        "last_name": "RICK",
        "mandate": "senador",
        "dob": "85-06-17",
    },
    "wrong_date_format_YYYYMMDD": {
        "first_name": "ALAN",
        "last_name": "RICK",
        "mandate": "senador",
        "dob": "19850617",
    },
}


def test_social_media_create():
    payload = {
        "venue": "Instagram",
        "handle": "guilhermeboulos.oficial",
        "followers_count": 14432,
        "description": "Social Media account description",
        "links": "link1, link2, link3",
    }
    links_response = ["link1", "link2", "link3"]
    request = json.dumps(payload)

    social_media = sms.SocialMediaCreate.model_validate_json(request)

    assert social_media.venue == payload["venue"].lower()
    assert social_media.handle == payload["handle"]
    assert social_media.followers_count == payload["followers_count"]
    assert social_media.description == payload["description"]
    assert social_media.links == links_response


def test_social_media_update():
    payload = {
        "venue": {
            "id": 1,
            "venue": "Instagram",
        },
        "handle": {
            "id": 1,
            "handle": "guilhermeboulos.oficial",
        },
        "followers_count": {
            "id": 1,
            "followers_count": 14432,
        },
        "description": {"id": 1, "description": "Social Media account description"},
    }
    venue = json.dumps(payload["venue"])
    social_media = sms.SocialMediaUpdate.model_validate_json(venue)
    assert social_media.venue == payload["venue"]["venue"].lower()

    handle = json.dumps(payload["handle"])
    social_media = sms.SocialMediaUpdate.model_validate_json(handle)
    assert social_media.handle == payload["handle"]["handle"]

    followers_count = json.dumps(payload["followers_count"])
    social_media = sms.SocialMediaUpdate.model_validate_json(followers_count)
    assert social_media.followers_count == payload["followers_count"]["followers_count"]

    venue = json.dumps(payload["venue"])
    social_media = sms.SocialMediaUpdate.model_validate_json(venue)
    assert social_media.venue == payload["venue"]["venue"].lower()


def test_social_media_response():

    response = {
        "id": 1,
        "venue": "Instagram",
        "handle": "RICK",
        "followers_count": 1000,
        "description": "Social Media Description",
        "links": ["link1", "link2", "link3"],
        "added": ADDED_STR,
        "updated": UPDATED_STR,
        "posts": [],
        "social_media": [],
    }

    social_media = sms.SocialMediaResponse(**response)

    assert social_media.id == response["id"]
    assert social_media.venue == response["venue"].lower()
    assert social_media.handle == response["handle"]
    assert social_media.followers_count == response["followers_count"]
    assert social_media.description == response["description"]
    assert social_media.links == "link1,link2,link3"


###########################
"""CARRY ON  FROM HERE"""


###########################
def test_social_media_filter():
    venue = '{"first_name": "ALAN"}'
    handle = '{"last_name": "RICK"}'
    followers_count = '{"mandate": "senador"}'
    description = '{"dob": "1985-06-17"}'
    parlamentar = '{"first_name": "ALAN","last_name": "RICK","mandate": "senador"}'

    social_media = sms.SocialMediaFilter(**payload["filter"])

    assert social_media.first_name == payload["filter"]["first_name"].lower()
    assert social_media.last_name == payload["filter"]["last_name"].lower()
    assert social_media.mandate == payload["filter"]["mandate"].lower()
    assert social_media.dob == DOB_DATE
    assert social_media.page == payload["filter"]["page"]
    assert social_media.limit == payload["filter"]["limit"]


def test_social_media_base_errors():
    """
    Add validation error for the below
    """

    with pytest.raises(ValidationError):
        sms.SocialMediaBase(**payload_error["no_first_name"])

    with pytest.raises(ValidationError):
        sms.SocialMediaBase(**payload_error["no_last_name"])

    with pytest.raises(ValidationError):
        sms.SocialMediaBase(**payload_error["no_mandate"])

    with pytest.raises(ValidationError):
        sms.SocialMediaBase(**payload_error["wrong_date_format_DD-MM-YYYY"])

    with pytest.raises(ValidationError):
        sms.SocialMediaBase(**payload_error["wrong_date_format_YY-MM-DD"])

    with pytest.raises(ValidationError):
        sms.SocialMediaBase(**payload_error["wrong_date_format_YYYY,MM,DD"])

    with pytest.raises(ValidationError):
        sms.SocialMediaBase(**payload_error["wrong_date_format_YYYYMMDD"])
