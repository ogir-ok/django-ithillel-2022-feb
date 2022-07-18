import os.path
from django.core.management.base import BaseCommand
from apps.movies.models import Person


class Command(BaseCommand):
    help = "Imports persons from tsv file"

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
                if not line.startswith("nm"):
                    continue

                data = line.split("\t")

                person_data = {
                    "name": data[1],
                    "birth_date": None if data[2] == "\\N" else f"{data[2]}-01-01",
                    "death_date": None if data[3] == "\\N" else f"{data[3]}-01-01",
                }
                person, created = Person.objects.get_or_create(
                    imdb_id=data[0], defaults=person_data
                )

                if created:
                    Person.objects.filter(id=person.id).update(**person_data)
