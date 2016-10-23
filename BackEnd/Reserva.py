'''
Created on 23 oct. 2016

@author: Macarena
'''
from django.db import models

class Reserva(models.Model):
    idPrecio = models.IntegerField()
    idCliente = models.IntegerField()
    aprobada = models.BooleanField()
    codigoQR = models.FilePathField()