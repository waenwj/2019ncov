from django.urls import path

from apps.peopleapp.views.api import EpidemicListAPIView, TotalEpidemicListAPIView

app_name = "peopleapp"

urlpatterns = [
    path("epidemic/", EpidemicListAPIView.as_view(), name="epidemic"),
    path("epidemic/total/", TotalEpidemicListAPIView.as_view(), name="epidemic-total"),
]
