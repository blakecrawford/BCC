from django.db import models
from django_enumfield import enum
from .containers import Franchise
from .containers import Series
from .containers import Season
from .predicates import SeriesToFranchisePredicatesEnum
from .predicates import SeasonToSeriesPredicatesEnum
from .predicates import EpisodeToSeasonPredicatesEnum
from .predicates import MovieToFranchisePredicatesEnum
from .predicates import SpecialToSeriesPredicatesEnum
from .predicates import ModuleToEpisodePredicatesEnum
from .predicates import ClipToEpisodePredicatesEnum
from .predicates import VersionToEpisodePredicatesEnum
from .items import Episode
from .items import Module
from .items import Clip
from .items import Movie
from .items import Special
from .versions import Version


class SeriesFranchiseRelation(models.Model):
    franchise = models.ForeignKey(Franchise)
    series = models.ForeignKey(Series)
    predicate = enum.EnumField(SeriesToFranchisePredicatesEnum, default=SeriesToFranchisePredicatesEnum.ISSERIESOF)

    def __unicode__(self):
        return unicode(self.series.default_title) + \
            u' :: ' + \
            unicode(self.predicate) + \
            u' :: ' + \
            unicode(self.franchise.default_title)


class SeasonSeriesRelation(models.Model):
    series = models.ForeignKey(Series)
    season = models.ForeignKey(Season)
    predicate = enum.EnumField(SeasonToSeriesPredicatesEnum, default=SeasonToSeriesPredicatesEnum.ISSEASONOF)

    def __unicode__(self):
        return unicode(self.season.default_title) + \
            u' :: ' + \
            unicode(self.predicate) + \
            u' :: ' + \
            unicode(self.series.default_title)


class EpisodeSeasonRelation(models.Model):
    episode = models.ForeignKey(Episode)
    season = models.ForeignKey(Season)
    predicate = enum.EnumField(EpisodeToSeasonPredicatesEnum, default=EpisodeToSeasonPredicatesEnum.ISEPISODEOF)

    def __unicode__(self):
        return unicode(self.episode.default_title) + \
            u' :: ' + \
            unicode(self.predicate) + \
            u' :: ' + \
            unicode(self.season.default_title)


class MovieFranchiseRelation(models.Model):
    movie = models.ForeignKey(Movie)
    franchise = models.ForeignKey(Franchise)
    predicate = enum.EnumField(MovieToFranchisePredicatesEnum, default=MovieToFranchisePredicatesEnum.ISMOVIEOF)

    def __unicode__(self):
        return unicode(self.movie.default_title) + \
            u' :: ' + \
            unicode(self.predicate) + \
            u' :: ' + \
            unicode(self.franchise.default_title)


class SpecialSeriesRelation(models.Model):
    special = models.ForeignKey(Special)
    series = models.ForeignKey(Series)
    predicate = enum.EnumField(SpecialToSeriesPredicatesEnum, default=SpecialToSeriesPredicatesEnum.ISSPECIALOF)

    def __unicode__(self):
        return unicode(self.movie.default_title) + \
            u' :: ' + \
            unicode(self.predicate) + \
            u' :: ' + \
            unicode(self.franchise.default_title)


class ModuleEpisodeRelation(models.Model):
    module = models.ForeignKey(Module)
    episode = models.ForeignKey(Episode)
    predicate = enum.EnumField(ModuleToEpisodePredicatesEnum, default=ModuleToEpisodePredicatesEnum.ISORIGINALLYFROMEPISODE)

    def __unicode__(self):
        return unicode(self.module.default_title) + \
            u' :: ' + \
            unicode(self.predicate) + \
            u' :: ' + \
            unicode(self.episode.default_title)


class ClipEpisodeRelation(models.Model):
    clip = models.ForeignKey(Clip)
    episode = models.ForeignKey(Episode)
    predicate = enum.EnumField(ClipToEpisodePredicatesEnum, default=ClipToEpisodePredicatesEnum.ISFROMEPISODE)

    def __unicode__(self):
        return unicode(self.clip.default_title) + \
            u' :: ' + \
            unicode(self.predicate) + \
            u' :: ' + \
            unicode(self.episode.default_title)


class VersionEpisodeRelation(models.Model):
    version = models.ForeignKey(Version)
    episode = models.ForeignKey(Episode)
    predicate = enum.EnumField(VersionToEpisodePredicatesEnum, default=VersionToEpisodePredicatesEnum.ISVERSIONOF)

    def __unicode__(self):
        return unicode(self.version.default_title) + \
            u' :: ' + \
            unicode(self.predicate) + \
            u' :: ' + \
            unicode(self.episode.default_title)