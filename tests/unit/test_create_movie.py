# TODO: Feature 2
import pytest
from movie_repository import create_movie

def test_create_movies():
    movie = movie_repository.create_movie("Inception", "james", '1')
    assert "Inception" == movie.title
    assert "james" == movie.director
    assert "1" == movie.rating