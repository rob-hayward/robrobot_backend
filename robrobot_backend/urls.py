# robrobot_backend/urls.py

from django.contrib import admin
from django.urls import path, include
from robrobot_app.views import health_check, health_check_debug
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('robrobot_app.urls')),
    path('health/', health_check, name='health_check'),
    path('health_debug/', health_check_debug, name='health_check_debug'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
