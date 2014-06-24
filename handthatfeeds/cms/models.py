from django.utils.translation import ugettext_lazy as _

from feincms.module.page.models import Page
from feincms.content.medialibrary.models import MediaFileContent
from feincms.content.richtext.models import RichTextContent


Page.register_extensions(
    'feincms.module.extensions.datepublisher',
    'feincms.module.extensions.translations',
)

Page.register_templates({
    'title': _('Standard template'),
    'path': 'base.html',
    'regions': (
        ('main', _('Main content area')),
        ('sidebar', _('Sidebar'), 'inherited'),
        ('footer', _('Footer'), 'inherited'),
    ),
})

Page.register_templates({
    'title': _('Map template'),
    'path': 'map.html',
    'regions': (
        ('main', _('Main content area')),
        ('sidebar', _('Sidebar'), 'inherited'),
        ('footer', _('Footer'), 'inherited'),
    ),
})

Page.objects.exclude_from_copy.append('template_key')

Page.create_content_type(RichTextContent)

Page.create_content_type(MediaFileContent, TYPE_CHOICES=(
    ('default', _('default')),
))
