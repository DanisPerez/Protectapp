# Generated by Django 5.1.1 on 2024-10-22 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0011_historialevento_usuario_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grabacionespantalla',
            name='ruta_grabacion',
        ),
        migrations.AddField(
            model_name='grabacionesllamadas',
            name='archivo_audio',
            field=models.FileField(default='llamadas/default.mp3', upload_to='llamadas/'),
        ),
        migrations.AddField(
            model_name='grabacionespantalla',
            name='archivo_video',
            field=models.FileField(default='llamadas/default.mp3', upload_to='grabaciones/pantalla/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='grabacionespantalla',
            name='fecha',
            field=models.DateField(auto_now_add=True),
        ),
    ]
