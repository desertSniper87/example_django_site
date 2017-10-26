"""
WSGI config for example_django_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "example_django_site.settings")

# pylint: disable=invalid-name
application = get_wsgi_application()
application = DjangoWhiteNoise(application)
