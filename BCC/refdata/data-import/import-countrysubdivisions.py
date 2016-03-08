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

with open('refdata/data-import/countrysubdivisions.xml') as fd:
    doc = xmltodict.parse(fd.read())

    for countrysub in doc['DataExchange']['root']['CountrySubdivision']:
        new_countrysub = refdata.models.CountrySubdivision()
        new_countrysub.name = countrysub['base'].get('name')
        new_countrysub.description = countrysub['base'].get('description', None)
        new_countrysub.subcode = countrysub.get('subCode', None)
        parent_country_ebxid = countrysub.get('parentCountry', None)
        if parent_country_ebxid:
            parent_country = refdata.models.Country.objects.get(ebxid=parent_country_ebxid)
        new_countrysub.country = parent_country
        new_countrysub.save()
