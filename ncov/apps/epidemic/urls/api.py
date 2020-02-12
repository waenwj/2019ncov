from django.urls import path
from apps.epidemic.views.api import EpidemicListAPIView

app_name = "epidemic"

urlpatterns = [
    path("", EpidemicListAPIView.as_view(), name="index"),
]
