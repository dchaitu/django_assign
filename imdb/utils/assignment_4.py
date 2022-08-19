from django.db.models import Q, Count,Avg

from imdb.models import Actor, Rating, Movie, Cast


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
    # Profile.objects.values('age').annotate(Count('age'))
    movies = Movie.objects.values('actors').annotate(actors_count=Count('actors',distinct=True))
    return movies
# Need to check

def get_male_and_female_actors_count_for_each_movie():
    """
    :return: a list of Movie model instances
    """

    movies = Movie.objects.annotate(male_count=Count('actors', filter=Q(actors__gender='M')),
                                    female_count=Count('actors', filter=Q(actors__gender='F'))).values('male_count',
                                                                                                       'female_count')
    return movies

def get_roles_count_for_each_movie():
    """
    :return:
    ["Avengers, End Game", "The Iron Man, Part 3"]
    """
    movies =  Movie.objects.values('name').annotate(roles_count = Count('actors__cast__role',distinct= True))
    return  movies

def get_role_frequency():
  """
  :return: {
    "role_1": 3,
    "role_2": 5
  }
  """

  roles = Cast.objects.values('role').annotate(roles_count =Count('role'))
  return roles


def get_role_frequency_in_order():
  """
  :return: [('role_2', 5), ('role_1', 3)]

  """
  roles = Cast.objects.values('role').annotate(roles_count =Count('role')).order_by('-roles_count')
  return roles


def get_no_of_movies_and_distinct_roles_for_each_actor():
    """
    :return: a list of Movie model instances
    """
    # Select
    # Count(*), imdb_actor.name
    # FROM
    # imdb_cast, imdb_actor
    # Where
    # imdb_cast.actor_id = imdb_actor.actor_id
    # Group
    # By
    # imdb_cast.actor_id
    # actors = Actor.objects.values('actor_id').annotate(Count('movie__cast__role',distinct=True)).annotate(Count('movie__movie_id'))
    actors = Cast.objects.values('actor__actor_id').annotate(Count('actor'))
    return actors
# Check

def get_movies_with_atleast_forty_actors():
    """
    :return: a list of Movie model instances
    """
    atleast_count = 40
    movie_actors = Movie.objects.annotate(atleast_count = Count('movie__actors')).filter(atleast_count__gt = atleast_count)
    return movie_actors

def get_average_no_of_actors_for_all_movies():
    """
    :return: 4.123
    """

    # fieldname = 'actors'
    # average_no_of_actors = Movie.objects.values(fieldname).annotate(the_count=Count('actors.all()'),the_avg = Avg(fieldname)).values('the_count','the_avg')
    # return  average_no_of_actors
    count_actors = Movie.objects.aggregate(Count('actors'))
    count_movies = Movie.objects.aggregate(Count('movie_id'))
    avg = count_actors/count_movies
    return round(avg, 3)