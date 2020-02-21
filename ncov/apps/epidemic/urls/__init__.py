from django.urls import path
from apps.epidemic.views import (
    EpidemicChartView,
    EpidemicDateChartView,
    EpidemicDateTotalChartView
)

app_name = "epidemic"

urlpatterns = [
    path("", EpidemicChartView.as_view(), name="index"),
    path("<str:date>/", EpidemicDateChartView.as_view(), name="date"),
    path("<str:date>/total/", EpidemicDateTotalChartView.as_view(), name="total"),
]
