from fastapi.testclient import TestClient
from main import app
import pytest
from unittest.mock import MagicMock
from db.database import get_db

# # Create a mock database session
# @pytest.fixture
# def db_session():
#     return MagicMock()

# # Override the dependency to use the mock database session
# @pytest.fixture
# def override_get_db(db_session):
#     def override():
#         return db_session
#     app.dependency_overrides[get_db] = override
#     yield
#     app.dependency_overrides.clear()

# # Initialize the test client with the FastAPI application
# @pytest.fixture
# def client():
#     with TestClient(app) as client:
#         yield client

client = TestClient(app)

def test_get_all_blogs():
    response = client.get('/blog/all')
    assert response.status_code == 200

# test authentication when invalid input
def test_auth_error():
    response = client.post('/token',
        data = {'username' : '', 'password': ''}
    )
    access_token = response.json().get('access_token')
    assert access_token == None
    message = response.json().get('detail')[0].get('msg')
    assert message == 'Field required'

# test authentication when valid input
def test_auth_success():
    response = client.post('/token',
        data = {'username' : 'jedzel', 'password': 'pass123'}
    )
    access_token = response.json().get('access_token')
    assert access_token

# test creation of article once authenticated
def test_post_article():
    auth = client.post('/token',
        data = {'username' : 'jedzel', 'password': 'pass123'}
    )
    access_token = auth.json().get('access_token')
    assert access_token
    response = client.post(
        '/article/',
        json={
            "title": "Test article",
            "content": "Test content",
            "published": True,
            "user_id": 4
        },
        headers={
            "Authorization": "bearer " + access_token
        }
    )
    assert response.status_code == 200
   
# test for getting a all users
def test_get_all_users():
    auth = client.post('/token',
        data = {'username': 'jedzel', 'password': 'pass123'}
    )
    access_token = auth.json().get('access_token')
    assert access_token
    response = client.get('/user/',
        headers={
            "Authorization": "bearer " + access_token
        }
    )
    assert response.status_code == 200

