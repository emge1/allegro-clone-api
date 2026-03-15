import os
from .base import *
import logging


DEBUG = False

INTERNAL_IPS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('POSTGRES_DB'),
        'USER': config('POSTGRES_USER'),
        'PASSWORD': config('POSTGRES_PASSWORD'),
        'PORT': config('DB_PORT'),
        'HOST': config('DB_HOST'),
        'OPTIONS': {
            'sslmode': 'require'
        }
    }
}

ADMINS = [('Admin', config('EMAIL_ADMIN'))]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = int(config('EMAIL_PORT'))
EMAIL_USE_TLS = config("EMAIL_USE_TLS", cast=bool, default=True)
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
    "version": 1,
    "disable_existing_loggers": False,

    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {name} {module} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
    },

    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
        "mask_sensitive_data": {
            "()": MaskSensitiveData,
            "sensitive_keys": SENSITIVE_KEYS,
        },
    },

    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "simple",
            "filters": ["mask_sensitive_data"],
        },

        "mail_admins": {
            "class": "django.utils.log.AdminEmailHandler",
            "level": "ERROR",
            "filters": ["require_debug_false"],
        },
    },

    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },

    "loggers": {
        "django": {
            "handlers": ["console", "mail_admins"],
            "level": "INFO",
            "propagate": True,
        },

        "django.request": {
            "handlers": ["console", "mail_admins"],
            "level": "ERROR",
            "propagate": False,
        },

        "clone": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}

MIDDLEWARE.append('v1.middleware.metrics.PrometheusMetricsMiddleware',)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '../media/')

CSRF_TRUSTED_ORIGINS = config(
    "CSRF_TRUSTED_ORIGINS",
    cast=Csv(),
    default="",
)

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
USE_X_FORWARDED_HOST = True

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SECURE_REDIRECT_EXEMPT = [r"^healthz$", r"^readyz$"]

