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

from django.contrib import admin
from .models import Usuario, Dispositivo, Llamadas, Mensajes, Contactos, Fotos, Videos, Ubicaciones, GrabacionesLlamadas, GrabacionesPantalla, CapturasPantalla, VerificacionPermisos, HistorialEvento

# Registrar todos los modelos para que sean visibles en el panel de administración
admin.site.register(Usuario)
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 8e18bd6d3b44f892c4e048fb7e4e553c2d8fe619
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
from django.contrib import admin
<<<<<<< HEAD
from .models import Dispositivo, Llamadas, Mensajes, Contactos, Fotos, Videos, Ubicaciones, GrabacionesLlamadas, GrabacionesPantalla, CapturasPantalla, VerificacionPermisos, HistorialEvento

# Registrar todos los modelos para que sean visibles en el panel de administración
=======
<<<<<<< HEAD
from .models import Dispositivo, Llamadas, Mensajes, Contactos, Fotos, Videos, Ubicaciones, GrabacionesLlamadas, GrabacionesPantalla, CapturasPantalla, VerificacionPermisos

# Registrar todos los modelos para que sean visibles en el panel de administración
=======
<<<<<<< HEAD
from .models import Dispositivo, Llamadas, Mensajes, Contactos, Fotos, Videos, Ubicaciones, GrabacionesLlamadas, GrabacionesPantalla, CapturasPantalla, VerificacionPermisos

# Registrar todos los modelos para que sean visibles en el panel de administración
=======
<<<<<<< HEAD
from .models import Dispositivo, Llamadas, Mensajes, Contactos, Fotos, Videos, Ubicaciones, GrabacionesLlamadas, GrabacionesPantalla, CapturasPantalla, VerificacionPermisos

# Registrar todos los modelos para que sean visibles en el panel de administración
=======
<<<<<<< HEAD
from .models import Dispositivo, Llamadas, Mensajes, Contactos, Fotos, Videos, Ubicaciones, GrabacionesLlamadas, GrabacionesPantalla, CapturasPantalla, VerificacionPermisos

# Registrar todos los modelos para que sean visibles en el panel de administración
=======
<<<<<<< HEAD
from .models import Dispositivo, Llamadas, Mensajes, Contactos, Fotos, Videos, Ubicaciones, GrabacionesLlamadas, GrabacionesPantalla, CapturasPantalla, VerificacionPermisos

# Registrar todos los modelos para que sean visibles en el panel de administración
=======
from .models import Usuario, Dispositivo, Llamadas, Mensajes, Contactos, Fotos, Videos, Ubicaciones, GrabacionesLlamadas, GrabacionesPantalla, CapturasPantalla, VerificacionPermisos

# Registrar todos los modelos para que sean visibles en el panel de administración
admin.site.register(Usuario)
>>>>>>> d78f1636227f72ec3b372de20a52ae977a0beea7
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
admin.site.register(Dispositivo)
admin.site.register(Llamadas)
admin.site.register(Mensajes)
admin.site.register(Contactos)
admin.site.register(Fotos)
admin.site.register(Videos)
admin.site.register(Ubicaciones)
admin.site.register(GrabacionesLlamadas)
admin.site.register(GrabacionesPantalla)
admin.site.register(CapturasPantalla)
admin.site.register(VerificacionPermisos)
<<<<<<< HEAD

# Registro de Historial de Eventos con personalización del administrador
=======
<<<<<<< HEAD

# Registro de Historial de Eventos con personalización del administrador
=======
<<<<<<< HEAD

<<<<<<< HEAD
# Registro de Historial de Eventos con personalización del administrador
=======
<<<<<<< HEAD

=======
<<<<<<< HEAD
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
# Registro de Historial de Eventos con personalización del administrador
=======
<<<<<<< HEAD



>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
>>>>>>> 7c9c8fce799681b798ac83cabdaf1af962be551a
<<<<<<< HEAD
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
=======
=======


>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
>>>>>>> 8e18bd6d3b44f892c4e048fb7e4e553c2d8fe619
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
>>>>>>> b5ca5ef48d2ae9ff505b8711631613fc593d45d5
@admin.register(HistorialEvento)
class HistorialEventoAdmin(admin.ModelAdmin):
    list_display = ('dispositivo', 'tipo_evento', 'fecha', 'hora', 'detalles')
    search_fields = ('dispositivo__nombre', 'tipo_evento')
    list_filter = ('tipo_evento', 'fecha')

    # Sobrescribimos el método save_model para agregar el usuario automáticamente
    def save_model(self, request, obj, form, change):
        if not obj.usuario:
            obj.usuario = request.user  # Asigna el usuario logueado
        super().save_model(request, obj, form, change)
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
=======
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
>>>>>>> 7c9c8fce799681b798ac83cabdaf1af962be551a
<<<<<<< HEAD
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
=======
=======
=======
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
>>>>>>> 8e18bd6d3b44f892c4e048fb7e4e553c2d8fe619
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
>>>>>>> b5ca5ef48d2ae9ff505b8711631613fc593d45d5
