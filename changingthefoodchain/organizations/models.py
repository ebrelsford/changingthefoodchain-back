from django.db import models

from changingthefoodchain.models import ModerationVisible
from inplace.models import Place


class Organization(ModerationVisible, Place):
    email = models.EmailField(blank=True, null=True,)
    site_url = models.URLField(blank=True, null=True,)
    phone = models.CharField(max_length=15, blank=True, null=True,)
    mission = models.TextField(blank=True, null=True)
    mission_es = models.TextField(blank=True, null=True)
    sectors = models.ManyToManyField('Sector', blank=True,)
    types = models.ManyToManyField('Type', blank=True,)
    fcwa_organization = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s' % self.name


class Sector(models.Model):
    name = models.CharField(max_length=50,)
    name_es = models.CharField(max_length=50, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.name


class Type(models.Model):
    name = models.CharField(max_length=50,)
    name_es = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.name
