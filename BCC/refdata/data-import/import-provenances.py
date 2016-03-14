import os, sys
import xmltodict

proj_path = "/Users/crawforb/Projects/Development/PyCharmProjects/BCC/"
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BCC.settings')
sys.path.append(proj_path)
os.chdir(proj_path)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
import refdata.models

with open('refdata/data-import/provenances.xml') as fd:
    doc = xmltodict.parse(fd.read())

    for prov in doc['DataExchange']['root']['Provenance']:
        new_prov = refdata.models.Provenance()
        new_prov.name = prov['base'].get('name', None)
        new_prov.description = prov['base'].get('description', None)
        new_prov.ebxid = prov['base'].get('id', None)
        new_prov.save()
