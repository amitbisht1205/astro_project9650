"""
WSGI config for astro_project9650 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application
sys.path.append('/path/to/your/astro_project9650')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'astro_project9650.settings')

application = get_wsgi_application()
