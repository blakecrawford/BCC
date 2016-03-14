import os, sys
import xmltodict

proj_path = "/Users/crawforb/Projects/Development/PyCharmProjects/BCC/"
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BCC.settings')
sys.path.append(proj_path)
os.chdir(proj_path)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
import core.containers
import core.enums
import refdata.models

with open('core/data-import/contentcontainers.xml') as fd:
    doc = xmltodict.parse(fd.read())

    for container in doc['DataExchange']['root']['ContentContainer']:
        container_type = container.get('contentContainerType', None)
        if container_type == 'Franchise':
            new_entity = core.containers.Franchise()
            new_entity.cctype = core.enums.ContainerTypesEnum.FRANCHISE
            new_entity.default_title = container['base'].get('name', None)
            new_entity.ebxid = container['base'].get('id', None)
            new_entity.description = container['base'].get('description', None)
            new_entity.vmid = container.get('vmId', None)
        new_entity.save()

        if container_type == 'Series':
            new_entity = core.containers.Series()
            new_entity.cctype = core.enums.ContainerTypesEnum.SERIES
            new_entity.default_title = container['base'].get('name', None)
            new_entity.ebxid = container['base'].get('id', None)
            new_entity.description = container['base'].get('description', None)
            new_entity.vmid = container.get('vmId', None)

            new_entity.save()

            provenance_ebxid = container.get('provenance', None)
            country_of_origin_ebxid = container.get('countryOfOrigin', None)
            genres_ebxids = container['genre']

            if provenance_ebxid:
                new_entity.provenance = refdata.models.Provenance.objects.get(ebxid=provenance_ebxid)

            if country_of_origin_ebxid:
                new_entity.country_of_origin = refdata.models.Country.objects.get(ebxid=country_of_origin_ebxid)

            for genre_ebxid in genres_ebxids:
                print(genre_ebxid)
                new_entity.genres.add(refdata.models.Genre.objects.get(ebxid=genre_ebxid))

            new_entity.save()



