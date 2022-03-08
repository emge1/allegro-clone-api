import os
from django.core.wsgi import get_wsgi_application
from django import setup

from config.environment import DJANGO_SETTINGS_MODULE

os.environ.setdefault('DJANGO_SETTINGS_MODULE', DJANGO_SETTINGS_MODULE)
setup()

application = get_wsgi_application()
