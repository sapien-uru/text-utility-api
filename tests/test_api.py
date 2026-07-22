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

def test_analyse_sentences_valid():
    response=client.post(
        "/analyse/sentences",
        json={"text":"Hello world. This is a test."}
    )
    assert response.status_code==200

    data=response.json()
    assert "sentence_count" in data
    assert data["sentence_count"]==2

def test_analyse_sentences_empty():
    response = client.post(
        "/analyse/sentences",
        json={"text": ""}
    )
    assert response.status_code == 400

def test_analyse_keywords_valid():
    response = client.post(
        "/analyse/keywords",
        json={"text": "Python is great. Python is fast. FastAPI is great."}
    )
    assert response.status_code == 200

    data = response.json()
    assert "keywords" in data

def test_analyse_keywords_empty():
    response = client.post(
        "/analyse/keywords",
        json={"text": ""}
    )
    assert response.status_code == 400