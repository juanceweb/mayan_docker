# Generated by Django 3.2.16 on 2023-02-07 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0087_alter_solicitud_aviso_ultimo_examen_tel_contacto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Constancia_Aprobacion_Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_propuesta', models.CharField(db_index=True, help_text='codigo de la propuesta.', max_length=255, verbose_name='codigo Propuesta')),
                ('descripcion_propuesta', models.CharField(db_index=True, help_text='descripcion de la propuesta.', max_length=255, verbose_name='descripcion propuesta')),
                ('nombres', models.CharField(db_index=True, help_text='nombres del estudiante.', max_length=255, verbose_name='nombres')),
                ('apellido', models.CharField(db_index=True, help_text='apellido del estudiante.', max_length=255, verbose_name='apellido')),
                ('tipo_documento', models.CharField(db_index=True, help_text='tipo de documento', max_length=255, verbose_name='tipo documento')),
                ('nro_documento', models.CharField(db_index=True, help_text='numero de documento.', max_length=255, verbose_name='numero documento')),
                ('agente_presentacion', models.CharField(db_index=True, help_text='agente de presentacion.', max_length=255, verbose_name='agente presentacion')),
                ('descripcion_actividad', models.CharField(db_index=True, help_text='descripcion de la actividad.', max_length=255, verbose_name='descripcion actividad')),
            ],
        ),
        migrations.AddField(
            model_name='document',
            name='constancia_aprobacion_materia',
            field=models.OneToOneField(blank=True, help_text='si el doc es una constancia de aprobacion de materia.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='extras', to='documents.constancia_aprobacion_materia', verbose_name='constancia aprobacion materia'),
        ),
    ]
