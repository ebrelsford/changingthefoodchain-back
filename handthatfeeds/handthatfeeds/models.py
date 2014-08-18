from django.db import models


class ModerationVisible(models.Model):
    visible = models.BooleanField(default=False)

    class Meta:
        abstract = True
