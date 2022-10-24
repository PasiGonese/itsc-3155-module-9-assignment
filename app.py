from flask import Flask, redirect, render_template

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

movie_repository = get_movie_repository()


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1
    list_movies = []
    movie_repository.create_movie("Inception", "Chris Nolan", 5)
    movie_repository.create_movie("Pulp Ficiton", "Quntin Tarantino", 4)
    movie_repository.create_movie("The Shining", "Stanley Kubrick", 3)
    list_movies = movie_repository.get_all_movies()
    # list_movies = ['yo','whatup','bro']

    print(list_movies)
    return render_template('list_all_movies.html', list_movies_active=True, list_movies=list_movies)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # TODO: Feature 2
    # After creating the movie in the database, we redirect to the list all movies page
    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    return render_template('search_movies.html', search_active=True)
