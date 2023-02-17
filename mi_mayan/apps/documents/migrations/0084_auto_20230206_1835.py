# Generated by Django 3.2.16 on 2023-02-06 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0083_auto_20230206_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='extra',
            field=models.OneToOneField(blank=True, help_text='Los datos extras del documento.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='extras', to='documents.unq', verbose_name='Extra'),
        ),
        migrations.AlterField(
            model_name='document',
            name='extra2',
            field=models.OneToOneField(blank=True, help_text='Los datos extras del documento.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='extras', to='documents.unqdos', verbose_name='Extra dos'),
        ),
    ]