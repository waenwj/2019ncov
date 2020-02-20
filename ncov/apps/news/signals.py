import requests
import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from apps.news.models import News
from apps.news.serializers import TransferNewsSerializer

logger = logging.getLogger("django")

headers = getattr(settings, "POST_HEADERS")
post_url = getattr(settings, "POST_URL")


@receiver(post_save, sender=News)
def crawled_post_action(sender, instance: News, created, **kwargs) -> None:
    if created:
        ser = TransferNewsSerializer(instance)
        logger.info(ser.data)

        res = requests.post(post_url, json=ser.data, headers=headers)
        if 200 <= res.status_code <= 299:
            logger.info("post ok")
        else:
            logger.error(res.content)
