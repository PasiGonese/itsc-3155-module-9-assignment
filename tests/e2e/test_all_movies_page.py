# TODO: Feature 1
from app import app
import pytest
from src.repositories.movie_repository import get_movie_repository

@pytest.fixture(scope='module')
def test_app():
   return app.test_client()


def test_add_movie(test_app):
    response = test_app.post("/movies", data=
    {
        "title": "Inception",
        "director": "James",
        "rating": 1    
    }, follow_redirects=True

    )
    assert b'Inception' in response.data
    assert b'James' in response.data
    assert b'1' in response.data

# def test_edit_user1(test_app):
    
#     assert b'Inception' not in response.data
#     assert b'James' not in response.data
#     assert b'1' not in response.data