
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
    
    def get_instructions(self):
        """ Retorna instrucciones detalladas de cómo conceder manualmente el permiso basado en su tipo. """
        instructions = {
            'CAMERA': (
                "Para conceder acceso a la cámara en la app Protect:\n"
                "1. Ve a Configuración en tu dispositivo.\n"
                "2. Selecciona 'Aplicaciones' o 'Administrar aplicaciones'.\n"
                "3. Busca y selecciona 'Protect'.\n"
                "4. Toca 'Permisos' y selecciona 'Cámara'.\n"
                "5. Cambia el permiso a 'Permitir'."
            ),
            'ACCESS_FINE_LOCATION': (
                "Para habilitar la ubicación precisa en Protect:\n"
                "1. Abre Configuración en tu dispositivo.\n"
                "2. Dirígete a 'Aplicaciones' y selecciona 'Protect'.\n"
                "3. Toca 'Permisos' y elige 'Ubicación'.\n"
                "4. Selecciona 'Permitir todo el tiempo' o 'Permitir solo mientras se usa la app'."
            ),
            'ACCESS_COARSE_LOCATION': (
                "Para habilitar la ubicación aproximada en Protect:\n"
                "1. Ve a Configuración y abre 'Aplicaciones'.\n"
                "2. Selecciona 'Protect' y luego 'Permisos'.\n"
                "3. Toca 'Ubicación' y selecciona 'Permitir'."
            ),
            'READ_CONTACTS': (
                "Para conceder acceso a los contactos:\n"
                "1. Abre Configuración y dirígete a 'Aplicaciones'.\n"
                "2. Selecciona 'Protect'.\n"
                "3. Toca 'Permisos' y selecciona 'Contactos'.\n"
                "4. Activa el permiso."
            ),
            'WRITE_CONTACTS': (
                "Para permitir modificar los contactos en Protect:\n"
                "1. Abre Configuración y selecciona 'Aplicaciones'.\n"
                "2. Toca en 'Protect' y ve a 'Permisos'.\n"
                "3. Selecciona 'Contactos' y asegúrate de que esté activado."
            ),
            'RECORD_AUDIO': (
                "Para permitir la grabación de audio:\n"
                "1. Ve a Configuración en tu dispositivo.\n"
                "2. Selecciona 'Aplicaciones' y busca 'Protect'.\n"
                "3. Abre 'Permisos' y selecciona 'Micrófono'.\n"
                "4. Activa el permiso de micrófono."
            ),
            'READ_EXTERNAL_STORAGE': (
                "Para leer el almacenamiento externo:\n"
                "1. Abre Configuración y ve a 'Aplicaciones'.\n"
                "2. Selecciona 'Protect' y luego 'Permisos'.\n"
                "3. Activa 'Almacenamiento'."
            ),
            'WRITE_EXTERNAL_STORAGE': (
                "Para escribir en el almacenamiento externo:\n"
                "1. Ve a Configuración y selecciona 'Aplicaciones'.\n"
                "2. Busca 'Protect' y toca 'Permisos'.\n"
                "3. Activa 'Almacenamiento'."
            ),
            'CALL_LOG': (
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
            'SEND_SMS': (
                "Para enviar SMS a través de Protect:\n"
                "1. Abre Configuración y ve a 'Aplicaciones'.\n"
                "2. Selecciona 'Protect', luego 'Permisos'.\n"
                "3. Activa el permiso para 'SMS'."
            ),
            'READ_PHONE_STATE': (
                "Para acceder al estado del teléfono:\n"
                "1. Ve a Configuración y selecciona 'Aplicaciones'.\n"
                "2. Abre 'Protect' y toca en 'Permisos'.\n"
                "3. Activa 'Teléfono'."
            ),
            'BLUETOOTH': (
                "Para usar Bluetooth en Protect:\n"
                "1. Abre Configuración en tu dispositivo.\n"
                "2. Ve a 'Aplicaciones' y selecciona 'Protect'.\n"
                "3. Abre 'Permisos' y asegúrate de que Bluetooth esté activado en la configuración general."
            ),
            'NOTIFICATIONS': (
                "Para habilitar notificaciones:\n"
                "1. Dirígete a Configuración y abre 'Notificaciones'.\n"
                "2. Selecciona 'Protect' y activa las notificaciones."
            ),
            'FOREGROUND_SERVICE': (
                "Este permiso se gestiona automáticamente al iniciar un servicio en primer plano en Protect.\n"
                "No se requiere configuración adicional."
            ),
            'BACKGROUND_LOCATION': (
                "Para usar la ubicación en segundo plano:\n"
                "1. Abre Configuración y ve a 'Aplicaciones'.\n"
                "2. Selecciona 'Protect' y activa 'Ubicación' como 'Permitir todo el tiempo'."
            ),
            'ACCESS_WIFI_STATE': (
                "Para ver el estado del Wi-Fi:\n"
                "1. Abre Configuración y dirígete a 'Aplicaciones'.\n"
                "2. Selecciona 'Protect' y asegúrate de que el Wi-Fi esté activado en configuración general."
            ),
            'MODIFY_AUDIO_SETTINGS': (
                "Para modificar configuraciones de audio:\n"
                "1. Ve a Configuración > Aplicaciones.\n"
                "2. Selecciona 'Protect' y revisa 'Permisos'.\n"
                "3. Asegúrate de que el dispositivo permita ajustar el audio para esta app."
            ),
            'VIBRATE': (
                "Para controlar la vibración:\n"
                "1. Asegúrate de que las notificaciones y el control de vibración estén habilitados en Configuración > Sonido.\n"
                "2. La aplicación no necesita permisos adicionales específicos para esta función."
            ),
            'INTERNET': (
                "El permiso de Internet está habilitado automáticamente para Protect cuando se conecta a redes.\n"
                "No se requieren pasos adicionales para configurar este permiso."
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

