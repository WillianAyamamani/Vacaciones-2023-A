from django.db import models

class Tipo(models.Model):
    Tip = models.CharField(max_length=50, default=None, null=True)

    def __str__(self):
        return self.Tip
    
class Producto(models.Model):
    nombre = models.CharField(max_length=25)
    descripcion = models.TextField()
    precio = models.CharField(max_length=25)

    class Meta:
        abstract = True

class catalogo(Producto):
    imagen = models.ImageField(null=True, blank=True, upload_to="img/")
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nombre

class Carrito(Producto):
    adquirido = models.BooleanField()
    rutaI = models.CharField(null=True, max_length=50000)
    
class Pedido(models.Model):
    NombreC = models.CharField(null=True, max_length=50)
    ApellidosC = models.CharField(null=True, max_length=50)
    telefono = models.IntegerField(null=True)
    Correo = models.EmailField(max_length=254, default='')
    direccion = models.CharField(max_length=50)
    fecha = models.DateField()
    Carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, null=True)
