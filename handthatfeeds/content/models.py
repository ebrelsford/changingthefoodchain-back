from django.db import models

from handthatfeeds.models import ModerationVisible


class Content(ModerationVisible):
    added = models.DateTimeField(auto_now=True)
    added_by = models.EmailField()
    organization = models.ForeignKey('organizations.Organization')

    class Meta:
        abstract = True


class Video(Content):
    url = models.URLField()


class Photo(Content):
    photo = models.ImageField(upload_to='content/photos')
