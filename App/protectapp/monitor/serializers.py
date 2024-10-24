<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Dispositivo, Llamadas, Mensajes, Contactos, Fotos, Videos, Ubicaciones, GrabacionesLlamadas, GrabacionesPantalla, CapturasPantalla, VerificacionPermisos, HistorialEvento


# Serializador para el modelo User (Usuario)
class UserSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(read_only=True)
    
<<<<<<< HEAD
=======
=======
<<<<<<< HEAD

from rest_framework import serializers
from .models import Dispositivo, Llamadas, Mensajes, Contactos, Fotos, Videos, Ubicaciones, GrabacionesLlamadas, GrabacionesPantalla, CapturasPantalla, VerificacionPermisos, HistorialEvento

class DispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispositivo
        fields = ['id', 'usuario', 'nombre', 'modelo', 'estado']

=======
from rest_framework import serializers
<<<<<<< HEAD
from django.contrib.auth.models import User  # Usar el modelo de usuario de Django
=======
<<<<<<< HEAD
from django.contrib.auth.models import User  # Usar el modelo de usuario de Django
=======
<<<<<<< HEAD
from django.contrib.auth.models import User  # Usar el modelo de usuario de Django
=======
<<<<<<< HEAD
from django.contrib.auth.models import User  # Usar el modelo de usuario de Django
=======
<<<<<<< HEAD
from django.contrib.auth.models import User  # Usar el modelo de usuario de Django
=======
from django.contrib.auth.models import User  # Usaremos el modelo User de Django
>>>>>>> 052f2d3b4d3ee496a9b96224faedb68f377a196d
>>>>>>> a8d19f143da4dcdf7a22fd08e935b212cf57580a
>>>>>>> b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
>>>>>>> b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
from .models import (
    Dispositivo, 
    Llamadas, 
    Mensajes, 
    Fotos, 
    Videos, 
    Ubicaciones, 
    GrabacionesLlamadas, 
    GrabacionesPantalla, 
    CapturasPantalla,
    Contactos,
<<<<<<< HEAD
    VerificacionPermisos,
    HistorialEvento
)

# Serializador para el modelo User (Usuario)
=======
    VerificacionPermisos
)

# Serializador para el modelo User (Usuario)
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> a8d19f143da4dcdf7a22fd08e935b212cf57580a
>>>>>>> b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
>>>>>>> b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6

class UserSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(read_only=True)
>>>>>>> 7c9c8fce799681b798ac83cabdaf1af962be551a
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'date_joined', 'is_active']

<<<<<<< HEAD
# Serializador para registrar nuevos usuarios
=======
<<<<<<< HEAD
# Serializador para registrar nuevos usuarios
=======


# Serializador para registrar nuevos usuarios

<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

# Serializador para registrar nuevos usuarios
>>>>>>> 052f2d3b4d3ee496a9b96224faedb68f377a196d
>>>>>>> a8d19f143da4dcdf7a22fd08e935b212cf57580a
>>>>>>> b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
>>>>>>> b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
>>>>>>> 7c9c8fce799681b798ac83cabdaf1af962be551a
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
<<<<<<< HEAD
    
=======
<<<<<<< HEAD
    
=======

>>>>>>> 7c9c8fce799681b798ac83cabdaf1af962be551a
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
# Serializador para el modelo Dispositivo
class DispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispositivo
        fields = ['id', 'usuario', 'nombre', 'modelo', 'estado']  # Campos a incluir en la API
        extra_kwargs = {
            'usuario': {'required': False}  # No requerir el campo usuario desde la solicitud
        }

    def create(self, validated_data):
        # Asegurar que el usuario venga del contexto de la solicitud
        usuario = self.context['request'].user
        dispositivo = Dispositivo.objects.create(usuario=usuario, **validated_data)
        return dispositivo

<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 7c9c8fce799681b798ac83cabdaf1af962be551a
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04

# Serializer para las Llamadas
class LlamadasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Llamadas
        fields = ['numero', 'duracion', 'fecha', 'hora', 'tipo']  # Aseguramos que 'tipo' esté presente

# Serializer para los Mensajes
class MensajesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mensajes
        fields = ['numero', 'contenido', 'fecha', 'hora', 'tipo']  # Aseguramos que 'tipo' esté presente

# Serializer para los Contactos
class ContactosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contactos
        fields = ['nombre', 'numero']

# Serializer para las Fotos
class FotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fotos
<<<<<<< HEAD
        fields = ['dispositivo', 'archivo_foto', 'fecha', 'hora']


=======
        fields = ['ruta_foto', 'fecha', 'hora']
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04

# Serializer para los Videos
class VideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = ['ruta_video', 'fecha', 'hora']
<<<<<<< HEAD

# Serializador para Ubicaciones
=======
<<<<<<< HEAD

# Serializador para Ubicaciones
=======
=======
# Serializador para Llamadas
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
class LlamadasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Llamadas
        fields = ['id', 'dispositivo', 'numero', 'duracion', 'fecha', 'hora', 'tipo']

<<<<<<< HEAD
=======
# Serializador para Mensajes
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
class MensajesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mensajes
        fields = ['id', 'dispositivo', 'numero', 'contenido', 'fecha', 'hora', 'tipo']

<<<<<<< HEAD
class ContactosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contactos
        fields = ['id', 'dispositivo', 'nombre', 'numero']

=======
# Serializador para Fotos
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
class FotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fotos
        fields = ['id', 'dispositivo', 'ruta_foto', 'fecha', 'hora']

<<<<<<< HEAD
=======
# Serializador para Videos
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
class VideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = ['id', 'dispositivo', 'ruta_video', 'fecha', 'hora']
<<<<<<< HEAD

=======
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6

# Serializador para Ubicaciones
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
>>>>>>> 7c9c8fce799681b798ac83cabdaf1af962be551a
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
class UbicacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubicaciones
        fields = ['id', 'dispositivo', 'latitud', 'longitud', 'fecha', 'hora']

<<<<<<< HEAD
# Serializador para Grabaciones de Llamadas
class GrabacionesLlamadasSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrabacionesLlamadas
        fields = ['id', 'dispositivo', 'archivo_audio', 'duracion', 'fecha', 'hora']

# Serializador para Grabaciones de Pantalla
class GrabacionesPantallaSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrabacionesPantalla
        fields = ['id', 'dispositivo', 'archivo_video', 'fecha', 'hora']

# Serializer para Capturas de Pantalla
class CapturasPantallaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CapturasPantalla
        fields = ['dispositivo', 'archivo_captura', 'fecha', 'hora']


=======
<<<<<<< HEAD
# Serializador para Grabaciones de Llamadas
=======
<<<<<<< HEAD
=======
# Serializador para Grabaciones de Llamadas
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
>>>>>>> 7c9c8fce799681b798ac83cabdaf1af962be551a
class GrabacionesLlamadasSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrabacionesLlamadas
        fields = ['id', 'dispositivo', 'ruta_grabacion', 'duracion', 'fecha', 'hora']

<<<<<<< HEAD
# Serializador para Grabaciones de Pantalla
=======
<<<<<<< HEAD
=======
# Serializador para Grabaciones de Pantalla
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
>>>>>>> 7c9c8fce799681b798ac83cabdaf1af962be551a
class GrabacionesPantallaSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrabacionesPantalla
        fields = ['id', 'dispositivo', 'ruta_grabacion', 'fecha', 'hora']

<<<<<<< HEAD
# Serializador para Capturas de Pantalla
=======
<<<<<<< HEAD
=======
# Serializador para Capturas de Pantalla
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
>>>>>>> 7c9c8fce799681b798ac83cabdaf1af962be551a
class CapturasPantallaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CapturasPantalla
        fields = ['id', 'dispositivo', 'ruta_captura', 'fecha', 'hora']

<<<<<<< HEAD
=======
<<<<<<< HEAD
class VerificacionPermisosSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerificacionPermisos
        fields = ['id', 'permiso', 'estado', 'fecha_verificacion']
=======
>>>>>>> 7c9c8fce799681b798ac83cabdaf1af962be551a
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
# Serializador para Contactos
class ContactosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contactos
        fields = ['id', 'dispositivo', 'nombre', 'numero']

# Serializador para Verificación de Permisos
class VerificacionPermisosSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerificacionPermisos
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
        fields = ['id', 'permiso', 'estado', 'fecha_verificacion', 'tipo_permiso', 'critico', 'clave_sistema']

# Serializador para Historial de Eventos
class HistorialEventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialEvento
<<<<<<< HEAD
        fields = ['id', 'tipo_evento', 'fecha', 'hora', 'detalles', 'dispositivo']
=======
        fields = ['id', 'tipo_evento', 'fecha', 'hora', 'detalles', 'dispositivo']
=======
<<<<<<< HEAD
        fields = ['id', 'permiso', 'estado', 'fecha_verificacion', 'tipo_permiso', 'critico', 'clave_sistema']


>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470

class HistorialEventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialEvento
        fields = ['id', 'tipo_evento', 'fecha', 'hora', 'detalles', 'dispositivo']
<<<<<<< HEAD
=======

=======
        fields = ['id', 'dispositivo', 'permiso', 'estado', 'fecha_verificacion']
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
>>>>>>> 7c9c8fce799681b798ac83cabdaf1af962be551a
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
