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
