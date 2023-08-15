from django.contrib import admin
from Decoraciones.models import Pedido,catalogo,Carrito,Tipo
# Register your models here.
admin.site.register(Tipo)
admin.site.register(Pedido)
admin.site.register(catalogo)
admin.site.register(Carrito)