from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from django.db.models import Sum
from Usuario.forms import Registro,Pedidos
from Decoraciones.models import Carrito
# Create your views here.

#Lista de productos.
List_prod=Carrito.objects.all()

def login_U(request):
    if request.method == "POST" :
        nombre=request.POST['username']
        contraseña=request.POST['password']
        usuario=authenticate(request,username=nombre,password=contraseña)
        if usuario is not None:
            login(request, usuario)
            return redirect('Inicio')
        else:
            messages.success(request, "Ocurrio -- Erro -- 403")
            return redirect('Login')
    else:
        return render(request, "login.html",{})

def logout_U(request):
    logout(request)
    #Aun por terminar
    #Carrito.objects.all().delete()
    return redirect('Login')
def regist_U(request):
    if request.method == "POST":
        form = Registro(request.POST)
        if form.is_valid():
            form.save()
            nombreN = form.cleaned_data['username']
            passN = form.cleaned_data['password1']
            usuarioA = authenticate(username=nombreN,password = passN)
            login(request,usuarioA)
            return redirect('Inicio')
    else:
        form=Registro()
    return render(request, 'registro.html',{"formulario":form})
def Proforma(request):
    if request.method == "POST":
        contrato = Pedidos(request.POST)
        if contrato.is_valid():
            contrato.save()
            contrato.carrito = Carrito.objects.all()
    else:
        contrato=Pedidos()
    return render(request, 'Proforma.html',{"Ped":contrato,"productos":List_prod})
def agregar(request):
    if request.method == "POST":
        nombreC = request.POST.get('nombre')
        descripcionC = request.POST.get('descripcion')
        precioC = request.POST.get('precio')
        urlC= request.POST.get('imagen_url')
        Articulo= Carrito(nombre=nombreC, descripcion=descripcionC, precio=precioC, adquirido=True, rutaI=urlC)
        Articulo.save()
        return redirect ("Inicio")
def borrar(request, numero):
    articulo = Carrito.objects.get(id=numero)
    articulo.delete()
    return redirect("bolsa")
def lista(request):
    listaArticulo=Carrito.objects.all()
    total = Carrito.objects.aggregate(Sum('precio'))['precio__sum'] or 0
    return render(request, 'lista.html', {"productos":listaArticulo,"total":total})