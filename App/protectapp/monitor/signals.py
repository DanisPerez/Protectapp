from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Llamadas, Mensajes, Ubicaciones, HistorialEvento

# Cuando se crea una llamada
@receiver(post_save, sender=Llamadas)
def registrar_evento_llamada(sender, instance, created, **kwargs):
    if created:
        HistorialEvento.objects.create(
            dispositivo=instance.dispositivo,
            tipo_evento='Llamada',
            fecha=instance.fecha,
            hora=instance.hora,
            detalles=f"Llamada al número {instance.numero}, duración: {instance.duracion} segundos"
        )

# Cuando se crea un mensaje
@receiver(post_save, sender=Mensajes)
def registrar_evento_mensaje(sender, instance, created, **kwargs):
    if created:
        HistorialEvento.objects.create(
            dispositivo=instance.dispositivo,
            tipo_evento='Mensaje',
            fecha=instance.fecha,
            hora=instance.hora,
            detalles=f"Mensaje del número {instance.numero}: {instance.contenido}"
        )