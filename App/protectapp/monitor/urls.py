<<<<<<< HEAD
from django.views.generic import TemplateView
=======
<<<<<<< HEAD
from django.views.generic import TemplateView
=======
<<<<<<< HEAD
from django.views.generic import TemplateView
=======
<<<<<<< HEAD
from django.views.generic import TemplateView
=======
<<<<<<< HEAD
<<<<<<< HEAD

>>>>>>> b5ca5ef48d2ae9ff505b8711631613fc593d45d5
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from .controllers import (
    login_user, register_user, update_user_profile, logout_user,
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
    dispositivo_list_create, get_user_data, 
    obtener_eventos, obtener_evento_detalle, dispositivo_detail_update,
    get_llamadas, get_mensajes, get_contactos, get_fotos, get_videos, 
    obtener_ubicaciones, enviar_ubicacion, recibir_llamadas, recibir_mensajes, 
    recibir_contactos, recibir_fotos, recibir_videos, registrar_evento, capturas_pantalla_list_create, 
<<<<<<< HEAD
    fotos_list_create, exportar_datos_csv, exportar_datos_excel, exportar_datos_pdf, 
    obtener_permisos, actualizar_permiso, eliminar_dispositivo, crear_dispositivo_despues_configuracion
)

from . import controllers
=======
<<<<<<< HEAD
=======
=======
<<<<<<< HEAD
    dispositivo_list_create, get_user_data, 
=======
    dispositivo_list_create, get_user_data, dispositivo_detail, reg_event, 
>>>>>>> b5ca5ef48d2ae9ff505b8711631613fc593d45d5
    obtener_eventos, obtener_evento_detalle, dispositivo_detail_update,
    get_llamadas, get_mensajes, get_contactos, get_fotos, get_videos, 
    obtener_ubicaciones, enviar_ubicacion, recibir_llamadas, recibir_mensajes, 
    recibir_contactos, recibir_fotos, recibir_videos, registrar_evento,
    grabaciones_llamadas_list_create, grabacion_llamada_detail, 
    grabaciones_pantalla_list_create, iniciar_grabacion_llamada, 
    detener_grabacion_llamada, iniciar_grabacion_pantalla, 
<<<<<<< HEAD
    detener_grabacion_pantalla, grabacion_pantalla_detail, capturas_pantalla_list_create, 
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
    fotos_list_create, exportar_datos_csv, exportar_datos_excel, exportar_datos_pdf, 
    obtener_permisos, solicitar_permiso, eliminar_dispositivo
)

from . import controllers
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
    detener_grabacion_pantalla, grabacion_view, capturas_pantalla_list_create, 
    fotos_list_create, exportar_datos_csv, exportar_datos_excel, exportar_datos_pdf,
    capturas_view, obtener_permisos, solicitar_permiso, eliminar_dispositivo
)

from . import controllers
=======
<<<<<<< HEAD
from django.urls import path
=======
from django.urls import path
<<<<<<< HEAD
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
from .controllers import login_user, register_user, update_user_profile, logout_user, dispositivo_list_create, get_user_data, dispositivo_detail, reg_event, obtener_eventos, obtener_evento_detalle, dispositivo_update, dispositivo_detail_update, get_llamadas, get_mensajes, get_contactos, get_fotos, get_videos
from . import controllers
=======
<<<<<<< HEAD
from django.urls import path
<<<<<<< HEAD
=======
=======
>>>>>>> 8e18bd6d3b44f892c4e048fb7e4e553c2d8fe619
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
from . import views

urlpatterns = [
    path('api/', views.api_overview, name='api-overview'),
    
    # Rutas para Dispositivos
    path('api/dispositivos/', views.dispositivo_list, name='dispositivo-list'),
    path('api/dispositivos/<str:pk>/', views.dispositivo_detail, name='dispositivo-detail'),
    path('api/dispositivos/create/', views.dispositivo_create, name='dispositivo-create'),
    path('api/dispositivos/update/<str:pk>/', views.dispositivo_update, name='dispositivo-update'),
    path('api/dispositivos/delete/<str:pk>/', views.dispositivo_delete, name='dispositivo-delete'),

    # Rutas para Llamadas
    path('api/llamadas/', views.llamadas_list, name='llamadas-list'),
    path('api/llamadas/<str:pk>/', views.llamadas_detail, name='llamadas-detail'),
    path('api/llamadas/create/', views.llamadas_create, name='llamadas-create'),
    path('api/llamadas/update/<str:pk>/', views.llamadas_update, name='llamadas-update'),
    path('api/llamadas/delete/<str:pk>/', views.llamadas_delete, name='llamadas-delete'),

    # Rutas para Mensajes
    path('api/mensajes/', views.mensajes_list, name='mensajes-list'),
    path('api/mensajes/<str:pk>/', views.mensajes_detail, name='mensajes-detail'),
    path('api/mensajes/create/', views.mensajes_create, name='mensajes-create'),
    path('api/mensajes/update/<str:pk>/', views.mensajes_update, name='mensajes-update'),
    path('api/mensajes/delete/<str:pk>/', views.mensajes_delete, name='mensajes-delete'),

    # Rutas para Contactos
    path('api/contactos/', views.contactos_list, name='contactos-list'),
    path('api/contactos/<str:pk>/', views.contactos_detail, name='contactos-detail'),
    path('api/contactos/create/', views.contactos_create, name='contactos-create'),
    path('api/contactos/update/<str:pk>/', views.contactos_update, name='contactos-update'),
    path('api/contactos/delete/<str:pk>/', views.contactos_delete, name='contactos-delete'),

    # Rutas para Fotos
    path('api/fotos/', views.fotos_list, name='fotos-list'),
    path('api/fotos/<str:pk>/', views.fotos_detail, name='fotos-detail'),
    path('api/fotos/create/', views.fotos_create, name='fotos-create'),
    path('api/fotos/update/<str:pk>/', views.fotos_update, name='fotos-update'),
    path('api/fotos/delete/<str:pk>/', views.fotos_delete, name='fotos-delete'),

    # Rutas para Videos
    path('api/videos/', views.videos_list, name='videos-list'),
    path('api/videos/<str:pk>/', views.videos_detail, name='videos-detail'),
    path('api/videos/create/', views.videos_create, name='videos-create'),
    path('api/videos/update/<str:pk>/', views.videos_update, name='videos-update'),
    path('api/videos/delete/<str:pk>/', views.videos_delete, name='videos-delete'),

    # Rutas para Ubicaciones
    path('api/ubicaciones/', views.ubicaciones_list, name='ubicaciones-list'),
    path('api/ubicaciones/<str:pk>/', views.ubicaciones_detail, name='ubicaciones-detail'),
    path('api/ubicaciones/create/', views.ubicaciones_create, name='ubicaciones-create'),
    path('api/ubicaciones/update/<str:pk>/', views.ubicaciones_update, name='ubicaciones-update'),
    path('api/ubicaciones/delete/<str:pk>/', views.ubicaciones_delete, name='ubicaciones-delete'),

    # Rutas para Grabaciones Llamadas
    path('api/grabaciones-llamadas/', views.grabaciones_llamadas_list, name='grabaciones-llamadas-list'),
    path('api/grabaciones-llamadas/<str:pk>/', views.grabaciones_llamadas_detail, name='grabaciones-llamadas-detail'),
    path('api/grabaciones-llamadas/create/', views.grabaciones_llamadas_create, name='grabaciones-llamadas-create'),
    path('api/grabaciones-llamadas/update/<str:pk>/', views.grabaciones_llamadas_update, name='grabaciones-llamadas-update'),
    path('api/grabaciones-llamadas/delete/<str:pk>/', views.grabaciones_llamadas_delete, name='grabaciones-llamadas-delete'),

    # Rutas para Grabaciones Pantalla
    path('api/grabaciones-pantalla/', views.grabaciones_pantalla_list, name='grabaciones-pantalla-list'),
    path('api/grabaciones-pantalla/<str:pk>/', views.grabaciones_pantalla_detail, name='grabaciones-pantalla-detail'),
    path('api/grabaciones-pantalla/create/', views.grabaciones_pantalla_create, name='grabaciones-pantalla-create'),
    path('api/grabaciones-pantalla/update/<str:pk>/', views.grabaciones_pantalla_update, name='grabaciones-pantalla-update'),
    path('api/grabaciones-pantalla/delete/<str:pk>/', views.grabaciones_pantalla_delete, name='grabaciones-pantalla-delete'),

    # Rutas para Capturas Pantalla
    path('api/capturas-pantalla/', views.capturas_pantalla_list, name='capturas-pantalla-list'),
    path('api/capturas-pantalla/<str:pk>/', views.capturas_pantalla_detail, name='capturas-pantalla-detail'),
    path('api/capturas-pantalla/create/', views.capturas_pantalla_create, name='capturas-pantalla-create'),
    path('api/capturas-pantalla/update/<str:pk>/', views.capturas_pantalla_update, name='capturas-pantalla-update'),
    path('api/capturas-pantalla/delete/<str:pk>/', views.capturas_pantalla_delete, name='capturas-pantalla-delete'),

    # Rutas para Verificación Permisos
    path('api/verificacion-permisos/', views.permisos_list, name='verificacion-permisos-list'),
    path('api/verificacion-permisos/<str:pk>/', views.permisos_detail, name='verificacion-permisos-detail'),
    path('api/verificacion-permisos/create/', views.permisos_create, name='verificacion-permisos-create'),
    path('api/verificacion-permisos/update/<str:pk>/', views.permisos_update, name='verificacion-permisos-update'),
    path('api/verificacion-permisos/delete/<str:pk>/', views.permisos_delete, name='verificacion-permisos-delete'),

    # Rutas para Historial Evento
    path('api/historial-evento/', views.historial_evento_list, name='historial-evento-list'),
    path('api/historial-evento/<str:pk>/', views.historial_evento_detail, name='historial-evento-detail'),
    path('api/historial-evento/create/', views.historial_evento_create, name='historial-evento-create'),
    path('api/historial-evento/update/<str:pk>/', views.historial_evento_update, name='historial-evento-update'),
    path('api/historial-evento/delete/<str:pk>/', views.historial_evento_delete, name='historial-evento-delete'),
]
=======
<<<<<<< HEAD
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from .views import exportar_datos_csv, exportar_datos_excel, exportar_datos_pdf
from .views import obtener_evento_detalle
from .views import obtener_eventos
=======
from django.urls import path
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
from django.conf import settings
from django.conf.urls.static import static
from . import views
=======
<<<<<<< HEAD
>>>>>>> b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
>>>>>>> b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
from django.conf import settings
from django.conf.urls.static import static
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
from . import views
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
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
<<<<<<< HEAD
=======
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
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6




# API Endpoints for CRUD operations and overview
urlpatterns = [
    # API Overview
    path('api/', controllers.api_overview, name='api-overview'),

<<<<<<< HEAD

=======
<<<<<<< HEAD

=======
<<<<<<< HEAD

=======
<<<<<<< HEAD

=======
>>>>>>> b5ca5ef48d2ae9ff505b8711631613fc593d45d5
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
    # Rutas para la autenticación con JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6





    path('api/dispositivos/activos/', controllers.dispositivos_activos, name='dispositivos-activos'),
    path('api/eventos/totales/', controllers.eventos_totales, name='eventos-totales'),
    path('api/actividad/ultima/', controllers.ultima_actividad_usuario, name='ultima_actividad_usuario'),






    # Rutas para autenticación y perfil de usuarios
<<<<<<< HEAD
=======
=======
<<<<<<< HEAD


    # Rutas para autenticación y perfil de usuarios
=======
<<<<<<< HEAD

    # Rutas para autenticación y perfil de usuarios
=======
    # User Registration
>>>>>>> b5ca5ef48d2ae9ff505b8711631613fc593d45d5
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
    path('api/login/', login_user, name='login'),
    path('api/register/', register_user, name='register'),
    path('api/profile/update/', update_user_profile, name='profile-update'),
    path('api/logout/', logout_user, name='logout'),
    path('api/user/', get_user_data, name='get_user_data'),
<<<<<<< HEAD
    path('api/user/profile/', controllers.get_user_profile, name='user-profile'),
=======
<<<<<<< HEAD
    path('api/user/profile/', controllers.get_user_profile, name='user-profile'),
=======

<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6

    # Ruta para listar y crear dispositivos
    path('api/dispositivos/', dispositivo_list_create, name='dispositivos-list-create'),
    # Ruta para obtener detalles de un dispositivo específico y actualizarlo
    path('api/dispositivos/<int:pk>/', dispositivo_detail_update, name='dispositivo-detail-update'),
    # Ruta para eliminar un dispositivo
    path('api/dispositivos/delete/<int:dispositivo_id>/', eliminar_dispositivo, name='eliminar_dispositivo'),
<<<<<<< HEAD
    # Ruta para crear un dispositivo despues de la configuración de permisos
    path('api/dispositivos/crear_despues_configuracion/', crear_dispositivo_despues_configuracion, name='crear_dispositivo_despues_configuracion'),
=======
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6


    # Ruta para obtener eventos por dispositivo
    path('api/dispositivos/<int:dispositivo_id>/eventos/', obtener_eventos, name='obtener_eventos'),
    # Ruta para obtener el detalle de un evento por ID
    path('api/eventos/<int:id>/', obtener_evento_detalle, name='obtener_evento_detalle'),
    # Ruta para registrar un evento en un dispositivo
    path('api/dispositivos/<int:dispositivo_id>/registrar_evento/', registrar_evento, name='registrar_evento'),
<<<<<<< HEAD
    #ruta para eliminar un evento
    path('api/eventos/<int:pk>/delete/', controllers.eliminar_evento, name='eliminar_evento'),
=======
<<<<<<< HEAD
    #ruta para eliminar un evento
    path('api/eventos/<int:pk>/delete/', controllers.eliminar_evento, name='eliminar_evento'),
=======
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6


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

<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
    # Ruta para obtener los datos del usuario autenticado 
    path('usuarios/', get_user_data, name='get_user_data'),
    path('api/usuarios/', get_user_data, name='get_user_data'),

    # Ruta para listar y crear dispositivo
    path('api/dispositivos/', dispositivo_list_create, name='dispositivos-list-create'),
    # Ruta para actualizar un dispositivo específico
    path('api/dispositivos/<int:pk>/', dispositivo_detail_update, name='dispositivo-detail-update'),
    # Ruta para ver detalles de un dispositivo específico
    path('api/dispositivos/<int:pk>/', dispositivo_detail, name='dispositivo-detail'),
    # Ruta para registrar eventos en un dispositivo específico
    path('dispositivo/<int:id>/reg_event/', reg_event, name='reg_event'),

    # Ruta para eliminar un dispositivo
    path('api/dispositivos/delete/<int:dispositivo_id>/', eliminar_dispositivo, name='eliminar_dispositivo'),

    # Ruta para obtener eventos
    path('api/dispositivos/<int:dispositivo_id>/eventos/', obtener_eventos, name='obtener_eventos'),
    path('api/eventos/<int:id>/', obtener_evento_detalle, name='obtener_evento_detalle'),
    # Ruta para registrar eventos
    path('api/dispositivos/<int:dispositivo_id>/registrar_evento/', registrar_evento, name='registrar_evento'),

    # Ruta para obtener la lista de llamadas
    path('api/dispositivos/<int:dispositivo_id>/llamadas/', get_llamadas, name='llamadas-list'),
    # Ruta para recibir llamadas
    path('api/dispositivos/<int:dispositivo_id>/llamadas/', recibir_llamadas, name='recibir-llamadas'),
    # Ruta para obtener la lista de mensajes
    path('api/dispositivos/<int:dispositivo_id>/mensajes/', get_mensajes, name='mensajes-list'),
    # Ruta para recibir mensajes
    path('api/dispositivos/<int:dispositivo_id>/mensajes/', recibir_mensajes, name='recibir-mensajes'),
    # Ruta para obtener la lista de contactos
    path('api/dispositivos/<int:dispositivo_id>/contactos/', get_contactos, name='contactos-list'),
    # Ruta para recibir contactos
    path('api/dispositivos/<int:dispositivo_id>/contactos/', recibir_contactos, name='recibir-contactos'),

    # Ruta para obtener la lista de fotos del dispositivo (listar)
    path('api/dispositivos/<int:dispositivo_id>/fotos/', get_fotos, name='fotos-list'),
    # Ruta para recibir fotos (subir nuevas fotos tomadas)
    path('api/dispositivos/<int:dispositivo_id>/fotos/recibir/', recibir_fotos, name='fotos-recibir'),

    # Ruta para obtener la lista de videos
    path('api/dispositivos/<int:dispositivo_id>/videos/', get_videos, name='videos-list'),
    # Ruta para recibir videos
    path('api/dispositivos/<int:dispositivo_id>/videos/', recibir_videos, name='recibir-videos'),
>>>>>>> b5ca5ef48d2ae9ff505b8711631613fc593d45d5
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6

    # Ruta para obtener la lista de ubicaciones por dispositivo_id
    path('api/dispositivos/<int:dispositivo_id>/ubicaciones/', obtener_ubicaciones, name='ubicaciones-list'),
    # Ruta para enviar ubicación por dispositivo_id
    path('api/dispositivos/<int:dispositivo_id>/ubicacion/', enviar_ubicacion, name='enviar-ubicacion'),

<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6

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




<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
<<<<<<< HEAD

    # Rutas para grabaciones de llamadas
    path('api/dispositivos/<int:dispositivo_id>/grabaciones/llamadas/', grabaciones_llamadas_list_create, name='grabaciones-llamadas-list-create'),
    path('api/dispositivos/<int:dispositivo_id>/grabaciones/llamadas/<int:pk>/', grabacion_llamada_detail, name='grabacion-llamada-detail'),
    path('api/dispositivos/<int:dispositivo_id>/grabar-llamada/', iniciar_grabacion_llamada, name='iniciar-grabacion-llamada'),
    path('api/dispositivos/<int:dispositivo_id>/detener-grabacion/', detener_grabacion_llamada, name='detener-grabacion-llamada'),
    
    # Rutas para grabaciones de pantalla
    path('api/dispositivos/<int:dispositivo_id>/grabaciones/pantalla/', grabaciones_pantalla_list_create, name='grabaciones-pantalla-list-create'),
    path('api/dispositivos/<int:dispositivo_id>/grabaciones/pantalla/<int:pk>/', grabacion_pantalla_detail, name='grabacion-pantalla-detail'),
    path('api/dispositivos/<int:dispositivo_id>/grabar-pantalla/', iniciar_grabacion_pantalla, name='iniciar-grabacion-pantalla'),
    path('api/dispositivos/<int:dispositivo_id>/detener-grabacion-pantalla/', detener_grabacion_pantalla, name='detener-grabacion-pantalla'),


    # Rutas para capturas de pantalla
    path('api/dispositivos/<int:dispositivo_id>/capturas/pantalla/', capturas_pantalla_list_create, name='capturas-pantalla-list-create'),
    path('api/dispositivos/<int:dispositivo_id>/fotos/', fotos_list_create, name='fotos-list-create'),
=======
    # Rutas para grabaciones de llamadas
    path('api/dispositivos/<int:dispositivo_id>/grabaciones/llamadas/', grabaciones_llamadas_list_create, name='grabaciones-llamadas-list-create'),
    path('api/dispositivos/<int:dispositivo_id>/grabaciones/llamadas/<int:pk>/', grabacion_llamada_detail, name='grabacion-llamada-detail'),
    # Ruta para iniciar la grabación de llamadas
    path('api/dispositivos/<int:dispositivo_id>/grabar-llamada/', iniciar_grabacion_llamada, name='iniciar-grabacion-llamada'),
    # Ruta para detener la grabación de llamadas
    path('api/dispositivos/<int:dispositivo_id>/detener-grabacion/', detener_grabacion_llamada, name='detener-grabacion-llamada'),

    # Rutas para grabaciones de pantalla
    path('api/dispositivos/<int:dispositivo_id>/grabaciones/pantalla/', grabaciones_pantalla_list_create, name='grabaciones-pantalla-list-create'),
    # Ruta para iniciar la grabación de pantalla
    path('api/dispositivos/<int:dispositivo_id>/grabar-pantalla/', iniciar_grabacion_pantalla, name='iniciar-grabacion-pantalla'),
    # Ruta para detener la grabación de pantalla
    path('api/dispositivos/<int:dispositivo_id>/detener-grabacion-pantalla/', detener_grabacion_pantalla, name='detener-grabacion-pantalla'),

    # Ruta para la vista de grabación
    path('grabacion/<int:dispositivo_id>/', grabacion_view, name='grabacion'),

    # Rutas para capturas de pantalla
    path('api/dispositivos/<int:dispositivo_id>/capturas/pantalla/', capturas_pantalla_list_create, name='capturas-pantalla-list-create'),
    path('dispositivos/<int:dispositivo_id>/fotos/', fotos_list_create, name='fotos'),
    path('capturas/<int:dispositivo_id>/', capturas_view, name='capturas-view'),
>>>>>>> b5ca5ef48d2ae9ff505b8711631613fc593d45d5
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6


    # Exportar datos
    path('api/dispositivos/<int:dispositivo_id>/exportar/csv/', exportar_datos_csv, name='exportar_csv'),
    path('api/dispositivos/<int:dispositivo_id>/exportar/xlsx/', exportar_datos_excel, name='exportar_excel'),
    path('api/dispositivos/<int:dispositivo_id>/exportar/pdf/', exportar_datos_pdf, name='exportar_pdf'),


<<<<<<< HEAD
    # Obtener los permisos de un dispositivo
    path('api/dispositivos/<int:dispositivo_id>/verificacion-permisos/', obtener_permisos, name='obtener_permisos'),
    # Solicitar un permiso para un dispositivo específico
    path('api/permisos/update/', actualizar_permiso, name='actualizar_permiso'),

=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
    # Obtener los permisos de un dispositivo
    path('api/dispositivos/<int:dispositivo_id>/verificacion-permisos/', obtener_permisos, name='obtener_permisos'),
    # Solicitar un permiso para un dispositivo específico
    path('api/dispositivos/<int:dispositivo_id>/solicitar-permiso/<int:permiso_id>/', solicitar_permiso, name='solicitar_permiso'),

<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
    # obtener y gestionar permisos (como parte del controlador de Permisos)
    path('api/dispositivos/<int:dispositivo_id>/verificacion-permisos/', obtener_permisos, name='obtener_permisos'),
    path('api/dispositivos/<int:dispositivo_id>/solicitar-permiso/<int:permiso_id>/', solicitar_permiso, name='solicitar_permiso'),
=======
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
    # Ruta para obtener los datos del usuario autenticado (desde controllers)
    path('usuarios/', get_user_data, name='get_user_data'),
    path('api/usuarios/', get_user_data, name='get_user_data'),

    # Rutas para gestionar dispositivos en controllers.py
    path('api/dispositivos/', dispositivo_list_create, name='dispositivos-list-create'),
    path('api/dispositivos/<int:pk>/', dispositivo_detail_update, name='dispositivo-detail-update'),
    path('api/dispositivos/<int:pk>/', dispositivo_update, name='dispositivo-update'),
    path('api/dispositivos/<int:pk>/', dispositivo_detail, name='dispositivo-detail'),
    path('dispositivo/<int:id>/reg_event/', reg_event, name='reg_event'),
    
    # Ruta para obtener eventos
    path('api/dispositivos/<int:dispositivo_id>/eventos/', obtener_eventos, name='obtener_eventos'),
    path('api/eventos/<int:id>/', obtener_evento_detalle, name='obtener_evento_detalle'),

    
    # Ruta para obtener la lista de llamadas, mensajes, contactos, fotos y videos por dispositivo_id
    path('api/dispositivos/<int:dispositivo_id>/llamadas/', get_llamadas, name='llamadas-list'),
    path('api/dispositivos/<int:dispositivo_id>/mensajes/', get_mensajes, name='mensajes-list'),
    path('api/dispositivos/<int:dispositivo_id>/contactos/', get_contactos, name='contactos-list'),
    path('api/dispositivos/<int:dispositivo_id>/fotos/', get_fotos, name='fotos-list'),
    path('api/dispositivos/<int:dispositivo_id>/videos/', get_videos, name='videos-list'),


    





































<<<<<<< HEAD
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
>>>>>>> b5ca5ef48d2ae9ff505b8711631613fc593d45d5
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6


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
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6


    # React Frontend
    path('', TemplateView.as_view(template_name='index.html'), name='react-frontend'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
]

# HTML Pages (Render Templates)
urlpatterns += [
    path('archivo_telefono/', controllers.archivo_telefono_view, name='archivo_telefono'),
    path('capturas/', controllers.capturas_view, name='capturas'),
    path('caracteristicas/', controllers.caracteristicas_view, name='caracteristicas'),
    path('compras/', controllers.compras_view, name='compras'),
    path('cuenta/', controllers.cuenta_view, name='cuenta'),
    path('exportar_datos/', controllers.exportar_datos_view, name='exportar_datos'),
    path('grabacion/', controllers.grabacion_view, name='grabacion'),
    path('index/', controllers.index_view, name='index'),
    path('inicio/', controllers.inicio_view, name='inicio'),
    path('login/', controllers.login_view, name='login'),
    path('mi_producto/', controllers.mi_producto_view, name='mi_producto'),
    path('mis_dispositivos/', controllers.mis_dispositivos_view, name='mis_dispositivos'),
    path('politica/', controllers.politica_view, name='politica'),
    path('preguntas/', controllers.preguntas_view, name='preguntas'),
    path('productos/', controllers.productos_view, name='productos'),
    path('prueba/', controllers.prueba_view, name='prueba'),
    path('recuperar_contra/', controllers.recuperar_contra_view, name='recuperar_contra'),
    path('recursos/', controllers.recursos_view, name='recursos'),
    path('reg_event/', controllers.reg_event_view, name='reg_event'),
    path('registrarse/', controllers.registrarse_view, name='registrarse'),
    path('registro/', controllers.registro_view, name='registro'),
    path('soporte/', controllers.soporte_view, name='soporte'),
    path('terminos/', controllers.terminos_view, name='terminos'),
    path('ubicacion/', controllers.ubicacion_view, name='ubicacion'),
    path('verificacion_permisos/', controllers.verificacion_permisos_view, name='verificacion_permisos'),
]
<<<<<<< HEAD
<<<<<<< HEAD


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
=======
<<<<<<< HEAD
=======
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 8e18bd6d3b44f892c4e048fb7e4e553c2d8fe619
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
from . import views
>>>>>>> 052f2d3b4d3ee496a9b96224faedb68f377a196d
>>>>>>> a8d19f143da4dcdf7a22fd08e935b212cf57580a
>>>>>>> b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
>>>>>>> b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6

urlpatterns = [
    # Ruta de prueba
    path('api/', views.api_overview, name='api-overview'),
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

    # Rutas para autenticación con JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
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
    
    # Rutas de usuarios
    path('api/register/', views.register_user, name='register'),
    path('api/login/', views.login_user, name='login'),
    path('api/profile/update/', views.update_user_profile, name='profile-update'),
    path('api/logout/', views.logout_user, name='logout'),

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
    # Ruta para obtener los datos del usuario autenticado

    path('usuarios/', views.get_user_data, name='get_user_data'),
    path('api/usuarios/', views.get_user_data, name='get_user_data'),

<<<<<<< HEAD
    # Rutas para gestionar dispositivos
    path('api/dispositivos/', views.dispositivo_list_create, name='dispositivos-list-create'),
    path('api/dispositivos/<int:pk>/', views.dispositivo_detail, name='dispositivo-detail'),
    path('dispositivo/<int:id>/reg_event/', views.reg_event, name='reg_event'),

    path('api/dispositivos/<int:dispositivo_id>/eventos/', obtener_eventos, name='obtener_eventos'),
    path('api/eventos/<int:id>/', obtener_evento_detalle, name='obtener_evento_detalle'),

    # Rutas para exportar datos
    path('api/dispositivos/<int:dispositivo_id>/exportar/csv/', exportar_datos_csv, name='exportar_csv'),
    path('api/dispositivos/<int:dispositivo_id>/exportar/xlsx/', exportar_datos_excel, name='exportar_excel'),
    path('api/dispositivos/<int:dispositivo_id>/exportar/pdf/', exportar_datos_pdf, name='exportar_pdf'),
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
    # Rutas para gestionar dispositivos
    path('api/dispositivos/', views.dispositivo_list_create, name='dispositivos-list-create'),
    path('api/dispositivos/<int:pk>/', views.dispositivo_detail, name='dispositivo-detail'),
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6

    # Rutas para llamadas
    path('api/dispositivos/<int:dispositivo_id>/llamadas/', views.llamadas_list_create, name='llamadas-list'),
    path('api/dispositivos/<int:dispositivo_id>/llamadas/<int:pk>/', views.llamadas_detail, name='llamadas-detail'),

    # Rutas para mensajes
    path('api/dispositivos/<int:dispositivo_id>/mensajes/', views.mensajes_list_create, name='mensajes-list'),
    path('api/dispositivos/<int:dispositivo_id>/mensajes/<int:pk>/', views.mensajes_detail, name='mensajes-detail'),

    # Rutas para fotos
    path('api/dispositivos/<int:dispositivo_id>/fotos/', views.fotos_list_create, name='fotos-list'),
    path('api/dispositivos/<int:dispositivo_id>/fotos/<int:pk>/', views.fotos_detail, name='fotos-detail'),

    # Rutas para videos
    path('api/dispositivos/<int:dispositivo_id>/videos/', views.videos_list_create, name='videos-list'),
    path('api/dispositivos/<int:dispositivo_id>/videos/<int:pk>/', views.videos_detail, name='videos-detail'),

    # Rutas para ubicaciones
    path('api/dispositivos/<int:dispositivo_id>/ubicaciones/', views.ubicaciones_list_create, name='ubicaciones-list'),
    path('api/dispositivos/<int:dispositivo_id>/ubicaciones/<int:pk>/', views.ubicaciones_detail, name='ubicaciones-detail'),

    # Rutas para grabaciones de llamadas
    path('api/dispositivos/<int:dispositivo_id>/grabaciones-llamadas/', views.grabaciones_llamadas_list_create, name='grabaciones-llamadas-list'),
    path('api/dispositivos/<int:dispositivo_id>/grabaciones-llamadas/<int:pk>/', views.grabacion_llamada_detail, name='grabacion-llamada-detail'),

    # Rutas para grabaciones de pantalla
    path('api/dispositivos/<int:dispositivo_id>/grabaciones-pantalla/', views.grabaciones_pantalla_list_create, name='grabaciones-pantalla-list'),
    path('api/dispositivos/<int:dispositivo_id>/grabaciones-pantalla/<int:pk>/', views.grabacion_pantalla_detail, name='grabacion-pantalla-detail'),

    # Rutas para capturas de pantalla
    path('api/dispositivos/<int:dispositivo_id>/capturas-pantalla/', views.capturas_pantalla_list_create, name='capturas-pantalla-list'),
    path('api/dispositivos/<int:dispositivo_id>/capturas-pantalla/<int:pk>/', views.capturas_pantalla_detail, name='capturas-pantalla-detail'),

    # Rutas para contactos
    path('api/dispositivos/<int:dispositivo_id>/contactos/', views.contactos_list_create, name='contactos-list'),
    path('api/dispositivos/<int:dispositivo_id>/contactos/<int:pk>/', views.contacto_detail, name='contacto-detail'),

    # Rutas para verificación de permisos
    path('api/dispositivos/<int:dispositivo_id>/verificacion-permisos/', views.verificacion_permisos_list_create, name='verificacion-permisos-list'),
    path('api/dispositivos/<int:dispositivo_id>/verificacion-permisos/<int:pk>/', views.verificacion_permiso_detail, name='verificacion-permiso-detail'),
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

    # -------------------- Rutas para las páginas HTML --------------------
    
    path('', views.index, name='index'),  # Página principal (index)
    path('archivo_telefono/', views.archivo_telefono, name='archivo_telefono'),
    path('capturas/', views.capturas, name='capturas'),
    path('caracteristicas/', views.caracteristicas, name='caracteristicas'),
    path('compras/', views.compras, name='compras'),
    path('cuenta/', views.cuenta, name='cuenta'),
    path('exportar_datos/', views.exportar_datos, name='exportar_datos'),
    path('grabacion/', views.grabacion, name='grabacion'),
    path('inicio/', views.inicio, name='inicio'),
    path('login/', views.login, name='login'),
    path('mi_producto/', views.mi_producto, name='mi_producto'),
    path('mis_dispositivos/', views.mis_dispositivos, name='mis_dispositivos'),
    path('panel_control/', views.panel_control, name='panel_control'),
    path('politica/', views.politica, name='politica'),
    path('preguntas/', views.preguntas, name='preguntas'),
    path('prueba/', views.prueba, name='prueba'),
    path('productos/', views.productos, name='productos'),
    path('recuperar_contra/', views.recuperar_contra, name='recuperar_contra'),
    path('recursos/', views.recursos, name='recursos'),
    path('registrarse/', views.registrarse, name='registrarse'),
<<<<<<< HEAD
    path('reg_event/', views.reg_event, name='reg_event'),
=======
<<<<<<< HEAD
    path('reg_event/', views.reg_event, name='reg_event'),
=======
    path('registro/', views.registro, name='registro'),
>>>>>>> b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
    path('soporte/', views.soporte, name='soporte'),
    path('terminos/', views.terminos, name='terminos'),
    path('ubicacion/', views.ubicacion, name='ubicacion'),
    path('verificacion_permisos/', views.verificacion_permisos, name='verificacion_permisos'),
]

# Añadir las rutas para servir archivos estáticos y de medios en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
]
>>>>>>> 052f2d3b4d3ee496a9b96224faedb68f377a196d
>>>>>>> a8d19f143da4dcdf7a22fd08e935b212cf57580a
>>>>>>> b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
>>>>>>> b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
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
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
