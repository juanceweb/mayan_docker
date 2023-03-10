# Generated by Django 3.2.16 on 2023-03-03 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0100_auto_20230227_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='email_alumno',
            field=models.EmailField(db_index=True, default='juani@hotmail.com', help_text='email.', max_length=255, verbose_name='email'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='id_alumno',
            field=models.CharField(db_index=True, default=245, help_text='uuid del alumno', max_length=255, verbose_name='uuid'),
            preserve_default=False,
        ),
    ]
