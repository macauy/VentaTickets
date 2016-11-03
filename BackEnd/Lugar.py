'''
Created on Oct 21, 2016

@author: sisinfo
'''

#from Lib.Model.Model import Model
from django.db import models
#import FrontEnd

class Lugar(models.Model):
    codigo      = models.CharField(max_length=3, null = True)
    nombre      = models.CharField(max_length=50, null = True)
    mapaLugar   = models.CharField(max_length=50, null = True)