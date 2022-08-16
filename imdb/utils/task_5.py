from imdb.models import Rating


# Task 5get
def get_average_rating_of_movie(movie_obj):
    """
    :param movie_obj: <Movie: movie_1>
    :return:
    Average Rating
    Sample Output: 4.5
    """
    # AR = 1*a+2*b+3*c+4*d+5*e/(R)
    rating = Rating.objects.get(movie_id=movie_obj.movie_id)
    total_rating = 1 * rating.rating_one_count + 2 * rating.rating_two_count + 3 * rating.rating_three_count + 4 * rating.rating_four_count + 5 * rating.rating_five_count
    count_of_rating = rating.rating_one_count + rating.rating_two_count + rating.rating_three_count + rating.rating_four_count + rating.rating_five_count
    average_rating = total_rating / count_of_rating
    return average_rating
