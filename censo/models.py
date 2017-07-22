from django.db import models
from django.utils import timezone
# from django.utils import timezone
from .utilidades import *
from openpyxl import Workbook

# Create your models here.


class censo_archivo(models.Model):
    '''Clase de archivo censo

    Es el formato cargado al sistema e historial de censos existentes'''
    archivo = models.FileField(upload_to='formatos/')
    fecha_subida = models.DateTimeField(default=timezone.now)
    fecha_censo = models.DateField()

    # TODO: función para carga de archivos
    def cargar_registros(self):
        '''Carga registros a partir de un formato subido por el usuario.'''
        None


class registro_censo(models.Model):
    '''Clase de registro de censo.

    Está basado en el formato expedido por el ministerio del interior
    de la república de Colombia'''
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
