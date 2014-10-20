import unicodecsv

from ftfy import fix_text

from django.core.management.base import BaseCommand

from organizations.models import Organization


class Command(BaseCommand):
    args = 'filename'
    help = 'Load the organization translations in the given CSV'

    def handle(self, filename, *args, **options):
        for row in unicodecsv.DictReader(open(filename, 'r'), encoding='latin-1'):
            mission = fix_text(row['Mission'])
            mission_es = fix_text(row['Mision (es)'])
            orgs = Organization.objects.filter(mission__contains=mission)
            if not orgs:
                print "Couldn't find organization matching %s" % mission
                continue
            orgs.update(mission_es=mission_es)
