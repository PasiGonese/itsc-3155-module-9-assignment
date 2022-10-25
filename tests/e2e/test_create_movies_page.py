# TODO: Feature 2
import pytest
from app import app

@pytest.fixture()
def client():
    return app.test_client()    

def test_create_movie_page(client):
    response = client.post("/movies", data= { 
        "title": "Inception",
        "director": "James",
        "rating": '1'
    })
    assert response.status_code == 302
    assert b'Inception' in response.data
    assert b'James' in response.data
    assert b'1' in response.data 

