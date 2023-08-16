from django.shortcuts import render
from Decoraciones.models import catalogo

def Historial(request):
    histories = catalogo.historial.all()
    return render(request, "Historial.html", {'History': histories})
# Lista de elementos
#Pagina de Inicio
def UPdate(request):
    return render(request, "update.html",{})

def Home(request):
    list_producto=catalogo.objects.all()
    return render(request,"home.html",{"producs":list_producto})
def Bebidas(request):
    list_producto=catalogo.objects.all()
    return render(request,"Bbs.html",{"producs":list_producto})
def Bocaditos(request):
    list_producto=catalogo.objects.all()
    return render(request,"Bts.html",{"producs":list_producto})
def Equipos(request):
    list_producto=catalogo.objects.all()
    return render(request,"Eps.html",{"producs":list_producto})
def Decoraciones(request):
    list_producto=catalogo.objects.all()
    return render(request,"Dec.html",{"producs":list_producto})