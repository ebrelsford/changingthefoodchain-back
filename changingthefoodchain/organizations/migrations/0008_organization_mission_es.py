# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0007_organization_visible'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='mission_es',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
