import os
from .base import *
import logging


DEBUG = False

INTERNAL_IPS = [
    '127.0.0.1',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('POSTGRES_DB'),
        'USER': config('POSTGRES_USER'),
        'PASSWORD': config('POSTGRES_PASSWORD'),
        'PORT': '5432',
        'HOST': 'db_production',
    }
}

ADMINS = [('Admin', config('EMAIL_ADMIN'))]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = int(config('EMAIL_PORT'))
EMAIL_USE_TLS = config('EMAIL_USE_TLS') == 'True'
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

class MaskSensitiveData(logging.Filter):
    def __init__(self, sensitive_keys):
        super().__init__()
        self.sensitive_keys = sensitive_keys

    def filter(self, record):
        for key in self.sensitive_keys:
            value = os.getenv(key)
            if value and value in record.msg:
                record.msg = record.msg.replace(value, "***MASKED***")
        return True

SENSITIVE_KEYS = [
    "SECRET_KEY", "EMAIL_ADMIN", "EMAIL_HOST", "EMAIL_PORT", "EMAIL_USE_TLS",
    "EMAIL_HOST_USER", "EMAIL_HOST_PASSWORD", "POSTGRES_USER", "POSTGRES_PASSWORD",
    "POSTGRES_DB", "GF_SECURITY_ADMIN_PASSWORD", "ENVIRONMENT"
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        }
    },
    'filters': {
        "require_debug_false": {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        "mask_sensitive_data": {
            '()': MaskSensitiveData,
            'sensitive_keys': SENSITIVE_KEYS,
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'filters': ['mask_sensitive_data'],
            'formatter': 'simple',
        },
        'file': {
                'level': 'INFO',
                'class': 'logging.FileHandler',
                'filename': os.path.join(BASE_DIR, '../logs/clone.log'),
                'formatter': 'verbose',
            },
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler',
            },
    },

    'loggers': {
            'django': {
                'handlers': ['console', 'file', 'mail_admins'],
                'level': 'INFO',
                'propagate': True,
            },
            'django.request': {
                'handlers': ['mail_admins', 'file'],
                'level': 'ERROR',
                'propagate': False,
            },
            'clone': {
                'handlers': ['console', 'file'],
                'level': 'DEBUG',
                'propagate': False,
        },
    },
}

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '../media/')

CORS_ORIGIN_WHITELIST = ['https://app.example.com']
CSRF_TRUSTED_ORIGINS = ['https://app.example.com']
