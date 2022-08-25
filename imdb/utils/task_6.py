from imdb.models import Rating, Movie, Actor


def delete_movie_rating(movie_obj):
    """
    :param movie_obj: <Movie: movie_1>
    :return:
    """
    return Rating.objects.get(movie_id=movie_obj.movie_id).delete()


def get_all_actor_objects_acted_in_given_movies(movie_objs):
    """
    :param movie_objs: [<Movie: movie_1>, <Movie: movie_2>, ..]
    :return:
    List of actor objects
    Sample Output: [<Actor: actor_1>, <Actor: actor_2>, ..]
    """

    # actors_list = []
    # for movie in movie_objs:
    #     for actor in movie.actors.all():
    #         if actor not in actors_list:
    #             actors_list.append(actor)
    actors_list = list(Actor.objects.filter(movie__in=movie_objs))
    return actors_list

