<<<<<<< HEAD
from django.urls import path
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
