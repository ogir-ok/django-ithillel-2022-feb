from unittest import TestCase
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

from apps.imdb.models import Movie, PersonMovie, Person
from apps.imdb.tests.factories import MovieFactory, PersonMovieFactory

User = get_user_model()


class MyTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(email="test@test.com")
        self.personmovie = PersonMovieFactory()
        self.personmovie2 = PersonMovieFactory(movie=self.personmovie.movie)

    def test_imdb_list(self):
        response = self.client.get("/api/imdb/")
        self.assertEqual(response.status_code, 200)

        self.assertEqual(
            response.data["results"],
            [
                {
                    "id": self.personmovie.movie.id,
                    "name": self.personmovie.movie.name,
                    "genres": self.personmovie.movie.genres,
                    "director": None,
                }
            ],
        )

    def test_create_movie__when_no_data__should_return_404(self):
        response = self.client.post(
            "/api/imdb/", {"name": "New Movie", "genres": ["a", "b"]}
        )
        self.assertEqual(response.status_code, 400)

    def test__create_movie__when_data_is_ok__should_create_movie(self):
        pass

    def test__create_movie__when_is_adult_is_not_passed__shoud_return_400(self):
        pass
