# Generated by Django 4.2.1 on 2023-06-03 01:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=150, verbose_name='Nombres')),
                ('surnames', models.CharField(max_length=150, verbose_name='Apellidos')),
                ('birthday', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de nacimiento')),
                ('address', models.CharField(blank=True, max_length=150, null=True, verbose_name='Dirección')),
                ('sexo', models.CharField(choices=[('male', 'Masculino'), ('female', 'Femenino')], default='male', max_length=10, verbose_name='Sexo')),
            ],
            options={
                'verbose_name': 'Estudiante',
                'verbose_name_plural': 'Estudiantes',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Universidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=150, null=True, verbose_name='Dirección')),
                ('estu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.estudiante')),
            ],
            options={
                'verbose_name': 'Universidad',
                'verbose_name_plural': 'Universidades',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Efecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Nombre')),
                ('detalle', models.CharField(blank=True, max_length=250, null=True, verbose_name='Detalle')),
                ('image', models.ImageField(blank=True, null=True, upload_to='efecto%Y/%m/%d')),
                ('cate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.category')),
            ],
            options={
                'verbose_name': 'Efecto',
                'verbose_name_plural': 'Efectos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='DetNoticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalles', models.CharField(blank=True, max_length=150, null=True, verbose_name='Detalles')),
                ('efect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.efecto')),
                ('uni', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.universidad')),
            ],
            options={
                'verbose_name': 'Detalle de Noticia',
                'verbose_name_plural': 'Detalle de Noticias',
                'ordering': ['id'],
            },
        ),
    ]
