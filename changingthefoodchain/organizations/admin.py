from django.contrib import admin

from moderation.admin import ModerationAdmin

from .models import Organization, Sector, Type


class OrganizationAdmin(ModerationAdmin):
    list_display = ('name', 'address_line1', 'city', 'state_province',)
    list_filter = ('sectors', 'types')
    search_fields = ('name', 'address_line1', 'city', 'state_province',)


class SectorAdmin(admin.ModelAdmin):
    pass


class TypeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Sector, SectorAdmin)
admin.site.register(Type, TypeAdmin)
