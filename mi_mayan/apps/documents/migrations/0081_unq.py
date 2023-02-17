# Generated by Django 3.2.16 on 2023-02-06 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0080_populate_file_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='UNQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(db_index=True, default='', help_text='nombres del estudiante.', max_length=255, verbose_name='Nombres')),
                ('apellido', models.CharField(db_index=True, default='', help_text='apellido del estudiante.', max_length=255, verbose_name='Apellido')),
            ],
        ),
    ]