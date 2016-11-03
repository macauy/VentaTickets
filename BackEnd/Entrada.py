'''
Created on 2 nov. 2016

@author: Macarena
'''


from django.db import models
from BackEnd.Precio import Precio
from BackEnd.Reserva import Reserva

class Entrada(models.Model):
    precio = models.ForeignKey(Precio, null=True)
    codigoQR = models.CharField(max_length=200)
    reserva = models.ForeignKey(Reserva, null=True)