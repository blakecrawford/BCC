from django_enumfield import enum

class ContainerTypesEnum(enum.Enum):
    FRANCHISE = 0
    SERIES = 1
    SEASON = 2

    labels = {
        FRANCHISE: 'Franchise',
        SERIES: 'Series',
        SEASON: 'Season'
    }


class ItemTypesEnum(enum.Enum):
    EPISODE = 0
    MOVIE = 1
    SPECIAL = 2
    MODULE = 3
    CLIP = 4
    VERSION = 5

    labels = {
        EPISODE: 'Episode',
        MOVIE: 'Movie',
        SPECIAL: 'Special',
        MODULE: 'Module',
        CLIP: 'Clip',
        VERSION: 'VERSION'
    }