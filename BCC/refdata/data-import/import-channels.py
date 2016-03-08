import os, sys
import xmltodict

proj_path = "/Users/crawforb/Projects/Development/PyCharmProjects/BCC/"
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BCC.settings')
sys.path.append(proj_path)
os.chdir(proj_path)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
import refdata.models

with open('refdata/data-import/channels.xml') as fd:
    doc = xmltodict.parse(fd.read())

    for channel in doc['DataExchange']['root']['Channel']:
        vmid = channel.get('vmId', None)
        name = channel['base'].get('name', None)
        description = channel['base'].get('description', None)
        code = channel.get('code', None)
        status = 0 if channel.get('status') == 'Active' else 1
        ebxid = channel['base'].get('id', None)

        new_channel = refdata.models.Channel()
        new_channel.vmid = vmid
        new_channel.name = name
        new_channel.description = description
        new_channel.short_name = code
        new_channel.status = status
        new_channel.ebxid = ebxid

        new_channel.save()
