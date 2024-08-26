import pytest
from app.infrastructure.models import Parlamentar, SocialMedia, Post
from datetime import date


def test_create_post(session):
    """Test creating a Post entry."""
    parlamentar = Parlamentar(
        first_name="Alice", last_name="Johnson", mandate="Councillor", dob=date(1975, 3, 3)  # type:ignore
    )  # type:ignore
    session.add(parlamentar)
    session.commit()

    social_media = SocialMedia(
        venue="Facebook",  # type:ignore
        handle="AliceJohnson",  # type:ignore
        followers_count=2500,  # type:ignore
        description="Official Facebook of Alice Johnson",  # type:ignore
        links="https://facebook.com/alicejohnson",  # type:ignore
        parlamentar_id=parlamentar.id,  # type:ignore
    )
    session.add(social_media)
    session.commit()

    post = Post(
        url="https://example.com/post",  # type:ignore
        media="Image",  # type:ignore
        views_count=100,  # type:ignore
        comments_count=10,  # type:ignore
        reposts_count=5,  # type:ignore
        likes_count=50,  # type:ignore
        content="This is a post content.",  # type:ignore
        contain_fake_news=False,  # type:ignore
        social_media_id=social_media.id,  # type:ignore
        post_date="2024-08-25",  # type:ignore
    )
    session.add(post)
    session.commit()

    result = session.query(Post).order_by(Post.id.desc()).first()  # type:ignore
    assert result is not None
    assert result.content == "This is a post content."
    assert result.social_media_id == social_media.id  # type:ignore


def test_get_post(session):
    result = session.query(Post).filter(Post.url == "https://example.com/post").first()
    assert result is not None
    assert result.url == "https://example.com/post"
    assert result.content == "This is a post content."


def test_update_post(session):
    post = session.query(Post).filter(Post.url == "https://example.com/post").first()
    post.content = "This is a NEW post content."
    session.commit()

    result = session.query(Post).filter(Post.content == "This is a NEW post content.").first()
    assert result.url == "https://example.com/post"


def test_delete_post(session):
    post = session.query(Post).filter(Post.url == "https://example.com/post").first()
    p_id = post.id

    result = session.query(Post).get(p_id)
    assert result is not None

    session.delete(post)
    session.commit()

    result = session.query(Post).get(p_id)
    assert result is None
