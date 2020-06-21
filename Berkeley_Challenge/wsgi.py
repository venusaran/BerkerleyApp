"""
    WSGI config for Berkeley_Challenge project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Berkeley_Challenge.settings')

application = get_wsgi_application()
