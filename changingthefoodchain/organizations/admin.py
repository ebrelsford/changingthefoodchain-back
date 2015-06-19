from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Organization, Sector, Type


class HasFilter(admin.SimpleListFilter):

    def lookups(self, request, model_admin):
        return (
            ('yes', _('Yes')),
            ('no', _('No')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'yes':
            return queryset.filter(**{
                '%s__isnull' % self.field_name: False,
            })
        elif self.value() == 'no':
            return queryset.filter(**{
                '%s__isnull' % self.field_name: True,
            })


class HasUrlFilter(HasFilter):
    field_name = 'site_url'
    parameter_name = 'has_url'
    title = _('has url')


class HasEmailFilter(HasFilter):
    field_name = 'email'
    parameter_name = 'has_email'
    title = _('has email address')


class HasPhoneFilter(HasFilter):
    field_name = 'phone'
    parameter_name = 'has_phone'
    title = _('has phone number')


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
    list_display = ('name', 'address_line1', 'city', 'state_province',
                    'site_url', 'email', 'phone',)
    list_editable = ('site_url', 'email', 'phone',)
    list_filter = ('sectors', 'types', 'fcwa_organization', HasUrlFilter,
                   HasEmailFilter, HasPhoneFilter,)
    search_fields = ('name', 'address_line1', 'city', 'state_province',)


class SectorAdmin(admin.ModelAdmin):
    pass


class TypeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Sector, SectorAdmin)
admin.site.register(Type, TypeAdmin)
