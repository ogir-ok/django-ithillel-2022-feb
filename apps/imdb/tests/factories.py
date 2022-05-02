import factory

from apps.imdb.models import Movie, PersonMovie, Person


class MovieFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Movie

    name = factory.Faker("name")
    is_adult = factory.LazyFunction(lambda: True)
    genres = factory.lazy_attribute(lambda x: [])


class PersonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Person

    name = factory.Faker("name")


class PersonMovieFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PersonMovie

    order = 1
    movie = factory.SubFactory(MovieFactory)
    person = factory.SubFactory(PersonFactory)
