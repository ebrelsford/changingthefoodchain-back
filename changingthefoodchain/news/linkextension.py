from django.db import models
from django.utils.translation import ugettext_lazy as _

from feincms import extensions


class Extension(extensions.Extension):
    def handle_model(self):
        # Add link url
        self.model.add_to_class('link',
            models.URLField(_('link'), blank=True, null=True)
        )

        # Add "read more at" text
        self.model.add_to_class('read_more_at',
            models.CharField(_('read more at'),
                max_length=100,
                blank=True,
                null=True,
            )
        )

    def handle_modeladmin(self, modeladmin):
        modeladmin.add_extension_options(_('External link'), {
            'fields': ['link', 'read_more_at',],
        })
