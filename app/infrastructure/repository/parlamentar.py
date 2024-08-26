""" Parlamentar Repository """

from typing import Type
from sqlalchemy.orm import Session
from .base import BaseRepository
from app.infrastructure.models.parlamentar import Parlamentar


class ParlamentarRepository(BaseRepository):
    """Parlamentar Repository"""

    def __init__(self, session: Session, model: Type[Parlamentar]):
        super().__init__(session, model)
        self.model = model
