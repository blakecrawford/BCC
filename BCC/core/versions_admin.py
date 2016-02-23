from django.contrib import admin

from .enums import ItemTypesEnum
from .versions import Version
from .versions import CustomizationSpecification

from .titles_admin import TitleInline
from .relations_admin import VersionEpisodeRelationInline


class CustomizationSpecificationsInline(admin.TabularInline):
    model = CustomizationSpecification
    extra = 1

    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            return 0
        return self.extra


@admin.register(CustomizationSpecification)
class CustomizationSpecificationAdmin(admin.ModelAdmin):
    list_display = ('get_customization', 'get_object_property', 'get_property_target',)

    def get_customization(self, obj):
        return obj.customization.name
    get_customization.short_description = 'Customization'

    def get_object_property(self, obj):
        return obj.object_property.name
    get_object_property.short_description = 'Object Property'

    def get_property_target(self, obj):
        return obj.property_target
    get_property_target.short_description = 'Property Value'


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    inlines = [
        TitleInline,
        VersionEpisodeRelationInline,
        CustomizationSpecificationsInline,
    ]

    list_display = ('label',)

    fields = ('citype', 'default_title', 'label', 'description', 'reference_channel', 'country_of_origin')

    def get_form(self, request, obj=None, **kwargs):
        form = super(VersionAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['citype'].initial = ItemTypesEnum.VERSION
        return form


