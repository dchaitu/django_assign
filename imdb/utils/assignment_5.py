from django.db.models import Q, Count

from imdb.models import Rating, Movie, Cast


def remove_all_actors_from_given_movie(movie_object):
    """
    :param movie_object: A Movie model instance
    """

    actors_of_movie = movie_object.actors.all()
    for actor in actors_of_movie:
        movie_object.actors.remove(actor)

    movie_object.save()


def get_all_rating_objects_for_given_movies(movie_objs):
    """
    :movie_objs: a list of Movie model instances
    :return: a list of rating model instances
    """
    rating_objs = []
    for movie in movie_objs:
        rating = Rating.objects.get(movie=movie)
        rating_objs.append(rating)
    return rating_objs


def get_movies_by_given_movie_names(movie_names):
    all_movies = []
    for name in movie_names:
        movie = Movie.objects.get(name=name)
        movie_obj = {}
        rating = Rating.objects.get(movie_id=movie.movie_id)

        crew = Cast.objects.filter(movie__movie_id=movie.movie_id)
        all_cast = []
        for cast in crew:
            cast_obj = {}
            actor_obj = {}
            actor_obj.update({"name": cast.actor.name, "actor_id": cast.actor.actor_id, })
            cast_obj.update({"actor": actor_obj, "role": cast.role, "is_debut_movie": cast.is_debut_movie})
            all_cast.append(cast_obj)
        total_rating = 1 * rating.rating_one_count + 2 * rating.rating_two_count + 3 * rating.rating_three_count + 4 * rating.rating_four_count + 5 * rating.rating_five_count
        count_of_rating = rating.rating_one_count + rating.rating_two_count + rating.rating_three_count + rating.rating_four_count + rating.rating_five_count
        try:
            average_rating = total_rating / count_of_rating
        except ZeroDivisionError:
            average_rating = 0
        movie_obj.update({"movie_id": movie.movie_id, "name": movie.name, "cast": all_cast,
                          "box_office_collection_in_crores": movie.box_office_collection_in_crores,
                          "release_date": f'{movie.release_date.year}-{movie.release_date.month}-{movie.release_date.day}',
                          "director_name": movie.director.name, "average_rating": average_rating,
                          "total_number_of_ratings": count_of_rating})
        all_movies.append(movie_obj)

    return all_movies


def get_all_actor_objects_acted_in_given_movies(movie_objs):
    """
    :param movie_objs: [<Movie: movie_1>, <Movie: movie_2>, ..]
    :return:
    List of actor objects
    Sample Output: [<Actor: actor_1>, <Actor: actor_2>, ..]
    """
    # m = Movie.objects.get(movie_id="movie_2")
    # m1 = Movie.objects.get(movie_id="movie_1")
    # m2 = Movie.objects.get(movie_id="movie_3")
    # actors_list=[]
    # movie_objs=[]
    # movie_objs.append(m)
    # movie_objs.append(m1)
    # movie_objs.append(m2)

    actors_list = []
    for movie in movie_objs:
        for actor in movie.actors.all():
            if actor not in actors_list:
                actors_list.append(actor)

    return actors_list


def get_female_cast_details_from_movies_having_more_than_five_female_cast():

    """
    :return:
    [{
        "movie_id": 1,
        "name": "Titanic",
        "cast": [
            {
                "actor": {
                    "name": "Kate Winslet",
                    "actor_id": 1
                },
                "role": "Lead Actress",
                "is_debut_movie": False
            }
        ],
        "box_office_collection_in_crores": "218.7",
        "release_date": "1997-11-18",
        "director_name": "James Cameron",
        "average_rating": 4.9,
        "total_number_of_ratings": 1000
    }]
    """


    movies = Movie.objects.annotate(total=Count('actors__gender')).filter(total_gt= 5).values()
    return movies
# check

def get_actor_movies_released_in_year_greater_than_or_equal_to_2000():
    """
    :return: a list of Movie model instances
    [
        {
            "name": "Kate Winslet",
            "actor_id": 1
            "movies": [
                {
                    "movie_id": 1,
                    "name": "Titanic",
                    "cast": [
                        {
                            "role": "Lead Actress",
                            "is_debut_movie": False
                        }
                    ],
                    "box_office_collection_in_crores": "218.7",
                    "release_date": "1997-11-18",
                    "director_name": "James Cameron",
                    "average_rating": 4.9,
                    "total_number_of_ratings": 1000
                }
            ]
        }
    ]
    """
    year =2000
    movies = Movie.objects.filter(release_date__year__gt =year)
    actors_of_2000=[]
    for movie in movies:
        actors = movie.actors.all()
        actors_of_2000.append(actors)

    return actors_of_2000


def reset_ratings_for_movies_in_given_year(year):
    """
    :return: year
    """

    movies = Movie.objects.filter(release_date__year =year)
    for movie in movies:
        rating = Rating.objects.get(movie=movie)
        rating.rating_five_count=0
        rating.rating_four_count=0
        rating.rating_three_count=0
        rating.rating_two_count=0
        rating.rating_one_count=0
        rating.save()

