from datetime import datetime

from django.db.utils import IntegrityError
from rest_framework import generics, permissions
from rest_framework.response import Response

from apps.epidemic.filters import EpidemicFilter
from apps.epidemic.models import Epidemic
from apps.epidemic.serializers import EpidemicSerializer, EpidemicTotalSerializer
from apps.epidemic.views.mixins import ProcessDateMixin
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


class EpidemicDateListAPIView(ProcessDateMixin, generics.ListAPIView):
    serializer_class = EpidemicSerializer
    search_fields = ["name", "province"]
    ordering_fields = ["cumulative_diagnosis", "cumulative_suspect", "cumulative_death"]

    def get_queryset(self):
        qs = Epidemic.objects.filter(published_at=self.process_date(**self.kwargs))
        return qs


class EpidemicTotalAPIView(ProcessDateMixin, generics.RetrieveAPIView):
    serializer_class = EpidemicTotalSerializer

    def get_object(self):
        _obj = Epidemic.objects.total_by_date(self.process_date(**self.kwargs))
        return _obj

