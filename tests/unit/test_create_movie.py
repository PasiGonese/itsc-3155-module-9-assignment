# TODO: Feature 2
import pytest
# import from movie_repository

def create_movies_test:
    movie = movie_repository.create_movie("Inception", "james", '1')
    assert "Inception" == movie.title
    assert "james" == movie.director
    assert "1" = movie.rating 
