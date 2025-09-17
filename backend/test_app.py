import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to Travel Memory API" in response.data

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert b"healthy" in response.data
