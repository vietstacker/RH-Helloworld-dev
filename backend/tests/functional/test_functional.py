import pytest
from backend.app import app as flask_app


@pytest.fixture(scope='module')
def test_client():
    testing_client = flask_app.test_client()
    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client  # this is where the testing happens!

    ctx.pop()


def test_api(test_client):
    """
    GIVEN a Flask application
    WHEN the '/api/hello' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/api/hello')
    assert response.status_code == 200
    assert response.data == b'HelloWorld from RedHat (1)'
