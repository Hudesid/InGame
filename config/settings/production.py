from .base import *

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

CSRF_TRUSTED_ORIGINS = env.list('CSRF_TRUSTED_ORIGINS')
CORS_ALLOWED_ORIGINS = env.list('CORS_ALLOWED_ORIGINS')

DEBUG = False

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 60 * 60 * 24 * 7 * 52
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOW_CREDENTIALS = False
CORS_ORIGIN_ALLOW_ALL = False
