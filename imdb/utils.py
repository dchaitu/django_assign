#
#
#
# # Task 5
#
# def get_average_rating_of_movie(movie_obj):
#     """
#     :param movie_obj: <Movie: movie_1>
#     :return:
#     Average Rating
#     Sample Output: 4.5
#     """
#     # AR = 1*a+2*b+3*c+4*d+5*e/(R)
#     rating = Rating.objects.get(movie_id=movie_obj.movie_id)
#     total_rating = 1 * rating.rating_one_count + 2 * rating.rating_two_count + 3 * rating.rating_three_count + 4 * rating.rating_four_count + 5 * rating.rating_five_count
#     count_of_rating = rating.rating_one_count + rating.rating_two_count + rating.rating_three_count + rating.rating_four_count + rating.rating_five_count
#     average_rating = total_rating / count_of_rating
#     return average_rating
#
#
# def delete_movie_rating(movie_obj):
#     """
#     :param movie_obj: <Movie: movie_1>
#     :return:
#     """
#     return Rating.objects.get(movie_id=movie_obj.movie_id).delete()
#
#
# if __name__ == '__main__':
#     pass
#     # populate_database(actors_list=[], movies_list=[], directors_list=[], movie_rating_list=[])
#     # populate_databases(actors_list=[], movies_list=[], directors_list=[], movie_rating_list=[])
#     # add_actors_to_movie(movie_id="movie_3")
# # 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
#
# # actor_2
# # Actor 2
# # Director 2
# # movie_2
# # Movie 2
