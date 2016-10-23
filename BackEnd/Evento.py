'''
Created on 23 oct. 2016

@author: Macarena
'''

from django.db import models

class Evento(models.Model):
    codigo = models.CharField(max_length=3)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    detalle = models.CharField(max_length=600)
    idLugar  = models.IntegerField()
    idCategoria = models.IntegerField()
    fecha = models.DateTimeField()
    afiche = models.FilePathField()  # filepath o url ??
    entradasVendidas = models.IntegerField()
    entradasDisponibles = models.IntegerField()
    entradasRestantes = models.IntegerField()
    estado = models.CharField(max_length=50)