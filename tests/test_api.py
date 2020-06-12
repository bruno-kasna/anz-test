import os
import pytest

from myapp import api

VERSION_TEST = "1.0.0"
LAST_COMMIT_SHA_TEST = "abc"

@pytest.fixture
def client():
    api.app.config['TESTING'] = True
    os.environ['VERSION'] = VERSION_TEST
    os.environ['LAST_COMMIT_SHA'] = LAST_COMMIT_SHA_TEST
    client = api.app.test_client()
    yield client


def test_version(client):
    response = client.get("/version")
    data = str(response.data)
    assert response.status_code == 200
    assert '"version":"%s"' % VERSION_TEST in data
    assert '"lastcommitsha":"%s"' % LAST_COMMIT_SHA_TEST in data
    assert '"description":"pre-interview technical test"' in data
