from datetime import date

from django.shortcuts import render

# Create your views here.
# """
#     :param actors_list:[
#         {
#             "actor_id": "actor_1",
#             "name": "Actor 1"
#         }
#     ]
#     :param movies_list: [
#         {
#             "movie_id": "movie_1",
#             "name": "Movie 1",
#             "actors": [
#                 {
#                     "actor_id": "actor_1",
#                     "role": "hero",
#                     "is_debut_movie": False
#                 }
#             ],
#             "box_office_collection_in_crores": "12.3",
#             "release_date": "2020-3-3",
#             "director_name": "Director 1"
#         }
#     ]
#     :param directors_list: [
#         "Director 1"
#     ]
#     :param movie_rating_list: [
#         {
#             "movie_id": "movie_1",
#             "rating_one_count": 4,
#             "rating_two_count": 4,
#             "rating_three_count": 4,
#             "rating_four_count": 4,
#             "rating_five_count": 4
#         }
#     ]
#     """
from .models import Rating, Movie, Cast, Actor, Director
from django.db.models import Q


# def create_actor():
#     actor_id = input("Actor id = ")
#     name = input("Actor name = ")
#     try:
#         actor = Actor.objects.get(actor_id=actor_id, name=name)
#     except:
#         actor = Actor.objects.get_or_create(actor_id=actor_id, name=name)
#         actor.save()

#     return actor

def get_actor():
    # actor_id = "actor_2"
    # name = "Actor 2"
    try:
        actor_id = input("Actor id = ")
        actor = Actor.objects.get(actor_id=actor_id)
    except:
        name = input("Actor name = ")
        actor = Actor.objects.create(actor_id=actor_id, name=name)
        actor.save()
    # actors_list.append(actor)
    print(f'Actor:- {actor},{type(actor)}')
    return actor


# def create_director():
#     name = input("Director name= ")
#     try:
#         director = Director.objects.get(name="Director 2")
#     except:
#         director = Director.objects.create(name="Director 2")
#         director.save()
#         # directors_list.append(director)
#     return director


def get_director():
    name = input("Director name= ")
    try:
        director = Director.objects.get(name=name)
    except:
        director = Director.objects.create(name=name)
        director.save()
    print(f'director:- {director}, {type(director)}')
    return director


# def create_cast(actor_id, actors_list):
#
#     for actor in actors_list:
#         # print(actor_id,actor.actor_id)
#         if actor_id == actor.actor_id:
#             role = input("Role is = ")
#             is_debut_movie = (int(input("Is Debut? = ")) == 1)
#             cast = Cast.objects.create(actor=actor, role=role, is_debut_movie=is_debut_movie)
#             # cast.save()
#             # cast_list.append(cast)
#
#     return cast

# def create_cast(actor_id):
#     # print(f'(actors_list) {actors_list}')
#     actor = Actor.objects.get(actor_id =actor_id)
#     role = input("Role is = ")
#     is_debut_movie = (int(input("Is Debut? = ")) == 1)
#     cast = Cast.objects.create(actor=actor, role=role, is_debut_movie=is_debut_movie)
#     cast.save()
#             # cast_list.append(cast)
#     print(f'cast:- {cast}')
#     print("*****Cast****")
#     return cast


def add_cast_to_movie(movie_id):
    actors_list=[]
    for i in range(2):
        role = input("Enter role of actor:-")
        actors = Cast.objects.get(role=role)
        actors_list.append(actors)
    print(actors_list)
    director,value = Director.objects.get_or_create(name="Director 3")
    movie = Movie.objects.get_or_create(movie_id=movie_id,release_date = date(2022, 10, 10),box_office_collection_in_crores = 11.3,director_id= director.id)
    movie.actors.add(*actors_list)
    movie.save()

#
# def create_movie(movie_id, name,director_name, directors_list, movies_list):
#     cast_list=[]
#     for director in directors_list:
#         if director_name == director.name:
#             release_date = date(2022,10,10)
#             box_office_collection_in_crores = 11.3
#             n= int(input("Enter Number of Cast:- "))
#             for i in range(n):
#                 cast_id = input("Enter actor_id:- ")
#                 actor = Actor.objects.get(actor_id=cast_id)
#                 cast = Cast.objects.filter(actor=actor)
#                 cast_list.append(cast)
#             movie = Movie.objects.create(movie_id=movie_id, name=name,box_office_collection_in_crores=box_office_collection_in_crores , release_date=release_date,
#                                   director=director)
#             movie.actors.add(cast)
#             # movie.save()
#             movies_list.append(movie)
#     return movie

def create_movies(director_name):
    movie_id = input("Enter movie id:")
    name = input("Enter movie name:")

    director = Director.objects.get(name=director_name)



    # date_entry = input('Enter a date in YYYY-MM-DD format')
    # year, month, day = map(int, date_entry.split('-'))
    # date1 = datetime.date(year, month, day)
    release_date = date(2022, 10, 10)
    box_office_collection_in_crores = 11.3
    movie = Movie.objects.create(movie_id=movie_id, name=name,
                                 box_office_collection_in_crores=box_office_collection_in_crores,
                                 release_date=release_date,
                                 director=director)
    movie.save()
    n= int(input("Enter Number of Cast:- "))
    for i in range(n):
        role = input(f"Enter role in {name}:- ")
        cast_role = Cast.objects.get(role=role).actor
        movie.actors.add(cast_role)
                # cast_id = "actor_2"
                # actor = Actor.objects.get(actor_id=cast_id)
            # cast = Cast.objects.get(role=role)
            # cast_list.append(cast)

            # movie.actors.add(cast)
            # movie.save()
            # movies_list.append(movie)
        print(f'movie;- {movie}')
    # return movie


def create_movie_rating(movie_rating_list):
    movie_id = input("Enter movie id:- ")
    movie = Movie.objects.get(movie_id=movie_id)
    rating_one_count = int(input())
    rating_two_count = int(input())
    rating_three_count = int(input())
    rating_four_count = int(input())
    rating_five_count = int(input())

    rating = Rating.objects.create(movie_id=movie, rating_one_count=rating_one_count,
                                   rating_two_count=rating_two_count, rating_three_count=rating_three_count,
                                   rating_four_count=rating_four_count, rating_five_count=rating_five_count)
    # rating.save()
    movie_rating_list.append(rating)


# def populate_database(actors_list, movies_list, directors_list, movie_rating_list):
#     cast_list=[]
#     no_of_actors = int(input("Enter Number of Actors:- "))
#     for i in range(no_of_actors):
#         actors_list.append(create_actor())
#     no_of_director = int(input("Enter Number of Directors:- "))
#     for i in range(no_of_director):
#         directors_list.append(create_director())
#     no_of_cast = int(input("Enter Number of Cast:- "))
#     for i in range(no_of_cast):
#         actor_id = input("Cast Actor id:- ")
#         cast_list.append(create_cast(actor_id, actors_list))
#     movie_id = input("Enter movie id:- ")
#     name = input("Enter Movie name:- ")
#     director_name = input("Add Director name:- ")
#     movies_list.append(create_movie(movie_id=movie_id, name=name, director_name=director_name,directors_list=directors_list, movies_list=movies_list))
#     create_movie_rating(movies_list, movie_rating_list)


cast_list = []
def get_actors_list():

    return Actor.objects.all()

def get_directors_list(directors_list):
    no_of_director = int(input("Enter Number of Directors:- "))
    for i in range(no_of_director):
        director = get_director()
        directors_list.append(director)
    return directors_list


def populate_databases(actors_list, movies_list, directors_list, movie_rating_list):

    director_name = input("Add Director name:- ")
    no_of_cast = int(input("Enter Number of Cast:- "))
    for i in range(no_of_cast):
        actor_id = input("Cast Actor id:- ")
        cast_list.append(create_cast(actors_list, actor_id))
    # movie_id = input("Enter movie id:- ")
    # movie_id = "movie_2"
    # name = input("Enter Movie name:- ")



    # director_name = "Director 2"
        movies_list.append(
        create_movies(director_name=director_name))
    create_movie_rating(movie_rating_list)


if __name__ == '__main__':
    # populate_database(actors_list=[], movies_list=[], directors_list=[], movie_rating_list=[])
    # populate_databases(actors_list=[], movies_list=[], directors_list=[], movie_rating_list=[])
    add_actors_to_movie(movie_id="movie_3")
# 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

# actor_2
# Actor 2
# Director 2
# movie_2
# Movie 2
