from datetime import datetime

from django.db.utils import IntegrityError
from rest_framework import generics, permissions
from rest_framework.response import Response

from apps.epidemic.filters import EpidemicFilter
from apps.epidemic.models import Epidemic
from apps.epidemic.serializers import EpidemicSerializer, EChartSerializer
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
    ordering_fields = ["cumulative_diagnosis", "cumulative_suspect", "cumulative_death"]

    def _process_date(self):
        dt_string = self.kwargs.get("date")
        dt = datetime.strptime(dt_string, "%Y%m%d")
        return dt

    def get_queryset(self):
        qs = Epidemic.objects.filter(published_at=self._process_date())
        return qs


class EChartDateListAPIView(generics.ListAPIView):
    serializer_class = EChartSerializer
    ordering_fields = ["cumulative_diagnosis", "cumulative_suspect", "cumulative_death"]
    pagination_class = None

    def _process_date(self):
        dt_string = self.kwargs.get("date")
        dt = datetime.strptime(dt_string, "%Y%m%d")
        return dt

    def get_queryset(self):
        qs = Epidemic.objects.filter(published_at=self._process_date())
        return qs

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        _data = serializer.data
        _data.insert(0, ["省市", "确诊", "疑似", "治愈", "死亡"])
        return Response(_data)

