# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0004_organization_site_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='mission',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
