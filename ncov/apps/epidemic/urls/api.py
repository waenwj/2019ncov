from django.urls import path

from apps.epidemic.views.api import EpidemicListAPIView, EChartDateListAPIView

app_name = "epidemic"

urlpatterns = [
    path("", EpidemicListAPIView.as_view(), name="index"),
    path("<str:date>/", EChartDateListAPIView.as_view(), name="date"),
]
