import sys
import os

# Add project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app  # Now that we created `app.py`, this will work!

import pytest

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_get_tasks(client):
    response = client.get("/tasks")
    assert response.status_code == 200