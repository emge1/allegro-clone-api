import os
from django.core.asgi import get_asgi_application
from django import setup

from config.environment import DJANGO_SETTINGS_MODULE

os.environ.setdefault('DJANGO_SETTINGS_MODULE', DJANGO_SETTINGS_MODULE)
setup()

application = get_asgi_application()
