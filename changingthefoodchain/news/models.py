from django.conf import settings
from django.utils.translation import ugettext as _

from feincms.content.raw.models import RawContent
from feincms.content.richtext.models import RichTextContent
from feincms.content.medialibrary.models import MediaFileContent
from feincms_oembed.contents import OembedContent

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

Entry.create_content_type(OembedContent,
    TYPE_CHOICES=(
        ('default', _('Default'), { 'maxwidth': 500, 'maxheight': 300, 'wmode': 'opaque'}),
    ),
    PARAMS={'wmode': 'opaque', 'key': settings.EMBEDLY_KEY}
)

Entry.create_content_type(RawContent,
    regions=('main', 'preview', 'cover',)
)
