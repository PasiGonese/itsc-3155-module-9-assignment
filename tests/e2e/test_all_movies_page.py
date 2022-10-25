# TODO: Feature 1
from urllib import response
from app import app
import pytest
from src.repositories.movie_repository import get_movie_repository

@pytest.fixture(scope='module')
def test_app():
   return app.test_client()


def test_edit_user(test_app):
    response =test_app.post("/movies", data=
    {
        "title": "Inception",
        "director": "James",
        "rating": 1    
    }, follow_redirects=True

    )
    assert b'Inception' in response.data
    assert b'James' in response.data
    assert b'1' in response.data

def test_edit_user(test_app):
    response = test_app.get("/movies")
    assert b'Inception' not in response.data
    assert b'James' not in response.data
    assert b'1' not in response.data
# #positive case test
# def test_list_all_movies_correct(test_app):  
#     movie_repository.create_movie("Inception", "Christopher Nolan", 5)
#     response = test_app.get("/movies")          
#     assert b'<td id="title">Inception</td>' in response.data
#     assert b'<td id="title">Christopher Nolan</td>' in response.data
#     assert b'<td id="title">5</td>' in response.data


# #negative case test
# def test_list_all_movies_false():
#     movie_repository.create_movie("Inception", "Christopher Nolan", 5)
#     response = test_app.get("/movies")          
#     assert b'<td id="title">Dune</td>' not in response.data
#     assert b'<td id="title">Ryan Coogler</td>' not in response.data
#     assert b'<td id="title">2</td>' not in response.data