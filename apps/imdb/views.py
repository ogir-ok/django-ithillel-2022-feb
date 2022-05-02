from rest_framework.generics import (
    ListCreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)

from apps.imdb.models import Movie
from apps.imdb.serializers import MovieSerilalizer


class MyView(ListCreateAPIView):
    serializer_class = MovieSerilalizer
    queryset = Movie.objects.all().prefetch_related("persons")


class MovieRetrieveUpdateView(RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerilalizer
    queryset = Movie.objects.all().prefetch_related("persons")
