# robrobot_app/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import send_email


router = DefaultRouter()
router.register(r'profiles', views.ProfileViewSet)
router.register(r'projects', views.ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('send-email/', send_email, name='send_email'),
]
