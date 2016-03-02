from django.db import models


class Codec(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)

    def __str__(self):
        return u'Codec :: ' + \
            self.name

    class Meta:
        verbose_name = 'Codec'
        verbose_name_plural = 'Codecs'


class Specification(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)

    def __str__(self):
        return u'Specification :: ' + \
            self.name

    class Meta:
        verbose_name = 'Specification'
        verbose_name_plural = 'Specifications'


class ScanType(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)

    def __str__(self):
        return u'Scan Type :: ' + \
            self.name

    class Meta:
        verbose_name = 'Scan Type'
        verbose_name_plural = 'Scan Types'


class EntityType(models.Model):
    name = models.CharField(max_length=256, null=False)

    def __str__(self):
        return u"Entity Type :: " + \
            self.name

    class Meta:
        verbose_name = "Entity Type"
        verbose_name_plural = "Entity Types"


class Endpoint(models.Model):
    name = models.CharField(max_length=256, null=False)

    def __str__(self):
        return u"Endpoint " + \
            u' :: ' + \
            self.name

    class Meta:
        verbose_name = "Endpoint"
        verbose_name_plural = "Endpoints"


class ImageType(models.Model):
    name = models.CharField(max_length=256, null=False)

    def __str__(self):
        return u'Image Type :: ' + \
            self.name

    class Meta:
        verbose_name = 'Image Type'
        verbose_name_plural = 'Image Types'

class Platform(models.Model):
    name = models.CharField(max_length=256, null=False)

    def __str__(self):
        return u"Platform " + \
            u" :: " + \
            self.name

    class Meta:
        verbose_name = "Platform"
        verbose_name_plural = "Platforms"


class TechnicalVideoRequirements(models.Model):
    codec = models.ForeignKey(Codec, blank=True, null=True)
    specification = models.ForeignKey(Specification, blank=True, null=True)
    scan_type = models.ForeignKey(ScanType, blank=True, null=True)
    video_average_bitrate = models.FloatField(blank=True, null=True)
    frame_rate = models.FloatField(blank=True, null=True)
    audio_sample_rate = models.IntegerField(blank=True, null=True)
    audio_bit_depth = models.IntegerField(blank=True, null=True)
    audio_channels = models.IntegerField(blank=True, null=True)
    audio_channel_configuration = models.CharField(max_length=256, blank=True, null=True)
    x_pixels_per_inch = models.IntegerField(blank=True, null=True)
    y_pixels_per_inch = models.IntegerField(blank=True, null=True)
    audio_track_configuration = models.CharField(max_length=256, null=True, blank=True)
    description = models.CharField(max_length=256, null=False)

    def __str__(self):
        return u"TVR :: " + \
               self.description

    class Meta:
        verbose_name = "Technical Video Requirement"
        verbose_name_plural = "Technical Video Requirements"


class StaticImageRequirements(models.Model):
    image_type = models.ForeignKey(ImageType, null=True, blank=True)
    image_content_relationship = models.CharField(max_length=256, blank=True, null=True)
    description = models.CharField(max_length=256, null=False)

    def __str__(self):
        return u"SIR :: " + \
               self.description

    class Meta:
        verbose_name = "Static Image Requirement"
        verbose_name_plural = "Static Image Requirements"


class MetadataSchema(models.Model):
    schema = models.CharField(max_length=256, null=False)
    xform = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return u"Metadata Schema :: " + \
               self.schema

    class Meta:
        verbose_name = "Metadata Schema"
        verbose_name_plural = "Metadata Schemas"


class PackageStructure(models.Model):
    structure_template = models.CharField(max_length=256, null=False)

    def __str__(self):
        return u"Package Structure :: " + \
               self.structure_template

    class Meta:
        verbose_name = "Package Structure"
        verbose_name_plural = "Package Structures"


class DeliveryProcess(models.Model):
    bpmn = models.CharField(max_length=256, null=False)
    delivery_location = models.CharField(max_length=1024, null=True, blank=True)
    delivery_method = models.CharField(max_length=1024, null=True, blank=True)
    receipt_acknowledgement = models.BooleanField(default=False)

    def __str__(self):
        return u"Delivery Process :: " + \
               self.bpmn

    class Meta:
        verbose_name = "Delivery Process"
        verbose_name_plural = "Delivery Processes"


class DeliveryContext(models.Model):
    endpoint = models.ForeignKey(Endpoint)
    platform = models.ForeignKey(Platform)
    entity_type = models.ForeignKey(EntityType)
    technical_requirements = models.ForeignKey(TechnicalVideoRequirements)
    image_requirements = models.ForeignKey(StaticImageRequirements)
    metadata_schema = models.ForeignKey(MetadataSchema)
    package_structure = models.ForeignKey(PackageStructure)
    delivery_process = models.ForeignKey(DeliveryProcess)

    def __str__(self):
        return u"Delivery Context ID " + \
                str(self.id)

    class Meta:
        verbose_name = "Delivery Context"
        verbose_name_plural = "Delivery Contexts"


