from django.core.management.base import BaseCommand
from ...models import Movie  # change class
import re


class Command(BaseCommand):
    help = 'Load Movies'  # change help

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
        if data[5] == '\\N':
            data[5] = None
        else:
            data[5] += '-12-31'
        data[8] = data[8].split(',')
        movie = Movie(data[0], data[1], data[2], data[4], data[5], data[8])  # char, char, char, bool, date, array
        movie.save()
