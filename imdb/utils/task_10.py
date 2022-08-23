from imdb.models import Rating


# Task 10

def remove_all_actors_from_given_movie(movie_obj):
    """
    :param movie_obj: <Movie: movie_1>
    :return:
    """
    movie_actors = movie_obj.actors.all()
    for a in movie_actors:
        movie_obj.actors.remove(a)


# Task 11

def get_all_rating_objects_for_given_movies(movie_objs):
    """
    :param movie_objs: [<Movie: movie_1>, <Movie: movie_2>, <Movie: movie_3>,..]
    :return:
    rating_objs: [<Rating: rating_1>, <Rating: rating_2>, ..]
    """
    rating_objs = []
    for movie in movie_objs:
        try:
            rating = Rating.objects.get(movie_id=movie.movie_id)
        except:
            rating = None

        rating_objs.append(rating)
        rating_objs = [rating for rating in rating_objs if rating is not None]

    return rating_objs
