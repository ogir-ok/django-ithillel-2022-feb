from django.core.management.base import BaseCommand
from ...models import Person  # change class
import re


class Command(BaseCommand):
    help = 'Load Person'  # change help

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
        if data[2] == '\\N':
            data[2] = None
        else:
            data[2] += '-12-31'
        if data[3] == '\\N':
            data[3] = None
        else:
            data[3] += '-12-31'
        person = Person(data[0], data[1], data[2], data[3])  # char, char, date, date
        person.save()
