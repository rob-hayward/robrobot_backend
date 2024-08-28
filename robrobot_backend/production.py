# robrobot_backend/production.py
from .settings import *

DEBUG = False

ALLOWED_HOSTS = ['robhayward.io', 'www.robhayward.io', 'localhost', '127.0.0.1', 'robrobot-backend.onrender.com']

CORS_ORIGIN_WHITELIST = [
    'https://robhayward.io',
    'https://www.robhayward.io',
    'https://robrobot-frontend.onrender.com'
]

CORS_ALLOW_CREDENTIALS = True

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Additional production-specific settings can go here
