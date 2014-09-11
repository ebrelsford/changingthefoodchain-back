from django import template
from django.conf import settings

from classytags.core import Options
from classytags.arguments import Argument
from classytags.helpers import AsTag

register = template.Library()


class Setting(AsTag):
    options = Options(
        Argument('name'),
        'as',
        Argument('varname', resolve=False, required=False),
    )

    def get_value(self, context, name):
        return getattr(settings, name)


register.tag(Setting)
