from django.urls import path
from .views import ProjectListCreateAPIView, ProjectRetrieveUpdateDestroyAPIView, PhotoListCreateAPIView,send_email,send_email_with_template

urlpatterns = [
    path('projects/', ProjectListCreateAPIView.as_view(), name='projects'),
    path('projects/<int:pk>/', ProjectRetrieveUpdateDestroyAPIView.as_view(), name='project'),
    path('photos/', PhotoListCreateAPIView.as_view(), name='photos'),
    # path('send-email/', send_email, name='send_email'),
    path('send-email/', send_email_with_template, name='send_email'),
]

