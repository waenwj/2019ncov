from rest_framework import serializers
from apps.epidemic.models import Epidemic


class EpidemicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Epidemic
        exclude = ["id"]
