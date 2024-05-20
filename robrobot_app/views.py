# robrobot_app/views.py
from rest_framework import viewsets
from .models import Profile, Project
from .serializers import ProfileSerializer, ProjectSerializer
from django.http import HttpResponse, JsonResponse


class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


def health_check(request):
    return HttpResponse("Health check passed!", status=200)


def health_check_debug(request):
    response_data = {
        'method': request.method,
        'headers': dict(request.headers),
        'body': request.body.decode('utf-8')
    }
    return JsonResponse(response_data, status=200)