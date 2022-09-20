from functools import total_ordering
from multiprocessing.dummy.connection import Client
from django.db import models
from .clientes import Cliente

class Compra(models.Model):
    total_count =models.PositiveIntegerField()
    fecha = models.DateTimeField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)