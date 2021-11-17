from django.db import models

# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=50)

class Genre(models.Model):
    name = models.CharField(max_length=50)
    
class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateField()
    runtime = models.CharField(max_length=30)
    vote_average = models.FloatField()
    poster_path = models.TextField()
    backdrop_path = models.TextField()
    video = models.TextField()
    actor = models.ManyToManyField(Actor, related_name='movies')
    genre = models.ManyToManyField(Genre, related_name='movies')