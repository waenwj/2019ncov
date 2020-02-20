from rest_framework import serializers
from .models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        exclude = ["id"]


class TransferNewsSerializer(serializers.ModelSerializer):

    cover = serializers.URLField(source="pictrueUrl", default="")
    categories = serializers.SerializerMethodField()
    c7e5c3d3d0d81771 = serializers.CharField(source="summary")
    ecc9f3c91d371a8e = serializers.CharField(source="reportSource")
    f12c47594e48848a = serializers.CharField(source="webpageUrl")
    review_state = serializers.IntegerField(default=0)
    published = serializers.DateTimeField(source="releaseTime")

    class Meta:
        model = News
        fields = [
            "cover",
            "categories",
            "review_state",
            "title",
            "c7e5c3d3d0d81771",
            "ecc9f3c91d371a8e",
            "f12c47594e48848a",
            "published",
        ]

    def get_categories(self, obj) -> list:
        return ["all"]
