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
<<<<<<< HEAD
        )
=======
<<<<<<< HEAD
        )
=======
        )
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
>>>>>>> 7c9c8fce799681b798ac83cabdaf1af962be551a
