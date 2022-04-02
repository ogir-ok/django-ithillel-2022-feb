from django.core.management.base import BaseCommand
from ...models import PersonMovie  # change class
import re


class Command(BaseCommand):
    help = 'Load PersonMovie'  # change help

    def add_arguments(self, parser):
        parser.add_argument('-f',
                            '--file',
                            type=str,
                            help='', )

    def handle(self, *a, **kwa):
        path_file: str = kwa['file']
        with open(path_file, 'r') as fr:
            while True:
                line: str = fr.readline().rstrip('\n')
                if line == "":
                    break
                self.get_save_data(line)  # change logic import

    @staticmethod
    def get_save_data(line):
        data: list = re.split(r'\t', line)  # data = [splits for splits in line.split('\t') if splits != '']
        data[3] = data[3].split(',')
        data[4] = data[4].split(',')
        data[5] = data[5].split(',')
        person_movie = PersonMovie(None, data[0], data[2], data[1], data[3], data[4], data[5])  # id, foreign(char), foreign(char), int, array, array, array
        person_movie.save()
