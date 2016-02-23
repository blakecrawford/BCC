from django.db import models
from refdata import models as refdata_models
from .items import ContentItem


class Version(ContentItem):
    label = models.CharField(max_length=1024, default='label')
    #customizations = models.ForeignKey(CustomizationSpecification, blank=True, null=True)

    def __unicode__(self):
        return u"Version :: " + \
               unicode(self.label)

    class Meta:
        ordering = ("label",)
        verbose_name = "Version"
        verbose_name_plural = "Versions"


class CustomizationSpecification(models.Model):
    customization = models.ForeignKey(refdata_models.Activity)
    object_property = models.ForeignKey(refdata_models.ObjectProperty)
    property_target = models.CharField(max_length=1024)
    for_version = models.ForeignKey(Version, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.customization.name) + \
               u" :: " + \
               unicode(self.object_property.name) + \
               u" :: " + \
               unicode(self.property_target)


