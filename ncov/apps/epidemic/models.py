from datetime import datetime, timedelta
from django.db import models
from django.db.models import Sum


class EpidemicManager(models.Manager):
    def total_group_by_date(self):
        dt = datetime.now() - timedelta(30)
        return self.filter(published_at__gte=dt).values("published_at").annotate(
            Sum("add_suspect"),
            Sum("cumulative_suspect"),
            Sum("new_diagnosis"),
            Sum("cumulative_diagnosis"),
            Sum("added_death"),
            Sum("cumulative_death"),
        ).order_by("published_at")

    def total_by_date(self, date):
        return self.filter(published_at=date).aggregate(
            Sum("add_suspect"),
            Sum("cumulative_suspect"),
            Sum("new_diagnosis"),
            Sum("cumulative_diagnosis"),
            Sum("added_death"),
            Sum("cumulative_death"),
        )


class Epidemic(models.Model):
    name = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    add_suspect = models.IntegerField(default=0)
    cumulative_suspect = models.IntegerField(default=0)
    new_diagnosis = models.IntegerField(default=0)
    cumulative_diagnosis = models.IntegerField(default=0)
    added_death = models.IntegerField(default=0)
    cumulative_death = models.IntegerField(default=0)
    published_at = models.DateField(db_index=True)

    objects = EpidemicManager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-published_at", "-cumulative_diagnosis", "-new_diagnosis"]
        constraints = [
            models.UniqueConstraint(fields=["name", "published_at"], name="unique_name")
        ]
