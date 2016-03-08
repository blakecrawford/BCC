import os, sys
import xmltodict

proj_path = "/Users/crawforb/Projects/Development/PyCharmProjects/BCC/"
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BCC.settings')
sys.path.append(proj_path)
os.chdir(proj_path)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
import refdata.models

with open('refdata/data-import/genreauthorities.xml') as fd:
    doc = xmltodict.parse(fd.read())

    for auth in doc['DataExchange']['root']['genreDetails']['GenreAuthority']:
        new_auth = refdata.models.GenreAuthority()
        new_auth.name = auth['base'].get('name', None)
        new_auth.description = auth['base'].get('description', None)
        new_auth.ref_link = auth.get('RefLink', None)
        new_auth.ebxid = auth['base'].get('id', None)
        new_auth.save()
