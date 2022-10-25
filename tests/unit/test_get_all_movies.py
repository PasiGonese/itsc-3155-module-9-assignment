# TODO: Feature 1
import pytest
from src.repositories.movie_repository import get_movie_repository
from app import app

movie_repository = get_movie_repository()
#positive case
def test_get_list_all_movies_correct():
    
    movie_list = movie_repository.get_all_movies()
    assert len(movie_list) == 0
    new_movie = movie_repository.create_movie("Inception", "Christopher Nolan", 5)
    assert len(movie_list) == 1


#negative case
# def test_get_list_all_movies_false():
#     new_movie = movie_repository.create_movie("Inception", "Christopher Nolan", 5)
#     assert "The Godfather" != new_movie.title
#     assert "Jordan Peele" != new_movie.director
#     assert 1 == new_movie.rating

#potential test that rating is not a number    