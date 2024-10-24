<<<<<<< HEAD
<<<<<<< HEAD
import csv
import logging 
import pandas as pd
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.http import require_http_methods
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status 
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import Dispositivo, Llamadas, Mensajes, Contactos, Fotos, Videos, Ubicaciones, GrabacionesLlamadas, GrabacionesPantalla, CapturasPantalla, VerificacionPermisos, HistorialEvento
from .serializers import DispositivoSerializer, UserSerializer, UserRegisterSerializer, LlamadasSerializer, MensajesSerializer, ContactosSerializer, FotosSerializer, VideosSerializer, UbicacionesSerializer, GrabacionesLlamadasSerializer, GrabacionesPantallaSerializer, CapturasPantallaSerializer, VerificacionPermisosSerializer, HistorialEventoSerializer

=======
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29

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
<<<<<<< HEAD
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29

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


<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
import logging

<<<<<<< HEAD
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
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


<<<<<<< HEAD
<<<<<<< HEAD







=======
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
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
<<<<<<< HEAD
<<<<<<< HEAD
    


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def eliminar_dispositivo(request, dispositivo_id):
    try:
        dispositivo = get_object_or_404(Dispositivo, id=dispositivo_id)
        dispositivo.delete()
        return Response({'mensaje': 'Dispositivo eliminado exitosamente'}, status=200)
    except Exception as e:
        return Response({'error': str(e)}, status=500)









=======
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29


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

<<<<<<< HEAD
<<<<<<< HEAD
# Recibir evento
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def registrar_evento(request, dispositivo_id):
    serializer = HistorialEventoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# mostrar llamadas
=======

# Get llamadas, mensajes, contactos, fotos y videos por dispositivo_id
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
=======

# Get llamadas, mensajes, contactos, fotos y videos por dispositivo_id
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_llamadas(request, dispositivo_id):
    llamadas = Llamadas.objects.filter(dispositivo_id=dispositivo_id)
    serializer = LlamadasSerializer(llamadas, many=True)
    return Response(serializer.data)

<<<<<<< HEAD
<<<<<<< HEAD
# Recibir llamadas
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def recibir_llamadas(request, dispositivo_id):
    serializer = LlamadasSerializer(data=request.data, many=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# mostrar mensajes
=======
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_mensajes(request, dispositivo_id):
    mensajes = Mensajes.objects.filter(dispositivo_id=dispositivo_id)
    serializer = MensajesSerializer(mensajes, many=True)
    return Response(serializer.data)

<<<<<<< HEAD
<<<<<<< HEAD
# Recibir mensajes
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def recibir_mensajes(request, dispositivo_id):
    serializer = MensajesSerializer(data=request.data, many=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# mostrar contactos
=======
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_contactos(request, dispositivo_id):
    contactos = Contactos.objects.filter(dispositivo_id=dispositivo_id)
    serializer = ContactosSerializer(contactos, many=True)
    return Response(serializer.data)

<<<<<<< HEAD
<<<<<<< HEAD
# Recibir contactos
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def recibir_contactos(request, dispositivo_id):
    serializer = ContactosSerializer(data=request.data, many=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Mostrar fotos
=======
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_fotos(request, dispositivo_id):
    fotos = Fotos.objects.filter(dispositivo_id=dispositivo_id)
    serializer = FotosSerializer(fotos, many=True)
    return Response(serializer.data)

<<<<<<< HEAD
<<<<<<< HEAD
#Recibir fotos
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def recibir_fotos(request, dispositivo_id):
    archivo = request.FILES.get('archivo_foto')  # Obtener el archivo enviado
    if archivo:
        data = request.data.copy()
        data['dispositivo'] = dispositivo_id
        data['archivo_foto'] = archivo
        serializer = FotosSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'error': 'No se proporcionó ninguna foto'}, status=status.HTTP_400_BAD_REQUEST)

# mostrar videos
=======
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_videos(request, dispositivo_id):
    videos = Videos.objects.filter(dispositivo_id=dispositivo_id)
    serializer = VideosSerializer(videos, many=True)
    return Response(serializer.data)

<<<<<<< HEAD
<<<<<<< HEAD
# Recibir videos
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def recibir_videos(request, dispositivo_id):
    videos_serializer = VideosSerializer(data=request.data, many=True)
    if videos_serializer.is_valid():
        videos_serializer.save()
        return Response(videos_serializer.data, status=status.HTTP_201_CREATED)
    return Response(videos_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Gestionar ubicaciones (listar y crear)
@api_view(['GET'])
@permission_classes([IsAuthenticated])  # Aseguramos que solo usuarios autenticados puedan acceder
def obtener_ubicaciones(request, dispositivo_id):
    try:
        # Filtrar las ubicaciones por dispositivo_id
        ubicaciones = Ubicaciones.objects.filter(dispositivo_id=dispositivo_id)
        
        # Si no se encuentran ubicaciones
        if not ubicaciones:
            return Response({'error': 'No se encontraron ubicaciones para este dispositivo'}, status=status.HTTP_404_NOT_FOUND)

        # Serializar los datos utilizando UbicacionesSerializer
        serializer = UbicacionesSerializer(ubicaciones, many=True)
        
        # Retornar los datos serializados como JSON
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Ubicaciones.DoesNotExist:
        return Response({'error': 'No se encontraron ubicaciones'}, status=status.HTTP_404_NOT_FOUND)

# recibir la ubicación del dispositivo 
@api_view(['POST'])
@permission_classes([IsAuthenticated])  # Aseguramos que solo usuarios autenticados puedan acceder
def enviar_ubicacion(request, dispositivo_id):
    serializer = UbicacionesSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Crear y listar grabaciones de llamadas (audio)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def grabaciones_llamadas_list_create(request, dispositivo_id):
    if request.method == 'GET':
        grabaciones = GrabacionesLlamadas.objects.filter(dispositivo_id=dispositivo_id)
        serializer = GrabacionesLlamadasSerializer(grabaciones, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        archivo = request.FILES.get('archivo_audio')  # Obtener el archivo enviado
        if archivo:
            data = request.data.copy()
            data['dispositivo'] = dispositivo_id
            data['archivo_audio'] = archivo
            serializer = GrabacionesLlamadasSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        return Response({'error': 'No se proporcionó ningún archivo de audio'}, status=400)

# Detalle, actualización y eliminación de una grabación de llamada específica
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def grabacion_llamada_detail(request, dispositivo_id, pk):
    try:
        grabacion = GrabacionesLlamadas.objects.get(pk=pk, dispositivo_id=dispositivo_id)
    except GrabacionesLlamadas.DoesNotExist:
        return Response({'error': 'Grabación de llamada no encontrada'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Detalle de la grabación
        serializer = GrabacionesLlamadasSerializer(grabacion)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # Actualizar (ej: detener la grabación)
        data = request.data.copy()
        if 'estado' in data and data['estado'] == 'completada':
            data['estado'] = 'completada'  # Marcar la grabación como completada
        serializer = GrabacionesLlamadasSerializer(grabacion, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # Eliminar la grabación
        grabacion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Crear y listar grabaciones de pantalla (video)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def grabaciones_pantalla_list_create(request, dispositivo_id):
    if request.method == 'GET':
        grabaciones = GrabacionesPantalla.objects.filter(dispositivo_id=dispositivo_id)
        serializer = GrabacionesPantallaSerializer(grabaciones, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        archivo = request.FILES.get('archivo_video')  # Obtener el archivo enviado
        if archivo:
            data = request.data.copy()
            data['dispositivo'] = dispositivo_id
            data['archivo_video'] = archivo
            serializer = GrabacionesPantallaSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        return Response({'error': 'No se proporcionó ningún archivo de video'}, status=400)

# Detalle, actualización y eliminación de una grabación de pantalla específica
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def grabacion_pantalla_detail(request, dispositivo_id, pk):
    try:
        grabacion = GrabacionesPantalla.objects.get(pk=pk, dispositivo_id=dispositivo_id)
    except GrabacionesPantalla.DoesNotExist:
        return Response({'error': 'Grabación de pantalla no encontrada'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Detalle de la grabación
        serializer = GrabacionesPantallaSerializer(grabacion)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # Actualizar (ej: detener la grabación)
        data = request.data.copy()
        if 'estado' in data and data['estado'] == 'completada':
            data['estado'] = 'completada'  # Marcar la grabación como completada
        serializer = GrabacionesPantallaSerializer(grabacion, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # Eliminar la grabación
        grabacion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Iniciar grabación de llamada
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def iniciar_grabacion_llamada(request, dispositivo_id):
    # Lógica para iniciar la grabación de llamada
    return Response({'message': 'Grabación de llamada iniciada'}, status=status.HTTP_200_OK)

# Detener grabación de llamada
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def detener_grabacion_llamada(request, dispositivo_id):
    # Lógica para detener la grabación de llamada
    return Response({'message': 'Grabación de llamada detenida'}, status=status.HTTP_200_OK)

# Iniciar grabación de pantalla
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def iniciar_grabacion_pantalla(request, dispositivo_id):
    # Lógica para iniciar la grabación de pantalla
    return Response({'message': 'Grabación de pantalla iniciada'}, status=status.HTTP_200_OK)

# Detener grabación de pantalla
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def detener_grabacion_pantalla(request, dispositivo_id):
    # Lógica para detener la grabación de pantalla
    return Response({'message': 'Grabación de pantalla detenida'}, status=status.HTTP_200_OK)

# Ruta para ver la grabación de llamada y de pantalla
def grabacion_view(request, dispositivo_id):
    grabaciones_llamadas = GrabacionesLlamadas.objects.filter(dispositivo_id=dispositivo_id)
    grabaciones_pantalla = GrabacionesPantalla.objects.filter(dispositivo_id=dispositivo_id)
    
    # Depuración
    print(f"Grabaciones de llamadas: {grabaciones_llamadas}")
    print(f"Grabaciones de pantalla: {grabaciones_pantalla}")

    return render(request, 'grabacion.html', {
        'grabaciones_llamadas': grabaciones_llamadas,
        'grabaciones_pantalla': grabaciones_pantalla,
    })

#------------------------------------------------------------------------------

#Crear y listar capturas de pantalla
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def capturas_pantalla_list_create(request, dispositivo_id):
    if request.method == 'GET':
        capturas = CapturasPantalla.objects.filter(dispositivo_id=dispositivo_id)
        serializer = CapturasPantallaSerializer(capturas, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        archivo = request.FILES.get('archivo_captura')  # Obtener el archivo enviado
        if archivo:
            data = request.data.copy()
            data['dispositivo'] = dispositivo_id
            data['archivo_captura'] = archivo
            serializer = CapturasPantallaSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        return Response({'error': 'No se proporcionó ninguna captura'}, status=400)

# Crear y listar fotos
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def fotos_list_create(request, dispositivo_id):
    if request.method == 'GET':
        fotos = Fotos.objects.filter(dispositivo_id=dispositivo_id)
        serializer = FotosSerializer(fotos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        archivo = request.FILES.get('archivo_foto')  # Obtener el archivo enviado
        if archivo:
            data = request.data.copy()
            data['dispositivo'] = dispositivo_id
            data['archivo_foto'] = archivo
            serializer = FotosSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        return Response({'error': 'No se proporcionó ninguna foto'}, status=400)

# Vista para las capturas
def capturas_view(request, dispositivo_id):
    capturas_pantalla = CapturasPantalla.objects.filter(dispositivo_id=dispositivo_id)
    fotos = Fotos.objects.filter(dispositivo_id=dispositivo_id)
    
    return render(request, 'capturas.html', {
        'capturas_pantalla': capturas_pantalla,
        'fotos': fotos,
    })


#------------------------------------------------------------------------------



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


# Función para obtener los permisos de un dispositivo móvil
def obtener_permisos(request, dispositivo_id):
    try:
        permisos = VerificacionPermisos.objects.filter(dispositivo_id=dispositivo_id)
        if not permisos.exists():
            return JsonResponse({"error": "No se encontraron permisos para este dispositivo."}, status=404)
        permisos_data = list(permisos.values(
            'permiso', 'tipo_permiso', 'estado_permiso', 'critico', 'fecha_verificacion'
        ))
        return JsonResponse(permisos_data, safe=False)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


# Función para solicitar un permiso para un dispositivo específico
@login_required
@require_POST  
def solicitar_permiso(request, dispositivo_id, permiso_id):
    try:
        dispositivo = Dispositivo.objects.get(id=dispositivo_id, usuario=request.user)
        permiso = VerificacionPermisos.objects.get(id=permiso_id, dispositivo=dispositivo)
        estado_solicitado = request.POST.get('estado_permiso', 'True') 
        permiso.estado_permiso = estado_solicitado == 'True'
        permiso.fecha_verificacion = timezone.now()
        permiso.save()
        return JsonResponse({"message": f"Permiso '{permiso.permiso}' actualizado exitosamente a {'Concedido' if permiso.estado_permiso else 'Denegado'}."}, status=200)

    except VerificacionPermisos.DoesNotExist:
        nuevo_permiso = VerificacionPermisos.objects.create(
            dispositivo=dispositivo,
            permiso=request.POST.get('permiso', 'Permiso no especificado'),  
            estado_permiso=request.POST.get('estado_permiso', 'True') == 'True',  
            tipo_permiso=request.POST.get('tipo_permiso', 'Desconocido'),  
            critico=request.POST.get('critico', False), 
            clave_sistema=request.POST.get('clave_sistema', ''), 
            fecha_verificacion=timezone.now() 
        )
        return JsonResponse({"message": f"Permiso '{nuevo_permiso.permiso}' creado y concedido."}, status=201)
    except Dispositivo.DoesNotExist:
        return JsonResponse({"error": "Dispositivo no encontrado."}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
=======
=======











>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
































<<<<<<< HEAD






>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04





=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
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
