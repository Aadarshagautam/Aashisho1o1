import csv
from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Point
from core.models import Alumni

class Command(BaseCommand):
    help = 'Load alumni data from a CSV file'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Alumni.objects.all().delete()

        #Path to your CSV file
        csv_file_path = '/Users/aahishsunar/Desktop/NDA/alumni.csv/'

        with open(csv_file_path, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                Alumni.objects.create(
                    name=row['Name'],
                    email=row['Email'],
                    city=row['City'],
                    country=row['Country'],
                    latitude=Point(float(row['Latitude']), float(row['Longitude'])),
                    longitude=Point(float(row['Latitude']), float(row['Longitude'])),
                    graduation_year=row['Graduation Year']
                )
        self.stdout.write(self.style.SUCCESS('Alumni data loaded successfully'))