from django.urls import path, include
from .views import (
    send_email_with_template,
    ProjectViewSet,
    PhotoViewset,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"projects", ProjectViewSet)
router.register(r"photos", PhotoViewset)


urlpatterns = [
    # path('photos/', PhotoListCreateAPIView.as_view(), name='photos'),
    path(
        "send-email/",
        send_email_with_template,
        name="send-email",
    ),
    path(
        "",
        include(router.urls),
    ),
]
