'''
Created on 23 oct. 2016

@author: Macarena
'''


from django.db import models

class Telefono(models.Model):
    numero = models.CharField(max_length = 11, null = True, unique = True)
    documento = models.CharField(max_length=10)
    