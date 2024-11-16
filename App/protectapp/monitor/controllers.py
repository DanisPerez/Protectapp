import csv
import logging 
import pandas as pd
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Fotos
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from rest_framework.parsers import MultiPartParser
from django.db.models import Count
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.http import require_http_methods
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status 
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.response import Response

from .models import Dispositivo, Llamadas, Mensajes, Contactos, Fotos, Videos, Ubicaciones, GrabacionesLlamadas, GrabacionesPantalla, CapturasPantalla, VerificacionPermisos, HistorialEvento, Evento
from .serializers import DispositivoSerializer, UserSerializer, UserRegisterSerializer, LlamadasSerializer, MensajesSerializer, ContactosSerializer, FotosSerializer, VideosSerializer, UbicacionesSerializer, GrabacionesLlamadasSerializer, GrabacionesPantallaSerializer, CapturasPantallaSerializer, VerificacionPermisosSerializer, HistorialEventoSerializer


# ----------------------------------------------------
# API Overview
# ----------------------------------------------------

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


# Configuración básica del logger
logger = logging.getLogger(__name__)

# ----------------------------------------------------
# Autenticación de Usuarios
# ----------------------------------------------------

# Inicio de sesión y obtención del token JWT
@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    email = request.data.get("email")
    password = request.data.get("password")

    # Validación de campos
    if not email or not password:
        logger.warning("Campos de email o contraseña faltantes")
        return Response({"detail": "Email y contraseña son requeridos"}, status=status.HTTP_400_BAD_REQUEST)

    logger.debug(f"Intento de inicio de sesión para: {email}")

    try:
        # Intentar obtener el usuario basado en el email
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        logger.warning(f"Usuario con email {email} no encontrado")
        return Response({"detail": "Credenciales incorrectas"}, status=status.HTTP_401_UNAUTHORIZED)

    # Autenticación con el nombre de usuario (Django usa `username` por defecto)
    user = authenticate(username=user.username, password=password)
    if user is not None:
        # Crear y devolver los tokens JWT
        refresh = RefreshToken.for_user(user)
        login(request, user)  # Opcional: solo necesario si necesitas mantener sesión en Django
        logger.debug(f"Inicio de sesión exitoso para: {user.username}")
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)

    # Mensaje de error si las credenciales son incorrectas
    logger.warning(f"Fallo de inicio de sesión: Credenciales incorrectas para {user.username}")
    return Response({"detail": "Credenciales incorrectas"}, status=status.HTTP_401_UNAUTHORIZED)


# ----------------------------------------------------
# Perfil de Usuario
# ----------------------------------------------------

# Registro de nuevos usuarios
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = UserRegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Registro exitoso"}, status=201)
    # Retorna el error del serializer si hay algún problema (por ejemplo, correo duplicado)
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
    








# ----------------------------------------------------
# pagina mi Inicio
# ----------------------------------------------------

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dispositivos_activos(request):
    # Filtrar dispositivos activos con estado=True
    cantidad_activos = Dispositivo.objects.filter(usuario=request.user, estado=True).count()
    return Response({"cantidad": cantidad_activos})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def eventos_totales(request):
    # Filtrar dispositivos asociados al usuario autenticado
    dispositivos = Dispositivo.objects.filter(usuario=request.user)
    
    # Asegúrate de que los dispositivos filtrados no estén vacíos
    if not dispositivos.exists():
        return Response({"total": 0})

    # Contar todos los eventos asociados a los dispositivos del usuario
    total_eventos = HistorialEvento.objects.filter(dispositivo__in=dispositivos).count()
    
    # Retornar el conteo total de eventos en formato JSON
    return Response({"total": total_eventos})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ultima_actividad_usuario(request):
    # Busca el evento más reciente del usuario en cualquiera de sus dispositivos
    ultimo_evento = HistorialEvento.objects.filter(usuario=request.user).order_by('-fecha', '-hora').first()
    
    if ultimo_evento:
        # Devuelve la fecha y hora del evento más reciente
        return Response({
            "ultima_actividad": f"{ultimo_evento.fecha} {ultimo_evento.hora}",
            "detalle": ultimo_evento.tipo_evento
        })
    else:
        # Si no hay eventos, retorna un mensaje indicativo
        return Response({"ultima_actividad": "Sin actividad registrada", "detalle": None})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listar_dispositivos(request):
    dispositivos = Dispositivo.objects.filter(usuario=request.user)
    serializer = DispositivoSerializer(dispositivos, many=True)
    return Response(serializer.data)




# ----------------------------------------------------














# ----------------------------------------------------
# pagina mi producto
# ----------------------------------------------------

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile(request):
    """
    Endpoint que devuelve los datos completos del usuario autenticado.
    """
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)

# ----------------------------------------------------


# ----------------------------------------------------
# Actualización del Perfil de Usuario
# ----------------------------------------------------

# Obtener y actualizar datos del usuario
@api_view(['GET', 'PUT', 'DELETE'])
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
        data = request.data
        if 'nombre' in data:
            user.username = data['nombre']
        if 'password' in data and data['password']:
            user.set_password(data['password'])  
        user.save()

        return Response({
            'message': 'Usuario actualizado correctamente'
        }, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        # Eliminar (o desactivar) el usuario
        user.delete()  # Esto elimina al usuario permanentemente de la base de datos
        return Response({
            'message': 'Usuario eliminado correctamente'
        }, status=status.HTTP_204_NO_CONTENT)


# ----------------------------------------------------
# Página Mis Dispositivos
# ----------------------------------------------------

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
            serializer.save(usuario=request.user)  # Asocia el dispositivo al usuario autenticado
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Eliminar un dispositivo
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def eliminar_dispositivo(request, dispositivo_id):
    try:
        dispositivo = get_object_or_404(Dispositivo, id=dispositivo_id, usuario=request.user)
        dispositivo.delete()
        return Response({'mensaje': 'Dispositivo eliminado exitosamente'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Crear un dispositivo al finalizar la configuración de permisos
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def crear_dispositivo_despues_configuracion(request):
    """
    Crea un nuevo dispositivo al finalizar la configuración de permisos.
    Asocia el dispositivo al usuario autenticado.
    """
    data = request.data.copy()
    data['usuario'] = request.user.id  # Asociar el dispositivo al usuario autenticado
    
    serializer = DispositivoSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)








# ----------------------------------------------------
# Pagina Registros
# ----------------------------------------------------

# Renderizar la vista de eventos desde el backend (si es necesario)
def reg_event(request, id):
    dispositivo = get_object_or_404(Dispositivo, id=id)
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
        return Response({"error": "No se encontraron eventos para este dispositivo"}, status=404)

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

# Registrar evento
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def registrar_evento(request, dispositivo_id):
    serializer = HistorialEventoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from monitor.models import Dispositivo

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def eliminar_evento(request, pk):
    # Obtener el evento
    evento = get_object_or_404(HistorialEvento, pk=pk)

    # Obtener el dispositivo asociado al evento
    dispositivo = evento.dispositivo

    # Verificar si el usuario autenticado es el propietario del dispositivo o un superusuario
    if dispositivo.usuario != request.user and not request.user.is_superuser:
        return JsonResponse({'error': 'No tienes permiso para eliminar este evento.'}, status=403)

    # Si tiene permiso, elimina el evento
    evento.delete()
    return JsonResponse({'message': 'Evento eliminado correctamente.'}, status=204)



# ----------------------------------------------------
# Pagina Archivos de teléfono
# ----------------------------------------------------

# Mostrar llamadas
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_llamadas(request, dispositivo_id):
    llamadas = Llamadas.objects.filter(dispositivo_id=dispositivo_id)
    serializer = LlamadasSerializer(llamadas, many=True)
    return Response(serializer.data)

# Recibir llamadas
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def recibir_llamadas(request, dispositivo_id):
    # Pasar dispositivo_id al contexto del serializador
    serializer = LlamadasSerializer(data=request.data, many=True, context={'dispositivo_id': dispositivo_id})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Mostrar mensajes
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_mensajes(request, dispositivo_id):
    mensajes = Mensajes.objects.filter(dispositivo_id=dispositivo_id)
    serializer = MensajesSerializer(mensajes, many=True)
    return Response(serializer.data)

# Recibir mensajes
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def recibir_mensajes(request, dispositivo_id):
    # Asigna dispositivo_id a cada mensaje en request.data
    for mensaje in request.data:
        mensaje['dispositivo'] = dispositivo_id

    serializer = MensajesSerializer(data=request.data, many=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Mostrar contactos
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_contactos(request, dispositivo_id):
    contactos = Contactos.objects.filter(dispositivo_id=dispositivo_id)
    serializer = ContactosSerializer(contactos, many=True)
    return Response(serializer.data)

# Recibir contactos
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def recibir_contactos(request, dispositivo_id):
    for contacto in request.data:
        contacto['dispositivo'] = dispositivo_id  # Asigna dispositivo_id a cada contacto
    serializer = ContactosSerializer(data=request.data, many=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Mostrar fotos
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_fotos(request, dispositivo_id):
    fotos = Fotos.objects.filter(dispositivo_id=dispositivo_id)
    serializer = FotosSerializer(fotos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser])  # Agregado para manejar archivos de imágenes
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

# Mostrar videos
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_videos(request, dispositivo_id):
    videos = Videos.objects.filter(dispositivo_id=dispositivo_id)
    serializer = VideosSerializer(videos, many=True)
    return Response(serializer.data)

# Recibir videos
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def recibir_videos(request, dispositivo_id):
    videos_serializer = VideosSerializer(data=request.data, many=True)
    if videos_serializer.is_valid():
        videos_serializer.save()
        return Response(videos_serializer.data, status=status.HTTP_201_CREATED)
    return Response(videos_serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# ----------------------------------------------------
# Pagina de ubicaciones
# ----------------------------------------------------

# Listar ubicaciones de un dispositivo específico
@api_view(['GET'])
@permission_classes([IsAuthenticated])  # Solo usuarios autenticados pueden acceder
def obtener_ubicaciones(request, dispositivo_id):
    try:
        # Filtrar las ubicaciones por dispositivo_id
        ubicaciones = Ubicaciones.objects.filter(dispositivo_id=dispositivo_id)
        
        # Si no se encuentran ubicaciones
        if not ubicaciones.exists():
            return Response({'error': 'No se encontraron ubicaciones para este dispositivo'}, status=status.HTTP_404_NOT_FOUND)

        # Serializar los datos utilizando UbicacionesSerializer
        serializer = UbicacionesSerializer(ubicaciones, many=True)
        
        # Retornar los datos serializados como JSON
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Recibir y almacenar la ubicación del dispositivo 
@api_view(['POST'])
@permission_classes([IsAuthenticated])  # Solo usuarios autenticados pueden acceder
def enviar_ubicacion(request, dispositivo_id):
    # Crear un nuevo registro de ubicación asociado al dispositivo
    serializer = UbicacionesSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save(dispositivo_id=dispositivo_id)  # Asociar la ubicación con el dispositivo
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





# ----------------------------------------------------
# Pagina de grabaciones
# ----------------------------------------------------

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
    grabacion = get_object_or_404(GrabacionesLlamadas, pk=pk, dispositivo_id=dispositivo_id)

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
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        # Eliminar la grabación
        grabacion.delete()
        return Response(status=204)

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
    grabacion = get_object_or_404(GrabacionesPantalla, pk=pk, dispositivo_id=dispositivo_id)

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
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        grabacion.delete()
        return Response(status=204)

# Iniciar grabación de llamada
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def iniciar_grabacion_llamada(request, dispositivo_id):
    return Response({'message': 'Grabación de llamada iniciada'}, status=200)

# Detener grabación de llamada
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def detener_grabacion_llamada(request, dispositivo_id):
    return Response({'message': 'Grabación de llamada detenida'}, status=200)

# Iniciar grabación de pantalla
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def iniciar_grabacion_pantalla(request, dispositivo_id):
    return Response({'message': 'Grabación de pantalla iniciada'}, status=200)

# Detener grabación de pantalla
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def detener_grabacion_pantalla(request, dispositivo_id):
    return Response({'message': 'Grabación de pantalla detenida'}, status=200)




# ----------------------------------------------------
# Pagina Capturas
# ----------------------------------------------------

# Crear y listar capturas de pantalla
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def capturas_pantalla_list_create(request, dispositivo_id):
    if request.method == 'GET':
        capturas = CapturasPantalla.objects.filter(dispositivo_id=dispositivo_id)
        serializer = CapturasPantallaSerializer(capturas, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        archivo = request.FILES.get('archivo_captura')  # Obtener el archivo enviado (si existe)
        
        if archivo:
            data = request.data.copy()
            data['dispositivo'] = dispositivo_id
            data['archivo_captura'] = archivo
            serializer = CapturasPantallaSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)

        # Simulación si no hay archivo
        captura_simulada = {
            "id": 999,
            "dispositivo": dispositivo_id,
            "archivo_captura": "/media/simulada/captura.png",
            "fecha": "2024-10-29",
            "hora": "15:30:00"
        }
        return Response(captura_simulada, status=201)

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

        # Simulación si no hay archivo
        foto_simulada = {
            "id": 1000,
            "dispositivo": dispositivo_id,
            "archivo_foto": "/media/simulada/foto.png",
            "fecha": "2024-10-29",
            "hora": "15:35:00"
        }
        return Response(foto_simulada, status=201)






# ----------------------------------------------------
# Pagina Exportar Datos 
# ----------------------------------------------------

# Función para exportar los datos de los dispositivos a un archivo CSV
@api_view(['GET'])
@permission_classes([IsAuthenticated])
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

# Función para exportar los datos de los dispositivos a un archivo Excel
@api_view(['GET'])
@permission_classes([IsAuthenticated])
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

# Función para exportar los datos de los dispositivos a un archivo PDF
@api_view(['GET'])
@permission_classes([IsAuthenticated])
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




# ----------------------------------------------------
# Pagina Verificación de Permisos
# ----------------------------------------------------

# Función para obtener los permisos de un dispositivo móvil
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def obtener_permisos(request, dispositivo_id):
    try:
        permisos = VerificacionPermisos.objects.filter(dispositivo_id=dispositivo_id)
        if not permisos.exists():
            return Response({"error": "No se encontraron permisos para este dispositivo."}, status=status.HTTP_404_NOT_FOUND)

        permisos_data = [
            {
                "id": permiso.id,
                "permiso": permiso.permiso,
                "estado_permiso": permiso.estado_permiso,
                "critico": permiso.critico,
                "fecha_verificacion": permiso.fecha_verificacion,
                "instrucciones": permiso.get_instructions()  # Obtener instrucciones detalladas
            }
            for permiso in permisos
        ]
        return Response(permisos_data, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Función para solicitar un permiso para un dispositivo específico
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def actualizar_permiso(request):
    try:
        dispositivo_id = request.data.get("dispositivo_id")
        tipo_permiso = request.data.get("tipo_permiso")
        estado_permiso = request.data.get("estado_permiso")

        dispositivo = get_object_or_404(Dispositivo, id=dispositivo_id, usuario=request.user)
        permiso, created = VerificacionPermisos.objects.update_or_create(
            dispositivo=dispositivo,
            permiso=tipo_permiso,
            defaults={'estado_permiso': estado_permiso, 'fecha_verificacion': timezone.now()}
        )

        mensaje = "Permiso creado y actualizado exitosamente" if created else "Permiso actualizado exitosamente"
        return Response({"message": mensaje}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



# ----------------------------------------------------
# CRUD for Dispositivo
# ----------------------------------------------------
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dispositivo_list(request):
    dispositivos = Dispositivo.objects.filter(usuario=request.user)
    serializer = DispositivoSerializer(dispositivos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dispositivo_detail(request, pk):
    dispositivo = get_object_or_404(Dispositivo, id=pk, usuario=request.user)
    serializer = DispositivoSerializer(dispositivo)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def dispositivo_create(request):
    serializer = DispositivoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(usuario=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def dispositivo_update(request, pk):
    dispositivo = get_object_or_404(Dispositivo, id=pk, usuario=request.user)
    serializer = DispositivoSerializer(instance=dispositivo, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def dispositivo_delete(request, pk):
    dispositivo = get_object_or_404(Dispositivo, id=pk, usuario=request.user)
    dispositivo.delete()
    return Response({"message": "Dispositivo eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)

# ----------------------------------------------------
# CRUD for Llamadas
# ----------------------------------------------------
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def llamadas_list(request):
    llamadas = Llamadas.objects.filter(usuario=request.user)
    serializer = LlamadasSerializer(llamadas, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def llamadas_detail(request, pk):
    llamadas = get_object_or_404(Llamadas, id=pk, usuario=request.user)
    serializer = LlamadasSerializer(llamadas)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def llamadas_create(request):
    serializer = LlamadasSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(usuario=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def llamadas_update(request, pk):
    llamadas = get_object_or_404(Llamadas, id=pk, usuario=request.user)
    serializer = LlamadasSerializer(instance=llamadas, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def llamadas_delete(request, pk):
    llamadas = get_object_or_404(Llamadas, id=pk, usuario=request.user)
    llamadas.delete()
    return Response({"message": "Llamada eliminada correctamente"}, status=status.HTTP_204_NO_CONTENT)

# ----------------------------------------------------
# CRUD for Mensajes
# ----------------------------------------------------
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def mensajes_list(request):
    mensajes = Mensajes.objects.filter(usuario=request.user)
    serializer = MensajesSerializer(mensajes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def mensajes_detail(request, pk):
    mensajes = get_object_or_404(Mensajes, id=pk, usuario=request.user)
    serializer = MensajesSerializer(mensajes)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def mensajes_create(request):
    serializer = MensajesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(usuario=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def mensajes_update(request, pk):
    mensajes = get_object_or_404(Mensajes, id=pk, usuario=request.user)
    serializer = MensajesSerializer(instance=mensajes, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def mensajes_delete(request, pk):
    mensajes = get_object_or_404(Mensajes, id=pk, usuario=request.user)
    mensajes.delete()
    return Response({"message": "Mensaje eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)

# ----------------------------------------------------
# CRUD for Contactos
# ----------------------------------------------------
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def contactos_list(request):
    contactos = Contactos.objects.filter(usuario=request.user)
    serializer = ContactosSerializer(contactos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def contactos_detail(request, pk):
    contactos = get_object_or_404(Contactos, id=pk, usuario=request.user)
    serializer = ContactosSerializer(contactos)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def contactos_create(request):
    serializer = ContactosSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(usuario=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def contactos_update(request, pk):
    contactos = get_object_or_404(Contactos, id=pk, usuario=request.user)
    serializer = ContactosSerializer(instance=contactos, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def contactos_delete(request, pk):
    contactos = get_object_or_404(Contactos, id=pk, usuario=request.user)
    contactos.delete()
    return Response({"message": "Contacto eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)

# ----------------------------------------------------
# CRUD for Fotos
# ----------------------------------------------------
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fotos_list(request):
    fotos = Fotos.objects.filter(usuario=request.user)
    serializer = FotosSerializer(fotos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fotos_detail(request, pk):
    fotos = get_object_or_404(Fotos, id=pk, usuario=request.user)
    serializer = FotosSerializer(fotos)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def fotos_create(request):
    serializer = FotosSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(usuario=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def fotos_update(request, pk):
    fotos = get_object_or_404(Fotos, id=pk, usuario=request.user)
    serializer = FotosSerializer(instance=fotos, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def fotos_delete(request, pk):
    fotos = get_object_or_404(Fotos, id=pk, usuario=request.user)
    fotos.delete()
    return Response({"message": "Foto eliminada correctamente"}, status=status.HTTP_204_NO_CONTENT)

# ----------------------------------------------------
# CRUD for Videos
# ----------------------------------------------------
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def videos_list(request):
    videos = Videos.objects.filter(usuario=request.user)
    serializer = VideosSerializer(videos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def videos_detail(request, pk):
    videos = get_object_or_404(Videos, id=pk, usuario=request.user)
    serializer = VideosSerializer(videos)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def videos_create(request):
    serializer = VideosSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(usuario=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def videos_update(request, pk):
    videos = get_object_or_404(Videos, id=pk, usuario=request.user)
    serializer = VideosSerializer(instance=videos, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def videos_delete(request, pk):
    videos = get_object_or_404(Videos, id=pk, usuario=request.user)
    videos.delete()
    return Response({"message": "Video eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)

# ----------------------------------------------------
# CRUD for Ubicaciones
# ----------------------------------------------------
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ubicaciones_list(request):
    ubicaciones = Ubicaciones.objects.filter(usuario=request.user)
    serializer = UbicacionesSerializer(ubicaciones, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ubicaciones_detail(request, pk):
    ubicaciones = get_object_or_404(Ubicaciones, id=pk, usuario=request.user)
    serializer = UbicacionesSerializer(ubicaciones)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def ubicaciones_create(request):
    serializer = UbicacionesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(usuario=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def ubicaciones_update(request, pk):
    ubicaciones = get_object_or_404(Ubicaciones, id=pk, usuario=request.user)
    serializer = UbicacionesSerializer(instance=ubicaciones, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def ubicaciones_delete(request, pk):
    ubicaciones = get_object_or_404(Ubicaciones, id=pk, usuario=request.user)
    ubicaciones.delete()
    return Response({"message": "Ubicación eliminada correctamente"}, status=status.HTTP_204_NO_CONTENT)

# ----------------------------------------------------
# CRUD for Grabaciones de Llamadas
# ----------------------------------------------------
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def grabaciones_llamadas_list(request):
    grabaciones = GrabacionesLlamadas.objects.filter(usuario=request.user)
    serializer = GrabacionesLlamadasSerializer(grabaciones, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def grabaciones_llamadas_detail(request, pk):
    grabaciones = get_object_or_404(GrabacionesLlamadas, id=pk, usuario=request.user)
    serializer = GrabacionesLlamadasSerializer(grabaciones)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def grabaciones_llamadas_create(request):
    serializer = GrabacionesLlamadasSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(usuario=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def grabaciones_llamadas_update(request, pk):
    grabaciones = get_object_or_404(GrabacionesLlamadas, id=pk, usuario=request.user)
    serializer = GrabacionesLlamadasSerializer(instance=grabaciones, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def grabaciones_llamadas_delete(request, pk):
    grabaciones = get_object_or_404(GrabacionesLlamadas, id=pk, usuario=request.user)
    grabaciones.delete()
    return Response({"message": "Grabación de llamada eliminada correctamente"}, status=status.HTTP_204_NO_CONTENT)

# ----------------------------------------------------
# CRUD for Grabaciones de Pantalla
# ----------------------------------------------------
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def grabaciones_pantalla_list(request):
    grabaciones = GrabacionesPantalla.objects.filter(usuario=request.user)
    serializer = GrabacionesPantallaSerializer(grabaciones, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def grabaciones_pantalla_detail(request, pk):
    grabaciones = get_object_or_404(GrabacionesPantalla, id=pk, usuario=request.user)
    serializer = GrabacionesPantallaSerializer(grabaciones)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def grabaciones_pantalla_create(request):
    serializer = GrabacionesPantallaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(usuario=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def grabaciones_pantalla_update(request, pk):
    grabaciones = get_object_or_404(GrabacionesPantalla, id=pk, usuario=request.user)
    serializer = GrabacionesPantallaSerializer(instance=grabaciones, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def grabaciones_pantalla_delete(request, pk):
    grabaciones = get_object_or_404(GrabacionesPantalla, id=pk, usuario=request.user)
    grabaciones.delete()
    return Response({"message": "Grabación de pantalla eliminada correctamente"}, status=status.HTTP_204_NO_CONTENT)

# ----------------------------------------------------
# CRUD for Capturas de Pantalla
# ----------------------------------------------------
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def capturas_pantalla_list(request):
    capturas = CapturasPantalla.objects.filter(usuario=request.user)
    serializer = CapturasPantallaSerializer(capturas, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def capturas_pantalla_detail(request, pk):
    capturas = get_object_or_404(CapturasPantalla, id=pk, usuario=request.user)
    serializer = CapturasPantallaSerializer(capturas)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def capturas_pantalla_create(request):
    serializer = CapturasPantallaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(usuario=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def capturas_pantalla_update(request, pk):
    capturas = get_object_or_404(CapturasPantalla, id=pk, usuario=request.user)
    serializer = CapturasPantallaSerializer(instance=capturas, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def capturas_pantalla_delete(request, pk):
    capturas = get_object_or_404(CapturasPantalla, id=pk, usuario=request.user)
    capturas.delete()
    return Response({"message": "Captura de pantalla eliminada correctamente"}, status=status.HTTP_204_NO_CONTENT)

# ----------------------------------------------------
# CRUD for VerificacionPermisos
# ----------------------------------------------------
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def permisos_list(request):
    permisos = VerificacionPermisos.objects.filter(usuario=request.user)
    serializer = VerificacionPermisosSerializer(permisos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def permisos_detail(request, pk):
    permisos = get_object_or_404(VerificacionPermisos, id=pk, usuario=request.user)
    serializer = VerificacionPermisosSerializer(permisos)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def permisos_create(request):
    serializer = VerificacionPermisosSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(usuario=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def permisos_update(request, pk):
    permisos = get_object_or_404(VerificacionPermisos, id=pk, usuario=request.user)
    serializer = VerificacionPermisosSerializer(instance=permisos, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def permisos_delete(request, pk):
    permisos = get_object_or_404(VerificacionPermisos, id=pk, usuario=request.user)
    permisos.delete()
    return Response({"message": "Permiso eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)

# ----------------------------------------------------
# CRUD for HistorialEvento
# ----------------------------------------------------
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def historial_evento_list(request):
    historial = HistorialEvento.objects.filter(usuario=request.user)
    serializer = HistorialEventoSerializer(historial, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def historial_evento_detail(request, pk):
    historial = get_object_or_404(HistorialEvento, id=pk, usuario=request.user)
    serializer = HistorialEventoSerializer(historial)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def historial_evento_create(request):
    serializer = HistorialEventoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(usuario=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def historial_evento_update(request, pk):
    historial = get_object_or_404(HistorialEvento, id=pk, usuario=request.user)
    serializer = HistorialEventoSerializer(instance=historial, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def historial_evento_delete(request, pk):
    historial = get_object_or_404(HistorialEvento, id=pk, usuario=request.user)
    historial.delete()
    return Response({"message": "Historial de evento eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)
