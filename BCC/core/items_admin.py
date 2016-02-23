from django.contrib import admin

from .items import Special
from .items import Movie
from .items import Clip
from .items import Module
from .items import Episode
from .items import ContentItem

from .titles_admin import TitleInline
from .relations_admin import EpisodeSeasonRelationInline
from .relations_admin import MovieFranchiseRelationInline
from .relations_admin import SpecialSeriesRelationInline
from .relations_admin import ModuleEpisodeRelationInline
from .relations_admin import ClipEpisodeRelationInline

from .enums import ItemTypesEnum


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    inlines = [
        TitleInline,
        EpisodeSeasonRelationInline,
    ]

    list_display = ('production_number', 'default_title',)
    fields = ('citype', 'default_title', 'description', 'reference_channel', 'country_of_origin',
        'typical_length', 'production_number',)

    def get_form(self, request, obj=None, **kwargs):
        form = super(EpisodeAdmin , self).get_form(request, obj, **kwargs)
        form.base_fields['citype'].initial = ItemTypesEnum.EPISODE
        return form


@admin.register(Special)
class SpecialAdmin(admin.ModelAdmin):
    inlines = [
        TitleInline,
        SpecialSeriesRelationInline,
    ]

    list_display = ('default_title',)
    fields = ('citype', 'default_title', 'description', 'reference_channel', 'country_of_origin',)

    def get_form(self, request, obj=None, **kwargs):
        form = super(SpecialAdmin , self).get_form(request, obj, **kwargs)
        form.base_fields['citype'].initial = ItemTypesEnum.SPECIAL
        return form

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    inlines = [
        TitleInline,
        MovieFranchiseRelationInline,
    ]

    list_display = ('default_title',)
    fields = ('citype', 'default_title', 'description', 'reference_channel', 'country_of_origin',)

    def get_form(self, request, obj=None, **kwargs):
        form = super(MovieAdmin , self).get_form(request, obj, **kwargs)
        form.base_fields['citype'].initial = ItemTypesEnum.MOVIE
        return form


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    inlines = [
        TitleInline,
        ModuleEpisodeRelationInline
    ]

    list_display = ('default_title',)
    fields = ('citype', 'default_title', 'description', 'reference_channel', 'country_of_origin',)

    def get_form(self, request, obj=None, **kwargs):
        form = super(ModuleAdmin , self).get_form(request, obj, **kwargs)
        form.base_fields['citype'].initial = ItemTypesEnum.MODULE
        return form


@admin.register(Clip)
class ClipAdmin(admin.ModelAdmin):
    inlines = [
        TitleInline,
        ClipEpisodeRelationInline
    ]

    list_display = ('default_title',)
    fields = ('citype', 'default_title', 'description', 'reference_channel', 'country_of_origin',)

    def get_form(self, request, obj=None, **kwargs):
        form = super(ClipAdmin , self).get_form(request, obj, **kwargs)
        form.base_fields['citype'].initial = ItemTypesEnum.CLIP
        return form