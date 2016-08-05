"""
WSGI config for tiku_demo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys

dir = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, dir)

os.environ['PYTHON_EGG_CACHE'] = '/var/www/.python-eggs'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tiku_demo.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
