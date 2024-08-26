""" Pytest configuration Module """

import sys
import os
import pytest
from app import db, create_app
from app.config import TestConfig


sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)


@pytest.fixture(scope="module")
def test_client():
    """Set up a test client for the application."""
    config = TestConfig()
    app = create_app(config)
    with app.test_client() as testing_client:
        with app.app_context():
            # Create the database and tables
            db.create_all()
            yield testing_client
        # Tear down the database
        db.drop_all()


@pytest.fixture(scope="function")
def session(test_client):
    """Set up a new database session for each test."""
    connection = db.engine.connect()
    transaction = connection.begin()
    session = db._make_scoped_session(options={"bind": connection})
    db.session = session
    yield session
    session.remove()
    transaction.rollback()
    connection.close()
