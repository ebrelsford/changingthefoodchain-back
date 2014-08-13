# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0005_organization_mission'),
    ]

    operations = [
        migrations.AddField(
            model_name='type',
            name='description',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='type',
            name='image',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
