<<<<<<< HEAD

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Dispositivo, Llamadas, Mensajes, Contactos, Fotos, Videos, Ubicaciones, GrabacionesLlamadas, GrabacionesPantalla, CapturasPantalla, Contactos, VerificacionPermisos, HistorialEvento
from .serializers import DispositivoSerializer, LlamadasSerializer, MensajesSerializer, ContactosSerializer, FotosSerializer, VideosSerializer, UbicacionesSerializer, GrabacionesLlamadasSerializer, GrabacionesPantallaSerializer, CapturasPantallaSerializer,VerificacionPermisosSerializer, HistorialEventoSerializer

# API Overview
@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'Dispositivos': '/api/dispositivos/',
        'Llamadas': '/api/llamadas/',
        'Mensajes': '/api/mensajes/',
        'Contactos': '/api/contactos/',
        'Fotos': '/api/fotos/',
        'Videos': '/api/videos/',
        'Ubicaciones': '/api/ubicaciones/',
        'Grabaciones Llamadas': '/api/grabaciones-llamadas/',
        'Grabaciones Pantalla': '/api/grabaciones-pantalla/',
        'Capturas Pantalla': '/api/capturas-pantalla/',
        'Verificación Permisos': '/api/verificacion-permisos/',
        'Historial Evento': '/api/historial-evento/',
    }
    return Response(api_urls)


# CRUD for Dispositivo
@api_view(['GET'])
def dispositivo_list(request):
    dispositivos = Dispositivo.objects.all()
    serializer = DispositivoSerializer(dispositivos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def dispositivo_detail(request, pk):
    dispositivo = get_object_or_404(Dispositivo, id=pk)
    serializer = DispositivoSerializer(dispositivo, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def dispositivo_create(request):
    serializer = DispositivoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def dispositivo_update(request, pk):
    dispositivo = get_object_or_404(Dispositivo, id=pk)
    serializer = DispositivoSerializer(instance=dispositivo, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def dispositivo_delete(request, pk):
    dispositivo = get_object_or_404(Dispositivo, id=pk)
    dispositivo.delete()
    return Response("Dispositivo eliminado correctamente")


# CRUD for Llamadas
@api_view(['GET'])
def llamadas_list(request):
    llamadas = Llamadas.objects.all()
    serializer = LlamadasSerializer(llamadas, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def llamadas_detail(request, pk):
    llamadas = get_object_or_404(Llamadas, id=pk)
    serializer = LlamadasSerializer(llamadas, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def llamadas_create(request):
    serializer = LlamadasSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def llamadas_update(request, pk):
    llamadas = get_object_or_404(Llamadas, id=pk)
    serializer = LlamadasSerializer(instance=llamadas, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def llamadas_delete(request, pk):
    llamadas = get_object_or_404(Llamadas, id=pk)
    llamadas.delete()
    return Response("Llamada eliminada correctamente")


# CRUD for Mensajes
@api_view(['GET'])
def mensajes_list(request):
    mensajes = Mensajes.objects.all()
    serializer = MensajesSerializer(mensajes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def mensajes_detail(request, pk):
    mensajes = get_object_or_404(Mensajes, id=pk)
    serializer = MensajesSerializer(mensajes, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def mensajes_create(request):
    serializer = MensajesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def mensajes_update(request, pk):
    mensajes = get_object_or_404(Mensajes, id=pk)
    serializer = MensajesSerializer(instance=mensajes, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def mensajes_delete(request, pk):
    mensajes = get_object_or_404(Mensajes, id=pk)
    mensajes.delete()
    return Response("Mensaje eliminado correctamente")


# CRUD for Contactos
@api_view(['GET'])
def contactos_list(request):
    contactos = Contactos.objects.all()
    serializer = ContactosSerializer(contactos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def contactos_detail(request, pk):
    contactos = get_object_or_404(Contactos, id=pk)
    serializer = ContactosSerializer(contactos, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def contactos_create(request):
    serializer = ContactosSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def contactos_update(request, pk):
    contactos = get_object_or_404(Contactos, id=pk)
    serializer = ContactosSerializer(instance=contactos, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def contactos_delete(request, pk):
    contactos = get_object_or_404(Contactos, id=pk)
    contactos.delete()
    return Response("Contacto eliminado correctamente")



# CRUD for Fotos
@api_view(['GET'])
def fotos_list(request):
    fotos = Fotos.objects.all()
    serializer = FotosSerializer(fotos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def fotos_detail(request, pk):
    fotos = get_object_or_404(Fotos, id=pk)
    serializer = FotosSerializer(fotos, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def fotos_create(request):
    serializer = FotosSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def fotos_update(request, pk):
    fotos = get_object_or_404(Fotos, id=pk)
    serializer = FotosSerializer(instance=fotos, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def fotos_delete(request, pk):
    fotos = get_object_or_404(Fotos, id=pk)
    fotos.delete()
    return Response("Foto eliminada correctamente")


# CRUD for Videos
@api_view(['GET'])
def videos_list(request):
    videos = Videos.objects.all()
    serializer = VideosSerializer(videos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def videos_detail(request, pk):
    videos = get_object_or_404(Videos, id=pk)
    serializer = VideosSerializer(videos, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def videos_create(request):
    serializer = VideosSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def videos_update(request, pk):
    videos = get_object_or_404(Videos, id=pk)
    serializer = VideosSerializer(instance=videos, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def videos_delete(request, pk):
    videos = get_object_or_404(Videos, id=pk)
    videos.delete()
    return Response("Video eliminado correctamente")


# CRUD for Ubicaciones
@api_view(['GET'])
def ubicaciones_list(request):
    ubicaciones = Ubicaciones.objects.all()
    serializer = UbicacionesSerializer(ubicaciones, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ubicaciones_detail(request, pk):
    ubicaciones = get_object_or_404(Ubicaciones, id=pk)
    serializer = UbicacionesSerializer(ubicaciones, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def ubicaciones_create(request):
    serializer = UbicacionesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def ubicaciones_update(request, pk):
    ubicaciones = get_object_or_404(Ubicaciones, id=pk)
    serializer = UbicacionesSerializer(instance=ubicaciones, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def ubicaciones_delete(request, pk):
    ubicaciones = get_object_or_404(Ubicaciones, id=pk)
    ubicaciones.delete()
    return Response("Ubicación eliminada correctamente")


# CRUD for Grabaciones de Llamadas
@api_view(['GET'])
def grabaciones_llamadas_list(request):
    grabaciones = GrabacionesLlamadas.objects.all()
    serializer = GrabacionesLlamadasSerializer(grabaciones, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def grabaciones_llamadas_detail(request, pk):
    grabaciones = get_object_or_404(GrabacionesLlamadas, id=pk)
    serializer = GrabacionesLlamadasSerializer(grabaciones, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def grabaciones_llamadas_create(request):
    serializer = GrabacionesLlamadasSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def grabaciones_llamadas_update(request, pk):
    grabaciones = get_object_or_404(GrabacionesLlamadas, id=pk)
    serializer = GrabacionesLlamadasSerializer(instance=grabaciones, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def grabaciones_llamadas_delete(request, pk):
    grabaciones = get_object_or_404(GrabacionesLlamadas, id=pk)
    grabaciones.delete()
    return Response("Grabación de llamada eliminada correctamente")


# CRUD for Grabaciones de Pantalla
@api_view(['GET'])
def grabaciones_pantalla_list(request):
    grabaciones = GrabacionesPantalla.objects.all()
    serializer = GrabacionesPantallaSerializer(grabaciones, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def grabaciones_pantalla_detail(request, pk):
    grabaciones = get_object_or_404(GrabacionesPantalla, id=pk)
    serializer = GrabacionesPantallaSerializer(grabaciones, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def grabaciones_pantalla_create(request):
    serializer = GrabacionesPantallaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def grabaciones_pantalla_update(request, pk):
    grabaciones = get_object_or_404(GrabacionesPantalla, id=pk)
    serializer = GrabacionesPantallaSerializer(instance=grabaciones, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def grabaciones_pantalla_delete(request, pk):
    grabaciones = get_object_or_404(GrabacionesPantalla, id=pk)
    grabaciones.delete()
    return Response("Grabación de pantalla eliminada correctamente")


# CRUD for Capturas de Pantalla
@api_view(['GET'])
def capturas_pantalla_list(request):
    capturas = CapturasPantalla.objects.all()
    serializer = CapturasPantallaSerializer(capturas, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def capturas_pantalla_detail(request, pk):
    capturas = get_object_or_404(CapturasPantalla, id=pk)
    serializer = CapturasPantallaSerializer(capturas, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def capturas_pantalla_create(request):
    serializer = CapturasPantallaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def capturas_pantalla_update(request, pk):
    capturas = get_object_or_404(CapturasPantalla, id=pk)
    serializer = CapturasPantallaSerializer(instance=capturas, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def capturas_pantalla_delete(request, pk):
    capturas = get_object_or_404(CapturasPantalla, id=pk)
    capturas.delete()
    return Response("Captura de pantalla eliminada correctamente")


# CRUD for VerificacionPermisos
@api_view(['GET'])
def permisos_list(request):
    permisos = VerificacionPermisos.objects.all()
    serializer = VerificacionPermisosSerializer(permisos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def permisos_detail(request, pk):
    permisos = get_object_or_404(VerificacionPermisos, id=pk)
    serializer = VerificacionPermisosSerializer(permisos, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def permisos_create(request):
    serializer = VerificacionPermisosSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def permisos_update(request, pk):
    permisos = get_object_or_404(VerificacionPermisos, id=pk)
    serializer = VerificacionPermisosSerializer(instance=permisos, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def permisos_delete(request, pk):
    permisos = get_object_or_404(VerificacionPermisos, id=pk)
    permisos.delete()
    return Response("Permiso eliminado correctamente")


# CRUD for HistorialEvento
@api_view(['GET'])
def historial_evento_list(request):
    historial = HistorialEvento.objects.all()
    serializer = HistorialEventoSerializer(historial, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def historial_evento_detail(request, pk):
    historial = get_object_or_404(HistorialEvento, id=pk)
    serializer = HistorialEventoSerializer(historial, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def historial_evento_create(request):
    serializer = HistorialEventoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def historial_evento_update(request, pk):
    historial = get_object_or_404(HistorialEvento, id=pk)
    serializer = HistorialEventoSerializer(instance=historial, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def historial_evento_delete(request, pk):
    historial = get_object_or_404(HistorialEvento, id=pk)
    historial.delete()
    return Response("Historial de evento eliminado correctamente")
=======
<<<<<<< HEAD
import logging 
import csv
import pandas as pd
from reportlab.pdfgen import canvas
from rest_framework import generics
=======
<<<<<<< HEAD
import logging 
=======
<<<<<<< HEAD
import logging 
=======
<<<<<<< HEAD
import logging 
=======
<<<<<<< HEAD
import logging 
=======
<<<<<<< HEAD
>>>>>>> 052f2d3b4d3ee496a9b96224faedb68f377a196d
>>>>>>> a8d19f143da4dcdf7a22fd08e935b212cf57580a
>>>>>>> b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
>>>>>>> b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
<<<<<<< HEAD
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import UserSerializer
from .serializers import HistorialEventoSerializer
=======
<<<<<<< HEAD
from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import UserSerializer
=======
<<<<<<< HEAD
from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import UserSerializer
=======
<<<<<<< HEAD
from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import UserSerializer
=======
<<<<<<< HEAD
from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import UserSerializer
=======
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
    Evento,
    HistorialEvento
=======
    VerificacionPermisos
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
)
from .serializers import (
    DispositivoSerializer, 
    UserSerializer, 
    UserRegisterSerializer, 
    LlamadasSerializer, 
    MensajesSerializer, 
    FotosSerializer, 
    VideosSerializer, 
    UbicacionesSerializer, 
    GrabacionesLlamadasSerializer, 
    GrabacionesPantallaSerializer, 
    CapturasPantallaSerializer,
    ContactosSerializer,
    VerificacionPermisosSerializer
)
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

<<<<<<< HEAD
=======
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
# Configuración básica del logger
logger = logging.getLogger(__name__)

# -----------------------------------
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 052f2d3b4d3ee496a9b96224faedb68f377a196d
>>>>>>> a8d19f143da4dcdf7a22fd08e935b212cf57580a
>>>>>>> b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
>>>>>>> b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
# Vista de prueba para verificar si la API funciona
@api_view(['GET'])
@permission_classes([AllowAny])
def api_overview(request):
    return Response({"message": "API is working correctly!"})
<<<<<<< HEAD

# -----------------------------------

=======
<<<<<<< HEAD

# -----------------------------------

=======
<<<<<<< HEAD

# -----------------------------------

=======
<<<<<<< HEAD
# -----------------------------------

=======

<<<<<<< HEAD
# -----------------------------------

=======
>>>>>>> 052f2d3b4d3ee496a9b96224faedb68f377a196d
>>>>>>> a8d19f143da4dcdf7a22fd08e935b212cf57580a
>>>>>>> b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
>>>>>>> b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
# Registro de nuevos usuarios
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = UserRegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

<<<<<<< HEAD
=======
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
# Inicio de sesión y obtención del token JWT con registro de logs
@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    email = request.data.get("email")
    password = request.data.get("password")

    # Registrar datos importantes para depuración
    logger.debug(f"Intento de inicio de sesión para: {email}")

    # Buscar el usuario por correo electrónico
    try:
        user = User.objects.get(email=email)
        username = user.username  # Obtener nombre de usuario
        logger.debug(f"Usuario encontrado: {username}")
    except User.DoesNotExist:
        logger.warning(f"Fallo de inicio de sesión: Usuario con email {email} no encontrado")
        return Response({"detail": "Credenciales incorrectas"}, status=status.HTTP_401_UNAUTHORIZED)

    # Autenticar usando el nombre de usuario
    user = authenticate(username=username, password=password)

    if user is not None:
        refresh = RefreshToken.for_user(user)
        logger.debug(f"Inicio de sesión exitoso para: {username}")
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
# Inicio de sesión y obtención del token JWT
@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(username=username, password=password)
    if user is not None:
        refresh = RefreshToken.for_user(user)
>>>>>>> 052f2d3b4d3ee496a9b96224faedb68f377a196d
>>>>>>> a8d19f143da4dcdf7a22fd08e935b212cf57580a
>>>>>>> b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
>>>>>>> b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
<<<<<<< HEAD
=======
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
    
    logger.warning(f"Fallo de inicio de sesión: Credenciales incorrectas para {username}")
    return Response({"detail": "Credenciales incorrectas"}, status=status.HTTP_401_UNAUTHORIZED)


<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
    return Response({"detail": "Credenciales incorrectas"}, status=status.HTTP_401_UNAUTHORIZED)

>>>>>>> 052f2d3b4d3ee496a9b96224faedb68f377a196d
>>>>>>> a8d19f143da4dcdf7a22fd08e935b212cf57580a
>>>>>>> b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
>>>>>>> b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
# Actualización de perfil (requiere autenticación)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user_profile(request):
    user = request.user
    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Cerrar sesión (invalidar el token)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    try:
        refresh_token = request.data.get("refresh_token")
        if not refresh_token:
            return Response({"detail": "Token de refresco no proporcionado"}, status=status.HTTP_400_BAD_REQUEST)
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response(status=status.HTTP_205_RESET_CONTENT)
    except Exception as e:
        return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

<<<<<<< HEAD
# Obtener y actualizar datos del usuario
=======
<<<<<<< HEAD
# Obtener y actualizar datos del usuario
=======
<<<<<<< HEAD
# Obtener y actualizar datos del usuario
=======
<<<<<<< HEAD
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status

=======
<<<<<<< HEAD
# Obtener y actualizar datos del usuario
>>>>>>> a8d19f143da4dcdf7a22fd08e935b212cf57580a
>>>>>>> b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
>>>>>>> b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def get_user_data(request):
    user = request.user

    if request.method == 'GET':
        # Responder con la información del usuario
        return Response({
            'nombre': user.username,
            'email': user.email,
            'date_joined': user.date_joined,
            'es_activo': user.is_active
        })

    elif request.method == 'PUT':
        # Actualización del nombre y contraseña
        data = request.data
        if 'nombre' in data:
            user.username = data['nombre']
        if 'password' in data and data['password'] != '':
            user.set_password(data['password'])  # Actualizar la contraseña
        user.save()

        return Response({
            'message': 'Usuario actualizado correctamente'
        }, status=status.HTTP_200_OK)


<<<<<<< HEAD
# -------------------- Vistas para gestionar dispositivos --------------------
=======
<<<<<<< HEAD
# -------------------- Vistas para gestionar dispositivos --------------------
=======
<<<<<<< HEAD
# -------------------- Vistas para gestionar dispositivos --------------------
=======
<<<<<<< HEAD


# -------------------- Vista para la página de inicio --------------------


# -------------------- Vistas para gestionar dispositivos --------------------



=======
# -------------------- Vistas para gestionar dispositivos --------------------
=======
# -------------------- Vistas para gestionar dispositivos --------------------

>>>>>>> 052f2d3b4d3ee496a9b96224faedb68f377a196d
>>>>>>> a8d19f143da4dcdf7a22fd08e935b212cf57580a
>>>>>>> b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
>>>>>>> b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def dispositivo_list_create(request):
    if request.method == 'GET':
        dispositivos = Dispositivo.objects.filter(usuario=request.user)
        serializer = DispositivoSerializer(dispositivos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DispositivoSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

<<<<<<< HEAD
# Obtener, actualizar o eliminar un dispositivo
=======
<<<<<<< HEAD
# Obtener, actualizar o eliminar un dispositivo
=======
<<<<<<< HEAD
# Obtener, actualizar o eliminar un dispositivo
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
# Obtener, actualizar o eliminar un dispositivo
=======
>>>>>>> 052f2d3b4d3ee496a9b96224faedb68f377a196d
>>>>>>> a8d19f143da4dcdf7a22fd08e935b212cf57580a
>>>>>>> b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
>>>>>>> b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def dispositivo_detail(request, pk):
    try:
        dispositivo = Dispositivo.objects.get(pk=pk, usuario=request.user)
    except Dispositivo.DoesNotExist:
        return Response({'error': 'Dispositivo no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DispositivoSerializer(dispositivo)
        return Response(serializer.data)
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
>>>>>>> b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
    
    elif request.method == 'PUT':
        data = request.data
        # Solo actualizamos el nombre si está en la solicitud
        if 'nombre' in data:
            dispositivo.nombre = data['nombre']
            dispositivo.save()
            return Response({'message': 'Nombre del dispositivo actualizado correctamente'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'No se proporcionó un nombre para actualizar'}, status=status.HTTP_400_BAD_REQUEST)

<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
>>>>>>> a8d19f143da4dcdf7a22fd08e935b212cf57580a
    elif request.method == 'PUT':
        serializer = DispositivoSerializer(dispositivo, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
<<<<<<< HEAD
=======
>>>>>>> 052f2d3b4d3ee496a9b96224faedb68f377a196d
>>>>>>> a8d19f143da4dcdf7a22fd08e935b212cf57580a
>>>>>>> b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
>>>>>>> b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
    elif request.method == 'DELETE':
        dispositivo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6





# -------------------- Vistas para los modelos de monitoreo --------------------


<<<<<<< HEAD

def reg_event(request, id):
    dispositivo = Dispositivo.objects.get(id=id)
    eventos = HistorialEvento.objects.filter(dispositivo=dispositivo)

    return render(request, 'reg_event.html', {'dispositivo': dispositivo, 'eventos': eventos})



@api_view(['GET'])
def obtener_eventos(request, dispositivo_id):
    try:
        # Filtrar los eventos por el dispositivo especificado
        eventos = HistorialEvento.objects.filter(dispositivo_id=dispositivo_id)
        serializer = HistorialEventoSerializer(eventos, many=True)
        return Response(serializer.data, status=200)
    except Dispositivo.DoesNotExist:
        return Response({"error": "Dispositivo no encontrado"}, status=404)


@api_view(['GET'])
def obtener_evento_detalle(request, id):
    try:
        evento = HistorialEvento.objects.get(id=id)
        serializer = HistorialEventoSerializer(evento)
        return Response(serializer.data, status=200)
    except HistorialEvento.DoesNotExist:
        return Response({"error": "Evento no encontrado"}, status=404)

# Funcion para exportar los datos de los dispositivos a un archivo CSV
def exportar_datos_csv(request, dispositivo_id):
    tipo = request.GET.get('tipo')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{tipo}.csv"'
    
    writer = csv.writer(response)
    
    if tipo == 'llamadas':
        llamadas = Llamadas.objects.filter(dispositivo_id=dispositivo_id)
        if llamadas.exists():
            writer.writerow(['Número', 'Duración', 'Fecha', 'Hora', 'Tipo'])
            for llamada in llamadas:
                writer.writerow([llamada.numero, llamada.duracion, llamada.fecha, llamada.hora, llamada.tipo])
        else:
            writer.writerow(['No se encontraron registros de llamadas.'])

    elif tipo == 'mensajes':
        mensajes = Mensajes.objects.filter(dispositivo_id=dispositivo_id)
        if mensajes.exists():
            writer.writerow(['Número', 'Contenido', 'Fecha', 'Hora', 'Tipo'])
            for mensaje in mensajes:
                writer.writerow([mensaje.numero, mensaje.contenido, mensaje.fecha, mensaje.hora, mensaje.tipo])
        else:
            writer.writerow(['No se encontraron registros de mensajes.'])

    elif tipo == 'contactos':
        contactos = Contactos.objects.filter(dispositivo_id=dispositivo_id)
        if contactos.exists():
            writer.writerow(['Nombre', 'Número'])
            for contacto in contactos:
                writer.writerow([contacto.nombre, contacto.numero])
        else:
            writer.writerow(['No se encontraron registros de contactos.'])

    elif tipo == 'fotos':
        fotos = Fotos.objects.filter(dispositivo_id=dispositivo_id)
        if fotos.exists():
            writer.writerow(['Ruta Foto', 'Fecha', 'Hora'])
            for foto in fotos:
                writer.writerow([foto.ruta_foto, foto.fecha, foto.hora])
        else:
            writer.writerow(['No se encontraron registros de fotos.'])

    elif tipo == 'videos':
        videos = Videos.objects.filter(dispositivo_id=dispositivo_id)
        if videos.exists():
            writer.writerow(['Ruta Video', 'Fecha', 'Hora'])
            for video in videos:
                writer.writerow([video.ruta_video, video.fecha, video.hora])
        else:
            writer.writerow(['No se encontraron registros de videos.'])

    elif tipo == 'ubicaciones':
        ubicaciones = Ubicaciones.objects.filter(dispositivo_id=dispositivo_id)
        if ubicaciones.exists():
            writer.writerow(['Latitud', 'Longitud', 'Fecha', 'Hora'])
            for ubicacion in ubicaciones:
                writer.writerow([ubicacion.latitud, ubicacion.longitud, ubicacion.fecha, ubicacion.hora])
        else:
            writer.writerow(['No se encontraron registros de ubicaciones.'])

    else:
        writer.writerow(['Tipo de datos no válido.'])

    return response

# Funcion para exportar los datos de los dispositivos a un archivo Excel
def exportar_datos_excel(request, dispositivo_id):
    tipo = request.GET.get('tipo')  # 'llamadas', 'mensajes', etc.
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{tipo}.xlsx"'

    if tipo == 'llamadas':
        llamadas = Llamadas.objects.filter(dispositivo_id=dispositivo_id)
        df = pd.DataFrame(list(llamadas.values('numero', 'duracion', 'fecha', 'hora', 'tipo')))
        df.to_excel(response, index=False)

    elif tipo == 'mensajes':
        mensajes = Mensajes.objects.filter(dispositivo_id=dispositivo_id)
        df = pd.DataFrame(list(mensajes.values('numero', 'contenido', 'fecha', 'hora', 'tipo')))
        df.to_excel(response, index=False)

    elif tipo == 'contactos':
        contactos = Contactos.objects.filter(dispositivo_id=dispositivo_id)
        df = pd.DataFrame(list(contactos.values('nombre', 'numero')))
        df.to_excel(response, index=False)

    elif tipo == 'fotos':
        fotos = Fotos.objects.filter(dispositivo_id=dispositivo_id)
        df = pd.DataFrame(list(fotos.values('ruta_foto', 'fecha', 'hora')))
        df.to_excel(response, index=False)

    elif tipo == 'videos':
        videos = Videos.objects.filter(dispositivo_id=dispositivo_id)
        df = pd.DataFrame(list(videos.values('ruta_video', 'fecha', 'hora')))
        df.to_excel(response, index=False)

    elif tipo == 'ubicaciones':
        ubicaciones = Ubicaciones.objects.filter(dispositivo_id=dispositivo_id)
        df = pd.DataFrame(list(ubicaciones.values('latitud', 'longitud', 'fecha', 'hora')))
        df.to_excel(response, index=False)

    else:
        df = pd.DataFrame([['Tipo de datos no válido']])
        df.to_excel(response, index=False)

    return response

# Funcion para exportar los datos de los dispositivos a un archivo PDF
def exportar_datos_pdf(request, dispositivo_id):
    tipo = request.GET.get('tipo')  # 'llamadas', 'mensajes', etc.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{tipo}.pdf"'

    p = canvas.Canvas(response)
    y = 730

    if tipo == 'llamadas':
        llamadas = Llamadas.objects.filter(dispositivo_id=dispositivo_id)
        p.drawString(100, y, f'Registro de {tipo}')
        if llamadas.exists():
            for llamada in llamadas:
                p.drawString(100, y, f'Número: {llamada.numero} - Duración: {llamada.duracion} - Fecha: {llamada.fecha} - Hora: {llamada.hora} - Tipo: {llamada.tipo}')
                y -= 20
        else:
            p.drawString(100, y, 'No se encontraron registros de llamadas.')

    elif tipo == 'mensajes':
        mensajes = Mensajes.objects.filter(dispositivo_id=dispositivo_id)
        p.drawString(100, y, f'Registro de {tipo}')
        if mensajes.exists():
            for mensaje in mensajes:
                p.drawString(100, y, f'Número: {mensaje.numero} - Contenido: {mensaje.contenido} - Fecha: {mensaje.fecha} - Hora: {mensaje.hora} - Tipo: {mensaje.tipo}')
                y -= 20
        else:
            p.drawString(100, y, 'No se encontraron registros de mensajes.')

    elif tipo == 'contactos':
        contactos = Contactos.objects.filter(dispositivo_id=dispositivo_id)
        p.drawString(100, y, f'Registro de {tipo}')
        if contactos.exists():
            for contacto in contactos:
                p.drawString(100, y, f'Nombre: {contacto.nombre} - Número: {contacto.numero}')
                y -= 20
        else:
            p.drawString(100, y, 'No se encontraron registros de contactos.')

    elif tipo == 'fotos':
        fotos = Fotos.objects.filter(dispositivo_id=dispositivo_id)
        p.drawString(100, y, f'Registro de {tipo}')
        if fotos.exists():
            for foto in fotos:
                p.drawString(100, y, f'Ruta: {foto.ruta_foto} - Fecha: {foto.fecha} - Hora: {foto.hora}')
                y -= 20
        else:
            p.drawString(100, y, 'No se encontraron registros de fotos.')

    elif tipo == 'videos':
        videos = Videos.objects.filter(dispositivo_id=dispositivo_id)
        p.drawString(100, y, f'Registro de {tipo}')
        if videos.exists():
            for video in videos:
                p.drawString(100, y, f'Ruta: {video.ruta_video} - Fecha: {video.fecha} - Hora: {video.hora}')
                y -= 20
        else:
            p.drawString(100, y, 'No se encontraron registros de videos.')

    elif tipo == 'ubicaciones':
        ubicaciones = Ubicaciones.objects.filter(dispositivo_id=dispositivo_id)
        p.drawString(100, y, f'Registro de {tipo}')
        if ubicaciones.exists():
            for ubicacion in ubicaciones:
                p.drawString(100, y, f'Latitud: {ubicacion.latitud} - Longitud: {ubicacion.longitud} - Fecha: {ubicacion.fecha} - Hora: {ubicacion.hora}')
                y -= 20
        else:
            p.drawString(100, y, 'No se encontraron registros de ubicaciones.')

    else:
        p.drawString(100, y, 'Tipo de datos no válido.')

    p.showPage()
    p.save()

    return response


# -------------------- Vistas para los modelos de monitoreo --------------------

=======
# -------------------- Vistas para los modelos de monitoreo --------------------

=======
# -------------------- Vistas para los modelos de monitoreo --------------------

<<<<<<< HEAD

# -------------------- Vistas para los modelos de monitoreo --------------------

=======
<<<<<<< HEAD
=======
<<<<<<< HEAD

# -------------------- Vistas para los modelos de monitoreo --------------------

=======
>>>>>>> 052f2d3b4d3ee496a9b96224faedb68f377a196d
>>>>>>> a8d19f143da4dcdf7a22fd08e935b212cf57580a
>>>>>>> b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
>>>>>>> b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
# Llamadas
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def llamadas_list_create(request, dispositivo_id):
    if request.method == 'GET':
        llamadas = Llamadas.objects.filter(dispositivo_id=dispositivo_id)
        serializer = LlamadasSerializer(llamadas, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        try:
            dispositivo = Dispositivo.objects.get(id=dispositivo_id, usuario=request.user)
        except Dispositivo.DoesNotExist:
            return Response({'error': 'Dispositivo no encontrado o no autorizado'}, status=status.HTTP_404_NOT_FOUND)

        data = request.data.copy()
        data['dispositivo'] = dispositivo.id
        serializer = LlamadasSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def llamadas_detail(request, dispositivo_id, pk):
    try:
        llamada = Llamadas.objects.get(dispositivo_id=dispositivo_id, pk=pk)
    except Llamadas.DoesNotExist:
        return Response({'error': 'Llamada no encontrada'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LlamadasSerializer(llamada)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = LlamadasSerializer(llamada, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        llamada.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Mensajes
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def mensajes_list_create(request, dispositivo_id):
    if request.method == 'GET':
        mensajes = Mensajes.objects.filter(dispositivo_id=dispositivo_id)
        serializer = MensajesSerializer(mensajes, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        try:
            dispositivo = Dispositivo.objects.get(id=dispositivo_id, usuario=request.user)
        except Dispositivo.DoesNotExist:
            return Response({'error': 'Dispositivo no encontrado o no autorizado'}, status=status.HTTP_404_NOT_FOUND)

        data = request.data.copy()
        data['dispositivo'] = dispositivo.id
        serializer = MensajesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def mensajes_detail(request, dispositivo_id, pk):
    try:
        mensaje = Mensajes.objects.get(pk=pk, dispositivo_id=dispositivo_id)
    except Mensajes.DoesNotExist:
        return Response({'error': 'Mensaje no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MensajesSerializer(mensaje)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MensajesSerializer(mensaje, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        mensaje.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Fotos
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def fotos_list_create(request, dispositivo_id):
    if request.method == 'GET':
        fotos = Fotos.objects.filter(dispositivo_id=dispositivo_id)
        serializer = FotosSerializer(fotos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        try:
            dispositivo = Dispositivo.objects.get(id=dispositivo_id, usuario=request.user)
        except Dispositivo.DoesNotExist:
            return Response({'error': 'Dispositivo no encontrado o no autorizado'}, status=status.HTTP_404_NOT_FOUND)

        data = request.data.copy()
        data['dispositivo'] = dispositivo.id
        serializer = FotosSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def fotos_detail(request, dispositivo_id, pk):
    try:
        foto = Fotos.objects.get(pk=pk, dispositivo_id=dispositivo_id)
    except Fotos.DoesNotExist:
        return Response({'error': 'Foto no encontrada'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FotosSerializer(foto)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = FotosSerializer(foto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        foto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Videos
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def videos_list_create(request, dispositivo_id):
    if request.method == 'GET':
        videos = Videos.objects.filter(dispositivo_id=dispositivo_id)
        serializer = VideosSerializer(videos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        try:
            dispositivo = Dispositivo.objects.get(id=dispositivo_id, usuario=request.user)
        except Dispositivo.DoesNotExist:
            return Response({'error': 'Dispositivo no encontrado o no autorizado'}, status=status.HTTP_404_NOT_FOUND)

        data = request.data.copy()
        data['dispositivo'] = dispositivo.id
        serializer = VideosSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def videos_detail(request, dispositivo_id, pk):
    try:
        video = Videos.objects.get(pk=pk, dispositivo_id=dispositivo_id)
    except Videos.DoesNotExist:
        return Response({'error': 'Video no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VideosSerializer(video)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = VideosSerializer(video, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        video.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Ubicaciones
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def ubicaciones_list_create(request, dispositivo_id):
    if request.method == 'GET':
        ubicaciones = Ubicaciones.objects.filter(dispositivo_id=dispositivo_id)
        serializer = UbicacionesSerializer(ubicaciones, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        try:
            dispositivo = Dispositivo.objects.get(id=dispositivo_id, usuario=request.user)
        except Dispositivo.DoesNotExist:
            return Response({'error': 'Dispositivo no encontrado o no autorizado'}, status=status.HTTP_404_NOT_FOUND)

        data = request.data.copy()
        data['dispositivo'] = dispositivo.id
        serializer = UbicacionesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def ubicaciones_detail(request, dispositivo_id, pk):
    try:
        ubicacion = Ubicaciones.objects.get(pk=pk, dispositivo_id=dispositivo_id)
    except Ubicaciones.DoesNotExist:
        return Response({'error': 'Ubicación no encontrada'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UbicacionesSerializer(ubicacion)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UbicacionesSerializer(ubicacion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        ubicacion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Grabaciones de Llamadas
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def grabaciones_llamadas_list_create(request, dispositivo_id):
    if request.method == 'GET':
        grabaciones = GrabacionesLlamadas.objects.filter(dispositivo_id=dispositivo_id)
        serializer = GrabacionesLlamadasSerializer(grabaciones, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        try:
            dispositivo = Dispositivo.objects.get(id=dispositivo_id, usuario=request.user)
        except Dispositivo.DoesNotExist:
            return Response({'error': 'Dispositivo no encontrado o no autorizado'}, status=status.HTTP_404_NOT_FOUND)

        data = request.data.copy()
        data['dispositivo'] = dispositivo.id
        serializer = GrabacionesLlamadasSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def grabacion_llamada_detail(request, dispositivo_id, pk):
    try:
        grabacion = GrabacionesLlamadas.objects.get(pk=pk, dispositivo_id=dispositivo_id)
    except GrabacionesLlamadas.DoesNotExist:
        return Response({'error': 'Grabación de llamada no encontrada'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GrabacionesLlamadasSerializer(grabacion)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = GrabacionesLlamadasSerializer(grabacion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        grabacion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Grabaciones de Pantalla
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def grabaciones_pantalla_list_create(request, dispositivo_id):
    if request.method == 'GET':
        grabaciones = GrabacionesPantalla.objects.filter(dispositivo_id=dispositivo_id)
        serializer = GrabacionesPantallaSerializer(grabaciones, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        try:
            dispositivo = Dispositivo.objects.get(id=dispositivo_id, usuario=request.user)
        except Dispositivo.DoesNotExist:
            return Response({'error': 'Dispositivo no encontrado o no autorizado'}, status=status.HTTP_404_NOT_FOUND)

        data = request.data.copy()
        data['dispositivo'] = dispositivo.id
        serializer = GrabacionesPantallaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def grabacion_pantalla_detail(request, dispositivo_id, pk):
    try:
        grabacion = GrabacionesPantalla.objects.get(pk=pk, dispositivo_id=dispositivo_id)
    except GrabacionesPantalla.DoesNotExist:
        return Response({'error': 'Grabación de pantalla no encontrada'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GrabacionesPantallaSerializer(grabacion)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = GrabacionesPantallaSerializer(grabacion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        grabacion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Capturas de Pantalla
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def capturas_pantalla_list_create(request, dispositivo_id):
    if request.method == 'GET':
        capturas = CapturasPantalla.objects.filter(dispositivo_id=dispositivo_id)
        serializer = CapturasPantallaSerializer(capturas, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        try:
            dispositivo = Dispositivo.objects.get(id=dispositivo_id, usuario=request.user)
        except Dispositivo.DoesNotExist:
            return Response({'error': 'Dispositivo no encontrado o no autorizado'}, status=status.HTTP_404_NOT_FOUND)

        data = request.data.copy()
        data['dispositivo'] = dispositivo.id
        serializer = CapturasPantallaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def capturas_pantalla_detail(request, dispositivo_id, pk):
    try:
        captura = CapturasPantalla.objects.get(pk=pk, dispositivo_id=dispositivo_id)
    except CapturasPantalla.DoesNotExist:
        return Response({'error': 'Captura de pantalla no encontrada'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CapturasPantallaSerializer(captura)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CapturasPantallaSerializer(captura, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        captura.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Contactos
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def contactos_list_create(request, dispositivo_id):
    if request.method == 'GET':
        contactos = Contactos.objects.filter(dispositivo_id=dispositivo_id)
        serializer = ContactosSerializer(contactos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        try:
            dispositivo = Dispositivo.objects.get(id=dispositivo_id, usuario=request.user)
        except Dispositivo.DoesNotExist:
            return Response({'error': 'Dispositivo no encontrado o no autorizado'}, status=status.HTTP_404_NOT_FOUND)

        data = request.data.copy()
        data['dispositivo'] = dispositivo.id
        serializer = ContactosSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def contacto_detail(request, dispositivo_id, pk):
    try:
        contacto = Contactos.objects.get(pk=pk, dispositivo_id=dispositivo_id)
    except Contactos.DoesNotExist:
        return Response({'error': 'Contacto no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ContactosSerializer(contacto)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ContactosSerializer(contacto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        contacto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Verificación de Permisos
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def verificacion_permisos_list_create(request, dispositivo_id):
    if request.method == 'GET':
        permisos = VerificacionPermisos.objects.filter(dispositivo_id=dispositivo_id)
        serializer = VerificacionPermisosSerializer(permisos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        try:
            dispositivo = Dispositivo.objects.get(id=dispositivo_id, usuario=request.user)
        except Dispositivo.DoesNotExist:
            return Response({'error': 'Dispositivo no encontrado o no autorizado'}, status=status.HTTP_404_NOT_FOUND)

        data = request.data.copy()
        data['dispositivo'] = dispositivo.id
        serializer = VerificacionPermisosSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def verificacion_permiso_detail(request, dispositivo_id, pk):
    try:
        permiso = VerificacionPermisos.objects.get(pk=pk, dispositivo_id=dispositivo_id)
    except VerificacionPermisos.DoesNotExist:
        return Response({'error': 'Permiso no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VerificacionPermisosSerializer(permiso)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = VerificacionPermisosSerializer(permiso, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        permiso.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
<<<<<<< HEAD
    


class VerificacionPermisosListView(generics.ListAPIView):
    queryset = VerificacionPermisos.objects.all()
    serializer_class = VerificacionPermisosSerializer
=======
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


# -------------------- Vistas para renderizar páginas HTML --------------------

# Vista para la página archivo_telefono
def archivo_telefono(request):
    return render(request, 'archivo_telefono.html')

# Vista para la página capturas
def capturas(request):
    return render(request, 'capturas.html')

# Vista para la página Caracteristicas
def caracteristicas(request):
    return render(request, 'Caracteristicas.html')

# Vista para la página compras
def compras(request):
    return render(request, 'compras.html')

# Vista para la página cuenta
def cuenta(request):
    return render(request, 'cuenta.html')

# Vista para la página exportar_datos
def exportar_datos(request):
    return render(request, 'exportar_datos.html')

# Vista para la página grabacion
def grabacion(request):
    return render(request, 'grabacion.html')

# Vista para la página index
def index(request):
    return render(request, 'index.html')

# Vista para la página inicio
def inicio(request):
    return render(request, 'inicio.html')

# Vista para la página Login
def login(request):
    return render(request, 'Login.html')

# Vista para la página mi_producto
def mi_producto(request):
    return render(request, 'mi_producto.html')

# Vista para la página mis_dispositivos
def mis_dispositivos(request):
    return render(request, 'mis_dispositivos.html')

# Vista para la página panel_control
def panel_control(request):
    return render(request, 'panel_control.html')

# Vista para la página politica
def politica(request):
    return render(request, 'politica.html')

# Vista para la página preguntas
def preguntas(request):
    return render(request, 'preguntas.html')

# Vista para la página prueba
def prueba(request):
    return render(request, 'prueba.html')

# Vista para la página Productos
def productos(request):
    return render(request, 'Productos.html')

# Vista para la página recuperar_contra
def recuperar_contra(request):
    return render(request, 'recuperar_contra.html')

# Vista para la página Recursos
def recursos(request):
    return render(request, 'Recursos.html')

# Vista para la página registrarse
def registrarse(request):
    return render(request, 'registrarse.html')

<<<<<<< HEAD
=======
# Vista para la página registro
<<<<<<< HEAD
def reg_event(request):
    return render(request, 'reg_event.html')
=======
def registro(request):
    return render(request, 'registro.html')
>>>>>>> b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e

>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
# Vista para la página soporte
def soporte(request):
    return render(request, 'soporte.html')

# Vista para la página terminos
def terminos(request):
    return render(request, 'terminos.html')

# Vista para la página ubicacion
def ubicacion(request):
    return render(request, 'ubicacion.html')

# Vista para la página verificacion_permisos
def verificacion_permisos(request):
<<<<<<< HEAD
    return render(request, 'verificacion_permisos.html')
=======
<<<<<<< HEAD
    return render(request, 'verificacion_permisos.html')
=======
<<<<<<< HEAD
    return render(request, 'verificacion_permisos.html')
=======
<<<<<<< HEAD
    return render(request, 'verificacion_permisos.html')
=======
    return render(request, 'verificacion_permisos.html')
=======
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> d78f1636227f72ec3b372de20a52ae977a0beea7
>>>>>>> 052f2d3b4d3ee496a9b96224faedb68f377a196d
>>>>>>> a8d19f143da4dcdf7a22fd08e935b212cf57580a
>>>>>>> b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
>>>>>>> b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
