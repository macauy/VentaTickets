'''
Created on 23 oct. 2016

@author: Macarena
'''


from django.db import models
from BackEnd.Telefono import Telefono

class Reserva(models.Model):
    cliente = models.ForeignKey(Telefono, null=True)
    nroEntradas = models.IntegerField()
    precioTotal = models.DecimalField(max_digits=10,decimal_places=2, default=0)