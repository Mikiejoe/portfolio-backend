from rest_framework.serializers import ModelSerializer
from core.models import Project,Photo,Emails

class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        
class PhotoSerializer(ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'
            
            

class EmailsSerializer(ModelSerializer):
    class Meta:
        model = Emails
        fields = '__all__'