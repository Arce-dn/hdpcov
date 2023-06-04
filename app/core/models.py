from django.db import models

from django.db import models
from datetime import datetime

from core.choices import gender_choices


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)

    def __str__(self):
        return 'Nombre: {}'.format(self.name)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']


class Efecto(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    cate = models.ForeignKey(Category, on_delete=models.CASCADE)
    detalle = models.CharField(max_length=250, null=True, blank=True, verbose_name='Detalle')
    image = models.ImageField(upload_to='efecto%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Efecto'
        verbose_name_plural = 'Efectos'
        ordering = ['id']


class Estudiante(models.Model):
    names = models.CharField(max_length=150, verbose_name='Nombres')
    surnames = models.CharField(max_length=150, verbose_name='Apellidos')
    birthday = models.DateField(default=datetime.now, verbose_name='Fecha de nacimiento')
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name='Dirección')
    sexo = models.CharField(max_length=10, choices=gender_choices, default='male', verbose_name='Sexo')

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'
        ordering = ['id']


class Universidad(models.Model):
    estu = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name='Dirección')


    def __str__(self):
        return self.cli.names

    class Meta:
        verbose_name = 'Universidad'
        verbose_name_plural = 'Universidades'
        ordering = ['id']


class DetNoticia(models.Model):
    uni = models.ForeignKey(Universidad, on_delete=models.CASCADE)
    efect = models.ForeignKey(Efecto, on_delete=models.CASCADE)
    detalles = models.CharField(max_length=150, null=True, blank=True, verbose_name='Detalles')


    def __str__(self):
        return self.prod.name

    class Meta:
        verbose_name = 'Detalle de Noticia'
        verbose_name_plural = 'Detalle de Noticias'
        ordering = ['id']
