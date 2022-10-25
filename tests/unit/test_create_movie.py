# TODO: Feature 2
import pytest
import movie_repository

def test_create_movies:
    movie = movie_repository.create_movie("Inception", "james", '1')
    assert "Inception" == movie.title
    assert "james" == movie.director
    assert "1" = movie.rating