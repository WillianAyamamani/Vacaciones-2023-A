from django.utils import timezone
from django.db import models
from Usuario.models import Usuario



# Create your models here.

class Fiesta(models.Model):
    motivo = models.CharField("Fiesta", max_length=50)

class Galeria(models.Model):
    Imagen = models.ImageField("Imagen",null=True, blank=True, upload_to="img/")

    def __str__(self):
        return self.Imagen.url

class Tipo(models.Model):
    Tip = models.CharField(max_length=50, default=None, null=True)

    def __str__(self):
        return self.Tip

    
class Distrito(models.Model):
    distrito = models.CharField("Distrito", max_length=50)

    def __str__(self):
        return self.distrito

class Asociaciones (models.Model):
    Distrito = models.ForeignKey(Distrito, on_delete=models.CASCADE)
    Asoc = models.CharField("Asociacion - Sector", max_length= 250)
    Mz = models.CharField(max_length=1, choices=[(chr(i), chr(i)) for i in range(65, 91)])
    Lt = models.IntegerField("Lote")

    def __str__(self):
        return f'{self.Distrito}>>{self.Asoc}>>{self.Mz}-{self.Lt}'
    
class Producto(models.Model):
    nombre = models.CharField(max_length=25)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    #Nivel de Categorias -> CTG: [A > B > C > D]
    Estado = models.BooleanField("Activo", default=True)
    Compra = models.BooleanField("Seleccionado (S/N)", default=False)

    class Meta:
        abstract = True

class catalogo(Producto):
    imagen = models.ForeignKey(Galeria, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.nombre
    

class Carrito(Producto):
    comprador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    adquirido = models.BooleanField()
    cantidad = models.IntegerField("Cantidad: U")
    rutaI = models.CharField(null=True, max_length=50000)

class Pedido(models.Model):
    Entregado = models.BooleanField()
    direccion = models.CharField(max_length=50)
    fecha = models.DateField()
    Carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, null=True)