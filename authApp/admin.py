from django.contrib import admin
from .models.person import persona
from .models.carro import carro
from .models.clientes import Cliente
from .models.purchase import Compra


# Register your models here.

admin.site.register(persona)
admin.site.register(carro)
admin.site.register(Cliente)
admin.site.register(Compra)
