from .base import *

ALLOWED_HOSTS = ['*']

DEBUG = True

INTERNAL_IPS = ["127.0.0.1"]

INSTALLED_APPS += ["debug_toolbar", 'drf_yasg']

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']

REST_FRAMEWORK.update({
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ]
})

SWAGGER_SETTINGS = {
    "SECURITY_DEFINITIONS": {
        "[Bearer {JWT}]": {
            "name": "Authorization",
            "type": "apiKey",
            "in": "header",
        }
    },
    "USE_SESSION_AUTH": False,
    "SUPPORTED_SUBMIT_METHODS": ["get", "post", "put", "delete", "patch"],
}
