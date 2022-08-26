from django.db.models import Q

from imdb.models import Rating, Movie, Cast, Actor


def get_movies_released_in_summer_in_given_years():
    """
    :return: movie dict as in task 1
    May,June,July
    """

    movies = Movie.objects.filter(release_date__year__gte=2005, release_date__month__gte=5,
                                  release_date__year__lte=2010, release_date__month__lte=7, ).distinct()
    movie_names = [movie.name for movie in movies]
    return get_movies_by_given_movie_names(movie_names)


def get_movie_names_with_actor_name_ending_with_smith():
    """
    :return:
    ["The Pursuit of Happyness", "Aladdin"]
    """
    selected_movies = Movie.objects.filter(actors__name__iendswith="Smith").distinct()
    movie_names = [movie.name for movie in selected_movies]
    return movie_names


def get_movie_names_with_ratings_in_given_range():
    """
    :return:
    ["Avengers, End Game", "The Iron Man, Part 3"]
    """
    min_rating = Q(rating_five_count__gte=1000)
    max_rating = Q(rating_five_count__lte=3000)
    movie_names = Rating.objects.filter(min_rating & max_rating).values_list('movie__name', flat=True)

    return list(movie_names)


def get_movie_names_with_ratings_above_given_minimum():
    """
    :return:
    ["Avengers, End Game", "The Iron Man, Part 3"]
    """
    released_year = Q(movie__release_date__year__gt=2000)
    min_five_rating = Q(rating_five_count__gte=500)
    min_four_rating = Q(rating_four_count__gte=1000)
    min_three_rating = Q(rating_three_count__gte=2000)
    min_two_rating = Q(rating_two_count__gte=4000)
    min_one_rating = Q(rating_two_count__gte=8000)
    movie_names = Rating.objects.filter(released_year &
                                        (
                                                    min_five_rating | min_four_rating | min_three_rating | min_two_rating | min_one_rating)).values_list(
        'movie__name', flat=True)

    return movie_names


def get_movie_directors_in_given_year():
    year = 2000
    movies = Movie.objects.filter(release_date__year=year).select_related('director')
    director_names = []
    for movie in movies:
        if movie.director.name not in director_names:
            director_names.append(movie.director.name)
    return director_names


def get_actor_names_debuted_in_21st_century():
    """
    :return:
    ["VD"]
    """
    year = 2000
    debut = Q(cast__is_debut_movie=True)
    twenty_first_century = Q(movie__release_date__year__gt=year)
    actors = Actor.objects.filter(debut & twenty_first_century)
    actor_names = [actor.name for actor in actors]
    return actor_names


def get_director_names_containing_big_as_well_as_movie_in_may():
    """
    :return:
    ["James Cameron"]
    """
    month = 5
    word = "big"
    movie_release = Q(release_date__month=month)
    movie_word = Q(name__contains=word)
    movies = Movie.objects.filter(movie_release | movie_word).select_related('director').distinct()
    director_names = []
    for movie in movies:
        if movie.director.name not in director_names:
            director_names.append(movie.director.name)
    return director_names


def get_director_names_containing_big_and_movie_in_may():
    """
    :return:
    ["James Cameron"]
    """
    month = 5
    word = "big"
    movie_release = Q(release_date__month=month)
    movie_word = Q(name__contains=word)
    movies = Movie.objects.filter(movie_release & movie_word).select_related('director').distinct()
    director_names = []
    for movie in movies:
        if movie.director.name not in director_names:
            director_names.append(movie.director.name)
    return director_names


def reset_ratings_for_movies_in_this_year():
    """
    """

    year = 2000
    Rating.objects.filter(movie__release_date__year=year).update(
        rating_five_count=0, rating_four_count=0, rating_three_count=0,
        rating_two_count=0, rating_one_count=0)


def get_movies_by_given_movie_names(movie_names):
    all_movies = []
    movie_cast_objs = Cast.objects.filter(movie__name__in=movie_names).select_related('movie__director', 'actor')
    movie_rating_objs = Rating.objects.filter(movie__name__in=movie_names).select_related('movie')

    rating_for_movies={}

    for cast in movie_cast_objs:
        movie_obj = {}
        all_casts=[]
        cast_obj = {}
        actor_obj = {}
        actor_obj.update({"name": cast.actor.name, "actor_id": cast.actor.actor_id, })
        cast_obj.update({"actor": actor_obj, "role": cast.role, "is_debut_movie": cast.is_debut_movie})
        all_casts.append(cast_obj)
        movie_obj.update({"movie_id": cast.movie.movie_id, "name": cast.movie.name, "cast": all_casts,
                    "box_office_collection_in_crores": cast.movie.box_office_collection_in_crores,
                    "release_date": f'{cast.movie.release_date.year}-{cast.movie.release_date.month}-{cast.movie.release_date.day}',
                    "director_name": cast.movie.director.name})
        rating_obj = {}
        for rating in movie_rating_objs:

            rating_obj.update({"rating_for_movie_id": rating.movie.movie_id})
            total_rating = 1 * rating.rating_one_count + 2 * rating.rating_two_count + 3 * rating.rating_three_count + 4 * rating.rating_four_count + 5 * rating.rating_five_count
            count_of_rating = rating.rating_one_count + rating.rating_two_count + rating.rating_three_count + rating.rating_four_count + rating.rating_five_count
            average_rating = total_rating / count_of_rating
            rating_obj.update({"average_ratings": round(average_rating, 2), "total_number_of_ratings": count_of_rating})


        movie_obj.update(rating_obj)
        all_movies.append(movie_obj)

    return all_movies


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
