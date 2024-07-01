# robrobot_backend/production.py
from .settings import *

DEBUG = False

ALLOWED_HOSTS = ['robhayward.io', 'www.robhayward.io', 'robrobot-loadbalancer-980562543.eu-west-2.elb.amazonaws.com', 'localhost', '127.0.0.1', 'backend']

CORS_ORIGIN_WHITELIST = [
    'http://robhayward.io',
    'https://robhayward.io',
    'http://www.robhayward.io',
    'https://www.robhayward.io',
    'http://localhost',
    'http://localhost:80',
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Additional production-specific settings can go here
