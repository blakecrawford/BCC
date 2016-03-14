import os, sys
import xmltodict

proj_path = "/Users/crawforb/Projects/Development/PyCharmProjects/BCC/"
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BCC.settings')
sys.path.append(proj_path)
os.chdir(proj_path)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
import refdata.models

with open('refdata/data-import/ratings.xml') as fd:
    doc = xmltodict.parse(fd.read())

    for rating in doc['DataExchange']['root']['Rating']:
        new_r = refdata.models.Rating()
        new_r.ebxid = rating['base'].get('id', None)
        new_r.name = rating['base'].get('name', None)
        new_r.description = rating['base'].get('description', None)
        rating_authority_id = rating.get('RatingAuthority', None)
        if rating_authority_id:
            new_r.authority = refdata.models.RatingAuthority.objects.get(ebxid=rating_authority_id)

        new_r.save()
        if rating['RatingContentDescriptor']:
            for value in rating['RatingContentDescriptor']:
                descript = refdata.models.RatingContentDescriptor.objects.get(ebxid=value)
                new_r.descriptors.add(descript)
        new_r.save()
