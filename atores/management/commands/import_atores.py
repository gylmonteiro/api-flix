import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from atores.models import Ator


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',
            type=str,
            help="Nome do arquivo com atores"
            )

    def handle(self, *args, **options):
        file_name = options['file_name']

        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                nome = row['nome']
                data_de_nascimento = datetime.strptime(row["data_nascimento"], '%Y-%m-%d').date()
                nacionalidade = row['nacionalidade']

                self.stdout.write(self.style.NOTICE(nome))
                Ator.objects.create(nome=nome, data_de_nascimento=data_de_nascimento, nacionalidade=nacionalidade)

            self.stdout.write(self.style.SUCCESS('ATORES IMPORTADOS COM SUCESSO'))
