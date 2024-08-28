# robrobot_backend/production.py
from .settings import *

DEBUG = False

ALLOWED_HOSTS = ['robhayward.io', 'www.robhayward.io', 'localhost', '127.0.0.1', 'backend', 'robrobot-backend.onrender.com']

CORS_ORIGIN_WHITELIST = [
    'http://robhayward.io',
    'https://robhayward.io',
    'http://www.robhayward.io',
    'https://www.robhayward.io',
    'http://localhost',
    'http://localhost:80',
    'https://robrobot-backend.onrender.com',
    'https://robrobot-frontend.onrender.com'
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Additional production-specific settings can go here
