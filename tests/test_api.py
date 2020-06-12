import os
import pytest

from myapp import api


@pytest.fixture
def client():
    api.app.config['TESTING'] = True
    os.environ['VERSION'] = "1.0.0"
    os.environ['LAST_COMMIT_SHA'] = "abc"
    client = api.app.test_client()
    yield client


def test_version(client):
    response = client.get("/version")
    assert response.status_code == 200
    assert b'"version":"1.0.0"' in response.data
    assert b'"lastcommitsha":"abc"' in response.data
    assert b'"description":"pre-interview technical test"' in response.data
