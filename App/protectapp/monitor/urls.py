from django.views.generic import TemplateView
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from .controllers import (
    login_user, register_user, update_user_profile, logout_user,
    dispositivo_list_create, get_user_data, 
    obtener_eventos, obtener_evento_detalle, dispositivo_detail_update,
    get_llamadas, get_mensajes, get_contactos, get_fotos, get_videos, 
    obtener_ubicaciones, enviar_ubicacion, recibir_llamadas, recibir_mensajes, 
    recibir_contactos, recibir_fotos, recibir_videos, registrar_evento, capturas_pantalla_list_create, 
    fotos_list_create, exportar_datos_csv, exportar_datos_excel, exportar_datos_pdf, 
    obtener_permisos, solicitar_permiso, eliminar_dispositivo
)

from . import controllers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)




# API Endpoints for CRUD operations and overview
urlpatterns = [
    # API Overview
    path('api/', controllers.api_overview, name='api-overview'),


    # Rutas para la autenticación con JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),






    path('api/dispositivos/activos/', controllers.dispositivos_activos, name='dispositivos-activos'),
    path('api/eventos/totales/', controllers.eventos_totales, name='eventos-totales'),
    path('api/actividad/ultima/', controllers.ultima_actividad_usuario, name='ultima_actividad_usuario'),






    # Rutas para autenticación y perfil de usuarios
    path('api/login/', login_user, name='login'),
    path('api/register/', register_user, name='register'),
    path('api/profile/update/', update_user_profile, name='profile-update'),
    path('api/logout/', logout_user, name='logout'),
    path('api/user/', get_user_data, name='get_user_data'),
    path('api/user/profile/', controllers.get_user_profile, name='user-profile'),

    # Ruta para listar y crear dispositivos
    path('api/dispositivos/', dispositivo_list_create, name='dispositivos-list-create'),
    # Ruta para obtener detalles de un dispositivo específico y actualizarlo
    path('api/dispositivos/<int:pk>/', dispositivo_detail_update, name='dispositivo-detail-update'),
    # Ruta para eliminar un dispositivo
    path('api/dispositivos/delete/<int:dispositivo_id>/', eliminar_dispositivo, name='eliminar_dispositivo'),


    # Ruta para obtener eventos por dispositivo
    path('api/dispositivos/<int:dispositivo_id>/eventos/', obtener_eventos, name='obtener_eventos'),
    # Ruta para obtener el detalle de un evento por ID
    path('api/eventos/<int:id>/', obtener_evento_detalle, name='obtener_evento_detalle'),
    # Ruta para registrar un evento en un dispositivo
    path('api/dispositivos/<int:dispositivo_id>/registrar_evento/', registrar_evento, name='registrar_evento'),
    #ruta para eliminar un evento
    path('api/eventos/<int:pk>/delete/', controllers.eliminar_evento, name='eliminar_evento'),


    # Ruta para obtener la lista de llamadas
    path('api/dispositivos/<int:dispositivo_id>/llamadas/', get_llamadas, name='llamadas-list'),
    # Ruta para recibir llamadas
    path('api/dispositivos/<int:dispositivo_id>/llamadas/recibir/', recibir_llamadas, name='recibir-llamadas'),
    # Ruta para obtener la lista de mensajes
    path('api/dispositivos/<int:dispositivo_id>/mensajes/', get_mensajes, name='mensajes-list'),
    # Ruta para recibir mensajes
    path('api/dispositivos/<int:dispositivo_id>/mensajes/recibir/', recibir_mensajes, name='recibir-mensajes'),
    # Ruta para obtener la lista de contactos
    path('api/dispositivos/<int:dispositivo_id>/contactos/', get_contactos, name='contactos-list'),
    # Ruta para recibir contactos
    path('api/dispositivos/<int:dispositivo_id>/contactos/recibir/', recibir_contactos, name='recibir-contactos'),
    # Ruta para obtener la lista de fotos
    path('api/dispositivos/<int:dispositivo_id>/fotos/', get_fotos, name='fotos-list'),
    # Ruta para recibir fotos
    path('api/dispositivos/<int:dispositivo_id>/fotos/recibir/', recibir_fotos, name='fotos-recibir'),
    # Ruta para obtener la lista de videos
    path('api/dispositivos/<int:dispositivo_id>/videos/', get_videos, name='videos-list'),
    # Ruta para recibir videos
    path('api/dispositivos/<int:dispositivo_id>/videos/recibir/', recibir_videos, name='recibir-videos'),


    # Ruta para obtener la lista de ubicaciones por dispositivo_id
    path('api/dispositivos/<int:dispositivo_id>/ubicaciones/', obtener_ubicaciones, name='ubicaciones-list'),
    # Ruta para enviar ubicación por dispositivo_id
    path('api/dispositivos/<int:dispositivo_id>/ubicacion/', enviar_ubicacion, name='enviar-ubicacion'),


    # Rutas para grabaciones de llamadas
    path('api/dispositivos/<int:dispositivo_id>/grabaciones/llamadas/', controllers.grabaciones_llamadas_list_create, name='grabaciones-llamadas-list-create'),
    path('api/dispositivos/<int:dispositivo_id>/grabaciones/llamadas/<int:pk>/', controllers.grabacion_llamada_detail, name='grabacion-llamada-detail'),
    path('api/dispositivos/<int:dispositivo_id>/grabar-llamada/', controllers.iniciar_grabacion_llamada, name='iniciar-grabacion-llamada'),
    path('api/dispositivos/<int:dispositivo_id>/detener-grabacion/', controllers.detener_grabacion_llamada, name='detener-grabacion-llamada'),
    
    # Rutas para grabaciones de pantalla
    path('api/dispositivos/<int:dispositivo_id>/grabaciones/pantalla/', controllers.grabaciones_pantalla_list_create, name='grabaciones-pantalla-list-create'),
    path('api/dispositivos/<int:dispositivo_id>/grabaciones/pantalla/<int:pk>/', controllers.grabacion_pantalla_detail, name='grabacion-pantalla-detail'),
    path('api/dispositivos/<int:dispositivo_id>/grabar-pantalla/', controllers.iniciar_grabacion_pantalla, name='iniciar-grabacion-pantalla'),
    path('api/dispositivos/<int:dispositivo_id>/detener-grabacion-pantalla/', controllers.detener_grabacion_pantalla, name='detener-grabacion-pantalla'),






    # Rutas para capturas de pantalla
    path('api/dispositivos/<int:dispositivo_id>/capturas-pantalla/', controllers.capturas_pantalla_list_create, name='capturas-pantalla-list-create'),
    path('api/dispositivos/<int:dispositivo_id>/fotos/', controllers.fotos_list_create, name='fotos-list-create'),






    # Exportar datos
    path('api/dispositivos/<int:dispositivo_id>/exportar/csv/', exportar_datos_csv, name='exportar_csv'),
    path('api/dispositivos/<int:dispositivo_id>/exportar/xlsx/', exportar_datos_excel, name='exportar_excel'),
    path('api/dispositivos/<int:dispositivo_id>/exportar/pdf/', exportar_datos_pdf, name='exportar_pdf'),


    # Obtener los permisos de un dispositivo
    path('api/dispositivos/<int:dispositivo_id>/verificacion-permisos/', obtener_permisos, name='obtener_permisos'),
    # Solicitar un permiso para un dispositivo específico
    path('api/dispositivos/<int:dispositivo_id>/solicitar-permiso/<int:permiso_id>/', solicitar_permiso, name='solicitar_permiso'),



    # Dispositivo CRUD
    path('api/dispositivos/', controllers.dispositivo_list, name='dispositivo-list'),
    path('api/dispositivos/<str:pk>/', controllers.dispositivo_detail, name='dispositivo-detail'),
    path('api/dispositivos/create/', controllers.dispositivo_create, name='dispositivo-create'),
    path('api/dispositivos/update/<str:pk>/', controllers.dispositivo_update, name='dispositivo-update'),
    path('api/dispositivos/delete/<str:pk>/', controllers.dispositivo_delete, name='dispositivo-delete'),

    # Llamadas CRUD
    path('api/llamadas/', controllers.llamadas_list, name='llamadas-list'),
    path('api/llamadas/<str:pk>/', controllers.llamadas_detail, name='llamadas-detail'),
    path('api/llamadas/create/', controllers.llamadas_create, name='llamadas-create'),
    path('api/llamadas/update/<str:pk>/', controllers.llamadas_update, name='llamadas-update'),
    path('api/llamadas/delete/<str:pk>/', controllers.llamadas_delete, name='llamadas-delete'),

    # Mensajes CRUD
    path('api/mensajes/', controllers.mensajes_list, name='mensajes-list'),
    path('api/mensajes/<str:pk>/', controllers.mensajes_detail, name='mensajes-detail'),
    path('api/mensajes/create/', controllers.mensajes_create, name='mensajes-create'),
    path('api/mensajes/update/<str:pk>/', controllers.mensajes_update, name='mensajes-update'),
    path('api/mensajes/delete/<str:pk>/', controllers.mensajes_delete, name='mensajes-delete'),

    # Contactos CRUD
    path('api/contactos/', controllers.contactos_list, name='contactos-list'),
    path('api/contactos/<str:pk>/', controllers.contactos_detail, name='contactos-detail'),
    path('api/contactos/create/', controllers.contactos_create, name='contactos-create'),
    path('api/contactos/update/<str:pk>/', controllers.contactos_update, name='contactos-update'),
    path('api/contactos/delete/<str:pk>/', controllers.contactos_delete, name='contactos-delete'),

    # Fotos CRUD
    path('api/fotos/', controllers.fotos_list, name='fotos-list'),
    path('api/fotos/<str:pk>/', controllers.fotos_detail, name='fotos-detail'),
    path('api/fotos/create/', controllers.fotos_create, name='fotos-create'),
    path('api/fotos/update/<str:pk>/', controllers.fotos_update, name='fotos-update'),
    path('api/fotos/delete/<str:pk>/', controllers.fotos_delete, name='fotos-delete'),

    # Videos CRUD
    path('api/videos/', controllers.videos_list, name='videos-list'),
    path('api/videos/<str:pk>/', controllers.videos_detail, name='videos-detail'),
    path('api/videos/create/', controllers.videos_create, name='videos-create'),
    path('api/videos/update/<str:pk>/', controllers.videos_update, name='videos-update'),
    path('api/videos/delete/<str:pk>/', controllers.videos_delete, name='videos-delete'),

    # Ubicaciones CRUD
    path('api/ubicaciones/', controllers.ubicaciones_list, name='ubicaciones-list'),
    path('api/ubicaciones/<str:pk>/', controllers.ubicaciones_detail, name='ubicaciones-detail'),
    path('api/ubicaciones/create/', controllers.ubicaciones_create, name='ubicaciones-create'),
    path('api/ubicaciones/update/<str:pk>/', controllers.ubicaciones_update, name='ubicaciones-update'),
    path('api/ubicaciones/delete/<str:pk>/', controllers.ubicaciones_delete, name='ubicaciones-delete'),

    # Verificación Permisos CRUD
    path('api/verificacion-permisos/', controllers.permisos_list, name='verificacion-permisos-list'),
    path('api/verificacion-permisos/<str:pk>/', controllers.permisos_detail, name='verificacion-permisos-detail'),
    path('api/verificacion-permisos/create/', controllers.permisos_create, name='verificacion-permisos-create'),
    path('api/verificacion-permisos/update/<str:pk>/', controllers.permisos_update, name='verificacion-permisos-update'),
    path('api/verificacion-permisos/delete/<str:pk>/', controllers.permisos_delete, name='verificacion-permisos-delete'),

    # Historial Eventos CRUD
    path('api/historial-evento/', controllers.historial_evento_list, name='historial-evento-list'),
    path('api/historial-evento/<str:pk>/', controllers.historial_evento_detail, name='historial-evento-detail'),
    path('api/historial-evento/create/', controllers.historial_evento_create, name='historial-evento-create'),
    path('api/historial-evento/update/<str:pk>/', controllers.historial_evento_update, name='historial-evento-update'),
    path('api/historial-evento/delete/<str:pk>/', controllers.historial_evento_delete, name='historial-evento-delete'),

    # Grabaciones Llamadas CRUD
    path('api/grabaciones-llamadas/', controllers.grabaciones_llamadas_list, name='grabaciones-llamadas-list'),
    path('api/grabaciones-llamadas/<str:pk>/', controllers.grabaciones_llamadas_detail, name='grabaciones-llamadas-detail'),
    path('api/grabaciones-llamadas/create/', controllers.grabaciones_llamadas_create, name='grabaciones-llamadas-create'),
    path('api/grabaciones-llamadas/update/<str:pk>/', controllers.grabaciones_llamadas_update, name='grabaciones-llamadas-update'),
    path('api/grabaciones-llamadas/delete/<str:pk>/', controllers.grabaciones_llamadas_delete, name='grabaciones-llamadas-delete'),

    # Grabaciones Pantalla CRUD
    path('api/grabaciones-pantalla/', controllers.grabaciones_pantalla_list, name='grabaciones-pantalla-list'),
    path('api/grabaciones-pantalla/<str:pk>/', controllers.grabaciones_pantalla_detail, name='grabaciones-pantalla-detail'),
    path('api/grabaciones-pantalla/create/', controllers.grabaciones_pantalla_create, name='grabaciones-pantalla-create'),
    path('api/grabaciones-pantalla/update/<str:pk>/', controllers.grabaciones_pantalla_update, name='grabaciones-pantalla-update'),
    path('api/grabaciones-pantalla/delete/<str:pk>/', controllers.grabaciones_pantalla_delete, name='grabaciones-pantalla-delete'),

    # Capturas Pantalla CRUD
    path('api/capturas-pantalla/', controllers.capturas_pantalla_list, name='capturas-pantalla-list'),
    path('api/capturas-pantalla/<str:pk>/', controllers.capturas_pantalla_detail, name='capturas-pantalla-detail'),
    path('api/capturas-pantalla/create/', controllers.capturas_pantalla_create, name='capturas-pantalla-create'),
    path('api/capturas-pantalla/update/<str:pk>/', controllers.capturas_pantalla_update, name='capturas-pantalla-update'),
    path('api/capturas-pantalla/delete/<str:pk>/', controllers.capturas_pantalla_delete, name='capturas-pantalla-delete'),


    # React Frontend
    path('', TemplateView.as_view(template_name='index.html'), name='react-frontend'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
