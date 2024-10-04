from django.db import models
from django.utils.text import slugify


class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, blank=True, null=True)
    technology = models.CharField(max_length=255, blank=True, null=True)
    overview = models.TextField(blank=True, null=True)
    key_features = models.TextField(
        blank=True, null=True
    )  # You can store this as a JSON string
    development = models.TextField(blank=True, null=True)
    conclusion = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    live_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            num = 1
            while Project.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            self.slug = slug
        super().save(*args, **kwargs)


class Photo(models.Model):
    project = models.ForeignKey(
        Project, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="portfolio/project-images/")
    uploaded_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"Image for {self.project.title}"
    @property
    def image_url(self):
        if self.image:
            return self.image.url
        return None


class Emails(models.Model):
    subject = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    message = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.subject
