from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Dispositivo, Llamadas, Mensajes, Contactos, Fotos, Videos, Ubicaciones, GrabacionesLlamadas, GrabacionesPantalla, CapturasPantalla, VerificacionPermisos, HistorialEvento


# Serializador para el modelo User (Usuario)
class UserSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(read_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'date_joined', 'is_active']

# Serializador para registrar nuevos usuarios
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
    
# Serializador para el modelo Dispositivo
class DispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispositivo
        fields = ['id', 'usuario', 'nombre', 'modelo', 'estado']  
        read_only_fields = ['id', 'usuario']  

    def create(self, validated_data):
        # Asegurar que el usuario venga del contexto de la solicitud
        usuario = self.context['request'].user
        dispositivo = Dispositivo.objects.create(usuario=usuario, **validated_data)
        return dispositivo


# Serializer para las Llamadas
class LlamadasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Llamadas
        fields = ['numero', 'duracion', 'fecha', 'hora', 'tipo']  

# Serializer para los Mensajes
class MensajesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mensajes
        fields = ['numero', 'contenido', 'fecha', 'hora', 'tipo']  

# Serializer para los Contactos
class ContactosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contactos
        fields = ['id', 'dispositivo', 'nombre', 'numero']
        read_only_fields = ['id', 'dispositivo']

# Serializer para las Fotos
class FotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fotos
        fields = ['dispositivo', 'archivo_foto', 'fecha', 'hora']
        read_only_fields = ['dispositivo']


# Serializer para los Videos
class VideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = ['ruta_video', 'fecha', 'hora']

# Serializador para Ubicaciones
class UbicacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubicaciones
        fields = ['id', 'dispositivo', 'latitud', 'longitud', 'fecha', 'hora']
        read_only_fields = ['id', 'dispositivo']

# Serializador para Grabaciones de Llamadas
class GrabacionesLlamadasSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrabacionesLlamadas
        fields = ['id', 'dispositivo', 'archivo_audio', 'duracion', 'fecha', 'hora']
        read_only_fields = ['id', 'dispositivo']

# Serializador para Grabaciones de Pantalla
class GrabacionesPantallaSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrabacionesPantalla
        fields = ['id', 'dispositivo', 'archivo_video', 'fecha', 'hora']
        read_only_fields = ['id', 'dispositivo']

# Serializer para Capturas de Pantalla
class CapturasPantallaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CapturasPantalla
        fields = ['dispositivo', 'archivo_captura', 'fecha', 'hora']
        read_only_fields = ['dispositivo']

# Serializador para Verificación de Permisos
class VerificacionPermisosSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerificacionPermisos
        fields = ['id', 'permiso', 'estado', 'fecha_verificacion', 'tipo_permiso', 'critico', 'clave_sistema']

# Serializador para Historial de Eventos
class HistorialEventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialEvento
        fields = ['id', 'tipo_evento', 'fecha', 'hora', 'detalles', 'dispositivo']
