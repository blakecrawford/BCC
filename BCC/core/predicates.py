from django_enumfield import enum


class SeriesToFranchisePredicatesEnum(enum.Enum):
    ISSERIESOF = 0
    ISRELATEDSERIESTO = 1

    labels = {
        ISSERIESOF: "is Series Of",
        ISRELATEDSERIESTO: "is Related Series To"
    }


class SeasonToSeriesPredicatesEnum(enum.Enum):
    ISSEASONOF = 0

    labels = {
        ISSEASONOF: 'is Season Of',
    }


class EpisodeToSeasonPredicatesEnum(enum.Enum):
    ISEPISODEOF = 0

    labels = {
        ISEPISODEOF: 'is Episode Of',
    }


class MovieToFranchisePredicatesEnum(enum.Enum):
    ISMOVIEOF = 0
    ISRELATEDTO = 1

    labels = {
        ISMOVIEOF: 'is Movie Of',
        ISRELATEDTO: 'is Related To'
    }


class SpecialToSeriesPredicatesEnum(enum.Enum):
    ISSPECIALOF = 0
    ISRELATEDTOSEASON = 1

    labels = {
        ISSPECIALOF: 'is Special Of',
        ISRELATEDTOSEASON: 'is Related To'
    }


class ModuleToEpisodePredicatesEnum(enum.Enum):
    ISORIGINALLYFROMEPISODE = 0
    HASBEENPACKAGEDINEPISODE = 1

    labels = {
        ISORIGINALLYFROMEPISODE: 'is Originally From Episode',
        HASBEENPACKAGEDINEPISODE: 'has Been Packaged In Episode'
    }


class ClipToEpisodePredicatesEnum(enum.Enum):
    ISFROMEPISODE = 0
    ISCLIPOFMODULE = 1

    labels = {
        ISFROMEPISODE: 'is Clip of Episode',
        ISCLIPOFMODULE: 'is Clip of Module'
    }


class VersionToEpisodePredicatesEnum(enum.Enum):
    ISVERSIONOF = 1

    labels = {
        ISVERSIONOF: 'is Version Of',
    }


# class ContainerChannelPredicatesEnum(enum.Enum):
#     ISOWNEDBY = 0
#     HASAIREDON = 1
#
#     labels = {
#         ISOWNEDBY: 'is Owned By',
#         HASAIREDON: 'has Aired On'
#     }
#
#
# class ContainerContainerPredicatesEnum(enum.Enum):
#     ISSERIESOF = 0
#     ISSEASONOF = 1
#
#     labels = {
#         ISSERIESOF: 'is Series Of',
#         ISSEASONOF: 'is Season Of'
#     }
#
#
# class ContainerItemPredicatesEnum(enum.Enum):
#     ISEPISODEOF = 0
#     ISMOVIEOF = 1
#     ISSPECIALOF = 2
#
#     labels = {
#         ISEPISODEOF: 'is Episode Of',
#         ISMOVIEOF: 'is Movie Of',
#         ISSPECIALOF: 'is Special Of'
#     }
#
#
# class ItemItemPredicatesEnum(enum.Enum):
#     ISCLIPOF = 0
#     ISMODULEOF = 1
#     ISVERSIONOF = 2
#
#     labels = {
#         ISCLIPOF: 'is Clip Of',
#         ISMODULEOF: 'is Module Of',
#         ISVERSIONOF: 'is Version Of'
#     }