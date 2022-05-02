from unittest import TestCase
from unittest.mock import patch

from django.http import HttpResponse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

from apps.authentication.tests.factories import UserFactory
from apps.imdb.models import Movie, PersonMovie, Person
from apps.imdb.tests.factories import MovieFactory, PersonMovieFactory

User = get_user_model()


def fake_init(self):
    self.get_response = lambda: HttpResponse()


@patch("apps.imdb.middleware.IMDBMiddleware.__init__", fake_init)
class TestMiddlewareTestcase(APITestCase):
    def setUp(self) -> None:
        self.user = UserFactory()
        self.user2 = UserFactory()

    def test_passing_4_requests__should_not_cause_errors(self):

        self.client.get("/imdb/movies")
        self.client.get("/imdb/movies")
        self.client.get("/imdb/movies")
        res = self.client.get("/imdb/movies")

        self.assertEqual(res.status_code, 200)

    def test_passing_5_requests__should_not_cause_errors(self):

        self.client.get("/imdb/movies")
        self.client.get("/imdb/movies")
        self.client.get("/imdb/movies")
        self.client.get("/imdb/movies")
        res = self.client.get("/imdb/movies")

        self.assertEqual(res.status_code, status.HTTP_402_PAYMENT_REQUIRED)

    def test_passing_5_request_by_first_user__second_user_ok(self):

        self.client.get("/imdb/movies")
        self.client.get("/imdb/movies")
        self.client.get("/imdb/movies")
        self.client.get("/imdb/movies")
        res = self.client.get("/imdb/movies")

        self.assertEqual(res.status_code, status.HTTP_402_PAYMENT_REQUIRED)
        self.client.login(self.user2)

        res = self.client.get("/imdb/movies")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
