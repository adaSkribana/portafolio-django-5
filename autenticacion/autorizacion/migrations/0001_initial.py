# Generated by Django 5.0.4 on 2024-04-27 23:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Texto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254)),
                ('comentario', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('texto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autorizacion.texto')),
            ],
        ),
    ]
