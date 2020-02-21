import logging
from rest_framework import serializers
from apps.epidemic.models import Epidemic

logger = logging.getLogger("django")


class EpidemicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Epidemic
        exclude = ["id"]


class EpidemicTotalSerializer(serializers.Serializer):
    add_suspect = serializers.IntegerField(source="add_suspect__sum")
    cumulative_suspect = serializers.IntegerField(source="cumulative_suspect__sum")
    new_diagnosis = serializers.IntegerField(source="new_diagnosis__sum")
    cumulative_diagnosis = serializers.IntegerField(source="cumulative_diagnosis__sum")
    added_death = serializers.IntegerField(source="added_death__sum")
    cumulative_death = serializers.IntegerField(source="cumulative_death__sum")


# class EChartSerializer(serializers.Serializer):
#
#     def to_representation(self, instance):
#         return [
#             instance.province,
#             instance.cumulative_diagnosis,
#             instance.cumulative_suspect,
#             "-",
#             instance.cumulative_death,
#         ]
