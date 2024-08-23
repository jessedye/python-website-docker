import pytest
from server import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index_page(client):
    """Test the index page."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to Flask!" in response.data