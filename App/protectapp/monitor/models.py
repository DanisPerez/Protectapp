<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 7c9c8fce799681b798ac83cabdaf1af962be551a
<<<<<<< HEAD
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
=======
=======
>>>>>>> 8e18bd6d3b44f892c4e048fb7e4e553c2d8fe619
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
>>>>>>> b5ca5ef48d2ae9ff505b8711631613fc593d45d5
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

<<<<<<< HEAD
# Modelo Usuario 
=======
<<<<<<< HEAD
# Modelo Usuario 
=======
<<<<<<< HEAD
# Modelo Usuario 
=======
<<<<<<< HEAD
<<<<<<< HEAD
# Modelo Usuario 
=======
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
<<<<<<< HEAD
# Modelo Usuario 
=======
# Modelo Usuario (Extendiendo el modelo por defecto de Django si es necesario)
>>>>>>> 7c9c8fce799681b798ac83cabdaf1af962be551a
<<<<<<< HEAD
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
=======
=======
# Modelo Usuario (Extendiendo el modelo por defecto de Django si es necesario)
>>>>>>> 8e18bd6d3b44f892c4e048fb7e4e553c2d8fe619
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
>>>>>>> b5ca5ef48d2ae9ff505b8711631613fc593d45d5
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=100)
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 8e18bd6d3b44f892c4e048fb7e4e553c2d8fe619
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
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
<<<<<<< HEAD
>>>>>>> 7c9c8fce799681b798ac83cabdaf1af962be551a
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
=======
<<<<<<< HEAD
>>>>>>> 7c9c8fce799681b798ac83cabdaf1af962be551a
=======
>>>>>>> 8e18bd6d3b44f892c4e048fb7e4e553c2d8fe619
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
>>>>>>> b5ca5ef48d2ae9ff505b8711631613fc593d45d5
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f

    def __str__(self):
        return self.nombre

<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
>>>>>>> b5ca5ef48d2ae9ff505b8711631613fc593d45d5
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
# Modelo para Dispositivos
class Dispositivo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) 
    nombre = models.CharField(max_length=80)
    modelo = models.CharField(max_length=80)
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
# Modelo para Dispositivos
class Dispositivo(models.Model):
<<<<<<< HEAD
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) 
    nombre = models.CharField(max_length=80)
    modelo = models.CharField(max_length=80)
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
=======
<<<<<<< HEAD
# Modelo para Dispositivos
class Dispositivo(models.Model):
<<<<<<< HEAD
=======
=======
>>>>>>> 8e18bd6d3b44f892c4e048fb7e4e553c2d8fe619
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
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
<<<<<<< HEAD
>>>>>>> 7c9c8fce799681b798ac83cabdaf1af962be551a
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
=======
<<<<<<< HEAD
>>>>>>> 7c9c8fce799681b798ac83cabdaf1af962be551a
=======
>>>>>>> 8e18bd6d3b44f892c4e048fb7e4e553c2d8fe619
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
>>>>>>> b5ca5ef48d2ae9ff505b8711631613fc593d45d5
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 7c9c8fce799681b798ac83cabdaf1af962be551a
<<<<<<< HEAD
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
=======
=======
>>>>>>> 8e18bd6d3b44f892c4e048fb7e4e553c2d8fe619
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
>>>>>>> b5ca5ef48d2ae9ff505b8711631613fc593d45d5
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
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
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
=======
<<<<<<< HEAD
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
>>>>>>> b5ca5ef48d2ae9ff505b8711631613fc593d45d5
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
    numero = models.CharField(max_length=15)
    contenido = models.TextField()
    fecha = models.DateField()
    hora = models.TimeField()
    tipo = models.CharField(max_length=10)  # Entrante o Salida

    def __str__(self):
        return f"Mensaje {self.tipo} del número {self.numero}"
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
=======
=======
=======
>>>>>>> 8e18bd6d3b44f892c4e048fb7e4e553c2d8fe619
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
    numero = models.CharField(max_length=20)
    contenido = models.TextField()
    fecha = models.DateField()
    hora = models.TimeField(default=timezone.now)
    tipo = models.CharField(max_length=10, choices=[('recibido', 'Recibido'), ('enviado', 'Enviado')])

    def __str__(self):
        return f"{self.numero} - {self.tipo}"
<<<<<<< HEAD
>>>>>>> 7c9c8fce799681b798ac83cabdaf1af962be551a
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
=======
<<<<<<< HEAD
>>>>>>> 7c9c8fce799681b798ac83cabdaf1af962be551a
=======
>>>>>>> 8e18bd6d3b44f892c4e048fb7e4e553c2d8fe619
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
>>>>>>> b5ca5ef48d2ae9ff505b8711631613fc593d45d5
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f

# Modelo para Contactos
class Contactos(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
<<<<<<< HEAD
    nombre = models.CharField(max_length=80)
    numero = models.CharField(max_length=15)
=======
<<<<<<< HEAD
    nombre = models.CharField(max_length=80)
    numero = models.CharField(max_length=15)
=======
<<<<<<< HEAD
    nombre = models.CharField(max_length=80)
    numero = models.CharField(max_length=15)
=======
<<<<<<< HEAD
<<<<<<< HEAD
    nombre = models.CharField(max_length=80)
    numero = models.CharField(max_length=15)
=======
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
<<<<<<< HEAD
    nombre = models.CharField(max_length=80)
    numero = models.CharField(max_length=15)
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 8e18bd6d3b44f892c4e048fb7e4e553c2d8fe619
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
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
<<<<<<< HEAD
>>>>>>> 7c9c8fce799681b798ac83cabdaf1af962be551a
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
=======
<<<<<<< HEAD
>>>>>>> 7c9c8fce799681b798ac83cabdaf1af962be551a
=======
>>>>>>> 8e18bd6d3b44f892c4e048fb7e4e553c2d8fe619
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
>>>>>>> b5ca5ef48d2ae9ff505b8711631613fc593d45d5
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f

    def __str__(self):
        return self.nombre

<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
# Modelo para Fotos
class Fotos(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
=======
# Modelo para Fotos
class Fotos(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
<<<<<<< HEAD
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
    ruta_foto = models.CharField(max_length=100)
=======
<<<<<<< HEAD
# Modelo para Fotos
class Fotos(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
<<<<<<< HEAD
=======
=======
>>>>>>> 8e18bd6d3b44f892c4e048fb7e4e553c2d8fe619
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
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
<<<<<<< HEAD
>>>>>>> 7c9c8fce799681b798ac83cabdaf1af962be551a
=======
<<<<<<< HEAD
>>>>>>> 7c9c8fce799681b798ac83cabdaf1af962be551a
=======
>>>>>>> 8e18bd6d3b44f892c4e048fb7e4e553c2d8fe619
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f"Foto tomada en {self.fecha}"

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
=======
<<<<<<< HEAD
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
>>>>>>> b5ca5ef48d2ae9ff505b8711631613fc593d45d5
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
# Modelo para Videos
class Videos(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    ruta_video = models.CharField(max_length=100)
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
<<<<<<< HEAD
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 8e18bd6d3b44f892c4e048fb7e4e553c2d8fe619
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29

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
<<<<<<< HEAD
>>>>>>> 7c9c8fce799681b798ac83cabdaf1af962be551a
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
=======
<<<<<<< HEAD
>>>>>>> 7c9c8fce799681b798ac83cabdaf1af962be551a
=======
>>>>>>> 8e18bd6d3b44f892c4e048fb7e4e553c2d8fe619
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
>>>>>>> b5ca5ef48d2ae9ff505b8711631613fc593d45d5
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f"Video grabado en {self.fecha}"

<<<<<<< HEAD
# Modelo para Ubicaciones
=======
<<<<<<< HEAD
# Modelo para Ubicaciones
=======
<<<<<<< HEAD
# Modelo para Ubicaciones
=======
<<<<<<< HEAD
<<<<<<< HEAD
# Modelo para Ubicaciones
=======
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
<<<<<<< HEAD
# Modelo para Ubicaciones
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 8e18bd6d3b44f892c4e048fb7e4e553c2d8fe619
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29

=======
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
# Modelo Ubicaciones
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
<<<<<<< HEAD
>>>>>>> 7c9c8fce799681b798ac83cabdaf1af962be551a
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
=======
<<<<<<< HEAD
>>>>>>> 7c9c8fce799681b798ac83cabdaf1af962be551a
=======
>>>>>>> 8e18bd6d3b44f892c4e048fb7e4e553c2d8fe619
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
>>>>>>> b5ca5ef48d2ae9ff505b8711631613fc593d45d5
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
class Ubicaciones(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    latitud = models.FloatField()
    longitud = models.FloatField()
    fecha = models.DateField()
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
=======
<<<<<<< HEAD
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
>>>>>>> b5ca5ef48d2ae9ff505b8711631613fc593d45d5
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
    hora = models.TimeField()

    def __str__(self):
        return f"Ubicación: {self.latitud}, {self.longitud} el {self.fecha}"
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
<<<<<<< HEAD
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 8e18bd6d3b44f892c4e048fb7e4e553c2d8fe619
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
    hora = models.TimeField(default=timezone.now)

    def __str__(self):
        return f"Ubicación registrada el {self.fecha} a las {self.hora}"
<<<<<<< HEAD
>>>>>>> 7c9c8fce799681b798ac83cabdaf1af962be551a
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
=======
<<<<<<< HEAD
>>>>>>> 7c9c8fce799681b798ac83cabdaf1af962be551a
=======
>>>>>>> 8e18bd6d3b44f892c4e048fb7e4e553c2d8fe619
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
>>>>>>> b5ca5ef48d2ae9ff505b8711631613fc593d45d5
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f

# Modelo para Grabaciones de Llamadas
class GrabacionesLlamadas(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    ruta_grabacion = models.CharField(max_length=255)
    duracion = models.IntegerField()  # En segundos
    fecha = models.DateField()
    hora = models.TimeField(default=timezone.now)
<<<<<<< HEAD
    archivo_audio = models.FileField(upload_to='llamadas/', default='llamadas/default.mp3')  # Definir un valor predeterminado
=======
<<<<<<< HEAD
    archivo_audio = models.FileField(upload_to='llamadas/', default='llamadas/default.mp3')  # Definir un valor predeterminado
=======
<<<<<<< HEAD
    archivo_audio = models.FileField(upload_to='llamadas/', default='llamadas/default.mp3')  # Definir un valor predeterminado
=======
<<<<<<< HEAD
<<<<<<< HEAD
    archivo_audio = models.FileField(upload_to='llamadas/', default='llamadas/default.mp3')  # Definir un valor predeterminado
=======
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
>>>>>>> b5ca5ef48d2ae9ff505b8711631613fc593d45d5
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f

    def __str__(self):
        return f"Grabación de llamada del {self.fecha}"

<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b5ca5ef48d2ae9ff505b8711631613fc593d45d5
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f

# Modelo para Grabaciones de Pantalla
class GrabacionesPantalla(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    archivo_video = models.FileField(upload_to='grabaciones/pantalla/')  # Campo para el archivo de video
    fecha = models.DateField(auto_now_add=True)
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
# Modelo para Grabaciones de Pantalla
class GrabacionesPantalla(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    ruta_grabacion = models.CharField(max_length=255)
    fecha = models.DateField()
<<<<<<< HEAD
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
>>>>>>> b5ca5ef48d2ae9ff505b8711631613fc593d45d5
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
    hora = models.TimeField(default=timezone.now)

    def __str__(self):
        return f"Grabación de pantalla del {self.fecha}"

<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b5ca5ef48d2ae9ff505b8711631613fc593d45d5
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f

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
<<<<<<< HEAD
    
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


=======

<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
# Modelo para Capturas de Pantalla
class CapturasPantalla(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
<<<<<<< HEAD
    ruta_captura = models.CharField(max_length=100)
=======
=======
# Modelo para Capturas de Pantalla
class CapturasPantalla(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
<<<<<<< HEAD
<<<<<<< HEAD
    ruta_captura = models.CharField(max_length=100)
=======
=======
>>>>>>> 8e18bd6d3b44f892c4e048fb7e4e553c2d8fe619
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
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
<<<<<<< HEAD
>>>>>>> 7c9c8fce799681b798ac83cabdaf1af962be551a
=======
<<<<<<< HEAD
>>>>>>> 7c9c8fce799681b798ac83cabdaf1af962be551a
=======
>>>>>>> 8e18bd6d3b44f892c4e048fb7e4e553c2d8fe619
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f"Captura de pantalla en {self.fecha}"

<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
# Modelo para Verificación de Permisos
=======
<<<<<<< HEAD

# Modelo Verificación de Permisos
>>>>>>> 7c9c8fce799681b798ac83cabdaf1af962be551a
<<<<<<< HEAD
=======
=======

# Modelo Verificación de Permisos
>>>>>>> 8e18bd6d3b44f892c4e048fb7e4e553c2d8fe619
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
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

<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 8e18bd6d3b44f892c4e048fb7e4e553c2d8fe619
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29

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

<<<<<<< HEAD
>>>>>>> 7c9c8fce799681b798ac83cabdaf1af962be551a
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
=======
<<<<<<< HEAD
>>>>>>> 7c9c8fce799681b798ac83cabdaf1af962be551a
=======
>>>>>>> 8e18bd6d3b44f892c4e048fb7e4e553c2d8fe619
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
>>>>>>> b5ca5ef48d2ae9ff505b8711631613fc593d45d5
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
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
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
=======
<<<<<<< HEAD
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
>>>>>>> b5ca5ef48d2ae9ff505b8711631613fc593d45d5
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
    fecha = models.DateField(default=timezone.now)
    hora = models.TimeField(default=timezone.now)
    detalles = models.TextField(blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Agrega este campo

    def __str__(self):
        return f"{self.tipo_evento} - {self.dispositivo.nombre}"

<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
=======
=======
=======
>>>>>>> 8e18bd6d3b44f892c4e048fb7e4e553c2d8fe619
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
    fecha = models.DateField()
    hora = models.TimeField(default=timezone.now)
    detalles = models.TextField(default='')

    def __str__(self):
        return f"Historial de evento {self.tipo_evento} en {self.fecha} a las {self.hora}"

=======
        return f"Permiso {self.permiso} verificado el {self.fecha_verificacion}"
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
<<<<<<< HEAD
>>>>>>> 7c9c8fce799681b798ac83cabdaf1af962be551a
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
=======
<<<<<<< HEAD
>>>>>>> 7c9c8fce799681b798ac83cabdaf1af962be551a
=======
>>>>>>> 8e18bd6d3b44f892c4e048fb7e4e553c2d8fe619
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
>>>>>>> b5ca5ef48d2ae9ff505b8711631613fc593d45d5
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
