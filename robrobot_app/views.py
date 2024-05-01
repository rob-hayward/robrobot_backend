# robrobot_app/views.py
from rest_framework import viewsets
from .models import Profile, Project
from .serializers import ProfileSerializer, ProjectSerializer


class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

