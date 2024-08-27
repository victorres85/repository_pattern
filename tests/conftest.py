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

    with app.app_context():
        db.create_all()

    # Add this part to ensure the test client runs in a request context
    with app.test_request_context():
        with app.test_client() as testing_client:
            yield testing_client

    with app.app_context():
        db.drop_all()


@pytest.fixture(scope="function")
def session(test_client):
    """Set up a new database session for each test."""
    with test_client.application.app_context():
        connection = db.engine.connect()
        transaction = connection.begin()

        # Override the session with a new one bound to the transaction
        session = db._make_scoped_session(options={"bind": connection})
        db.session = session

        yield session  # provide the fixture value

        session.remove()
        transaction.rollback()
        connection.close()
