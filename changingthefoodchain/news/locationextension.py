from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _

from feincms import extensions


class Extension(extensions.Extension):

    def handle_model(self):
        # Add location field
        self.model.add_to_class('location',
            models.PointField(_('location'), blank=True, null=True)
        )

    def handle_modeladmin(self, modeladmin):
        modeladmin.add_extension_options(_('Location'), {
            'fields': ('location',),
        })
