# monitor/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class EventoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()  # Acepta la conexión WebSocket

    async def disconnect(self, close_code):
        pass  # Aquí puedes manejar la lógica de desconexión, si es necesario

    async def receive(self, text_data):
        # Método para recibir mensajes del cliente si es necesario
        pass

    # Método para enviar un nuevo evento a la conexión WebSocket
    async def enviar_evento(self, event):
        await self.send(text_data=json.dumps({
            'evento': event['evento'],
        }))
