from django.shortcuts import render
from Decoraciones.models import catalogo
# Lista de elementos
list_producto=catalogo.objects.all()
#Pagina de Inicio
def Home(request):
    return render(request,"home.html",{"producs":list_producto})
def Bebidas(request):
    return render(request,"Bbs.html",{"producs":list_producto})
def Bocaditos(request):
    return render(request,"Bts.html",{"producs":list_producto})
def Equipos(request):
    return render(request,"Eps.html",{"producs":list_producto})
def Decoraciones(request):
    return render(request,"Dec.html",{"producs":list_producto})