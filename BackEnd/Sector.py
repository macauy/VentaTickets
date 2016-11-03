'''
Created on 23 oct. 2016

@author: Macarena
'''

from django.db import models
from BackEnd.Lugar import Lugar

class Sector(models.Model):
    codigo = models.CharField(max_length=3)
    nombre = models.CharField(max_length=40)
    lugar  = models.ForeignKey(Lugar, null=True)