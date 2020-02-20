import logging
from rest_framework import serializers
from apps.epidemic.models import Epidemic

logger = logging.getLogger("django")


class EpidemicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Epidemic
        exclude = ["id"]


class EChartSerializer(serializers.Serializer):

    def to_representation(self, instance):
        return [
            instance.province,
            instance.cumulative_diagnosis,
            instance.cumulative_suspect,
            "-",
            instance.cumulative_death,
        ]
