# production.py
from .settings import *

DEBUG = True  # False for production, True for development

ALLOWED_HOSTS = ['robrobot-loadbalancer-980562543.eu-west-2.elb.amazonaws.com', 'localhost', '127.0.0.1', 'backend']

CORS_ORIGIN_WHITELIST = [
    'http://robrobot-loadbalancer-980562543.eu-west-2.elb.amazonaws.com',
    'http://localhost',
    'http://localhost:80',
]

# Static file settings for production
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Add any other production-specific settings here
