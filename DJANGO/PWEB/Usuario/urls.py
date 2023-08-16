from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView,logout_then_login
from django.urls import path
from . import views

app_name = 'usuario'

urlpatterns = [
    path('descargar_pdf/', views.download_pdf, name='descargar_pdf'),
    path('Registro/', views.regist_U.as_view(),name = "regist_u"),
    path('Contrato/', views.Proforma, name="contrato"),
    path('Agregar/', views.agregar, name="carrito"),
    path('lista/', views.lista, name="bolsa"),
    path('Borrar/<int:numero>/', views.borrar, name='borrar'),
    ]
