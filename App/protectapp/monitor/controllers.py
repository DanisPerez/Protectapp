
import logging 
import json
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework import status 
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import Dispositivo, Llamadas, Mensajes, Contactos, Fotos, Videos, Ubicaciones, GrabacionesLlamadas, GrabacionesPantalla, CapturasPantalla, Contactos, VerificacionPermisos, HistorialEvento
from .serializers import DispositivoSerializer, UserSerializer, UserRegisterSerializer, LlamadasSerializer, MensajesSerializer, ContactosSerializer, FotosSerializer, VideosSerializer, UbicacionesSerializer, GrabacionesLlamadasSerializer, GrabacionesPantallaSerializer, CapturasPantallaSerializer,VerificacionPermisosSerializer, HistorialEventoSerializer

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


from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
import logging

# Configuración básica del logger
logger = logging.getLogger(__name__)

# Inicio de sesión y obtención del token JWT
@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    email = request.data.get("email")
    password = request.data.get("password")

    logger.debug(f"Intento de inicio de sesión para: {email}")

    try:
        user = User.objects.get(email=email)
        username = user.username
        logger.debug(f"Usuario encontrado: {username}")
    except User.DoesNotExist:
        logger.warning(f"Fallo de inicio de sesión: Usuario con email {email} no encontrado")
        return Response({"detail": "Credenciales incorrectas"}, status=401)

    # Autenticar usando el nombre de usuario
    user = authenticate(username=username, password=password)
    if user is not None:
        refresh = RefreshToken.for_user(user)
        login(request, user)  # Inicia la sesión en Django
        logger.debug(f"Inicio de sesión exitoso para: {username}")
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=200)

    logger.warning(f"Fallo de inicio de sesión: Credenciales incorrectas para {username}")
    return Response({"detail": "Credenciales incorrectas"}, status=401)

# Registro de nuevos usuarios
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = UserRegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

# Actualización de perfil
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user_profile(request):
    user = request.user
    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

# Cerrar sesión e invalidar el token
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    try:
        refresh_token = request.data.get("refresh_token")
        if not refresh_token:
            return Response({"detail": "Token de refresco no proporcionado"}, status=400)
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response(status=205)
    except Exception as e:
        return Response({"detail": str(e)}, status=400)

# Obtener y actualizar datos del usuario
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


# Gestionar detalles y actualización de dispositivos
@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def dispositivo_detail_update(request, pk):
    try:
        dispositivo = Dispositivo.objects.get(pk=pk, usuario=request.user)
    except Dispositivo.DoesNotExist:
        return Response({'error': 'Dispositivo no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        # Detalles del dispositivo
        serializer = DispositivoSerializer(dispositivo)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        # Actualizar datos del dispositivo
        if 'nombre' in request.data:
            dispositivo.nombre = request.data['nombre']
            dispositivo.save()
            return Response({'message': 'Nombre del dispositivo actualizado correctamente'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'No se proporcionó un nombre para actualizar'}, status=status.HTTP_400_BAD_REQUEST)


# Gestionar dispositivos (listar y crear)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def dispositivo_list_create(request):
    if request.method == 'GET':
        # Obtener dispositivos asociados al usuario autenticado
        dispositivos = Dispositivo.objects.filter(usuario=request.user)
        serializer = DispositivoSerializer(dispositivos, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        # Crear un nuevo dispositivo asociado al usuario autenticado
        serializer = DispositivoSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def reg_event(request, id):
    # Lógica de la función reg_event
    dispositivo = Dispositivo.objects.get(id=id)
    eventos = HistorialEvento.objects.filter(dispositivo=dispositivo)

    return render(request, 'reg_event.html', {'dispositivo': dispositivo, 'eventos': eventos})

# Obtener eventos por dispositivo
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def obtener_eventos(request, dispositivo_id):
    try:
        eventos = HistorialEvento.objects.filter(dispositivo_id=dispositivo_id)
        serializer = HistorialEventoSerializer(eventos, many=True)
        return Response(serializer.data, status=200)
    except HistorialEvento.DoesNotExist:
        return Response({"error": "Dispositivo no encontrado"}, status=404)

# Obtener evento por ID
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def obtener_evento_detalle(request, id):
    try:
        evento = HistorialEvento.objects.get(id=id)
        serializer = HistorialEventoSerializer(evento)
        return Response(serializer.data, status=200)
    except HistorialEvento.DoesNotExist:
        return Response({"error": "Evento no encontrado"}, status=404)


# Get llamadas, mensajes, contactos, fotos y videos por dispositivo_id
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_llamadas(request, dispositivo_id):
    llamadas = Llamadas.objects.filter(dispositivo_id=dispositivo_id)
    serializer = LlamadasSerializer(llamadas, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_mensajes(request, dispositivo_id):
    mensajes = Mensajes.objects.filter(dispositivo_id=dispositivo_id)
    serializer = MensajesSerializer(mensajes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_contactos(request, dispositivo_id):
    contactos = Contactos.objects.filter(dispositivo_id=dispositivo_id)
    serializer = ContactosSerializer(contactos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_fotos(request, dispositivo_id):
    fotos = Fotos.objects.filter(dispositivo_id=dispositivo_id)
    serializer = FotosSerializer(fotos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_videos(request, dispositivo_id):
    videos = Videos.objects.filter(dispositivo_id=dispositivo_id)
    serializer = VideosSerializer(videos, many=True)
    return Response(serializer.data)












































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



# Views rendering Views

def archivo_telefono_view(request):
    return render(request, 'archivo_telefono.html')

def capturas_view(request):
    return render(request, 'capturas.html')

def caracteristicas_view(request):
    return render(request, 'Caracteristicas.html')

def compras_view(request):
    return render(request, 'compras.html')

def cuenta_view(request):
    return render(request, 'cuenta.html')

def exportar_datos_view(request):
    return render(request, 'exportar_datos.html')

def grabacion_view(request):
    return render(request, 'grabacion.html')

def index_view(request):
    return render(request, 'index.html')

def inicio_view(request):
    return render(request, 'inicio.html')

def login_view(request):
    return render(request, 'Login.html')

def mi_producto_view(request):
    return render(request, 'mi_producto.html')

def mis_dispositivos_view(request):
    return render(request, 'mis_dispositivos.html')

def politica_view(request):
    return render(request, 'politica.html')

def preguntas_view(request):
    return render(request, 'preguntas.html')

def productos_view(request):
    return render(request, 'Productos.html')

def prueba_view(request):
    return render(request, 'prueba.html')

def recuperar_contra_view(request):
    return render(request, 'recuperar_contra.html')

def recursos_view(request):
    return render(request, 'Recursos.html')

def reg_event_view(request):
    return render(request, 'reg_event.html')

def registrarse_view(request):
    return render(request, 'registrarse.html')

def registro_view(request):
    return render(request, 'registro.html')

def soporte_view(request):
    return render(request, 'soporte.html')

def terminos_view(request):
    return render(request, 'terminos.html')

def ubicacion_view(request):
    return render(request, 'ubicacion.html')

def verificacion_permisos_view(request):
    return render(request, 'verificacion_permisos.html')
