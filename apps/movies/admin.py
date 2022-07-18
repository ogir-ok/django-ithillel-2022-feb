from django.contrib import admin

from apps.movies.models import Movie, Person, PersonMovie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(PersonMovie)
class PersonMovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'person_id', 'movie_id')
