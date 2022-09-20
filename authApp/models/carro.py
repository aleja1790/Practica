from django.db import models

class carro(models.Model):
    nombre = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
   