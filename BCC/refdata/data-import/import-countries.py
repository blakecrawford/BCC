import os, sys
import xmltodict
import uuid

proj_path = "/Users/crawforb/Projects/Development/PyCharmProjects/BCC/"
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BCC.settings')
sys.path.append(proj_path)
os.chdir(proj_path)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
import refdata.models

with open('refdata/data-import/countries.xml') as fd:
    doc = xmltodict.parse(fd.read())

    for country in doc['DataExchange']['root']['Country']:
        new_country = refdata.models.Country()
        new_country.name = country['base'].get('name')
        new_country.description = country ['base'].get('description', None)
        new_country.code2 = country.get('code2', None)
        new_country.code3 = country.get('code3', None)
        new_country.codeN = country.get('nCode', None)
        new_country.ebxid = country['base'].get('id', None)
        new_country.save()
