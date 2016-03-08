import uuid
from django.db import models

CHANNEL_STATUSES = (
    (0, "Active"),
    (1, "Inactive")
)


class Channel(models.Model):
    vmid = models.UUIDField(default=uuid.uuid4, editable=True, primary_key=True)
    short_name = models.CharField(max_length=25)
    name = models.CharField(max_length=256)
    description = models.TextField(null=True)
    status = models.IntegerField(choices=CHANNEL_STATUSES)
    ebxid = models.IntegerField(null=True)

    def __str__(self):
        return self.short_name + \
               u" :: " + \
               str(self.vmid)

    class Meta:
        ordering = ("short_name",)
        verbose_name = "Channel"
        verbose_name_plural = "Channels"


class Country(models.Model):
    vmid = models.UUIDField(default=uuid.uuid4, editable=True, primary_key=True)
    name = models.CharField(max_length=255)
    code2 = models.CharField(max_length=2)
    code3 = models.CharField(max_length=3)
    codeN = models.IntegerField()
    ebxid = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name + \
               u" :: " + \
               str(self.vmid)

    class Meta:
        ordering = ("name",)
        verbose_name = "Country"
        verbose_name_plural = "Countries"


class CountrySubdivision(models.Model):
    vmid = models.UUIDField(default=uuid.uuid4, editable=True, primary_key=True)
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country)
    subcode = models.CharField(max_length=3)
    ebxid = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name + \
               u" :: " + \
               str(self.vmid)

    class Meta:
        ordering = ("name",)
        verbose_name = "Country Subdivision"
        verbose_name_plural = "Country Subdivisions"


class GenreType(models.Model):
    vmid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=45)
    ebxid = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name + \
               u" :: " + \
               str(self.vmid)

    class Meta:
        ordering = ("name",)
        verbose_name = "Genre Type"
        verbose_name_plural = "Genre Types"


class GenreAuthority(models.Model):
    vmid = models.UUIDField(default=uuid.uuid4, editable=True, primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    ref_link = models.URLField(null=True, blank=True)
    ebxid = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name + \
               u" :: " + \
               str(self.vmid)

    class Meta:
        ordering = ("name",)
        verbose_name = "Genre Authority"
        verbose_name_plural = "Genre Authorities"


class Genre(models.Model):
    vmid = models.UUIDField(default=uuid.uuid4, editable=True, primary_key=True)
    name = models.CharField(max_length=255)
    parent = models.ForeignKey("self", null=True, blank=True)
    authority = models.ForeignKey(GenreAuthority)
    type = models.ForeignKey(GenreType)
    ebxid = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name + \
               u" :: " + \
               str(self.vmid)

    class Meta:
        ordering = ("name",)
        verbose_name = "Genre"
        verbose_name_plural = "Genres"


class RatingAuthority(models.Model):
    vmid = models.UUIDField(default=uuid.uuid4, editable=True, primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1024)
    ref_link = models.URLField(null=True)
    ebxid = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name + \
               u" :: " + \
               str(self.vmid)

    class Meta:
        ordering = ("name",)
        verbose_name = "Rating Authority"
        verbose_name_plural = "Rating Authorities"


class RatingContentDescriptor(models.Model):
    vmid = models.UUIDField(default=uuid.uuid4, editable=True, primary_key=True)
    descriptor = models.CharField(max_length=255)
    ebxid = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.descriptor

    class Meta:
        ordering = ("descriptor",)
        verbose_name = "Content Descriptor"
        verbose_name_plural = "Content Descriptors"


class Rating(models.Model):
    vmid = models.UUIDField(default=uuid.uuid4, editable=True, primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1024)
    authority = models.ForeignKey(RatingAuthority)
    descriptors = models.ManyToManyField(RatingContentDescriptor, blank=True)
    ebxid = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name + \
               u" :: " + \
               str(self.vmid)

    class Meta:
        ordering = ("name",)
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"


class Language(models.Model):
    vmid = models.UUIDField(default=uuid.uuid4, editable=True, primary_key=True)
    name = models.CharField(max_length=100)
    code2 = models.CharField(max_length=2)
    code3 = models.CharField(max_length=3)
    ebxid = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name + \
               u" :: " + \
               str(self.vmid)

    class Meta:
        ordering = ("name",)
        verbose_name = "Language"
        verbose_name_plural = "Languages"


class ScriptName(models.Model):
    vmid = models.UUIDField(default=uuid.uuid4, editable=True, primary_key=True)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=8)
    number = models.IntegerField()
    ebxid = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name + \
               u" :: " + \
               str(self.vmid)

    class Meta:
        ordering = ("name",)
        verbose_name = "Script Name"
        verbose_name_plural = "Script Names"


class BCP47Language(models.Model):
    vmid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    language = models.ForeignKey(Language)
    script = models.ForeignKey(ScriptName)
    country = models.ForeignKey(Country)
    ebxid = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.language.code2 + \
               u"-" + \
               self.script.code + \
               u"-" + \
               self.country.code2

    class Meta:
        ordering = ("language", "script", "country")
        verbose_name = "BCP-47 Language"
        verbose_name_plural = "BCP-47 Languages"


class ActivityType(models.Model):
    vmid = models.UUIDField(default=uuid.uuid4, editable=True, primary_key=True)
    name = models.CharField(max_length=256)
    order = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name + " :: " + str(self.vmid)

    class Meta:
        ordering = ("name",)
        verbose_name = "Activity Type"
        verbose_name_plural = "Activity Types"


class ObjectProperty(models.Model):
    vmid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=256)
    object_type = models.CharField(max_length=256)
    order = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name + \
               u" (takes a " + \
               self.object_type + \
               u")"

    class Meta:
        ordering = ("name",)
        verbose_name = "Object Property"
        verbose_name_plural = "Object Properties"


class Activity(models.Model):
    vmid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    type = models.ForeignKey(ActivityType)
    name = models.CharField(max_length=256)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='subactivities')
    order = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.type.name + \
               u" :: " + \
               self.name

    class Meta:
        ordering = ("name",)
        verbose_name = "Activity"
        verbose_name_plural = "Activities"


class ActivityPropertyRelation(models.Model):
    activity = models.ForeignKey(Activity)
    object_property = models.ForeignKey(ObjectProperty)
    required = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.activity.name + \
               u" :: " + \
                self.object_property.name + \
                u" :: " + \
                str(self.required)

    class Meta:
        verbose_name = "Activity-to-Object Property Relationship"
        verbose_name_plural = "Activity-to-Object Property Relationships"
