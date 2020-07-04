import datetime
from rest_framework import serializers

from .models import *


class TinyUrlSerializer(serializers.ModelSerializer):
    short_url = serializers.URLField(read_only=True)
    expire_date = serializers.DateTimeField(required=False)

    class Meta:
        model = TinyUrlModel
        fields = "__all__"

    def validate(self, attrs):
        from .utils import generate_short_url
        attrs["short_url"] = generate_short_url()
        return attrs
