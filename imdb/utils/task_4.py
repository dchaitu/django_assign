from imdb.models import Movie

# Task 4
def get_movies_directed_by_director(director_obj):
    """
    :param director_obj: <Director: Director 1>
    :return:
    List of movie objects
    Sample Output: [<Movie: movie_1_obj>, <Movie: movie_2_obj>]
    """
    return Movie.objects.filter(director=director_obj)

