# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0012_auto_20150623_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='sectors',
            field=models.ManyToManyField(to='organizations.Sector', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='types',
            field=models.ManyToManyField(to='organizations.Type', null=True, blank=True),
        ),
    ]
