# robrobot_backend/wsgi.py

import os

from django.core.wsgi import get_wsgi_application

settings_module = 'robrobot_backend.production' if os.getenv('DJANGO_SETTINGS_MODULE') else 'robrobot_backend.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_wsgi_application()