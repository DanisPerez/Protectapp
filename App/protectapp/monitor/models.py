<<<<<<< HEAD

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Modelo Usuario (Extendiendo el modelo por defecto de Django si es necesario)
class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=100)
=======
from django.db import models
<<<<<<< HEAD
from django.contrib.auth.models import User
from django.utils import timezone
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 052f2d3b4d3ee496a9b96224faedb68f377a196d
>>>>>>> a8d19f143da4dcdf7a22fd08e935b212cf57580a
>>>>>>> b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
>>>>>>> b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
from django.contrib.auth.models import User  # Usar el modelo de usuario de Django
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6

# Modelo Dispositivo
class Dispositivo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Usar el modelo de Django
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======

# Modelo Usuario
class Usuario(models.Model):
    nombre = models.CharField(max_length=80)
    email = models.EmailField(unique=True, max_length=80)
    contraseña = models.CharField(max_length=80)
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470

    def __str__(self):
        return self.nombre

<<<<<<< HEAD
# Modelo para Dispositivos
class Dispositivo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
=======
# Modelo Dispositivo
class Dispositivo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
>>>>>>> d78f1636227f72ec3b372de20a52ae977a0beea7
>>>>>>> 052f2d3b4d3ee496a9b96224faedb68f377a196d
>>>>>>> a8d19f143da4dcdf7a22fd08e935b212cf57580a
>>>>>>> b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
>>>>>>> b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
    nombre = models.CharField(max_length=80)
    modelo = models.CharField(max_length=80)
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

<<<<<<< HEAD
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
    numero = models.CharField(max_length=20)
    contenido = models.TextField()
    fecha = models.DateField()
    hora = models.TimeField(default=timezone.now)
    tipo = models.CharField(max_length=10, choices=[('recibido', 'Recibido'), ('enviado', 'Enviado')])

    def __str__(self):
        return f"{self.numero} - {self.tipo}"

# Modelo para Contactos
class Contactos(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    numero = models.CharField(max_length=20)
=======
<<<<<<< HEAD

# Modelo Evento
class Evento(models.Model):
    descripcion = models.CharField(max_length=255)
    fecha = models.DateTimeField(auto_now_add=True)
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion


# modelos Llamadas
=======
# Modelo Llamadas
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
class Llamadas(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    numero = models.CharField(max_length=15)
    duracion = models.IntegerField()
    fecha = models.DateField()
    hora = models.TimeField()
<<<<<<< HEAD
    tipo = models.CharField(max_length=10)  # Entrante, Salida, Perdida
=======
    tipo = models.CharField(max_length=10)
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6

    def __str__(self):
        return f"Llamada al número {self.numero}"

<<<<<<< HEAD
# modelos Mensajes
=======
# Modelo Mensajes
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
class Mensajes(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    numero = models.CharField(max_length=15)
    contenido = models.TextField()
    fecha = models.DateField()
    hora = models.TimeField()
<<<<<<< HEAD
    tipo = models.CharField(max_length=10)  # Entrante o Salida
=======
    tipo = models.CharField(max_length=10)
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6

    def __str__(self):
        return f"Mensaje {self.tipo} del número {self.numero}"

<<<<<<< HEAD


=======
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
# Modelo Contactos
class Contactos(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=80)
    numero = models.CharField(max_length=15)
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470

    def __str__(self):
        return self.nombre

<<<<<<< HEAD
# Modelo para Fotos
class Fotos(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    ruta_foto = models.CharField(max_length=255)
    fecha = models.DateField()
    hora = models.TimeField(default=timezone.now)

    def __str__(self):
        return f"Foto tomada el {self.fecha} a las {self.hora}"

# Modelo para Videos
class Videos(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    ruta_video = models.CharField(max_length=255)
    fecha = models.DateField()
    hora = models.TimeField(default=timezone.now)

    def __str__(self):
        return f"Video grabado el {self.fecha} a las {self.hora}"

# Modelo para Ubicaciones
=======
<<<<<<< HEAD

# Modelo Fotos
class Fotos(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    ruta_foto = models.CharField(max_length=100)
=======
# Modelo Fotos
class Fotos(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
<<<<<<< HEAD
    ruta_foto = models.CharField(max_length=100)
=======
<<<<<<< HEAD
    ruta_foto = models.CharField(max_length=100)
=======
<<<<<<< HEAD
    ruta_foto = models.CharField(max_length=100)
=======
<<<<<<< HEAD
    ruta_foto = models.CharField(max_length=100)
=======
<<<<<<< HEAD
    ruta_foto = models.CharField(max_length=100)
=======
    ruta_foto = models.CharField(max_length=100)  # Ajuste de longitud
>>>>>>> d78f1636227f72ec3b372de20a52ae977a0beea7
>>>>>>> 052f2d3b4d3ee496a9b96224faedb68f377a196d
>>>>>>> a8d19f143da4dcdf7a22fd08e935b212cf57580a
>>>>>>> b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
>>>>>>> b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f"Foto tomada en {self.fecha}"

<<<<<<< HEAD

# Modelo Videos
class Videos(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    ruta_video = models.CharField(max_length=100)
=======
# Modelo Videos
class Videos(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
<<<<<<< HEAD
    ruta_video = models.CharField(max_length=100)
=======
<<<<<<< HEAD
    ruta_video = models.CharField(max_length=100)
=======
<<<<<<< HEAD
    ruta_video = models.CharField(max_length=100)
=======
<<<<<<< HEAD
    ruta_video = models.CharField(max_length=100)
=======
<<<<<<< HEAD
    ruta_video = models.CharField(max_length=100)
=======
    ruta_video = models.CharField(max_length=100)  # Ajuste de longitud
>>>>>>> d78f1636227f72ec3b372de20a52ae977a0beea7
>>>>>>> 052f2d3b4d3ee496a9b96224faedb68f377a196d
>>>>>>> a8d19f143da4dcdf7a22fd08e935b212cf57580a
>>>>>>> b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
>>>>>>> b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f"Video grabado en {self.fecha}"

<<<<<<< HEAD

=======
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
# Modelo Ubicaciones
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
class Ubicaciones(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    latitud = models.FloatField()
    longitud = models.FloatField()
    fecha = models.DateField()
<<<<<<< HEAD
    hora = models.TimeField(default=timezone.now)

    def __str__(self):
        return f"Ubicación registrada el {self.fecha} a las {self.hora}"

# Modelo para Grabaciones de Llamadas
class GrabacionesLlamadas(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    ruta_grabacion = models.CharField(max_length=255)
    duracion = models.IntegerField()  # En segundos
    fecha = models.DateField()
    hora = models.TimeField(default=timezone.now)

    def __str__(self):
        return f"Grabación de llamada del {self.fecha}"

# Modelo para Grabaciones de Pantalla
class GrabacionesPantalla(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    ruta_grabacion = models.CharField(max_length=255)
    fecha = models.DateField()
    hora = models.TimeField(default=timezone.now)

    def __str__(self):
        return f"Grabación de pantalla del {self.fecha}"

# Modelo para Capturas de Pantalla
class CapturasPantalla(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    ruta_captura = models.CharField(max_length=255)
    fecha = models.DateField()
    hora = models.TimeField(default=timezone.now)

    def __str__(self):
        return f"Captura de pantalla tomada el {self.fecha}"

# Modelo para Verificación de Permisos
=======
    hora = models.TimeField()

    def __str__(self):
        return f"Ubicación: {self.latitud}, {self.longitud} el {self.fecha}"

<<<<<<< HEAD

# Modelo Grabaciones de Llamadas
class GrabacionesLlamadas(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    ruta_grabacion = models.CharField(max_length=100)
=======
# Modelo Grabaciones de Llamadas
class GrabacionesLlamadas(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
<<<<<<< HEAD
    ruta_grabacion = models.CharField(max_length=100)
=======
<<<<<<< HEAD
    ruta_grabacion = models.CharField(max_length=100)
=======
<<<<<<< HEAD
    ruta_grabacion = models.CharField(max_length=100)
=======
<<<<<<< HEAD
    ruta_grabacion = models.CharField(max_length=100)
=======
<<<<<<< HEAD
    ruta_grabacion = models.CharField(max_length=100)
=======
    ruta_grabacion = models.CharField(max_length=100)  # Ajuste de longitud
>>>>>>> d78f1636227f72ec3b372de20a52ae977a0beea7
>>>>>>> 052f2d3b4d3ee496a9b96224faedb68f377a196d
>>>>>>> a8d19f143da4dcdf7a22fd08e935b212cf57580a
>>>>>>> b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
>>>>>>> b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
    duracion = models.IntegerField()
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f"Grabación de llamada en {self.fecha}"

<<<<<<< HEAD

# Modelo Grabaciones de Pantalla
class GrabacionesPantalla(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    ruta_grabacion = models.CharField(max_length=100)
=======
# Modelo Grabaciones de Pantalla
class GrabacionesPantalla(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
<<<<<<< HEAD
    ruta_grabacion = models.CharField(max_length=100)
=======
<<<<<<< HEAD
    ruta_grabacion = models.CharField(max_length=100)
=======
<<<<<<< HEAD
    ruta_grabacion = models.CharField(max_length=100)
=======
<<<<<<< HEAD
    ruta_grabacion = models.CharField(max_length=100)
=======
<<<<<<< HEAD
    ruta_grabacion = models.CharField(max_length=100)
=======
    ruta_grabacion = models.CharField(max_length=100)  # Ajuste de longitud
>>>>>>> d78f1636227f72ec3b372de20a52ae977a0beea7
>>>>>>> 052f2d3b4d3ee496a9b96224faedb68f377a196d
>>>>>>> a8d19f143da4dcdf7a22fd08e935b212cf57580a
>>>>>>> b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
>>>>>>> b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f"Grabación de pantalla en {self.fecha}"

<<<<<<< HEAD

# Modelo Capturas de Pantalla
class CapturasPantalla(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    ruta_captura = models.CharField(max_length=100)
=======
# Modelo Capturas de Pantalla
class CapturasPantalla(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
<<<<<<< HEAD
    ruta_captura = models.CharField(max_length=100)
=======
<<<<<<< HEAD
    ruta_captura = models.CharField(max_length=100)
=======
<<<<<<< HEAD
    ruta_captura = models.CharField(max_length=100)
=======
<<<<<<< HEAD
    ruta_captura = models.CharField(max_length=100)
=======
<<<<<<< HEAD
    ruta_captura = models.CharField(max_length=100)
=======
    ruta_captura = models.CharField(max_length=100)  # Ajuste de longitud
>>>>>>> d78f1636227f72ec3b372de20a52ae977a0beea7
>>>>>>> 052f2d3b4d3ee496a9b96224faedb68f377a196d
>>>>>>> a8d19f143da4dcdf7a22fd08e935b212cf57580a
>>>>>>> b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
>>>>>>> b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f"Captura de pantalla en {self.fecha}"

<<<<<<< HEAD

# Modelo Verificación de Permisos
class VerificacionPermisos(models.Model):
    permiso = models.CharField(max_length=100)
    estado = models.BooleanField()  # 1 = concedido, 0 = denegado
    fecha_verificacion = models.DateTimeField()
    dispositivo = models.ForeignKey('Dispositivo', on_delete=models.CASCADE)
    tipo_permiso = models.CharField(max_length=50, blank=True, null=True)  # Ej: 'Cámara', 'Ubicación'
    critico = models.BooleanField(default=False)  # Indica si el permiso es crítico
    clave_sistema = models.CharField(max_length=50, blank=True, null=True)  # Clave del SO, como 'CAMERA' o 'LOCATION'

    def __str__(self):
        return self.permiso


# Modelo HistorialEvento (Nuevo modelo que agregamos)

class HistorialEvento(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    tipo_evento = models.CharField(max_length=100)
    fecha = models.DateField(default=timezone.now)
    hora = models.TimeField(default=timezone.now)
    detalles = models.TextField(blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Agrega este campo

    def __str__(self):
        return f"{self.tipo_evento} - {self.dispositivo.nombre}"

=======
# Modelo Verificación de Permisos
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
class VerificacionPermisos(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    permiso = models.CharField(max_length=100)
    estado = models.BooleanField(default=False)
    fecha_verificacion = models.DateTimeField()

    def __str__(self):
<<<<<<< HEAD
        return f"Permiso {self.permiso} - {self.estado}"

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
    fecha = models.DateField()
    hora = models.TimeField(default=timezone.now)
    detalles = models.TextField(default='')

    def __str__(self):
        return f"Historial de evento {self.tipo_evento} en {self.fecha} a las {self.hora}"

=======
        return f"Permiso {self.permiso} verificado el {self.fecha_verificacion}"
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
