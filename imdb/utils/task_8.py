from imdb.models import Movie

# Movie 8

def update_director_for_given_movie(movie_obj, director_obj):
    """
    :param movie_obj: <Movie movie_1>
    :param director_obj: <Director: Director 1>
    :return:
    """
    movie = Movie.objects.get(movie_id=movie_obj.movie_id)
    movie.director = director_obj
    movie.save()


# Movie 9
def get_distinct_movies_acted_by_actor_whose_name_contains_john():
    """
    :return:
    movie_objs: [<Movie movie_1>, <Movie movie_2>, ..]
    """
    movie = Movie.objects.filter(actors__name__icontains="john").distinct()
    return movie
