import pytest
from app.main import create_app
from app.db import db

# Token valid din auth.py pentru test
AUTH_HEADER = {"Authorization": "Bearer token123"}

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    # Folosește o bază de date SQLite în memorie
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.session.remove()
        db.drop_all()

def test_pow_endpoint(client):
    response = client.post("/api/math/pow", json={"base": 2, "exp": 8}, headers=AUTH_HEADER)
    assert response.status_code == 200
    data = response.get_json()
    assert data["result"] == 256
    assert data["operation"] == "pow"
    assert data["user"] == "alice@endava.com"

def test_factorial_endpoint(client):
    response = client.post("/api/math/factorial", json={"n": 5}, headers=AUTH_HEADER)
    assert response.status_code == 200
    data = response.get_json()
    assert data["result"] == 120

def test_fibonacci_endpoint(client):
    response = client.post("/api/math/fibonacci", json={"n": 6}, headers=AUTH_HEADER)
    assert response.status_code == 200
    data = response.get_json()
    assert data["result"] == 8

def test_auth_required(client):
    response = client.post("/api/math/pow", json={"base": 2, "exp": 2})  # Fără token
    assert response.status_code == 401

def test_history_endpoint(client):
    # Fă câteva requesturi înainte
    client.post("/api/math/pow", json={"base": 2, "exp": 3}, headers=AUTH_HEADER)
    client.post("/api/math/factorial", json={"n": 4}, headers=AUTH_HEADER)
    response = client.get("/api/math/history", headers=AUTH_HEADER)
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) >= 2
    assert data[0]["operation"] in ("pow", "factorial")
