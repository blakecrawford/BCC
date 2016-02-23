import uuid
from refdata import models as refdata_models
from django.db import models
from .containers import Endeavor


class TitleType(models.Model):
    vmid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=256)
    length_restriction = models.IntegerField(null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ("name",)
        verbose_name = "Title Type"
        verbose_name_plural = "Title Types"


class Title(models.Model):
    vmid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    title_text = models.CharField(max_length=1056)
    title_type = models.ForeignKey(TitleType)
    language = models.ForeignKey(refdata_models.BCP47Language, null=True)
    endeavor = models.ForeignKey(Endeavor)

    def __unicode__(self):
        return unicode(self.title_type.name) + \
               u" :: " + \
               unicode(self.title_text)

    class Meta:
        ordering = ("title_text",)
        verbose_name = "Title"
        verbose_name_plural = "Titles"