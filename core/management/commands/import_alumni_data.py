from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Point
from core.models import Alumni  # Adjust this import as needed
import csv

class Command(BaseCommand):
    help = 'Import alumni data from CSV to PostgreSQL'

    def handle(self, *args, **options):
        with open('//Users/aahishsunar/Desktop/NDA/alumni.csv', 'r') as file:  # Update this path
            reader = csv.DictReader(file)
            for row in reader:
                Alumni.objects.create(
                    name=row['Name'],
                    email=row['Email'],
                    city=row.get('City', ''),
                    country=row.get('Country', ''), 
                    latitude=Point(float(row['Latitude']), float(row['Longitude'])),
                    longitude=Point(float(row['Latitude']), float(row['Longitude'])),
                    graduation_year=int(row['Graduation Year'])
                )
        self.stdout.write(self.style.SUCCESS('Successfully imported alumni data'))


