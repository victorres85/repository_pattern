""" Parlamentar Repository """

from typing import Any
from sqlalchemy.orm import Session
from app.validation.schemas.parlamentar_schema import ModelInterface


class BaseRepository:
    """Base class for Repositories"""

    def __init__(self, session: Session, model: Any):
        self.session = session
        self.model = model

    def list(self, page: int = 1, limit: int = 10):
        offset = (page - 1) * limit
        return (
            self.session.query(self.model)
            .order_by(self.model.id.desc())
            .offset(offset)
            .limit(limit)
            .all()
        )

    def get(self, id: int):
        result = self.session.query(self.model).get(id)
        return result

    def add(self, data: ModelInterface):
        obj = self.model(**data.model_dump())
        self.session.add(obj)
        self.session.commit()
        return "obj added"

    def delete(self, id: int):
        obj = self.session.query(self.model).get(id)
        self.session.delete(obj)
        self.session.commit()
        return "obj deleted"

    def update(self, data: ModelInterface):
        data_dict = data.model_dump()
        obj_id = data_dict.pop("id")
        obj = self.session.query(self.model).get(obj_id)
        for k, v in data_dict.items():
            if hasattr(obj, k):
                setattr(obj, k, v)
        self.session.commit()
        return "obj updated"

    def filter(self, filters: ModelInterface):
        query = self.session.query(self.model)
        filters = filters.model_dump()  # type: ignore
        page = filters.pop("page")  # type: ignore
        limit = filters.pop("limit")  # type: ignore
        offset = (page - 1) * limit
        for key, value in filters.items():  # type: ignore
            if value is not None:
                query = query.filter(getattr(self.model, key) == value)

        return query.offset(offset).limit(limit).all()
