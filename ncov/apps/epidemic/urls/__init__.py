from django.urls import path
from apps.epidemic.views import EpidemicChartView


urlpatterns = [
    path("<str:date>/", EpidemicChartView.as_view(), name="date"),
]
