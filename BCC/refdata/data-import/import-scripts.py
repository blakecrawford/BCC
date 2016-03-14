import os, sys
import xmltodict

proj_path = "/Users/crawforb/Projects/Development/PyCharmProjects/BCC/"
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BCC.settings')
sys.path.append(proj_path)
os.chdir(proj_path)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
import refdata.models

with open('refdata/data-import/scripts.xml') as fd:
    doc = xmltodict.parse(fd.read())

    for script in doc['DataExchange']['root']['Script']:
        new_script = refdata.models.ScriptName()
        new_script.name = script['base'].get('name', None)
        new_script.description = script['base'].get('description', None)
        new_script.ebxid = script['base'].get('id', None)
        new_script.code = script.get('code', None)
        new_script.number = script.get('number', None)
        new_script.save()
