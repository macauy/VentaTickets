'''
Created on 23 oct. 2016

@author: Macarena
'''


from django.db import models

class Cliente(models.Model):
    telefono  = models.CharField(max_length=10)
    documento = models.CharField(max_length=10)
    nombre    = models.CharField(max_length=40)
    apellido  = models.CharField(max_length=40)