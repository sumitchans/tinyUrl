import datetime
from django.db import models

from .managers import TinyUrlManager


class TinyUrlModel(models.Model):
    short_url = models.URLField(unique=True)
    long_url = models.URLField(unique=True)
    expire_date = models.DateTimeField(default=datetime.datetime.now()+datetime.timedelta(days=3))

    objects = TinyUrlManager()
