"""
WSGI config for server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

settings = "server.settings.dev" if os.environ['DJ_DB_HOST'] == 'localhost' else "server.settings.prod"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings)

application = get_wsgi_application()
