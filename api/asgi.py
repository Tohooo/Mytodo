"""
Experimental adapter to expose Django WSGI app as ASGI for Vercel serverless.
This uses asgiref.WsgiToAsgi to wrap the WSGI application. Success is not guaranteed
— Vercel's Python serverless environment has constraints (timeouts, cold starts,
database connections must be external, etc.). Use this only for testing.
"""
import os
from asgiref.wsgi import WsgiToAsgi

# Ensure DJANGO_SETTINGS_MODULE is set
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mytodo.settings')

from django.core.wsgi import get_wsgi_application

# Get the standard Django WSGI application
_wsgi_app = get_wsgi_application()

# Wrap WSGI app into ASGI
app = WsgiToAsgi(_wsgi_app)

# Vercel's Python runtime will try to use this module as an entrypoint.
# Exported name is `app` (ASGI application).
