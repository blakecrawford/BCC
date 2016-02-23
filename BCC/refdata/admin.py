from django.contrib import admin
from suit.admin import SortableModelAdmin

from .models import Channel
from .models import Country
from .models import CountrySubdivision
from .models import GenreAuthority
from .models import GenreType
from .models import Genre
from .models import RatingAuthority
from .models import Rating
from .models import RatingContentDescriptor
from .models import Language
from .models import ScriptName
from .models import BCP47Language
from .models import ActivityType
from .models import ObjectProperty
from .models import Activity
from .models import ActivityPropertyRelation


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code2', 'code3', 'codeN',)


@admin.register(ScriptName)
class ScriptAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'number',)


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ('short_name', 'name', 'status',)


@admin.register(CountrySubdivision)
class CountrySubdivisionAdmin(admin.ModelAdmin):
    list_display = ('subcode', 'name', 'get_country',)

    def get_country(self, obj):
        return obj.country.name
    get_country.short_description = 'Country'


@admin.register(RatingAuthority)
class RatingAuthorityAdmin(admin.ModelAdmin):
    list_display = ('name', 'ref_link',)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_authority',)

    def get_authority(self, obj):
        return obj.authority.name
    get_authority.short_description = 'Authority'



@admin.register(GenreAuthority)
class GenreAuthorityAdmin(admin.ModelAdmin):
    list_display = ('name', 'ref_link',)


@admin.register(GenreType)
class GenreTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_authority', 'get_type',)

    def get_authority(self, obj):
        return obj.authority.name
    get_authority.short_description = 'Authority'

    def get_type(self, obj):
        return obj.type.name
    get_type.short_description = 'Type'


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'code2', 'code3',)



@admin.register(ObjectProperty)
class ObjectPropertyAdmin(SortableModelAdmin):
    sortable = 'order'
    list_display = ('name', 'object_type',)


@admin.register(ActivityPropertyRelation)
class ActivityPropertyRelationAdmin(SortableModelAdmin):
    sortable = 'order'
    list_display = ('get_activity', 'get_property', 'get_required',)


    def get_activity(self, obj):
        return obj.activity.name
    get_activity.short_description = 'Activity Name'

    def get_property(self, obj):
        return obj.object_property.name
    get_property.short_description = 'Property Name'

    def get_required(self, obj):
        return obj.required
    get_required.short_description = 'Required?'


class ActivityPropertyInline(admin.TabularInline):
    model = ActivityPropertyRelation
    extra = 1
    list_display = ('get_object_property', 'required',)
    show_change_link = True

    def get_object_property(self, obj):
        return obj.object_property.name
    get_object_property.short_description = 'Object Property'

    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            return 0
        return self.extra


@admin.register(Activity)
class ActivityAdmin(SortableModelAdmin):
    inlines = [
        ActivityPropertyInline,
    ]
    sortable = 'order'
    list_display = ('get_type', 'name', 'get_parent',)
    list_display_links = ('name',)
    # readonly_fields = ('get_type',)
    # ordering = ('get_type',)

    def get_type(self, obj):
        return obj.type.name
    get_type.short_description = 'Type'

    def get_parent(self, obj):
        if obj.parent:
            return obj.parent.name
        return 'Top Level'
    get_parent.short_description = 'Parent'


class ActivityInline(admin.TabularInline):
    model = Activity
    extra = 1
    fields = ('name', 'parent',)
    show_change_link = True

    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            return 0
        return self.extra


@admin.register(ActivityType)
class ActivityTypeAdmin(SortableModelAdmin):
    inlines = [
        ActivityInline,
    ]
    sortable = 'order'


admin.site.register(RatingContentDescriptor)
admin.site.register(BCP47Language)
