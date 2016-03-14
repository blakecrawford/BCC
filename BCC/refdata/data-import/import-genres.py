import os, sys
import xmltodict

proj_path = "/Users/crawforb/Projects/Development/PyCharmProjects/BCC/"
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BCC.settings')
sys.path.append(proj_path)
os.chdir(proj_path)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
import refdata.models

with open('refdata/data-import/genres.xml') as fd:
    doc = xmltodict.parse(fd.read())

    for old_genre in doc['DataExchange']['root']['Genre']:
        new_genre = refdata.models.Genre()
        new_genre.name = old_genre['base'].get('name', None)
        new_genre.ebxid = old_genre['base'].get('id', None)
        new_genre.description = old_genre['base'].get('description', None)
        new_genre_authority_ebxid = old_genre.get('GenreAuthority', None)
        new_genre_type_ebxid = old_genre.get('GenreType', None)
        new_genre_parent_ebxid = old_genre.get('parentGenre', None)
        if new_genre_authority_ebxid:
            authority = refdata.models.GenreAuthority.objects.get(ebxid=new_genre_authority_ebxid)
            new_genre.authority = authority
        if new_genre_type_ebxid:
            ntype = refdata.models.GenreType.objects.get(ebxid=new_genre_type_ebxid)
            new_genre.type = ntype
        if new_genre_parent_ebxid:
            parent = refdata.models.Genre.objects.get(ebxid=new_genre_parent_ebxid)
            new_genre.parent = parent
        new_genre.save()
