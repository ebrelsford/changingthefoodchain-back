# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20140818_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='added_by',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='video',
            name='added_by',
            field=models.EmailField(max_length=254),
        ),
    ]
