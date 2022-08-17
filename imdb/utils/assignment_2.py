from django.db.models import Q

from imdb.models import Actor, Rating, Movie, Cast


# Get the list of movies released in the months of May, June & July & between 2005 to 2010.
def get_movies_released_in_summer_in_given_years():
    """
    :return: movie dict as in task 1
    May,June,July
    """
    movie_list = []
    for i in range(2005, 2011):
        start_date = f'{i}-05-01'
        end_date = f'{i}-07-31'
        movies = Movie.objects.filter(release_date__gte=start_date, release_date__lte=end_date)
        if movies:
            movie_list.append(movies)
    return movie_list


# Get the list of movie names which have at least one actor with their name ending with “smith”.
# The search should be case insensitive & should return unique movie names.
def get_movie_names_with_actor_name_ending_with_smith():
    """
    :return:
    ["The Pursuit of Happyness", "Aladdin"]
    """

    movie_list = []
    movies = Movie.objects.filter(actors__name__icontains="Smith")
    for movie in movies:
        movie_list.append(movie.name)

    return movie_list


def get_movie_names_with_ratings_in_given_range():
    """
    :return:
    ["Avengers, End Game", "The Iron Man, Part 3"]
    """
    ratings_list = []
    min_rating = Q(rating_five_count__gt=1000)
    max_rating = Q(rating_five_count__lte=3000)
    ratings = Rating.objects.filter(min_rating & max_rating)
    for rating in ratings:
        movie = Movie.objects.get(movie_id=rating.movie_id_id)
        ratings_list.append(movie.name)
    return ratings_list


# Task 5
# Get the list of movie names which are released in the 21st century(release year >2000)
# and have at least 500 five star ratings or 1000 four star ratings or 2000 three star ratings or 4000 two star ratings or 8000 one star ratings
def get_movie_names_with_ratings_in_given_range():
    """
    :return:
    ["Avengers, End Game", "The Iron Man, Part 3"]
    """
    ratings_list = []

    # release_year = Q(movie_id__release_date.year=)
    min_rating = Q(rating_five_count__gt=500)
    min_four_rating = Q(rating_four_count__gt=1000)
    min_three_rating = Q(rating_three_count__gt=2000)
    min_two_rating = Q(rating_two_count__gt=4000)
    min_one_rating = Q(rating_two_count__gt=8000)
    ratings = Rating.objects.filter(min_rating | min_four_rating | min_three_rating | min_two_rating | min_one_rating)
    for rating in ratings:
        movie = Movie.objects.get(movie_id=rating.movie_id_id)
        ratings_list.append(movie.name)
    return ratings_list


# Task 6
def get_movie_directors_in_given_year():
    director_list = []
    year = 2000
    movies = Movie.objects.filter(release_date__year=year)
    for movie in movies:
        director_list.append(movie.director.name)

    return director_list


def get_actor_names_debuted_in_21st_century():
    """
    :return:
    ["VD"]
    """
    actor_names = []
    all_actors = []
    year = 2000
    movies = Movie.objects.filter(release_date__year__gt=year)
    for movie in movies:
        for actor in movie.actors.all():
            all_actors.append(actor)
    for actor in all_actors:
        cast_debuts = Cast.objects.filter(actor__actor_id=actor.actor_id)
        casts = cast_debuts.filter(is_debut_movie=True)
        for cast in casts:
            if cast:
                actor_names.append(cast.actor.name)

    return actor_names


def get_director_names_containing_big_as_well_as_movie_in_may():
    """
    :return:
    ["James Cameron"]
    """
    director_list = []
    month = 5
    word = "big"
    movie_release = Q(release_date__month=month)
    movie_word = Q(name__contains=word)
    movies = Movie.objects.filter(movie_release | movie_word)
    for movie in movies:
        director_list.append(movie.director.name)

    return director_list


def reset_ratings_for_movies_in_this_year():
    """
    """
    movie_ratings=[]
    year = 2000
    movies = Movie.objects.filter(release_date__year=year)
    for movie in movies:
        try:
            rating = Rating.objects.get(movie_id = movie.movie_id)
        except:
            rating = None
        if rating is not None:
            movie_ratings.append(rating)

        for rating in movie_ratings:
            rating.rating_five_count=0
            rating.rating_one_count=0
            rating.rating_two_count=0
            rating.rating_three_count=0
            rating.rating_four_count=0
            rating.save()

    return movie_ratings

def get_movies_by_given_movie_names(movie_names):
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
    all_movies=[]
    for name in movie_names:
        movie_details={}
        movie = Movie.objects.get(name=name)
        obj ={}
        rating = Rating.objects.get(movie_id=movie.movie_id)

        crew = Cast.objects.filter(movie__movie_id=movie.movie_id)


        total_rating = 1 * rating.rating_one_count + 2 * rating.rating_two_count + 3 * rating.rating_three_count + 4 * rating.rating_four_count + 5 * rating.rating_five_count
        count_of_rating = rating.rating_one_count + rating.rating_two_count + rating.rating_three_count + rating.rating_four_count + rating.rating_five_count
        average_rating = total_rating / count_of_rating
        obj.update({"movie_id": movie.movie_id,"name":movie.name,"box_office_collection_in_crores":movie.box_office_collection_in_crores,"release_date":movie.release_date,"director_name":movie.director.name,"average_rating":average_rating,"total_number_of_ratings":count_of_rating})
        all_movies.append(obj)

    return all_movies

