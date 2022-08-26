from datetime import date
from imdb.models import Rating, Movie, Cast, Actor, Director


def create_actor(actor_id):
    name = input("Actor name = ")
    if len(name) == 0:
        raise Actor.DoesNotExist
    try:
        actor = Actor.objects.create(actor_id=actor_id, name=name)
        actor.save()
        return actor
    except Actor.DoesNotExist:
        print("Actor should have a name")


def get_director(name):
    director = Director.objects.get_or_create(name=name)
    return director


def add_cast_to_movie(movie_id):
    n = int(input("Enter no of cast:-"))
    for i in range(n):
        role = input("Enter role of actor:-")
        actor_id = input("Enter actor id:-")
        is_debut_movie = True if int(input("Enter debut id:-")) else False
        Cast.objects.get_or_create(role=role, actor_id=actor_id, movie_id=movie_id, is_debut_movie=is_debut_movie)


def create_movies():
    movie_id = input("Enter movie id:")
    name = input("Enter movie name:")
    director_name = input("Enter Director name:")
    box_office_collection_in_crores = float(input("Enter box office collection in crores"))
    director, val = Director.objects.get_or_create(name=director_name)
    date_entry = input('Enter a date in YYYY-MM-DD format')
    year, month, day = map(int, date_entry.split('-'))
    release_date = date(year, month, day)
    Movie.objects.create(movie_id=movie_id, name=name,
                         box_office_collection_in_crores=box_office_collection_in_crores,
                         release_date=release_date,
                         director=director)

    add_cast_to_movie(movie_id)


def create_movie_rating(movie_id):
    movie = Movie.objects.get(movie_id=movie_id)
    rating_one_count = int(input("*:-"))
    rating_two_count = int(input("**:-"))
    rating_three_count = int(input("***:-"))
    rating_four_count = int(input("****:-"))
    rating_five_count = int(input("*****:-"))

    Rating.objects.create(movie_id=movie, rating_one_count=rating_one_count,
                          rating_two_count=rating_two_count, rating_three_count=rating_three_count,
                          rating_four_count=rating_four_count, rating_five_count=rating_five_count)


# def populate_databases(actors_list, movies_list, directors_list, movie_rating_list):
#     pass
