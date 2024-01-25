"""
This module provides CRUD (Create, Read, Update, Delete) operations for the models
used in the 'pages' application of the Django project. It includes functions to
create, retrieve, update, and delete instances of Movie, Director, and Actor models.
"""
from pages.models import Actor, Director, Movie


# Actor CRUD operations

def get_all_actors():
    return Actor.objects.all()

def get_all_directors():
    return Director.objects.all()

def get_all_movies():
    return Movie.objects.all()
