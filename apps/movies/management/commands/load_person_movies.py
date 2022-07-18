import json
import os.path

from django.core.management.base import BaseCommand, CommandError

from apps.movies.models import Movie, Person, PersonMovie


class Command(BaseCommand):
    help = "Imports person+movies from tsv file"

    def add_arguments(self, parser):
        parser.add_argument("-f", "--file", type=str, required=True)

    def handle(self, *args, **options):
        file = options.get("file")

        if not os.path.exists(file):
            raise CommandError("File does not exist")

        with open(file, encoding="utf-8") as fileopen:
            for line in fileopen.readlines():
                if not line:
                    continue
                if not line.startswith("tt"):
                    continue
                data = line.split("\t")

                movie_id = Movie.objects.filter(imdb_id=data[0]).first()
                if not movie_id:
                    continue

                person_id = Person.objects.filter(imdb_id=data[2]).first()
                if not person_id:
                    continue

                person_movie_data = {
                    "ordering": int(data[1]),
                    "category": data[3],
                    "job": None if data[4] == "\\N" else data[4],
                    "characters": None if data[5].startswith("\\N") else json.loads(data[5]),
                }

                PersonMovie.objects.get_or_create(
                    movie_id=movie_id, person_id=person_id, defaults=person_movie_data
                )
