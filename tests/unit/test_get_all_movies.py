# TODO: Feature 1
import pytest
from src.repositories.movie_repository import get_movie_repository
from app import app

#positive case
def test_get_list_all_movies_correct():
    new_movie = movie_repository.create_movie("Inception", "Christopher Nolan", 5)
    assert "Inception" == new_movie.title
    assert "Christopher Nolan" == new_movie.director
    assert 5 == new_movie.rating

#negative case
def test_get_list_all_movies_correct():
    new_movie = movie_repository.create_movie("Inception", "Christopher Nolan", 5)
    assert "The Godfather" == new_movie.title
    assert "Jordan Peele" == new_movie.director
    assert 1 == new_movie.rating