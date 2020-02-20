from rest_framework import generics
from apps.news.serializers import NewsSerializer
from apps.news.models import News


class NewsListAPIView(generics.ListCreateAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()


class NewsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()
    lookup_field = "webpageCode"
    lookup_url_kwarg = "webpageCode"

