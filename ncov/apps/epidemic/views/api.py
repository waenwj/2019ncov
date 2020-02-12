from rest_framework import generics, permissions

from apps.epidemic.models import Epidemic
from apps.epidemic.serializers import EpidemicSerializer


class EpidemicListAPIView(generics.ListCreateAPIView):
    serializer_class = EpidemicSerializer
    queryset = Epidemic.objects.all()
    permission_classes = [permissions.AllowAny]
    ordering_fields = ["published_at"]
    search_fields = ["name", "province"]
