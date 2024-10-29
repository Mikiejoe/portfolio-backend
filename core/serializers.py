from rest_framework.serializers import ModelSerializer, SerializerMethodField
from core.models import Project, Photo, Emails


class PhotoSerializer(ModelSerializer):
    image = SerializerMethodField()

    class Meta:
        model = Photo
        fields = ["image"]

    def get_image(self, obj):
        return obj.image.url if hasattr(obj.image, 'url') else None


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
