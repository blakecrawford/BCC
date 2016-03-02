from django.contrib import admin

from .models import EntityType
from .models import Endpoint
from .models import Platform
from .models import TechnicalVideoRequirements
from .models import StaticImageRequirements
from .models import MetadataSchema
from .models import PackageStructure
from .models import DeliveryProcess
from .models import DeliveryContext
from .models import Codec
from .models import Specification
from .models import ScanType
from .models import ImageType


class DeliveryContextInline(admin.TabularInline):
    model = DeliveryContext
    extra = 1
    show_change_link = True

    verbose_name = "Delivery Context"
    verbose_name_plural = "Delivery Contexts"

    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            return 0
        return self.extra


@admin.register(Codec)
class CodecAdmin(admin.ModelAdmin):
    pass


@admin.register(Specification)
class SpecificationAdmin(admin.ModelAdmin):
    pass


@admin.register(ScanType)
class ScanTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(ImageType)
class ImageTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(EntityType)
class EntityTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Endpoint)
class EndpointAdmin(admin.ModelAdmin):
    pass


@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    pass


@admin.register(TechnicalVideoRequirements)
class TechnicalVideoRequirementsAdmin(admin.ModelAdmin):
    pass


@admin.register(StaticImageRequirements)
class StaticImageRequirementsAdmin(admin.ModelAdmin):
    pass


@admin.register(MetadataSchema)
class MetadataSchemaAdmin(admin.ModelAdmin):
    pass


@admin.register(PackageStructure)
class PackageStructureAdmin(admin.ModelAdmin):
    pass


@admin.register(DeliveryProcess)
class DeliveryProcessAdmin(admin.ModelAdmin):
    pass


@admin.register(DeliveryContext)
class DeliveryContextAdmin(admin.ModelAdmin):
    list_display = ('endpoint', 'platform', 'entity_type',)

