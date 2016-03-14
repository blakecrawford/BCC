import os, sys
import xmltodict

proj_path = "/Users/crawforb/Projects/Development/PyCharmProjects/BCC/"
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BCC.settings')
sys.path.append(proj_path)
os.chdir(proj_path)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
import refdata.models

with open('refdata/data-import/ratingauthority.xml') as fd:
    doc = xmltodict.parse(fd.read())

    for ra in doc['DataExchange']['root']['ratingDetails']['RatingAuthority']:
        new_ra = refdata.models.RatingAuthority()
        new_ra.ebxid = ra['base'].get('id', None)
        new_ra.name = ra['base'].get('name', None)
        new_ra.description = ra['base'].get('description', None)
        new_ra.ref_link = ra.get('RefLink', None)
        new_ra.save()
