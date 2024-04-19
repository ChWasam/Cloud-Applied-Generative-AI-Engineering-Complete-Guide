from fastapi.testclient import TestClient
from my_first_fastapi_docker.main import app


def test_home():
    client = TestClient(app=app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Home":"Welcome to HomeScreen"}


def test_username():
    client = TestClient(app=app)
    response = client.get("/username")
    assert response.status_code == 200
    assert response.json() == {"Username":"Chaudhry Wasam Ur Rehman"}


def test_email():
    client = TestClient(app=app)
    response = client.get("/email")
    assert response.status_code == 200
    assert response.json() == {"Email":"ch.wasam@gmail.com"}
















