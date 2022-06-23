from os import path
from uuid import uuid1

from django.db import models


class Photo(models.Model):
    """
    Public info without IP restrictions.
    """
    name = models.CharField(max_length=50, primary_key=True)
    file = models.FileField(
        max_length=255,
        blank=False,
        null=False,
        verbose_name="file",
        upload_to=path.join("photos/uploads", str(uuid1())),
    )
    mime = models.CharField(
        blank=False,
        null=False,
        max_length=256,
        verbose_name="mime",
    )
