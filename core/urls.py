from django.urls import path
from .views import ProjectListCreateAPIView, ProjectRetrieveUpdateDestroyAPIView, PhotoListCreateAPIView

urlpatterns = [
    path('projects/', ProjectListCreateAPIView.as_view(), name='projects'),
    path('projects/<int:pk>/', ProjectRetrieveUpdateDestroyAPIView.as_view(), name='project'),
    path('photos/', PhotoListCreateAPIView.as_view(), name='photos'),
]

