# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0009_auto_20141027_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='fcwa_organization',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
