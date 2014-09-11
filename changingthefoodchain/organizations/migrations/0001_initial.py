# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('centroid', django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, verbose_name='centroid', blank=True)),
                ('polygon', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326, null=True, verbose_name='polygon', blank=True)),
                ('name', models.CharField(max_length=256, null=True, verbose_name='name', blank=True)),
                ('address_line1', models.CharField(max_length=150, null=True, verbose_name='address line 1', blank=True)),
                ('address_line2', models.CharField(max_length=150, null=True, verbose_name='address line 2', blank=True)),
                ('postal_code', models.CharField(max_length=10, null=True, verbose_name='postal code', blank=True)),
                ('city', models.CharField(max_length=50, null=True, verbose_name='city', blank=True)),
                ('state_province', models.CharField(max_length=40, null=True, verbose_name='state/province', blank=True)),
                ('country', models.CharField(max_length=40, null=True, verbose_name='country', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
