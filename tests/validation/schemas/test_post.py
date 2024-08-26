""" Test post Domain """

import json
from datetime import date
import pytest
from pydantic import ValidationError
from app.validation.schemas import post_schema as ps


ADDED_DATE = date(2024, 8, 8)
ADDED_STR = "2024-08-08"
UPDATED_DATE = date(2024, 8, 9)
UPDATED_STR = "2024-08-09"
PUBLISHED_ON_DATE = date(2024, 8, 7)
PUBLISHED_ON_STR = "2024-08-07"


def test_post_create():
    payload = {
        "url": "post_url",
        "media": "media",
        "views_count": 100,
        "comments_count": 1,
        "reposts_count": 10,
        "likes_count": 10,
        "content": "Test social media post content",
        "contain_fake_news": "true",
        "published_on": PUBLISHED_ON_STR,
    }

    p = json.dumps(payload)
    post = ps.PostCreate.model_validate_json(p)

    assert post.url == payload["url"]
    assert post.media == payload["media"]
    assert post.views_count == payload["views_count"]
    assert post.reposts_count == payload["reposts_count"]
    assert post.likes_count == payload["likes_count"]
    assert post.content == payload["content"]
    assert post.contain_fake_news is True
    assert post.published_on == PUBLISHED_ON_DATE


def test_post_update():
    payload = {"views_count": 10, "comments_count": 1, "reposts_count": 10, "likes_count": 10}
    post = ps.PostUpdate(**payload)  # type: ignore

    assert post.views_count == payload["views_count"]
    assert post.comments_count == payload["comments_count"]
    assert post.reposts_count == payload["reposts_count"]
    assert post.likes_count == payload["likes_count"]


def test_post_response():
    payload = {
        "id": 1,
        "url": "post_url",
        "media": "media",
        "views_count": 100,
        "comments_count": 1,
        "reposts_count": 10,
        "likes_count": 10,
        "content": "Test social media post content",
        "contain_fake_news": "true",
        "published_on": PUBLISHED_ON_DATE,
        "added": ADDED_DATE,
        "updated": UPDATED_DATE,
    }

    post = ps.PostResponse(**payload["response"])

    assert post.url == payload["post_url"]
    assert post.media == payload["media"]
    assert post.views_count == payload["views_count"]
    assert post.reposts_count == payload["reposts_count"]
    assert post.likes_count == payload["likes_count"]
    assert post.content == payload["content"]
    assert post.contain_fake_news == payload["contain_fake_news"]
    assert post.published_on == PUBLISHED_ON_STR
    assert post.added == ADDED_STR
    assert post.updated == UPDATED_STR


def test_post_filter():
    payload = {
        "filter_by_url": {"url": "post_url"},
        "filter_by_media": {
            "media": "media",
            "page": 1,
            "limit": 10,
        },
        "filter_by_views_count": {
            "views_count": 100,
            "page": 2,
            "limit": 20,
        },
        "filter_by_comments_count": {
            "comments_count": 1,
            "page": 3,
            "limit": 30,
        },
        "filter_by_reposts_count": {
            "reposts_count": 10,
            "page": 4,
            "limit": 40,
        },
        "filter_by_likes_count": {
            "likes_count": 10,
            "page": 5,
            "limit": 50,
        },
        "filter_by_content": {
            "content": "Test social media post content",
            "page": 6,
            "limit": 60,
        },
        "filter_by_contain_fake_news": {
            "contain_fake_news": "true",
            "page": 7,
            "limit": 70,
        },
        "filter_by_published_on": {
            "published_on": "2024-08-07",
            "page": 8,
            "limit": 80,
        },
    }

    filter_by_url = json.dumps(payload["filter_by_url"])
    response = ps.PostFilter.model_validate_json(filter_by_url)
    assert response.url == payload["filter_by_url"]["url"]

    filter_by_media = json.dumps(payload["filter_by_media"])
    response = ps.PostFilter.model_validate_json(filter_by_media)
    assert response.media == payload["filter_by_media"]["media"]

    filter_by_views_count = json.dumps(payload["filter_by_views_count"])
    response = ps.PostFilter.model_validate_json(filter_by_views_count)
    assert response.views_count == payload["filter_by_views_count"]["views_count"]

    filter_by_comments_count = json.dumps(payload["filter_by_comments_count"])
    response = ps.PostFilter.model_validate_json(filter_by_comments_count)
    assert response.comments_count == payload["filter_by_comments_count"]["comments_count"]

    filter_by_reposts_count = json.dumps(payload["filter_by_reposts_count"])
    response = ps.PostFilter.model_validate_json(filter_by_reposts_count)
    assert response.reposts_count == payload["filter_by_reposts_count"]["reposts_count"]

    filter_by_likes_count = json.dumps(payload["filter_by_likes_count"])
    response = ps.PostFilter.model_validate_json(filter_by_likes_count)
    assert response.likes_count == payload["filter_by_likes_count"]["likes_count"]

    filter_by_content = json.dumps(payload["filter_by_content"])
    response = ps.PostFilter.model_validate_json(filter_by_content)
    assert response.content == payload["filter_by_content"]["content"]

    filter_by_contain_fake_news = json.dumps(payload["filter_by_contain_fake_news"])
    response = ps.PostFilter.model_validate_json(filter_by_contain_fake_news)
    assert response.contain_fake_news is True

    filter_by_published_on = json.dumps(payload["filter_by_published_on"])
    response = ps.PostFilter.model_validate_json(filter_by_published_on)
    assert response.published_on == PUBLISHED_ON_DATE


def test_parlamentar_get():
    request = '{"id":"1"}'
    response = ps.PostGet.model_validate_json(request)
    assert response.id == 1


def test_post_base_errors():

    payload_error = {
        "no_url": {
            "media": "media",
            "views_count": "100",
            "comments_count": "1",
            "reposts_count": "10",
            "likes_count": "10",
            "content": "Test social media post content",
            "contain_fake_news": "true",
            "published_on": PUBLISHED_ON_STR,
        },
        "no_published_on": {
            "url": "post_url",
            "media": "media",
            "views_count": 100,
            "comments_count": 1,
            "reposts_count": 10,
            "likes_count": 10,
            "content": "Test social media post content",
            "contain_fake_news": "true",
        },
    }

    with pytest.raises(ValidationError):
        ps.PostBase(**payload_error["no_url"])

    with pytest.raises(ValidationError):
        ps.PostBase(**payload_error["no_published_on"])
