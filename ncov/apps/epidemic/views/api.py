from rest_framework import generics, permissions, status
from rest_framework.exceptions import APIException

from django.db.utils import IntegrityError

from apps.epidemic.filters import EpidemicFilter
from apps.epidemic.models import Epidemic
from apps.epidemic.serializers import EpidemicSerializer


class EpidemicListAPIView(generics.ListCreateAPIView):
    serializer_class = EpidemicSerializer
    queryset = Epidemic.objects.all()
    permission_classes = [permissions.AllowAny]
    filterset_class = EpidemicFilter
    ordering_fields = ["published_at"]
    search_fields = ["name", "province"]

    def perform_create(self, serializer):
        try:
            serializer.save()
        except IntegrityError as e:
            raise APIException(detail=e, code=status.HTTP_400_BAD_REQUEST)
