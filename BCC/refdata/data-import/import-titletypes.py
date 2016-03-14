import os, sys
import xmltodict

proj_path = "/Users/crawforb/Projects/Development/PyCharmProjects/BCC/"
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BCC.settings')
sys.path.append(proj_path)
os.chdir(proj_path)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
import core.titles

with open('refdata/data-import/titletypes.xml') as fd:
    doc = xmltodict.parse(fd.read())

    for tt in doc['DataExchange']['root']['TitleType']:
        new_tt = core.titles.TitleType()
        new_tt.name = tt['base'].get('name', None)
        new_tt.description = tt['base'].get('description', None)
        new_tt.ebxid = tt['base'].get('id', None)
        new_tt.length_restriction = tt.get('lengthRestriction', None)
        new_tt.is_Unique = tt.get('isUnique', False)
        new_tt.save()
