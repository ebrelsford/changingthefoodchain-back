from django.utils.translation import ugettext as _

from feincms.content.richtext.models import RichTextContent
from feincms.content.medialibrary.models import MediaFileContent

from elephantblog.models import Entry


Entry.register_extensions(
    'feincms.module.extensions.translations',
    'news.linkextension',
    'news.locationextension',
)

Entry.register_regions(
    ('main', _('Main content area')),
    ('preview', _('Preview')),
    ('cover', _('Cover image')),
)

Entry.create_content_type(RichTextContent,
    regions=('main', 'preview', 'cover',)
)

Entry.create_content_type(MediaFileContent, TYPE_CHOICES=(
    ('default', _('default')),
))
