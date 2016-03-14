import os, sys
import xmltodict

proj_path = "/Users/crawforb/Projects/Development/PyCharmProjects/BCC/"
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BCC.settings')
sys.path.append(proj_path)
os.chdir(proj_path)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
import refdata.models

with open('refdata/data-import/ratingcontentdescriptors.xml') as fd:
    doc = xmltodict.parse(fd.read())

    for cd in doc['DataExchange']['root']['ratingDetails']['RatingContentDescriptor']:
        new_cd = refdata.models.RatingContentDescriptor()
        new_cd.ebxid = cd['base'].get('id', None)
        new_cd.descriptor = cd['base'].get('name', None)
        new_cd.description = cd['base'].get('description', None)
        new_cd.save()
