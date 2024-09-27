from rest_framework.serializers import ModelSerializer
from core.models import Project, Photo, Emails


class PhotoSerializer(ModelSerializer):
    class Meta:
        model = Photo
        fields = ["image", "uploaded_at"]


class ProjectSerializer(ModelSerializer):
    images = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "slug",
            "technology",
            "overview",
            "key_features",
            "development",
            "conclusion",
            "images",
            "github_url",
            "live_url",
        ]


class EmailsSerializer(ModelSerializer):
    class Meta:
        model = Emails
        fields = "__all__"
