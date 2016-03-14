import uuid
from refdata import models as refdata_models
from django.db import models
from django_enumfield import enum
from .enums import ContainerTypesEnum


class Endeavor(models.Model):
    vmid = models.UUIDField(default=uuid.uuid4, editable=True, primary_key=True)
    description = models.TextField(max_length=1024, null=True)
    reference_channel = models.ForeignKey(refdata_models.Channel, null=True)
    country_of_origin = models.ForeignKey(refdata_models.Country, null=True)
    ebxid = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return u'Endeavor :: ' + str(self.vmid)

    class Meta:
        ordering = ("vmid",)
        verbose_name = "Endeavor"
        verbose_name_plural = "Endeavors"


class ContentContainer(Endeavor):
    default_title = models.CharField(max_length=255, null=False, default='title')
    cctype = enum.EnumField(ContainerTypesEnum, default=ContainerTypesEnum.FRANCHISE)

    def __unicode__(self):
        return str(self.cctype) + \
                        u" :: " + \
                        self.default_title + \
                        u" :: " + \
                        str(self.vmid)

    class Meta:
        ordering = ("cctype", "vmid")
        verbose_name = "Content Container"
        verbose_name_plural = "Content Containers"


class Franchise(ContentContainer):

    def __unicode__(self):
        return u"Franchise" + \
            u" :: " + \
            self.default_title + \
            u" :: " + \
            str(self.vmid)

    class Meta:
        verbose_name = "Franchise"
        verbose_name_plural = "Franchises"


class Series(ContentContainer):
    reference_language = models.ForeignKey(refdata_models.BCP47Language, null=True)
    typical_length = models.CharField(max_length=12, null=True)
    provenance = models.ForeignKey(refdata_models.Provenance, null=True)
    genres = models.ManyToManyField(refdata_models.Genre, null=True)

    def __unicode__(self):
        return u"Series" + \
            u" :: " + \
            self.default_title + \
            u" :: " + \
            str(self.vmid)

    class Meta:
        verbose_name = "Series"
        verbose_name_plural = "Series"


class Season(ContentContainer):
    number = models.IntegerField(null=True)
    sequence = models.IntegerField(null=True)

    def __unicode__(self):
        return u"Season" + \
            u" :: " + \
            self.default_title + \
            u" :: " + \
            str(self.vmid)

    class Meta:
        verbose_name = "Season"
        verbose_name_plural = "Season"
