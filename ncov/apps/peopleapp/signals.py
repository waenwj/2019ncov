import json
import logging

import requests
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.peopleapp.models import TotalEpidemic
from apps.peopleapp.serializers import TransferTotalEpidemicSerializer

logger = logging.getLogger("django")

headers = getattr(settings, "POST_HEADERS")
post_url = getattr(settings, "POST_TOTAL_EPIDEMIC_URL")


@receiver(post_save, sender=TotalEpidemic)
def crawl_post_action(sender, instance: TotalEpidemic, created, **kwargs) -> None:
    if created:
        ser = TransferTotalEpidemicSerializer(instance, many=False)
        _data = ser.data

        update_data = {
            "title": _data.get("title"),
            "5d7593ade13c29b1": _data.get("updateTime"),
            "28a310ca23baf2ad": _data.get("totalDeadAddCnt"),
            "6a41a68b042deea9": _data.get("totalHealAddCnt"),
            "32a8a3a964c30ccc": _data.get("totalSuspectedAddCnt"),
            "6440ff5d6e79baf9": _data.get("totalNowConfirmCnt"),
        }
        json_str = json.dumps(update_data)
        logger.info(headers)
        logger.info(json_str)
        res = requests.put(post_url, data=json_str, headers=headers)
        r = res.json()
        if r.get("code") == 200:
            logger.info("update ok")
        else:
            logger.error(r["msg"])
