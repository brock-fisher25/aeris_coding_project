import pytest
from app import app as my_app

@pytest.fixture()
def client():
    return my_app.test_client()
