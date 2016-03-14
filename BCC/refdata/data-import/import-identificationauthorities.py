import os, sys
import xmltodict

proj_path = "/Users/crawforb/Projects/Development/PyCharmProjects/BCC/"
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BCC.settings')
sys.path.append(proj_path)
os.chdir(proj_path)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
import refdata.models

with open('refdata/data-import/identificationauthorities.xml') as fd:
    doc = xmltodict.parse(fd.read())

    for old_idauth in doc['DataExchange']['root']['IdentificationAuthority']:
        new_idauth = refdata.models.ThirdPartyIdentificationAuthority()
        new_idauth.name = old_idauth['base'].get('name', None)
        new_idauth.ebxid = old_idauth['base'].get('id', None)
        new_idauth.description = old_idauth['base'].get('description', None)
        new_idauth.save()
