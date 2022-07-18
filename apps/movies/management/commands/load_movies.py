import os.path

from django.core.management.base import BaseCommand

from apps.movies.models import Movie


class Command(BaseCommand):
    help = "Imports movies from tsv file"

    def add_arguments(self, parser):
        parser.add_argument("-f", "--file", type=str, required=True)

    def handle(self, *args, **options):
        file = options.get("file")

        if not os.path.exists(file):
            print("File does not exist")

        with open(file, encoding="utf-8") as fileopen:
            for line in fileopen.readlines():
                if not line:
                    continue
                if not line.startswith("tt"):
                    continue
                data = line.split("\t")

                if data[1] not in ("movie", "short"):
                    continue

                movie_data = {
                    "title_type": data[1],
                    "name": data[2],
                    "is_adult": data[4],
                    "date": None if data[5] == "\\N" else data[5],
                    "genres": data[8].split(","),
                }
                movie, created = Movie.objects.get_or_create(
                    imdb_id=data[0], defaults=movie_data
                )

                if created:
                    Movie.objects.filter(id=movie.id).update(**movie_data)
