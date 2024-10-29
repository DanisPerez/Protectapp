
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
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    numero = models.CharField(max_length=15)
    contenido = models.TextField()
    fecha = models.DateField()
    hora = models.TimeField()
    tipo = models.CharField(max_length=10)  # Entrante o Salida

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
        ('CAMERA', 'Cámara'),
        ('ACCESS_FINE_LOCATION', 'Ubicación Precisa'),
        ('ACCESS_COARSE_LOCATION', 'Ubicación Aproximada'),
        ('READ_CONTACTS', 'Leer Contactos'),
        ('WRITE_CONTACTS', 'Modificar Contactos'),
        ('RECORD_AUDIO', 'Grabar Audio'),
        ('READ_EXTERNAL_STORAGE', 'Leer Almacenamiento Externo'),
        ('WRITE_EXTERNAL_STORAGE', 'Escribir en Almacenamiento Externo'),
        ('CALL_LOG', 'Registro de Llamadas'),
        ('READ_SMS', 'Leer SMS'),
        ('SEND_SMS', 'Enviar SMS'),
        ('READ_PHONE_STATE', 'Estado del Teléfono'),
        ('BLUETOOTH', 'Bluetooth'),
        ('NOTIFICATIONS', 'Notificaciones'),
        ('INTERNET', 'Acceso a Internet'),
        ('FOREGROUND_SERVICE', 'Servicio en Primer Plano'),
        ('BACKGROUND_LOCATION', 'Ubicación en Segundo Plano'),
        ('ACCESS_WIFI_STATE', 'Estado del Wi-Fi'),
        ('MODIFY_AUDIO_SETTINGS', 'Modificar Configuración de Audio'),
        ('VIBRATE', 'Controlar Vibración'),
    ]
    
    permiso = models.CharField(max_length=100)  # Nombre del permiso (ej: 'Acceso a cámara')
    estado_permiso = models.BooleanField()  # 1 = concedido, 0 = denegado
    fecha_verificacion = models.DateTimeField(auto_now_add=True)  # Registrar automáticamente la fecha de creación
    dispositivo = models.ForeignKey('Dispositivo', on_delete=models.CASCADE)
    tipo_permiso = models.CharField(max_length=50, choices=PERMISOS_ANDROID_CHOICES, blank=True, null=True)  # Lista de permisos Android
    critico = models.BooleanField(default=False)  # Indica si el permiso es crítico para la app
    clave_sistema = models.CharField(max_length=50, blank=True, null=True)  # Clave interna del sistema operativo

    def __str__(self):
        return f"{self.permiso} - {'Concedido' if self.estado_permiso else 'Denegado'}"

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

