# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0006_auto_20140813_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='visible',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
