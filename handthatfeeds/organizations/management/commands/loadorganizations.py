import csv

from django.contrib.gis.geos import Point
from django.core.management.base import BaseCommand

from organizations.models import Organization, Sector, Type


class Command(BaseCommand):
    args = 'filename'
    help = 'Load the organizations in the given CSV'

    def get_sectors(self, raw):
        sectors = [sector.strip() for sector in raw.lower().split('/')]
        return [Sector.objects.get_or_create(name=s)[0] for s in sectors]

    def get_types(self, raw):
        # TODO expand to full type names
        types = [t.strip() for t in raw.lower().split('/')]
        return [Type.objects.get_or_create(name=t)[0] for t in types]

    def handle(self, filename, *args, **options):
        for row in csv.DictReader(open(filename, 'r')):
            try:
                point = Point(float(row['longitude']), float(row['latitude']),
                              srid=4326)
            except:
                self.stdout.write(u'Failed to get point for %s' % row['Name'])
                point = None

            organization = Organization(
                name=row['Name'],
                address_line1=row['Address'],
                city=row['City'],
                state_province=row['State'],
                postal_code=row['Zip'],
                email=row['Email'],
                phone=row['Phone #'],
                centroid=point,
            )
            organization.save()
            organization.sectors.add(*self.get_sectors(row['Food Sector(s)']))
            organization.types.add(*self.get_types(row['Organization Type']))
