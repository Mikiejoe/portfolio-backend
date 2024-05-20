from rest_framework.serializers import ModelSerializer
from core.models import Project,Photo

class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        
class PhotoSerializer(ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'