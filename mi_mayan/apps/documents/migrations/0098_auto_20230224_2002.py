# Generated by Django 3.2.16 on 2023-02-24 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0097_remove_solicitud_equivalencias_guarani_tutores'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='constancia_examen',
            name='domicilio',
        ),
        migrations.RemoveField(
            model_name='constancia_examen',
            name='tutores',
        ),
    ]
