from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Movie(models.Model):  # title.basics.tsv
    TITLE_TYPE = [
        ('short', 'human readable: SHORT'),
        ('movie', 'human readable: MOVIE'),
    ]
    imdb_id = models.CharField(primary_key=True, max_length=255)  # tconst
    title_type = models.CharField(max_length=255, choices=TITLE_TYPE)  # titleType: short/movie
    name = models.CharField(max_length=255)  # primaryTitle
    is_adult = models.BooleanField()  # isAdult
    year = models.DateField(null=True)  # startYear
    genres = ArrayField(models.CharField(max_length=255), default=list)  # genres

    def __str__(self):
        return self.name


class Person(models.Model):  # name.basics.tsv
    imdb_id = models.CharField(primary_key=True, max_length=255)  # nconst
    name = models.CharField(max_length=255)  # primaryName
    birth_year = models.DateField(null=True)  # birthYear
    death_year = models.DateField(null=True)  # deathYear

    def __str__(self):
        return self.name


class PersonMovie(models.Model):  # title.principals.tsv
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)  # tconst
    person = models.ForeignKey('Person', on_delete=models.CASCADE)  # nconst
    order = models.IntegerField()  # ordering
    category = ArrayField(models.CharField(max_length=255), default=list)  # category
    job = ArrayField(models.CharField(max_length=255), default=list)  # job
    characters = ArrayField(models.CharField(max_length=255), default=list)  # characters
