import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Test strony głównej
def test_home_status_code(client):
    response = client.get('/')
    assert response.status_code == 200

# Test zawartości strony głównej
def test_home_content(client):
    response = client.get('/')
    assert b'Welcome to Simple App!' in response.data
