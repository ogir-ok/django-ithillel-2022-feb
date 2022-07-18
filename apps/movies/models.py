from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Movie(models.Model):

    class TitleType(models.TextChoices):

        SHORT = "short", _("Short")
        MOVIE = "movie", _("Movie")

    imdb_id = models.CharField(max_length=255, verbose_name=_("IMDB ID"))
    title_type = models.CharField(max_length=255, choices=TitleType.choices, verbose_name=_("Type of the title"))
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    is_adult = models.BooleanField(verbose_name=_('Is Adult'))
    date = models.DateField(verbose_name=_("Release Date"), null=True)
    genres = ArrayField(models.CharField(max_length=255), verbose_name=_("Genres"), null=True)

    def __str__(self):
        return f"{self.name}"


class Person(models.Model):

    imdb_id = models.CharField(max_length=255, verbose_name=_("IMDB ID"))
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    birth_date = models.DateField(verbose_name=_("Birth Date"), null=True)
    death_date = models.DateField(verbose_name=_("Death Date"), null=True)

    def __str__(self):
        return f"{self.name}"


class PersonMovie(models.Model):

    movie_id = models.ForeignKey(Movie, on_delete=models.PROTECT)
    person_id = models.ForeignKey(Person, on_delete=models.PROTECT)
    ordering = models.IntegerField(verbose_name=_("Ordering"))
    category = models.CharField(max_length=255, verbose_name=_("Category"))
    job = models.CharField(max_length=255, verbose_name=_("Job"), null=True)
    characters = ArrayField(models.CharField(max_length=255), verbose_name=_("Characters"), null=True)
