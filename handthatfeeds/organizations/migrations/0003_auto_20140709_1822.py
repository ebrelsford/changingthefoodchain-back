# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0002_auto_20140707_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='phone',
            field=models.CharField(max_length=15, null=True, blank=True),
        ),
    ]
