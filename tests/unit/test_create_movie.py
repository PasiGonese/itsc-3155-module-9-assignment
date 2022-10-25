# TODO: Feature 2
import pytest
from src.repositories.movie_repository import get_movie_repository

movie_repository = get_movie_repository()

# happy moment
def test_create_movies_sunny_day():
    movie = movie_repository.create_movie("Inception", "Christopher Nolan", '1')
    assert "Inception" == movie.title
    assert "Christopher Nolan" == movie.director
    assert "1" == movie.rating

def test_create_movies_rainy_day():
    movie1 = movie_repository.create_movie("Star Wars", "George Lucas", "10")
    assert "Star Trek" != movie1.title
    assert "James Cameron" != movie1.director
    assert b'10' != movie1.rating
    