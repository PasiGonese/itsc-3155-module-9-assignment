# DONE: Feature 1
from asyncio.windows_events import NULL
import pytest
from src.repositories.movie_repository import get_movie_repository
from app import app

movie_repository = get_movie_repository()

def test_get_list_all_movies_correct():
    movie_list = movie_repository.get_all_movies()
    assert len(movie_list) == 1 # e2e test added first movie
    new_movie = movie_repository.create_movie("Inception", "Christopher Nolan", "5")
    assert len(movie_list) == 2 # next movie added

   