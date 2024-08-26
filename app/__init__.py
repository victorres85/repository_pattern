""" APP Setup """

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, class_mapper
from pytz import timezone
from .config import Config, DevConfig


def time_now():
    utc = timezone("UTC")
    return datetime.now(utc)


class Base(DeclarativeBase):
    """base model"""

    metadata = MetaData(
        naming_convention={
            "ix": "ix_%(column_0_label)s",
            "uq": "uq_%(table_name)s_%(column_0_name)s",
            "ck": "ck_%(table_name)s_%(constraint_name)s",
            "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
            "pk": "pk_%(table_name)s",
        }
    )

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    added: Mapped[datetime] = mapped_column(default=time_now)
    updated: Mapped[datetime] = mapped_column(default=time_now, onupdate=time_now)

    def to_dict(self):
        """Convert the SQLAlchemy model instance to a dictionary."""
        return {c.key: getattr(self, c.key) for c in class_mapper(self.__class__).columns}


db = SQLAlchemy(model_class=Base)


def create_app(config_object: Config = DevConfig()):
    app = Flask(__name__)
    app.config.from_object(config_object)

    db.init_app(app)

    with app.app_context():
        # Register blueprints
        from .rest.parlamentar import parlamentar_api_blueprint

        db.create_all()
        app.register_blueprint(parlamentar_api_blueprint)
        return app
