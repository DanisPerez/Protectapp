# monitor/routing.py
from django.urls import path
from . import consumers  # Asegúrate de tener un archivo consumers.py en monitor

websocket_urlpatterns = [
    path('ws/eventos/', consumers.EventoConsumer.as_asgi()),
]
