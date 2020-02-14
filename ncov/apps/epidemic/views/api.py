from datetime import timedelta, datetime
from django.db.utils import IntegrityError
from rest_framework import generics, permissions

from apps.epidemic.filters import EpidemicFilter
from apps.epidemic.models import Epidemic
from apps.epidemic.serializers import EpidemicSerializer
from apps.ext.rest.exceptions import IntegrityException


class EpidemicListAPIView(generics.ListCreateAPIView):
    serializer_class = EpidemicSerializer
    queryset = Epidemic.objects.all()
    permission_classes = [permissions.AllowAny]
    filterset_class = EpidemicFilter
    ordering_fields = ["published_at", "cumulative_diagnosis", "new_diagnosis"]
    search_fields = ["name", "province"]

    def perform_create(self, serializer):
        try:
            serializer.save()
        except IntegrityError as e:
            raise IntegrityException(detail=e)


class EpidemicDateListAPIView(generics.ListAPIView):
    serializer_class = EpidemicSerializer
    search_fields = ["name", "province"]
    ordering_fields = ["cumulative_diagnosis", "new_diagnosis"]

    def _process_date(self):
        dt_string = self.kwargs.get("date")
        dt = datetime.strptime(dt_string, "%Y%m%d")
        return dt

    def get_queryset(self):
        qs = Epidemic.objects.filter(published_at=self._process_date())
        return qs
