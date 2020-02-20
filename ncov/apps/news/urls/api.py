from django.urls import path
from apps.news.views.api import NewsListAPIView, NewsDetailAPIView

app_name = "news"

urlpatterns = [
    path("", NewsListAPIView.as_view(), name="index"),
    path("<slug:webpageCode>/", NewsDetailAPIView.as_view(), name="detail")
]
