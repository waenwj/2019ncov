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
