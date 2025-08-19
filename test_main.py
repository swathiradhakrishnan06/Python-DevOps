from fastapi.testclient import TestClient
from main import app


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Wikipedia API"}


def test_read_phrase():
    response = client.get("/phrase/Artificial Intelligence")
    assert response.status_code == 200
    assert response.json() == {
        "result": [
            "artificial",
            "ai",
            "computational systems",
            "human intelligence",
        ]
    }
