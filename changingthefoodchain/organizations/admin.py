from django.contrib import admin

from .models import Organization, Sector, Type


class OrganizationAdmin(admin.ModelAdmin):
    fields = ('name',
              ('address_line1', 'address_line2',),
              ('city', 'state_province', 'country',),
              ('email', 'phone',),
              'site_url',
              ('mission', 'mission_es',),
              ('sectors', 'types',),
              'fcwa_organization',
              'centroid',)
    list_display = ('name', 'address_line1', 'city', 'state_province',)
    list_filter = ('sectors', 'types', 'fcwa_organization',)
    search_fields = ('name', 'address_line1', 'city', 'state_province',)


class SectorAdmin(admin.ModelAdmin):
    pass


class TypeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Sector, SectorAdmin)
admin.site.register(Type, TypeAdmin)
