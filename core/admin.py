from django.contrib import admin

# Register your models here.
from .models import Project, Photo

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'url')
    search_fields = ('title', 'description')
    list_filter = ('title', 'description')
    
    
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('image', 'project')
    search_fields = ('project',)
    list_filter = ('project',)


admin.site.register(Project, ProjectAdmin)
admin.site.register(Photo, PhotoAdmin)

# admin.si