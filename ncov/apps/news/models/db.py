from django.db import models
from django_extensions.db import fields


class News(models.Model):
    slug = fields.RandomCharField(
        length=12, unique=True, include_alpha=False, db_index=True, editable=False
    )
    title = models.CharField(max_length=255, )
    summary = models.TextField()
    crawlSource = models.CharField(max_length=255)
    majorClassification = models.CharField(max_length=255)
    metaInfoName = models.CharField(max_length=255)
    pictrueUrl = models.URLField(max_length=255, blank=True, null=True)
    webpageCode = models.CharField(max_length=32, unique=True)
    webpageUrl = models.URLField(max_length=255, blank=True, default="")
    reportSource = models.CharField(max_length=255, blank=True, default="")
    releaseTime = models.DateTimeField(db_index=True)

    class Meta:
        ordering = ["-releaseTime"]

    def __str__(self):
        return self.title
