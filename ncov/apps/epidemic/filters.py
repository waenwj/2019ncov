from django_filters import rest_framework as filters
from apps.epidemic.models import Epidemic


class EpidemicFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name")
    published_at = filters.DateFilter(field_name="published_at")

    class Meta:
        models = Epidemic
        fields = ["name", "published_at"]
