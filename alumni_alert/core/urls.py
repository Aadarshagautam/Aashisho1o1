from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . views import AlumniViewSet, DisasterAlertViewSet

router = DefaultRouter()
router.register(r'alumni', AlumniViewSet)
router.register(r'alerts', DisasterAlertViewSet)

urlpatterns = [
    path('', include(router.urls)),
]