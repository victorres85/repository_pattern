""" Module containing helpers methods """

from datetime import date
from dateutil.parser import parse


def parse_date_to_str(v):
    if isinstance(v, date):
        return v.strftime("%Y-%m-%d")
    return v


def parse_str_to_date(v):
    if isinstance(v, str):
        try:
            return parse(v).date()
        except ValueError as exc:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.") from exc
    return v


def parse_str_to_int(v):
    if isinstance(v, str):
        try:
            return int(v)
        except ValueError as exc:
            raise ValueError("The 'id' field must be an integer.") from exc
    return v


def parse_bool(v):
    if isinstance(v, str):
        return bool(v)
    return v


def ensure_lowercase(v):
    if isinstance(v, str):
        try:
            return v.lower()
        except ValueError as exc:
            raise ValueError from exc
    return v


def split_links(v):
    if v:
        return v.replace(" ", "").split(",")
    return []


def join_links(v):
    if isinstance(v, list):
        return ",".join(v)
    return ""
