from django.contrib import admin
#from Decoraciones.models import Pedido,catalogo,Carrito,Tipo,Usuario
from Decoraciones.models import Tipo,Distrito,Asociaciones,Galeria,Fiesta,catalogo
# Register your models here.
admin.site.register(Galeria)
admin.site.register(Tipo)
admin.site.register(Distrito)
admin.site.register(Asociaciones)
admin.site.register(catalogo)
admin.site.register(Fiesta)
#admin.site.register(Tipo)
#admin.site.register(Pedido)
#admin.site.register(catalogo)
#admin.site.register(Carrito)