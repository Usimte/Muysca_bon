from django.db import models
# from django.utils import timezone
from .utilidades import *

# Create your models here.


class Registro_censo(models.Model):
    vigencia = models.DateField(auto_now=True)
    resguardo = models.CharField(max_length=10, blank=True)
    comunidad_indigena = models.CharField(max_length=10, blank=True)
    familia = models.CharField(max_length=10)
    tipo_identificacion = models.CharField(
        max_length=6, choices=TIPO_IDENTIFICACION_CHOICES,
        default=CEDULA_CIUDADANIA)
    numero_documento = models.CharField(max_length=10)
    nombres = models.CharField(max_length=60)
    apellidos = models.CharField(max_length=60)
    # formato MM/DD/AAAA
    fecha_nacimiento = models.DateField(blank=True)
    parentesco = models.CharField(
        max_length=4, choices=PARENTESCO_CHOICES, default=CABEZA_FAMILIA)
    genero = models.CharField(max_length=2, choices=GENERO_CHOICES)
    estado_civil = models.CharField(
        max_length=2, choices=ESTADO_CIVIL_CHOICES, default=SOLTERO)
    profesion = models.CharField(blank=True, max_length=10)
    escolaridad = models.CharField(
        max_length=3, choices=ESCOLARIDAD_CHOICES, default=PRIMARIA)
    integrantes = models.IntegerField()
    direccion = models.CharField(max_length=60)
    telefono = models.CharField(max_length=15)
    usuario = models.CharField(max_length=15)

    def __str__(self):
        return self.nombres + " " + self.apellidos
