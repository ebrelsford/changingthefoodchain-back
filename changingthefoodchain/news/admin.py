from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from elephantblog.models import Entry
from feincms.admin import item_editor
from leaflet.admin import LeafletGeoAdmin


# EntryAdmin copied from elephantblog.admin
class EntryAdmin(item_editor.ItemEditor):
    actions = []

    date_hierarchy = 'published_on'
    filter_horizontal = ['categories']
    list_display = [
        'title', 'is_active', 'is_featured', 'published_on', 'author']
    list_editable = ['is_active', 'is_featured']
    list_filter = ['is_active', 'is_featured', 'categories', 'author']
    raw_id_fields = ['author']
    search_fields = ['title', 'slug']
    prepopulated_fields = {
        'slug': ('title',),
    }

    fieldset_insertion_index = 1
    fieldsets = [
        [None, {
            'fields': [
                ('is_active', 'is_featured', 'published_on'),
                ('title', 'slug'),
                'author',
                'categories',
            ]
        }],
        [_('Other options'), {
            'fields': [],
            'classes': ('collapse',),
        }],
        item_editor.FEINCMS_CONTENT_FIELDSET,
    ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'author':
            kwargs['initial'] = request.user.id
        return super(EntryAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs)


class GeoEntryAdmin(LeafletGeoAdmin, EntryAdmin):
    pass


admin.site.unregister(Entry)
admin.site.register(Entry, GeoEntryAdmin)
