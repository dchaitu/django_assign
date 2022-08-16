from imdb.models import Actor, Director


def get_actors_list():
    return Actor.objects.all()


def get_directors_list():
    return Director.objects.all()