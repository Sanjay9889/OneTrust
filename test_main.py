from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to One Trust!!"}


def test_increment_count():
    response = client.post(
        "/increment_count/",
        json={"name": "foo", "value": 2},
    )
    assert response.status_code == 200


def test_increment_count_invalid():
    response = client.post(
        "/increment_count/",
        json={"name": "foo", "value": 11},
    )
    assert response.status_code != 200

def test_get_tags():
    response = client.get("/get_tags/")
    assert response.status_code == 200
