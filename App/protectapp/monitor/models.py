
import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Modelo Usuario 
class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# Modelo para Dispositivos
class Dispositivo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) 
    nombre = models.CharField(max_length=80)
    modelo = models.CharField(max_length=80)
    estado = models.BooleanField(default=True)
    unique_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)  # Añadir este campo
    
    def __str__(self):
        return self.nombre

# Modelo para Llamadas
class Llamadas(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    numero = models.CharField(max_length=20)
    duracion = models.IntegerField()  # Duración en segundos
    fecha = models.DateField()
    hora = models.TimeField(default=timezone.now)
    tipo = models.CharField(max_length=10, choices=[('entrante', 'Entrante'), ('saliente', 'Saliente')])

    def __str__(self):
        return f"{self.numero} - {self.tipo}"

# Modelo para Mensajes
class Mensajes(models.Model):
    TIPO_CHOICES = [
        ('entrante', 'Entrante'),
        ('saliente', 'Saliente'),
    ]

    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    numero = models.CharField(max_length=15)
    contenido = models.TextField()
    fecha = models.DateField()
    hora = models.TimeField()
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)  # 'entrante' o 'saliente'

    def __str__(self):
        return f"Mensaje {self.tipo} del número {self.numero}"

# Modelo para Contactos
class Contactos(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=80)
    numero = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

# Modelo para Videos
class Videos(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    ruta_video = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f"Video grabado en {self.fecha}"

# Modelo para Ubicaciones
class Ubicaciones(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    latitud = models.FloatField()
    longitud = models.FloatField()
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f"Ubicación: {self.latitud}, {self.longitud} el {self.fecha}"

# Modelo para Grabaciones de Llamadas
class GrabacionesLlamadas(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    ruta_grabacion = models.CharField(max_length=255)
    duracion = models.IntegerField()  # En segundos
    fecha = models.DateField()
    hora = models.TimeField(default=timezone.now)
    archivo_audio = models.FileField(upload_to='llamadas/', default='llamadas/default.mp3')  # Definir un valor predeterminado

    def __str__(self):
        return f"Grabación de llamada del {self.fecha}"


# Modelo para Grabaciones de Pantalla
class GrabacionesPantalla(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    archivo_video = models.FileField(upload_to='grabaciones/pantalla/')  # Campo para el archivo de video
    fecha = models.DateField(auto_now_add=True)
    hora = models.TimeField(default=timezone.now)

    def __str__(self):
        return f"Grabación de pantalla del {self.fecha}"


# Modelo para Capturas de Pantalla
class CapturasPantalla(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    archivo_captura = models.ImageField(upload_to='capturas/pantalla/')  # Campo para la captura de pantalla
    fecha = models.DateField(auto_now_add=True)
    hora = models.TimeField(default=timezone.now)

    def __str__(self):
        return f"Captura de pantalla del {self.fecha}"


# modelos para Fotos
class Fotos(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    archivo_foto = models.ImageField(upload_to='fotos/', default='fotos/default.jpg')  
    fecha = models.DateField(auto_now_add=True)
    hora = models.TimeField(default=timezone.now)

    def __str__(self):
        return f"Foto del {self.fecha}"


# Modelo para Verificación de Permisos en Android
class VerificacionPermisos(models.Model):
    PERMISOS_ANDROID_CHOICES = [
        ('READ_CALENDAR', 'Calendario'),
        ('POST_NOTIFICATIONS', 'Notificaciones'),
        ('CAMERA', 'Cámara'),
        ('READ_CONTACTS', 'Leer Contactos'),
        ('RECORD_AUDIO', 'Grabar Audio'),
        ('READ_CALL_LOG', 'Registro de Llamadas'),
        ('READ_SMS', 'Leer SMS'),
        ('ACCESS_FINE_LOCATION', 'Ubicación Precisa'),
        ('READ_MEDIA_IMAGES', 'Fotos y Videos'),
        ('READ_MEDIA_AUDIO', 'Música y Audio'),
    ]
    
    permiso = models.CharField(max_length=100, choices=PERMISOS_ANDROID_CHOICES)
    estado_permiso = models.BooleanField()  # True = concedido, False = denegado
    fecha_verificacion = models.DateTimeField(default=timezone.now)
    dispositivo = models.ForeignKey('Dispositivo', on_delete=models.CASCADE)
    critico = models.BooleanField(default=False)  # Indica si el permiso es crítico para la app
    tipo_permiso = models.CharField(max_length=100, choices=PERMISOS_ANDROID_CHOICES, blank=True, null=True)

    def __str__(self):
        return f"{self.get_permiso_display()} - {'Concedido' if self.estado_permiso else 'Denegado'}"
    
    def get_instructions(self):
        """ Retorna instrucciones detalladas de cómo conceder manualmente el permiso basado en su tipo. """
        instructions = {
        'READ_CALENDAR': (
            "Para conceder acceso al calendario en la app Protect:\n"
            "1. Ve a Configuración en tu dispositivo.\n"
            "2. Selecciona 'Aplicaciones' o 'Administrar aplicaciones'.\n"
            "3. Busca y selecciona 'Protect'.\n"
            "4. Toca 'Permisos' y selecciona 'Calendario'.\n"
            "5. Cambia el permiso a 'Permitir'."
        ),
        'POST_NOTIFICATIONS': (
            "Para habilitar notificaciones de Protect:\n"
            "1. Ve a Configuración en tu dispositivo.\n"
            "2. Dirígete a 'Aplicaciones' y selecciona 'Protect'.\n"
            "3. Toca 'Notificaciones' y activa la opción para permitir notificaciones."
        ),
        'CAMERA': (
            "Para conceder acceso a la cámara en la app Protect:\n"
            "1. Ve a Configuración en tu dispositivo.\n"
            "2. Selecciona 'Aplicaciones' o 'Administrar aplicaciones'.\n"
            "3. Busca y selecciona 'Protect'.\n"
            "4. Toca 'Permisos' y selecciona 'Cámara'.\n"
            "5. Cambia el permiso a 'Permitir'."
        ),
        'READ_CONTACTS': (
            "Para conceder acceso a los contactos:\n"
            "1. Abre Configuración y dirígete a 'Aplicaciones'.\n"
            "2. Selecciona 'Protect'.\n"
            "3. Toca 'Permisos' y selecciona 'Contactos'.\n"
            "4. Activa el permiso."
        ),
        'RECORD_AUDIO': (
            "Para permitir la grabación de audio:\n"
            "1. Ve a Configuración en tu dispositivo.\n"
            "2. Selecciona 'Aplicaciones' y busca 'Protect'.\n"
            "3. Abre 'Permisos' y selecciona 'Micrófono'.\n"
            "4. Activa el permiso de micrófono."
        ),
        'READ_CALL_LOG': (
            "Para acceder al registro de llamadas:\n"
            "1. Abre Configuración en tu dispositivo.\n"
            "2. Selecciona 'Aplicaciones' y elige 'Protect'.\n"
            "3. Ve a 'Permisos' y activa 'Teléfono'."
        ),
        'READ_SMS': (
            "Para leer SMS en Protect:\n"
            "1. Dirígete a Configuración y selecciona 'Aplicaciones'.\n"
            "2. Toca 'Protect' y luego 'Permisos'.\n"
            "3. Activa el permiso para 'SMS'."
        ),
        'ACCESS_FINE_LOCATION': (
            "Para habilitar la ubicación precisa en Protect:\n"
            "1. Abre Configuración en tu dispositivo.\n"
            "2. Dirígete a 'Aplicaciones' y selecciona 'Protect'.\n"
            "3. Toca 'Permisos' y elige 'Ubicación'.\n"
            "4. Selecciona 'Permitir todo el tiempo' o 'Permitir solo mientras se usa la app'."
        ),
        'READ_MEDIA_IMAGES': (
            "Para conceder acceso a fotos y videos en Protect:\n"
            "1. Ve a Configuración en tu dispositivo.\n"
            "2. Selecciona 'Aplicaciones' y busca 'Protect'.\n"
            "3. Abre 'Permisos' y selecciona 'Fotos y videos'.\n"
            "4. Activa el permiso para acceder a fotos y videos."
        ),
        'READ_MEDIA_AUDIO': (
            "Para conceder acceso a música y audio en Protect:\n"
            "1. Abre Configuración y selecciona 'Aplicaciones'.\n"
            "2. Busca y selecciona 'Protect'.\n"
            "3. Toca 'Permisos' y selecciona 'Música y audio'.\n"
            "4. Activa el permiso para acceder a música y audio."
        ),
    }
        return instructions.get(self.tipo_permiso, "Por favor, concede este permiso manualmente en la configuración del dispositivo.")


# Modelo para Evento
class Evento(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    tipo_evento = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField(default=timezone.now)
    detalles = models.TextField(default='')

    def __str__(self):
        return f"Evento {self.tipo_evento} en {self.fecha} a las {self.hora}"

# Modelo para Historial de Eventos
class HistorialEvento(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    tipo_evento = models.CharField(max_length=100)
    fecha = models.DateField(default=timezone.now)
    hora = models.TimeField(default=timezone.now)
    detalles = models.TextField(blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Agrega este campo

    def __str__(self):
        return f"{self.tipo_evento} - {self.dispositivo.nombre}"

