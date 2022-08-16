from imdb.models import Movie

# Task 3
def get_no_of_distinct_movies_actor_acted(actor_id):
    """
    :param actor_id: 'actor_1'
    :return:
    Number of movies he/she acted
	Sample Output: 4
    """
    return Movie.objects.filter(actors__actor_id=actor_id).count()
