"""
ASGI config for online_book_sharing_system project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
import django
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import mainapp.routing

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'online_book_sharing_system.settings')
django.setup()


application = ProtocolTypeRouter({
    "http":  get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            mainapp.routing.websocket_urlpatterns
        ),
    ),
})
