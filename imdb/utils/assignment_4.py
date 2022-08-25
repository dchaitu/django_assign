from django.db.models import Q, Count, Avg

from imdb.models import Actor, Movie, Cast


def get_average_box_office_collections():
    """
    :return: float value
    100.123
    """
    average_box_office_collections = Movie.objects.aggregate(Avg('box_office_collection_in_crores'))
    return average_box_office_collections


def get_movies_with_distinct_actors_count():
    """
    :return: a list of Movie model instances
    """

    movies_with_actors = Movie.objects.values('actors__movie__name').annotate(actors_count=Count('actors', distinct=True))
    return movies_with_actors



def get_male_and_female_movies_count_for_each_movie():
    """
    :return: a list of Movie model instances
    """
    male_count=Count('actors', filter=Q(actors__gender='M'))
    female_count = Count('actors', filter=Q(actors__gender='F'))
    movies = Movie.objects.annotate(male_count=male_count,female_count=female_count).values('name','male_count','female_count')
    return movies


def get_roles_count_for_each_movie():
    """
    :return:
    ["Avengers, End Game", "The Iron Man, Part 3"]
    """
    movies = Movie.objects.annotate(roles_count=Count('actors__cast__role', distinct=True)).values('name','roles_count')
    return movies


def get_role_frequency():
    """
  :return: {
    "role_1": 3,
    "role_2": 5
  }
  """

    roles = Cast.objects.values('role').annotate(roles_count=Count('role'))
    return roles


def get_role_frequency_in_order():
    """
  :return: [('role_2', 5), ('role_1', 3)]

  """
    roles = Cast.objects.values('role').annotate(roles_count=Count('role')).order_by('-roles_count')
    d={}
    for role in roles:
        d.update({role['role']:role['roles_count']})

    return roles


def get_no_of_movies_and_distinct_roles_for_each_actor():
    """
    :return: a list of Movie model instances
    """

    # Movie.objects.annotate(movies_count=Count('actors')).values('movies_count').order_by('-movies_count')
    role_count = Actor.objects.annotate(roles_count=Count('cast__role', distinct=True),count_of_movies=Count('movie', distinct=True)).values('name',
                                                                                               'roles_count','count_of_movies').order_by(
        '-roles_count')

    return role_count


# Check

def get_movies_with_atleast_forty_actors():
    """
    :return: a list of Movie model instances
    """
    atleast_count = 40
    movie_actors = Movie.objects.annotate(atleast_count=Count('actors')).filter(
        atleast_count__gt=atleast_count)
    return movie_actors


def get_average_no_of_actors_for_all_movies():
    """
    :return: 4.123
    """

    count_actors = Actor.objects.count()
    count_movies = Movie.objects.count()
    avg = count_actors / count_movies
    return round(avg, 3)
