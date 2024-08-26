""" Test crud operations on Parlamentar model """

from app.infrastructure.models import Parlamentar
from datetime import date


def test_create_parlamentar(session):
    """Test creating a Parlamentar entry."""
    parlamentar = Parlamentar(
        first_name="John",
        last_name="Doe",
        mandate="Senator",
        dob=date(1980, 1, 1),  # type:ignore
    )  # type:ignore
    session.add(parlamentar)
    session.commit()

    result = (
        session.query(Parlamentar).order_by(Parlamentar.id.desc()).first()
    )  # type:ignore
    assert result is not None
    assert result.first_name == "John"
    assert result.last_name == "Doe"


def test_get_parlamentar(session):
    result = (
        session.query(Parlamentar)
        .filter(Parlamentar.first_name == "John")
        .first()
    )
    assert result is not None
    assert result.first_name == "John"
    assert result.last_name == "Doe"


def test_update_parlamentar(session):
    parlamentar = (
        session.query(Parlamentar)
        .filter(Parlamentar.first_name == "John")
        .first()
    )
    parlamentar.last_name = "New Last Name"
    session.commit()

    result = (
        session.query(Parlamentar)
        .filter(Parlamentar.last_name == "New Last Name")
        .first()
    )
    assert result.first_name == "John"


def test_delete_parlamentar(session):
    parlamentar = (
        session.query(Parlamentar)
        .filter(Parlamentar.first_name == "John")
        .first()
    )
    p_id = parlamentar.id

    result = session.query(Parlamentar).get(p_id)
    assert result is not None

    session.delete(parlamentar)
    session.commit()

    result = session.query(Parlamentar).get(p_id)
    assert result is None
