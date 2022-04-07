from django.core.management.base import BaseCommand
from ...models import Movie
import re


class Command(BaseCommand):
    help = 'Load Movies'


    def add_arguments(self, parser):
        parser.add_argument('-f', '--file', type=str, help='', )

    def handle(self, *args, **kwargs):
        path_file: str = kwargs['file']
        with open(path_file, 'r') as fr:
            while True:
                line: str = fr.readline().rstrip('\n')
                if line == "":
                    break

                data: list = re.split(r'\t', line)
                if data[5] == '\\N':
                    data[5] = None
                else:
                    data[5] += '-12-31'
                data[8] = data[8].split(',')
                movie = Movie(data[0], data[1], data[2], data[4], data[5], data[8])
                movie.save()
