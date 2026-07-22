from fastapi.testclient import TestClient
from app.main import app

client=TestClient(app)

def test_analysis_basic_valid():
    response=client.post(
        "/analyse/basic",
        json={"text":"Hello World"}
    )
    assert response.status_code==200

def test_analyse_basic_empty():
    response=client.post(
        "/analyse/basic",
        json={"text":""}
      
    )
    assert response.status_code==400

def test_analyse_basic_invalid_type():
    response=client.post(
        "/analyse/basic",
        json={"text":123}
    )
    assert response.status_code==422