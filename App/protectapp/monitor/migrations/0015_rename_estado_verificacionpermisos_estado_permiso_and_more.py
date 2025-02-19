# Generated by Django 5.1.1 on 2024-10-22 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0014_remove_fotos_ruta_foto_fotos_archivo_foto_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='verificacionpermisos',
            old_name='estado',
            new_name='estado_permiso',
        ),
        migrations.AlterField(
            model_name='verificacionpermisos',
            name='fecha_verificacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='verificacionpermisos',
            name='tipo_permiso',
            field=models.CharField(blank=True, choices=[('CAMERA', 'Cámara'), ('ACCESS_FINE_LOCATION', 'Ubicación Precisa'), ('ACCESS_COARSE_LOCATION', 'Ubicación Aproximada'), ('READ_CONTACTS', 'Leer Contactos'), ('WRITE_CONTACTS', 'Modificar Contactos'), ('RECORD_AUDIO', 'Grabar Audio'), ('READ_EXTERNAL_STORAGE', 'Leer Almacenamiento Externo'), ('WRITE_EXTERNAL_STORAGE', 'Escribir en Almacenamiento Externo'), ('CALL_LOG', 'Registro de Llamadas'), ('READ_SMS', 'Leer SMS'), ('SEND_SMS', 'Enviar SMS'), ('READ_PHONE_STATE', 'Estado del Teléfono'), ('BLUETOOTH', 'Bluetooth'), ('NOTIFICATIONS', 'Notificaciones'), ('INTERNET', 'Acceso a Internet'), ('FOREGROUND_SERVICE', 'Servicio en Primer Plano'), ('BACKGROUND_LOCATION', 'Ubicación en Segundo Plano'), ('ACCESS_WIFI_STATE', 'Estado del Wi-Fi'), ('MODIFY_AUDIO_SETTINGS', 'Modificar Configuración de Audio'), ('VIBRATE', 'Controlar Vibración')], max_length=50, null=True),
        ),
    ]
