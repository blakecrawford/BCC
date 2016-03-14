import os, sys
import xmltodict

proj_path = "/Users/crawforb/Projects/Development/PyCharmProjects/BCC/"
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BCC.settings')
sys.path.append(proj_path)
os.chdir(proj_path)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
import refdata.models

with open('refdata/data-import/languages.xml') as fd:
    doc = xmltodict.parse(fd.read())

    for language in doc['DataExchange']['root']['Language']:
        new_lang = refdata.models.Language()
        new_lang.ebxid = language['base'].get('id', None)
        new_lang.name = language['base'].get('name', None)
        new_lang.code2 = language.get('code2', None)
        new_lang.code3 = language.get('code3', None)
        new_lang.save()
