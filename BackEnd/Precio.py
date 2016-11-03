'''
Created on 23 oct. 2016

@author: Macarena
'''

from django.db import models
from BackEnd.Evento import Evento
from BackEnd.Sector import Sector

class Precio(models.Model):
    evento = models.ForeignKey(Evento, null=True)
    sector = models.ForeignKey(Sector, null=True)
    precio = models.DecimalField(decimal_places=2,max_digits=10)