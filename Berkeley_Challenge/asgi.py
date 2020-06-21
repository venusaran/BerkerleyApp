"""
    ASGI config for Berkeley_Challenge project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Berkeley_Challenge.settings')

application = get_asgi_application()
