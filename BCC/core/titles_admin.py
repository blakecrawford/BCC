from django.contrib import admin

from .titles import TitleType
from .titles import Title


class TitleInline(admin.TabularInline):
    model = Title
    extra = 1
    fields = ('vmid', 'title_type', 'title_text', 'language',)
    readonly_fields = ('vmid',)

    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            return 0
        return self.extra


admin.site.register(TitleType)
admin.site.register(Title)
