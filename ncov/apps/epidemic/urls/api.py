from django.urls import path

from apps.epidemic.views.api import EpidemicListAPIView, EpidemicDateListAPIView, EpidemicTotalAPIView

app_name = "epidemic"

urlpatterns = [
    path("", EpidemicListAPIView.as_view(), name="index"),
    path("<str:date>/", EpidemicDateListAPIView.as_view(), name="date"),
    path("<str:date>/total/", EpidemicTotalAPIView.as_view(), name="total"),
]
