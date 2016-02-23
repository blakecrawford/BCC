from django.contrib import admin


from .containers import Franchise
from .containers import Series
from .containers import Season
from .containers import ContentContainer
from .containers import Endeavor

from .enums import ContainerTypesEnum

from .titles_admin import TitleInline
from .relations_admin import SeriesFranchiseRelationInline
from .relations_admin import SeasonSeriesRelationInline


@admin.register(Franchise)
class FranchiseAdmin(admin.ModelAdmin):
    inlines = [
        TitleInline,
    ]

    list_display = ('default_title', 'get_country', 'get_channel',)
    fields = ('cctype', 'default_title', 'description', 'reference_channel', 'country_of_origin',)

    def get_country(self, obj):
        return obj.country_of_origin.name
    get_country.short_description = 'Country of Origin'

    def get_channel(self, obj):
        return obj.reference_channel.name
    get_channel.short_description = 'Reference Channel'

    def get_form(self, request, obj=None, **kwargs):
        form = super(FranchiseAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['cctype'].initial = ContainerTypesEnum.FRANCHISE
        return form


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    inlines = [
        TitleInline,
        SeriesFranchiseRelationInline,
    ]

    list_display = ('get_title', 'get_country', 'get_channel',)
    fields = ('cctype', 'default_title', 'description', 'reference_channel', 'country_of_origin', 'reference_language', 'typical_length',)

    def get_title(self, obj):
        # title_obj = obj.title_set.filter(title_type__name='Default Title')
        # return title_obj.values('title_text')[0]['title_text']
        #return title_obj
        return obj.default_title
    get_title.short_description = 'Title'

    def get_country(self, obj):
        return obj.country_of_origin.name
    get_country.short_description = 'Country of Origin'

    def get_channel(self, obj):
        return obj.reference_channel.name
    get_channel.short_description = 'Reference Channel'

    def get_form(self, request, obj=None, **kwargs):
        form = super(SeriesAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['cctype'].initial = ContainerTypesEnum.SERIES
        return form


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):

    inlines = [
        SeasonSeriesRelationInline,
    ]

    list_display = ('get_title', 'number', 'sequence',)
    fields = ('cctype', 'default_title', 'description', 'reference_channel', 'country_of_origin', 'number', 'sequence',)

    def get_title(self, obj):
        return obj.default_title
    get_title.short_description = 'Title'

    def get_form(self, request, obj=None, **kwargs):
        form = super(SeasonAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['cctype'].initial = ContainerTypesEnum.SEASON
        return form


@admin.register(Endeavor)
class EndeavorAdmin(admin.ModelAdmin):
    inlines = [
        #TitleInline,
    ]



admin.site.register(ContentContainer)