# robrobot_app/views.py
from rest_framework import viewsets
from .models import Profile, Project
from .serializers import ProfileSerializer, ProjectSerializer
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import EmailMessage


@api_view(['POST'])
def send_email(request):
    data = request.data
    email = EmailMessage(
        subject="New Contact Form Submission",
        body=f"Message from {data['firstName']} {data['lastName']} ({data['email']}): {data['message']}",
        from_email='hayward.m.rob@gmail.com',
        to=['hayward.m.rob@gmail.com'],
        headers={'Reply-To': data['email']}
    )
    try:
        email.send()
        return Response({"message": "Email sent successfully"}, status=200)
    except Exception as e:
        return Response({"error": str(e)}, status=500)



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