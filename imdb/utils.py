from datetime import datetime

from django.shortcuts import render

# Create your views here.
"""
    :param actors_list:[
        {
            "actor_id": "actor_1",
            "name": "Actor 1"
        }
    ]
    :param movies_list: [
        {
            "movie_id": "movie_1",
            "name": "Movie 1",
            "actors": [
                {
                    "actor_id": "actor_1",
                    "role": "hero",
                    "is_debut_movie": False
                }
            ],
            "box_office_collection_in_crores": "12.3",
            "release_date": "2020-3-3",
            "director_name": "Director 1"
        }
    ]
    :param directors_list: [
        "Director 1"
    ]
    :param movie_rating_list: [
        {
            "movie_id": "movie_1",
            "rating_one_count": 4,
            "rating_two_count": 4,
            "rating_three_count": 4,
            "rating_four_count": 4,
            "rating_five_count": 4
        }
    ]
    """
from imdb.models import Rating, Movie, Cast, Actor, Director

# n = 1
# actors_list = []
# directors_list = []
cast_list = []
#
#
# movie_list = []
# movie_rating_list = []


def create_actors(actors_list):
    actor_id = input("Actor id = ")
    name = input("Actor name = ")
    actor = Actor(actor_id=actor_id, name=name)
    actors_list.append(actor)
    return actors_list



def create_director(directors_list):
    name = input("Director name")
    director = Director(name=name)
    directors_list.append(director)
    return directors_list


def create_cast(actor_id, actors_list):
    for actor in actors_list:
        if actor_id == actor.actor_id:
            role = input("Role is")
            is_debut_movie = (int(input()) == 1)
            cast = Cast(actor=actor, role=role, is_debut_movie=is_debut_movie)
            cast_list.append(cast)


def create_movie(movie_id, name, cast_id, director_name, directors_list, movie_list):
    for director in directors_list:
        if director_name == director.name:
            release_date = datetime.date
            for cast in cast_list:
                if cast_id == cast.actor_id:
                    movie = Movie(movie_id=movie_id, name=name, actors=cast, release_date=release_date,
                                  director=director)

                    movie_list.append(movie)


def create_movie_rating(movies_list, movie_rating_list):
    movie_id = input("Enter movie id")
    for movie in movies_list:
        if movie_id == movie.movie_id:
            rating_one_count = int(input())
            rating_two_count = int(input())
            rating_three_count = int(input())
            rating_four_count = int(input())
            rating_five_count = int(input())

            rating = Rating(movie_id=movie_id, rating_one_count=rating_one_count,
                            rating_two_count=rating_two_count, rating_three_count=rating_three_count,
                            rating_four_count=rating_four_count, rating_five_count=rating_five_count)

            movie_rating_list.append(rating)


def populate_database(actors_list, movies_list, directors_list, movie_rating_list):
    no_of_actors = int(input("Enter Number of Actors"))
    for i in range(no_of_actors):
        create_actors(actors_list)
    no_of_director = int(input("Enter Number of Directors"))
    for i in range(no_of_director):
        create_director(directors_list)
    no_of_cast = int(input("Enter Number of Directors"))
    for i in range(no_of_cast):
        actor_id = input("Cast Actor id")
        create_cast(actor_id, actors_list)
    movie_id = input("Enter movie id")
    name = input("Enter Movie name")
    cast_id = input("Cast Actor id")
    director_name = input("Director name")
    create_movie(movie_id, name, cast_id, director_name, movies_list)
    create_movie_rating(movies_list, movie_rating_list)


if __name__ == '__main__':
    populate_database(actors_list=[], movies_list=[], directors_list=[], movie_rating_list=[])


