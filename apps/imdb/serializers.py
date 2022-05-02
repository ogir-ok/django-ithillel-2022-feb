from rest_framework import serializers

from apps.imdb.models import Movie, Person, PersonMovie


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ["id", "name"]


class MovieSerilalizer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            "id",
            "name",
            "genres",
            "director",
        ]

    director = serializers.SerializerMethodField()

    def get_director(self, object):
        director = PersonMovie.objects.filter(
            movie=object, job__startswith="director"
        ).first()
        if not director:
            return None
        return director.person.name


class MovieDetailSerializer(MovieSerilalizer):
    class Meta:
        model = Movie
        fields = ["id", "name", "genres", "director", "persons"]

    persons = PersonSerializer(many=True)
