from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from django.http.response import HttpResponse


from .serializers import TinyUrlSerializer
from .utils import get_long_url


class TinyUrlView(APIView):
    def get(self, request):
        return render(request, "tiny_forms.html")

    def post(self, request):
        data = request.data
        params = {"long_url": data["url"]}
        serializer = TinyUrlSerializer(data=params)
        if not serializer.is_valid():
            return HttpResponse(repr(serializer.errors), status=400)
        serializer.save()
        short_url = serializer.data["short_url"]
        return HttpResponse(short_url)


class LongUrlView(APIView):
    def get(self, request):
        return render(request, "long_forms.html")

    def post(self, request):
        data = request.data
        params = {"short_url": data["url"]}
        long_url = get_long_url(params)
        if long_url:
            return HttpResponse(long_url)
        else:
            return HttpResponse("Url does not exist")
