from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AlumniViewSet, DisasterAlertViewSet, home

router = DefaultRouter()
router.register(r'alumni', AlumniViewSet)
router.register(r'disasters', DisasterAlertViewSet, basename='disaster-alert')

urlpatterns = [
    path('', home, name='home'),
] + router.urls