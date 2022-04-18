import csv
import os.path

from django.core.management.base import BaseCommand

from apps.imdb.models import Person


class Command(BaseCommand):
    help = "Imorts movies from tsv file"

    def add_arguments(self, parser):
        parser.add_argument("-f", "--file", type=str, required=True)

    def handle(self, *args, **options):
        file_name = options.get("file")

        if not os.path.exists(file_name):
            print("No file exists.")

        with open(file_name, encoding='utf-8') as f:
            reader = csv.DictReader(
                f,
                dialect=csv.excel_tab,
                fieldnames=[
                    "imdb_id",
                    "name",
                    "birth_date",
                    "death_date",
                    "primary_profession",
                    "known_for",
                ],
            )

            for line in reader:
                person_data = line
                imdb_id = person_data["imdb_id"]
                person_data.pop("primary_profession")
                person_data.pop("known_for")

                if person_data["birth_date"] == "\\N":
                    person_data["birth_date"] = None
                else:
                    person_data["birth_date"] = f'{person_data["birth_date"]}-01-01'

                if person_data["death_date"] == "\\N":
                    person_data["death_date"] = None
                else:
                    person_data["death_date"] = f'{person_data["death_date"]}-01-01'

                person, created = Person.objects.get_or_create(
                    imdb_id=imdb_id, defaults=person_data
                )

                if not created:
                    Person.objects.filter(id=person.id).update(**person_data)
