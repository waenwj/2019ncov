from django.urls import path
from apps.epidemic.views.api import EpidemicListAPIView, EpidemicDateListAPIView

app_name = "epidemic"

urlpatterns = [
    path("", EpidemicListAPIView.as_view(), name="index"),
    path("<str:date>/", EpidemicDateListAPIView.as_view(), name="epidemic-date"),
]
