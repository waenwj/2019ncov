import logging

from rest_framework import serializers

from apps.peopleapp.models import Epidemic, TotalEpidemic

logger = logging.getLogger("django")


class EpidemicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Epidemic
        exclude = ["id"]


class TotalEpidemicSerializer(serializers.ModelSerializer):
    class Meta:
        model = TotalEpidemic
        exclude = ["id"]


class TransferTotalEpidemicSerializer(serializers.ModelSerializer):
    class Meta:
        model = TotalEpidemic
        fields = [
            "title",
            "totalHealAddCnt",
            "totalDeadAddCnt",
            "totalSuspectedAddCnt",
            "totalNowConfirmCnt",
            "updateTime",
        ]
