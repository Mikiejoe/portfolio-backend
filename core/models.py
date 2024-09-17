from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to=f'portfolio/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
    
    
class Photo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=f'portfolio/images/')

    def __str__(self):
        return self.project.title
    
    
class Emails(models.Model):
    subject = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    message = models.TextField()
    email = models.EmailField()

    def __str__(self):
            return self.subject
    

    
