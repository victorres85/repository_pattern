import pytest
from app.infrastructure.models import Parlamentar, SocialMedia, Post
from datetime import date


def test_create_social_media(session):
    """Test creating a SocialMedia entry."""
    parlamentar = Parlamentar(
        first_name="Jane", last_name="Smith", mandate="Representative", dob=date(1990, 2, 2)  # type:ignore
    )  # type:ignore
    session.add(parlamentar)
    session.commit()

    social_media = SocialMedia(
        venue="Twitter",  # type:ignore
        handle="@janesmith",  # type:ignore
        followers_count=1500,  # type:ignore
        description="Official Twitter of Jane Smith",  # type:ignore
        links="https://twitter.com/janesmith",  # type:ignore
        parlamentar_id=parlamentar.id,  # type:ignore
    )  # type:ignore
    session.add(social_media)
    session.commit()

    result = session.query(SocialMedia).order_by(SocialMedia.id.desc()).first()  # type:ignore
    assert result is not None
    assert result.handle == "@janesmith"
    assert result.parlamentar_id == parlamentar.id  # type:ignore


def test_get_social_media(session):
    result = session.query(SocialMedia).filter(SocialMedia.venue == "Twitter").first()
    assert result is not None
    assert result.venue == "Twitter"
    assert result.handle == "@janesmith"


def test_update_social_media(session):
    social_media = session.query(SocialMedia).filter(SocialMedia.venue == "Twitter").first()
    social_media.handle = "@newHandle"
    session.commit()

    result = session.query(SocialMedia).filter(SocialMedia.handle == "@newHandle").first()
    assert result.venue == "Twitter"


def test_delete_social_media(session):
    social_media = session.query(SocialMedia).filter(SocialMedia.venue == "Twitter").first()
    p_id = social_media.id

    result = session.query(SocialMedia).get(p_id)
    assert result is not None

    session.delete(social_media)
    session.commit()

    result = session.query(SocialMedia).get(p_id)
    assert result is None
