""" Test Parlamentar Domain """

import json
from datetime import date
import pytest
from pydantic import ValidationError
from dateutil.parser import parse
from app.validation.schemas import parlamentar_schema as ps


added = date(2024, 8, 8)
updated = date(2024, 8, 9)


def test_parlamentar_create():
    payload = {
        "first_name": "ALAN",
        "last_name": "RICK",
        "mandate": "senador",
        "dob": "1985-06-17",
    }
    request_ = json.dumps(payload)

    parlamentar = ps.ParlamentarCreate.model_validate_json(request_)

    assert parlamentar.first_name == payload["first_name"].lower()
    assert parlamentar.last_name == payload["last_name"].lower()
    assert parlamentar.mandate == payload["mandate"].lower()
    assert parlamentar.dob == parse(payload["dob"]).date()


def test_parlamentar_update():
    import datetime

    payload = {
        "update_first_name": {
            "id": 1,
            "first_name": "ALAN",
        },
        "update_last_name": {
            "id": 1,
            "last_name": "RICK",
        },
        "update_mandate": {
            "id": 1,
            "mandate": "senador",
        },
        "update_dob": {
            "id": 1,
            "dob": "1985-06-17",
        },
    }
    update_first_name = json.dumps(payload["update_first_name"])
    parlamentar = ps.ParlamentarUpdate.model_validate_json(update_first_name)
    assert parlamentar.first_name == payload["update_first_name"]["first_name"].lower()

    update_last_name = json.dumps(payload["update_last_name"])
    parlamentar = ps.ParlamentarUpdate.model_validate_json(update_last_name)
    assert parlamentar.last_name == payload["update_last_name"]["last_name"].lower()

    update_mandate = json.dumps(payload["update_mandate"])
    parlamentar = ps.ParlamentarUpdate.model_validate_json(update_mandate)
    assert parlamentar.mandate == payload["update_mandate"]["mandate"].lower()

    update_dob = json.dumps(payload["update_dob"])
    parlamentar = ps.ParlamentarUpdate.model_validate_json(update_dob)
    assert parlamentar.dob == datetime.date(1985, 6, 17)


def test_parlamentar_response():

    added = date(2024, 8, 8)
    updated = date(2024, 8, 9)
    dob = date(1985, 6, 17)
    payload = {
        "id": 1,
        "first_name": "alan",
        "last_name": "rick",
        "mandate": "senador",
        "dob": dob,
        "added": added,
        "updated": updated,
    }
    dob_response = "1985-06-17"
    added_response = "2024-08-08"
    updated_response = "2024-08-09"

    parlamentar = ps.ParlamentarResponse(**payload)

    assert parlamentar.id == payload["id"]
    assert parlamentar.first_name == payload["first_name"].lower()
    assert parlamentar.last_name == payload["last_name"].lower()
    assert parlamentar.mandate == payload["mandate"].lower()
    assert parlamentar.dob == dob_response
    assert parlamentar.added == added_response
    assert parlamentar.updated == updated_response


def test_parlamentar_filter():
    first_name = {
        "first_name": "ALAN",
    }

    resquest = json.dumps(first_name)
    parlamentar = ps.ParlamentarFilter.model_validate_json(resquest)
    assert parlamentar.first_name == first_name["first_name"].lower()
    assert parlamentar.page == 1
    assert parlamentar.limit == 10

    last_name = {
        "last_name": "RICK",
        "page": 2,
        "limit": 20,
    }
    resquest = json.dumps(last_name)
    parlamentar = ps.ParlamentarFilter.model_validate_json(resquest)
    assert parlamentar.last_name == last_name["last_name"].lower()
    assert parlamentar.page == last_name["page"]
    assert parlamentar.limit == last_name["limit"]

    mandate = {
        "mandate": "senador",
        "page": 3,
        "limit": 30,
    }
    resquest = json.dumps(mandate)
    parlamentar = ps.ParlamentarFilter.model_validate_json(resquest)
    assert parlamentar.mandate == mandate["mandate"].lower()
    assert parlamentar.page == mandate["page"]
    assert parlamentar.limit == mandate["limit"]


def test_parlamentar_get():
    request = '{"id":"1"}'
    parlamentar = ps.ParlamentarGet.model_validate_json(request)
    assert parlamentar.id == 1


def test_parlamentar_base_errors():

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
        "wrong_date_format_YYYY,MM,DD": {
            "first_name": "ALAN",
            "last_name": "RICK",
            "mandate": "senador",
            "dob": "1985,06,17",
        },
    }
    with pytest.raises(ValidationError):
        ps.ParlamentarBase(**payload_error["no_first_name"])  # type: ignore

    with pytest.raises(ValidationError):
        ps.ParlamentarBase(**payload_error["no_last_name"])  # type: ignore

    with pytest.raises(ValidationError):
        ps.ParlamentarBase(**payload_error["no_mandate"])  # type: ignore

    with pytest.raises(ValidationError):
        ps.ParlamentarBase(**payload_error["wrong_date_format_YYYY,MM,DD"])  # type: ignore
