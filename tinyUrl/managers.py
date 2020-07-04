import datetime
from django.db.models.manager import Manager


class TinyUrlManager(Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(expire_date__gte=datetime.datetime.now())
