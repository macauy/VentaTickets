'''
Created on 23 oct. 2016

@author: Macarena
'''

from django.db import models

class Precio(models.Model):
    idEvento = models.IntegerField()
    idSector = models.IntegerField()
    precio = models.DecimalField(decimal_places=2,max_digits=10)