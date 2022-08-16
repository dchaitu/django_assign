from imdb.models import Rating, Movie


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

