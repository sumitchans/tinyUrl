import random
from django.db.models import Max
from .models import TinyUrlModel


def generate_short_url():
    max_id = TinyUrlModel.objects.aggregate(m_id=Max("id"))["m_id"] or 0
    chrs = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 97+26)]
    short_url = "".join(random.sample(chrs, 3)) + str(max_id+1)
    return "https://" + short_url + ".com"


def get_long_url(params):
    try:
        return TinyUrlModel.objects.get(**params).long_url
    except Exception as ex:
        return None
