from django.db import ProgrammingError
from rest_framework import generics
from rest_framework.response import Response

from apps.peopleapp.models import Epidemic, TotalEpidemic
from apps.peopleapp.serializers import (
    EpidemicSerializer,
    TotalEpidemicSerializer,
    TransferTotalEpidemicSerializer,
)


class EpidemicListAPIView(generics.ListCreateAPIView):
    serializer_class = EpidemicSerializer

    def get_queryset(self):
        try:
            qs = Epidemic.objects.first()
        except ProgrammingError:
            qs = None
        return qs

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=False)
        return Response(serializer.data)


class TotalEpidemicListAPIView(generics.ListCreateAPIView):
    serializer_class = TotalEpidemicSerializer

    def get_queryset(self):
        try:
            qs = TotalEpidemic.objects.first()
        except ProgrammingError:
            qs = None
        return qs

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        # serializer = self.get_serializer(queryset, many=False)
        serializer = TransferTotalEpidemicSerializer(queryset, many=False)
        return Response(serializer.data)
