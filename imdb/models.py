from django.db import models

# Create your models here.
'''
name, a string value of maximum 100 characters long
movie_id a string of maximum 100 characters long can be used to uniquely identifiy a movie in the database.
release_date indicating the date on which the movie is released.
box_office_collection_in_crores a float value representing the box office collections of the movie in crores i.e. 100.23
Only one director directs a movie. And a movie must have a director


'''

'''

An Actor has

actor_id, a string of maximum 100 characters long, which can be used to uniquely identify an actor in the database.
a name, a string of maximum 100 characters long

'''


class Actor(models.Model):
    actor_id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    GENDER = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(max_length=1,choices=GENDER,default="M")


    def __str__(self):
        return self.name


'''
An actor can act in more than one movie.
A movie can have more than one actor.
An actor can have more than one role (a string of maximum 50 characters long) in the movie.
is_debut_movie a boolean in Cast represents if it is a debut movie for that specific actor and is false by default.

'''


class Director(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return  self.name


class Cast(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    actor = models.ForeignKey('Actor', on_delete=models.CASCADE)
    role = models.CharField(max_length=50)
    is_debut_movie = models.BooleanField()

    def __str__(self):
        return  self.role


class Movie(models.Model):
    name = models.CharField(max_length=100)
    movie_id = models.CharField(max_length=100, primary_key=True)
    actors = models.ManyToManyField(Actor,through=Cast)
    release_date = models.DateField()
    box_office_collection_in_crores = models.FloatField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return  self.name






'''


In rating, we store the number of 1,2,3,4 & 5 ratings a movie has got in the following fields rating_one_count, rating_two_count,rating_three_count,rating_four_coun & rating_five_count respectively.
Ratings start with 0 by default.

'''


class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating_one_count = models.IntegerField(default=0)
    rating_two_count = models.IntegerField(default=0)
    rating_three_count = models.IntegerField(default=0)
    rating_four_count = models.IntegerField(default=0)
    rating_five_count = models.IntegerField(default=0)

    def __str__(self):
        return  f'Rating for {self.movie_id}'
