from django.db import models
from django.contrib.postgres.fields import ArrayField


class Movie(models.Model):
    choices_type = [('short', 'sh: SHORT'), ('movie', 'mv: MOVIE'), ]

    imdb_id = models.CharField(primary_key=True, max_length=255)
    title_type = models.CharField(max_length=255, choices=choices_type)
    name = models.CharField(max_length=255)
    is_adult = models.BooleanField()
    year = models.DateField(null=True)
    genres = ArrayField(models.CharField(max_length=255), default=list)

    def __str__(self):
        return self.name


class Person(models.Model):
    imdb_id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)
    birth_year = models.DateField(null=True)
    death_year = models.DateField(null=True)

    def __str__(self):
        return self.name


class PersonMovie(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    order = models.IntegerField()
    category = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    characters = ArrayField(models.CharField(max_length=255), null=True)
