from fastapi.testclient import TestClient
from project_poetry_fastapi.main import app

def test_read_root():
    client = TestClient(app=app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello":"World"}

def test_city():
    client = TestClient(app = app)
    response = client.get("/city/")
    assert response.status_code == 200
    assert response.json() == {"city":"Islamabad"} 


