""" Module containing helpers methods """

from datetime import date
from app.validation.schemas.helpers import (
    parse_date_to_str,
    parse_str_to_date,
    parse_str_to_int,
    parse_bool,
    ensure_lowercase,
    split_links,
)

DATE_AS_DATE = date(2024, 6, 7)
DATE_AS_STR = "2024-06-07"
INT_AS_STR = "1"
BOOL_TRUE = "true"
BOOL_FALSE = ""
UPPER_CASE = "UPPER_CASE"


def test_parse_date_to_str():
    as_str = parse_date_to_str(DATE_AS_DATE)
    assert as_str == DATE_AS_STR


def test_parse_str_to_date():
    as_date = parse_str_to_date(DATE_AS_STR)
    assert as_date == DATE_AS_DATE


def test_parse_str_to_int():
    as_int = parse_str_to_int(INT_AS_STR)
    assert as_int == int(INT_AS_STR)


def test_parse_bool():
    true = parse_bool(BOOL_TRUE)
    assert true is True

    false = parse_bool(BOOL_FALSE)
    assert false is False


def test_ensure_lowercase():
    lower_case = ensure_lowercase(UPPER_CASE)
    assert lower_case == UPPER_CASE.lower()


def test_split_links():
    text = "text1,text2,text3"
    response = split_links(text)
    assert response == ["text1", "text2", "text3"]

    text = ""
    response = split_links(text)
    assert response == []
