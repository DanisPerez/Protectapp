<<<<<<< HEAD
# protectapp/asgi.py
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from monitor import routing  # Importa routing desde tu aplicación "monitor"

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'protectapp.settings')  # Asegúrate de usar el nombre correcto del proyecto

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    ),
})
=======
"""
ASGI config for protectapp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'protectapp.settings')

application = get_asgi_application()
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
