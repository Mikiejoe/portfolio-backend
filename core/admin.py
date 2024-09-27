from django.contrib import admin

# Register your models here.
from .models import Project, Photo, Emails


class ProjectImageInline(admin.TabularInline):
    model = Photo
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "github_url", "created_at")
    search_fields = ("title", "technology")
    list_filter = ("title", "technology")
    inlines = [ProjectImageInline]


class PhotoAdmin(admin.ModelAdmin):
    list_display = ("image", "project")
    search_fields = ("project",)
    list_filter = ("project",)


admin.site.register(Project, ProjectAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Emails)


# admin.si
