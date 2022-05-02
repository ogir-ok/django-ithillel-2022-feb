from unittest import mock
from unittest.mock import patch

from django.test import TestCase
from apps.imdb.utils import next_num


class TestUtils(TestCase):
    def return_50(self):
        return 50

    def test_next_num__when_rand_more_than_50__should_return_n_plus_5(self):
        with patch("apps.imdb.utils.get_rand", lambda: 50):
            assert next_num(5) == 10
