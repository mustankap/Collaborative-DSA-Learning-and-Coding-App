"""
ASGI config for multiapp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

import chat.routing
from django.conf.urls import url
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

# from channels.asgi import get_channel_layer


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "multiapp.settings")

# application = get_asgi_application()
# channel_layer = get_channel_layer()
application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(
            # URLRouter(board.routing.websocket_urlpatterns)
            URLRouter(chat.routing.websocket_urlpatterns)
        ),
    }
)
