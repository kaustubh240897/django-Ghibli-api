from django.db import models

class Actor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=100)
    url = models.URLField()

class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    actors = models.ManyToManyField(Actor)
