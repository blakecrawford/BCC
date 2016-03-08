import os, sys
import xmltodict

proj_path = "/Users/crawforb/Projects/Development/PyCharmProjects/BCC/"
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BCC.settings')
sys.path.append(proj_path)
os.chdir(proj_path)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
import refdata.models

with open('refdata/data-import/genretypes.xml') as fd:
    doc = xmltodict.parse(fd.read())

    for old_type in doc['DataExchange']['root']['genreDetails']['GenreType']:
        new_type = refdata.models.GenreType()
        new_type.name = old_type['base'].get('name', None)
        new_type.ebxid = old_type['base'].get('id', None)
        new_type.save()
