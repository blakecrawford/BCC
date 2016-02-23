from django.contrib import admin
#from simple_history.admin import SimpleHistoryAdmin
# from .relations import ContainerItemRelations
# from .relations import ItemItemRelations
# from .relations import ContainerContainerRelation
from .relations import SeriesFranchiseRelation
from .relations import SeasonSeriesRelation
from .relations import EpisodeSeasonRelation
from .relations import MovieFranchiseRelation
from .relations import SpecialSeriesRelation
from .relations import ModuleEpisodeRelation
from .relations import ClipEpisodeRelation
from .relations import VersionEpisodeRelation


class SeriesFranchiseRelationInline(admin.TabularInline):
    model = SeriesFranchiseRelation
    extra = 1
    show_change_link = True

    fields = ('predicate', 'franchise',)

    verbose_name = 'Related Franchise'
    verbose_name_plural = 'Related Franchises'

    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            return 0
        return self.extra


class SeasonSeriesRelationInline(admin.TabularInline):
    model = SeasonSeriesRelation
    extra = 1
    show_change_link = True

    fields = ('predicate', 'series',)

    verbose_name = 'Related Series'
    verbose_name_plural = 'Related Series'

    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            return 0
        return self.extra


class EpisodeSeasonRelationInline(admin.TabularInline):
    model = EpisodeSeasonRelation
    extra = 1
    show_change_link = True

    fields = ('predicate', 'season',)

    verbose_name = 'Related Season'
    verbose_name_plural = 'Related Seasons'

    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            return 0
        return self.extra


class MovieFranchiseRelationInline(admin.TabularInline):
    model = MovieFranchiseRelation
    extra = 1
    show_change_link = True

    fields = ('predicate', 'franchise',)

    verbose_name = 'Related Franchise'
    verbose_name_plural = 'Related Franchises'

    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            return 0
        return self.extra


class SpecialSeriesRelationInline(admin.TabularInline):
    model = SpecialSeriesRelation
    extra = 1
    show_change_link = True

    fields = ('predicate', 'series',)

    verbose_name = 'Related Series'
    verbose_name_plural = 'Related Series'

    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            return 0
        return self.extra


class ModuleEpisodeRelationInline(admin.TabularInline):
    model = ModuleEpisodeRelation
    extra = 1
    show_change_link = True

    fields = ('predicate', 'episode',)

    verbose_name = 'Related Episode'
    verbose_name_plural = 'Related Episodes'

    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            return 0
        return self.extra


class ClipEpisodeRelationInline(admin.TabularInline):
    model = ClipEpisodeRelation
    extra = 1
    show_change_link = True

    fields = ('predicate', 'episode',)

    verbose_name = 'Related Episode'
    verbose_name_plural = 'Related Episodes'

    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            return 0
        return self.extra


class VersionEpisodeRelationInline(admin.TabularInline):
    model = VersionEpisodeRelation
    extra = 1
    show_change_link = True

    fields = ('predicate', 'episode',)

    verbose_name = 'Related Episode'
    verbose_name_plural = 'Related Episodes'

    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            return 0
        return self.extra

# class ContainerContainerRelationsSourcesInline(admin.StackedInline):
#     model = ContainerContainerRelation
#     extra = 1
#     show_change_link = True
#     fk_name = 'target'
#     fields = ('target', 'predicate', 'source',)
#     readonly_fields = ('target',)
#
#     def get_target(self, obj):
#         title_obj = obj.title_set.filter(title_type__name='Default Title')
#         return title_obj.values('title_text')[0]['title_text']
#
#     def get_extra(self, request, obj=None, **kwargs):
#         if obj:
#             return 0
#         return self.extra
#
#
# class ContainerContainerRelationsTargetsInline(admin.TabularInline):
#     model = ContainerContainerRelation
#     extra = 1
#     show_change_link = True
#     fk_name = 'target'
#
#     def get_extra(self, request, obj=None, **kwargs):
#         if obj:
#             return 0
#         return self.extra
#
#
# admin.site.register(ContainerContainerRelation)
# admin.site.register(ContainerItemRelations)
# admin.site.register(ItemItemRelations)
