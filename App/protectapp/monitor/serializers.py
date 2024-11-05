<<<<<<< HEAD
from rest_framework import serializers
=======
<<<<<<< HEAD
from rest_framework import serializers
=======
<<<<<<< HEAD
from rest_framework import serializers
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04

from rest_framework import serializers
=======

from rest_framework import serializers
<<<<<<< HEAD
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
>>>>>>> b5ca5ef48d2ae9ff505b8711631613fc593d45d5
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
from django.contrib.auth.models import User
from .models import Dispositivo, Llamadas, Mensajes, Contactos, Fotos, Videos, Ubicaciones, GrabacionesLlamadas, GrabacionesPantalla, CapturasPantalla, VerificacionPermisos, HistorialEvento


# Serializador para el modelo User (Usuario)
class UserSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(read_only=True)
    
<<<<<<< HEAD
    class Meta:
        model = User
        fields = ['id','username', 'email', 'first_name', 'last_name', 'date_joined', 'is_active']

# Serializador para registrar nuevos usuarios
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
=======
<<<<<<< HEAD

from rest_framework import serializers
<<<<<<< HEAD
=======
=======
>>>>>>> 8e18bd6d3b44f892c4e048fb7e4e553c2d8fe619
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
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
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'date_joined', 'is_active']

<<<<<<< HEAD
# Serializador para registrar nuevos usuarios
=======
<<<<<<< HEAD
# Serializador para registrar nuevos usuarios
=======
<<<<<<< HEAD
<<<<<<< HEAD
# Serializador para registrar nuevos usuarios
=======
<<<<<<< HEAD
# Serializador para registrar nuevos usuarios
=======
=======
<<<<<<< HEAD
# Serializador para registrar nuevos usuarios
=======
=======
>>>>>>> 8e18bd6d3b44f892c4e048fb7e4e553c2d8fe619
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29


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
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
<<<<<<< HEAD

    def validate_email(self, value):
        # Verifica si el correo ya está registrado
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("El correo ya está registrado.")
        return value

    def create(self, validated_data):
        # Crea un nuevo usuario
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    
# Serializador para el modelo Dispositivo
class DispositivoSerializer(serializers.ModelSerializer):
    eventos = serializers.SerializerMethodField()
    estado_texto = serializers.SerializerMethodField()
    ultima_actividad = serializers.SerializerMethodField()  # Nueva información de última actividad

    class Meta:
        model = Dispositivo
        fields = ['id', 'usuario', 'nombre', 'modelo', 'estado', 'eventos', 'estado_texto', 'ultima_actividad']

    def get_eventos(self, obj):
        return HistorialEvento.objects.filter(dispositivo=obj).count()

    def get_estado_texto(self, obj):
        return "Activo" if obj.estado else "Inactivo"

    def get_ultima_actividad(self, obj):
        # Obtener el último evento registrado para el dispositivo
        ultimo_evento = HistorialEvento.objects.filter(dispositivo=obj).order_by('-fecha', '-hora').first()
        if ultimo_evento:
            return f"{ultimo_evento.fecha} {ultimo_evento.hora}"
        return "Sin actividad registrada"

=======
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
<<<<<<< HEAD
<<<<<<< HEAD
    
=======
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
<<<<<<< HEAD
    
=======

>>>>>>> 7c9c8fce799681b798ac83cabdaf1af962be551a
<<<<<<< HEAD
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
=======
=======

>>>>>>> 8e18bd6d3b44f892c4e048fb7e4e553c2d8fe619
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
>>>>>>> b5ca5ef48d2ae9ff505b8711631613fc593d45d5
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
# Serializador para el modelo Dispositivo
class DispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispositivo
<<<<<<< HEAD
        fields = ['id', 'usuario', 'nombre', 'modelo', 'estado']  
        read_only_fields = ['id', 'usuario']  
=======
<<<<<<< HEAD
        fields = ['id', 'usuario', 'nombre', 'modelo', 'estado']  
        read_only_fields = ['id', 'usuario']  
=======
        fields = ['id', 'usuario', 'nombre', 'modelo', 'estado']  # Campos a incluir en la API
        extra_kwargs = {
            'usuario': {'required': False}  # No requerir el campo usuario desde la solicitud
        }
>>>>>>> b5ca5ef48d2ae9ff505b8711631613fc593d45d5
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145

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

# Serializer para las Llamadas
class LlamadasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Llamadas
<<<<<<< HEAD
        fields = ['numero', 'duracion', 'fecha', 'hora', 'tipo']  
=======
<<<<<<< HEAD
        fields = ['numero', 'duracion', 'fecha', 'hora', 'tipo']  
=======
<<<<<<< HEAD
        fields = ['numero', 'duracion', 'fecha', 'hora', 'tipo']  
=======
        fields = ['numero', 'duracion', 'fecha', 'hora', 'tipo']  # Aseguramos que 'tipo' esté presente
>>>>>>> b5ca5ef48d2ae9ff505b8711631613fc593d45d5
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f

# Serializer para los Mensajes
class MensajesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mensajes
<<<<<<< HEAD
        fields = ['numero', 'contenido', 'fecha', 'hora', 'tipo']  
=======
<<<<<<< HEAD
        fields = ['numero', 'contenido', 'fecha', 'hora', 'tipo']  
=======
<<<<<<< HEAD
        fields = ['numero', 'contenido', 'fecha', 'hora', 'tipo']  
=======
        fields = ['numero', 'contenido', 'fecha', 'hora', 'tipo']  # Aseguramos que 'tipo' esté presente
>>>>>>> b5ca5ef48d2ae9ff505b8711631613fc593d45d5
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f

# Serializer para los Contactos
class ContactosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contactos
<<<<<<< HEAD
        fields = ['id', 'dispositivo', 'nombre', 'numero']
        read_only_fields = ['id', 'dispositivo']
=======
<<<<<<< HEAD
        fields = ['id', 'dispositivo', 'nombre', 'numero']
        read_only_fields = ['id', 'dispositivo']
=======
<<<<<<< HEAD
        fields = ['id', 'dispositivo', 'nombre', 'numero']
        read_only_fields = ['id', 'dispositivo']
=======
        fields = ['nombre', 'numero']
>>>>>>> b5ca5ef48d2ae9ff505b8711631613fc593d45d5
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f

# Serializer para las Fotos
class FotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fotos
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
        fields = ['dispositivo', 'archivo_foto', 'fecha', 'hora']
        read_only_fields = ['dispositivo']


<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
        fields = ['dispositivo', 'archivo_foto', 'fecha', 'hora']


=======
        fields = ['ruta_foto', 'fecha', 'hora']
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
=======
        fields = ['ruta_foto', 'fecha', 'hora']
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29

>>>>>>> b5ca5ef48d2ae9ff505b8711631613fc593d45d5
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
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
<<<<<<< HEAD

# Serializador para Ubicaciones
=======
<<<<<<< HEAD
<<<<<<< HEAD

# Serializador para Ubicaciones
=======
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
<<<<<<< HEAD

# Serializador para Ubicaciones
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 8e18bd6d3b44f892c4e048fb7e4e553c2d8fe619
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
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
class UbicacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubicaciones
        fields = ['id', 'dispositivo', 'latitud', 'longitud', 'fecha', 'hora']
<<<<<<< HEAD
        read_only_fields = ['id', 'dispositivo']

=======
<<<<<<< HEAD
        read_only_fields = ['id', 'dispositivo']

=======
<<<<<<< HEAD
        read_only_fields = ['id', 'dispositivo']

=======

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b5ca5ef48d2ae9ff505b8711631613fc593d45d5
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
# Serializador para Grabaciones de Llamadas
class GrabacionesLlamadasSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrabacionesLlamadas
        fields = ['id', 'dispositivo', 'archivo_audio', 'duracion', 'fecha', 'hora']
<<<<<<< HEAD
        read_only_fields = ['id', 'dispositivo']
=======
<<<<<<< HEAD
        read_only_fields = ['id', 'dispositivo']
=======
<<<<<<< HEAD
        read_only_fields = ['id', 'dispositivo']
=======
>>>>>>> b5ca5ef48d2ae9ff505b8711631613fc593d45d5
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f

# Serializador para Grabaciones de Pantalla
class GrabacionesPantallaSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrabacionesPantalla
        fields = ['id', 'dispositivo', 'archivo_video', 'fecha', 'hora']
<<<<<<< HEAD
        read_only_fields = ['id', 'dispositivo']
=======
<<<<<<< HEAD
        read_only_fields = ['id', 'dispositivo']
=======
<<<<<<< HEAD
        read_only_fields = ['id', 'dispositivo']
=======
>>>>>>> b5ca5ef48d2ae9ff505b8711631613fc593d45d5
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f

# Serializer para Capturas de Pantalla
class CapturasPantallaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CapturasPantalla
        fields = ['dispositivo', 'archivo_captura', 'fecha', 'hora']
<<<<<<< HEAD
        read_only_fields = ['dispositivo']
=======
<<<<<<< HEAD
        read_only_fields = ['dispositivo']
=======
<<<<<<< HEAD
        read_only_fields = ['dispositivo']
=======


=======
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
<<<<<<< HEAD
# Serializador para Grabaciones de Llamadas
=======
<<<<<<< HEAD
=======
# Serializador para Grabaciones de Llamadas
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
>>>>>>> 7c9c8fce799681b798ac83cabdaf1af962be551a
<<<<<<< HEAD
=======
=======
=======
# Serializador para Grabaciones de Llamadas
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
>>>>>>> 8e18bd6d3b44f892c4e048fb7e4e553c2d8fe619
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
class GrabacionesLlamadasSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrabacionesLlamadas
        fields = ['id', 'dispositivo', 'ruta_grabacion', 'duracion', 'fecha', 'hora']

<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
# Serializador para Grabaciones de Pantalla
=======
<<<<<<< HEAD
=======
# Serializador para Grabaciones de Pantalla
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
>>>>>>> 7c9c8fce799681b798ac83cabdaf1af962be551a
<<<<<<< HEAD
=======
=======
=======
# Serializador para Grabaciones de Pantalla
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
>>>>>>> 8e18bd6d3b44f892c4e048fb7e4e553c2d8fe619
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
class GrabacionesPantallaSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrabacionesPantalla
        fields = ['id', 'dispositivo', 'ruta_grabacion', 'fecha', 'hora']

<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
# Serializador para Capturas de Pantalla
=======
<<<<<<< HEAD
=======
# Serializador para Capturas de Pantalla
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
>>>>>>> 7c9c8fce799681b798ac83cabdaf1af962be551a
<<<<<<< HEAD
=======
=======
=======
# Serializador para Capturas de Pantalla
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
>>>>>>> 8e18bd6d3b44f892c4e048fb7e4e553c2d8fe619
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
class CapturasPantallaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CapturasPantalla
        fields = ['id', 'dispositivo', 'ruta_captura', 'fecha', 'hora']

<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 8e18bd6d3b44f892c4e048fb7e4e553c2d8fe619
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
class VerificacionPermisosSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerificacionPermisos
        fields = ['id', 'permiso', 'estado', 'fecha_verificacion']
=======
<<<<<<< HEAD
>>>>>>> 7c9c8fce799681b798ac83cabdaf1af962be551a
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
=======
<<<<<<< HEAD
>>>>>>> 7c9c8fce799681b798ac83cabdaf1af962be551a
=======
>>>>>>> 8e18bd6d3b44f892c4e048fb7e4e553c2d8fe619
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
# Serializador para Contactos
class ContactosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contactos
        fields = ['id', 'dispositivo', 'nombre', 'numero']
>>>>>>> b5ca5ef48d2ae9ff505b8711631613fc593d45d5
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f

# Serializador para Verificación de Permisos
class VerificacionPermisosSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerificacionPermisos
<<<<<<< HEAD
        fields = ['id', 'permiso', 'estado', 'fecha_verificacion', 'tipo_permiso', 'critico', 'clave_sistema']

=======
<<<<<<< HEAD
        fields = ['id', 'permiso', 'estado', 'fecha_verificacion', 'tipo_permiso', 'critico', 'clave_sistema']

=======
<<<<<<< HEAD
        fields = ['id', 'permiso', 'estado', 'fecha_verificacion', 'tipo_permiso', 'critico', 'clave_sistema']

=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
        fields = ['id', 'permiso', 'estado', 'fecha_verificacion', 'tipo_permiso', 'critico', 'clave_sistema']

=======
        fields = ['id', 'permiso', 'estado', 'fecha_verificacion', 'tipo_permiso', 'critico', 'clave_sistema']

<<<<<<< HEAD
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
>>>>>>> b5ca5ef48d2ae9ff505b8711631613fc593d45d5
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
# Serializador para Historial de Eventos
class HistorialEventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialEvento
<<<<<<< HEAD
        fields = ['id', 'tipo_evento', 'fecha', 'hora', 'detalles', 'dispositivo']
=======
<<<<<<< HEAD
        fields = ['id', 'tipo_evento', 'fecha', 'hora', 'detalles', 'dispositivo']
=======
<<<<<<< HEAD
        fields = ['id', 'tipo_evento', 'fecha', 'hora', 'detalles', 'dispositivo']
=======
<<<<<<< HEAD
<<<<<<< HEAD
        fields = ['id', 'tipo_evento', 'fecha', 'hora', 'detalles', 'dispositivo']
=======
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
        fields = ['id', 'tipo_evento', 'fecha', 'hora', 'detalles', 'dispositivo']
=======
<<<<<<< HEAD
        fields = ['id', 'permiso', 'estado', 'fecha_verificacion', 'tipo_permiso', 'critico', 'clave_sistema']

<<<<<<< HEAD
=======
=======
>>>>>>> 8e18bd6d3b44f892c4e048fb7e4e553c2d8fe619
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29

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
