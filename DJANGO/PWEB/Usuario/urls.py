from django.urls import path
from . import views
urlpatterns = [
    path('Ingreso/', views.login_U, name="Login"),
    path('salida/', views.logout_U, name="Logout"),
    path('registro/', views.regist_U, name="Registro"),
    path('Contrato/', views.Proforma, name="contrato"),
    path('Agregar/', views.agregar, name="carrito"),
    path('lista/', views.lista, name="bolsa"),
    path('Borrar/<int:numero>/', views.borrar, name='borrar'),
]
