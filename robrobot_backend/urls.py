# robrobot_backend/urls.py
from django.contrib import admin
from django.urls import path, include
from robrobot_app.views import health_check

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('robrobot_app.urls')),
    path('health/', health_check, name='health_check'),
]
