from django.db import models


class EntityType(models.Model):
    name = models.CharField(max_length=256, null=False)

    def __unicode__(self):
        return u"Entity Type :: " + \
            self.name

    class Meta:
        verbose_name = "Entity Type"
        verbose_name_plural = "Entity Types"


class Endpoint(models.Model):
    name = models.CharField(max_length=256, null=False)

    def __unicode__(self):
        return u"Endpoint " + \
            u' :: ' + \
            self.name

    class Meta:
        verbose_name = "Endpoint"
        verbose_name_plural = "Endpoints"


class Platform(models.Model):
    name = models.CharField(max_length=256, null=False)

    def __unicode__(self):
        return u"Platform " + \
            u" :: " + \
            self.name

    class Meta:
        verbose_name = "Platform"
        verbose_name_plural = "Platforms"


class TechnicalVideoRequirements(models.Model):
    description = models.CharField(max_length=256, null=False)

    def __unicode__(self):
        return u"TVR :: " + \
               self.description

    class Meta:
        verbose_name = "Technical Video Requirement"
        verbose_name_plural = "Technical Video Requirements"


class StaticImageRequirements(models.Model):
    description = models.CharField(max_length=256, null=False)

    def __unicode__(self):
        return u"SIR :: " + \
               self.description

    class Meta:
        verbose_name = "Static Image Requirement"
        verbose_name_plural = "Static Image Requirements"


class MetadataSchema(models.Model):
    schema = models.CharField(max_length=256, null=False)

    def __unicode__(self):
        return u"Metadata Schema :: " + \
               self.schema

    class Meta:
        verbose_name = "Metadata Schema"
        verbose_name_plural = "Metadata Schemas"


class PackageStructure(models.Model):
    structure_template = models.CharField(max_length=256, null=False)

    def __unicode__(self):
        return u"Package Structure :: " + \
               self.structure_template

    class Meta:
        verbose_name = "Package Structure"
        verbose_name_plural = "Package Structures"


class DeliveryProcess(models.Model):
    bpmn = models.CharField(max_length=256, null=False)

    def __unicode__(self):
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
    entity_type = models.ForeignKey(EntityType)

    def __unicode__(self):
        return u"Delivery Context ID " + \
                str(self.id)

    class Meta:
        verbose_name = "Delivery Context"
        verbose_name_plural = "Delivery Contexts"


