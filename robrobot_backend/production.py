# robrobot_backend/production.py
from .settings import *  # Import base settings

DEBUG = False

ALLOWED_HOSTS = ['robrobot-loadbalancer-980562543.eu-west-2.elb.amazonaws.com']  # Replace with your load balancer URL

CORS_ORIGIN_WHITELIST = [
    'http://robrobot-loadbalancer-980562543.eu-west-2.elb.amazonaws.com',  # Replace with your load balancer URL
]

# Static file settings for production
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Add any other production-specific settings here