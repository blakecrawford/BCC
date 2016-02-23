from refdata import models as refdata_models
from django.db import models
from django_enumfield import enum
#from simple_history.models import HistoricalRecords
from .containers import Endeavor
from .enums import ItemTypesEnum


class ContentItem(Endeavor):
    citype = enum.EnumField(ItemTypesEnum, default=ItemTypesEnum.EPISODE)
    default_title = models.CharField(max_length=255, null=False, default='title')

    def __unicode__(self):
        return unicode(self.citype) + \
               u" :: " + \
               unicode(self.vmid)

    class Meta:
        ordering = ("citype", "vmid")
        verbose_name = "Content Item"
        verbose_name_plural = "Content Item"


class Special(ContentItem):

    def __unicode__(self):
        return u"Special" +\
            u' :: ' + \
            self.default_title + \
            u' :: ' + \
            unicode(self.vmid)

    class Meta:
        verbose_name = "Special"
        verbose_name_plural = "Special"


class Movie(ContentItem):

    def __unicode__(self):
        return u"Movie" + \
            u' :: ' + \
            self.default_title + \
            u' :: ' + \
            unicode(self.vmid)

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movie"


class Clip(ContentItem):

    def __unicode__(self):
        return u"Clip" + \
            u' :: ' + \
            self.default_title + \
            u' :: ' + \
            unicode(self.vmid)

    class Meta:
        verbose_name = "Clip"
        verbose_name_plural = "Clip"


class Module(ContentItem):
    typical_length = models.CharField(max_length=12, null=True)

    def __unicode__(self):
        return u"Module" + \
            u' :: ' + \
            self.default_title + \
            u' :: ' + \
            unicode(self.vmid)

    class Meta:
        verbose_name = "Module"
        verbose_name_plural = "Module"


class Episode(ContentItem):
    typical_length = models.CharField(max_length=12, null=True)
    production_number = models.CharField(max_length=10, null=True)

    def __unicode__(self):
        return u"Episode" + \
            u' :: ' + \
            self.default_title + \
            u' :: ' + \
            unicode(self.vmid)

    class Meta:
        verbose_name = "Episode"
        verbose_name_plural = "Episode"


