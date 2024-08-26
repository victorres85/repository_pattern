""" Test Parlamentar Repository """

from app.infrastructure.models.parlamentar import Parlamentar
from app.validation.schemas import parlamentar_schema as ps
from app.infrastructure.repository.parlamentar import ParlamentarRepository


def test_add_parlamentar(session):
    # Create a Parlamentar instance
    payload = {
        "first_name": "ALAN",
        "last_name": "RICK",
        "mandate": "senador",
        "dob": "1985-06-17",
    }
    parlamentar = ps.ParlamentarCreate(**payload)  # type: ignore
    repository = ParlamentarRepository(session=session, model=Parlamentar)
    result = repository.add(parlamentar)  # type: ignore
    assert result == "obj added"


def test_list(session):
    result = ParlamentarRepository(session=session, model=Parlamentar).list()
    assert len(result) <= 10


def test_get(session):
    parlamentares = ParlamentarRepository(
        session=session, model=Parlamentar
    ).list()
    parlamentar_id = parlamentares[0].id
    result = ParlamentarRepository(session=session, model=Parlamentar).get(
        parlamentar_id
    )
    assert result is not None
    assert result.id == parlamentar_id


def test_delete(session):
    parlamentares = ParlamentarRepository(
        session=session, model=Parlamentar
    ).list()
    parlamentar_id = parlamentares[0].id
    result = ParlamentarRepository(session=session, model=Parlamentar).delete(
        parlamentar_id
    )
    assert result == "obj deleted"


def test_filter(session):
    payload = {
        "first_name": "ALAN",
        "dob": "1985-06-17",
    }
    parlamentar_filter = ps.ParlamentarFilter(**payload)  # type: ignore
    repository = ParlamentarRepository(session=session, model=Parlamentar)
    result = repository.filter(parlamentar_filter)  # type: ignore
    assert result is not None


def test_update(session):
    # Create a Parlamentar instance
    payload = {
        "first_name": "ALAN",
        "last_name": "RICK",
        "mandate": "senador",
        "dob": "1985-06-17",
    }
    parlamentar = ps.ParlamentarCreate(**payload)  # type: ignore
    repository = ParlamentarRepository(session=session, model=Parlamentar)
    repository.add(parlamentar)  # type: ignore

    # Get Parlamentar obj id
    payload = {
        "first_name": "ALAN",
        "dob": "1985-06-17",
    }
    parlamentar_filter = ps.ParlamentarFilter(**payload)  # type: ignore
    parlamentares = repository.filter(parlamentar_filter)  # type: ignore
    parlamentar_id = parlamentares[0].id

    # Update values
    new_payload = {
        "id": parlamentar_id,
        "first_name": "VICTOR",
        "last_name": "ALMEIDA",
        "mandate": "deputado",
        "dob": "1985-06-17",
    }
    parlamentar = ps.ParlamentarUpdate(**new_payload)
    repository.update(data=parlamentar)  # type: ignore

    # Get updated parlamentar
    parlamentar = repository.get(parlamentar_id)
    assert parlamentar.first_name == "victor"  # type: ignore
