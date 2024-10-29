
from django.contrib import admin
from .models import Usuario, Dispositivo, Llamadas, Mensajes, Contactos, Fotos, Videos, Ubicaciones, GrabacionesLlamadas, GrabacionesPantalla, CapturasPantalla, VerificacionPermisos, HistorialEvento

# Registrar todos los modelos para que sean visibles en el panel de administración
admin.site.register(Usuario)
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

# Registro de Historial de Eventos con personalización del administrador
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
