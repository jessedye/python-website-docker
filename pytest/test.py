import pytest
import sys
import os

# Add the directory containing server.py to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

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