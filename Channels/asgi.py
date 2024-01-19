"""
ASGI config for Channels project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Channels.settings')

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter

django_asgi_applictaion=get_asgi_application()

from channels.auth import AuthMiddleware
import navbat.routing
from channels.auth import AuthMiddlewareStack


application = ProtocolTypeRouter({
    "http": django_asgi_applictaion,
    "websocket": AuthMiddlewareStack(
        URLRouter(
            navbat.routing.websocket_urlpatterns
        )
    )
})





