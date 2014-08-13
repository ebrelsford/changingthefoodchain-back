# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0003_auto_20140709_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='site_url',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
