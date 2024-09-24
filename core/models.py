from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)
    technology = models.CharField(max_length=255,null=True)
    overview = models.TextField(null=True)
    key_features = models.TextField(null=True)  # You can store this as a JSON string
    development = models.TextField(null=True)
    conclusion = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    github_url = models.URLField(null=True)
    live_url = models.URLField(null=True)

    def __str__(self):
        return self.title  
       
class Photo(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=f'portfolio/project-images/{project.title}')
    uploaded_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return f"Image for {self.project.title}"
    
    
class Emails(models.Model):
    subject = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    message = models.TextField()
    email = models.EmailField()

    def __str__(self):
            return self.subject
    

    
