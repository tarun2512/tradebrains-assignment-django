import csv
from django.core.management.base import BaseCommand
from companies.models import Company

class Command(BaseCommand):
    help = 'Load companies from CSV'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to CSV file')

    def handle(self, *args, **options):
        file_path = options['file_path']
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Company.objects.update_or_create(
                    symbol=row.get('symbol'),
                    defaults={
                        'company_name': row.get('company_name'),
                        'symbol': row.get('symbol'),
                        'scripcode': row.get('scripcode'),
                    }
                )
        self.stdout.write("Companies loaded successfully.")