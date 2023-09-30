from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Wikipedia API. Call /search or /wiki"}


def test_read_phrases():
    response = client.get("/wiki/phrases/Barack Obama")
    assert response.status_code == 200
    assert response.json() == {
        "Wikipedia Phrases": [
            "barack hussein obama ii",
            "bə-rahk hoo-sayn oh-bah-mə",
            "august",
            "american politician",
            "44th president",
        ]
    }
