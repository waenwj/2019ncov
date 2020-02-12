from django.db import models


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

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-published_at"]
        constraints = [
            models.UniqueConstraint(fields=['name', 'published_at'], name='unique_name'),
        ]
