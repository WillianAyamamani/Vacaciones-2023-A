from django.urls import path
from . import views

urlpatterns = [
    #urls >> BUFFETApp >> Home
    path('Home', views.home, name="Inicio"),
    #urls >> BUFFETApp >> Decoraciones
    path('Decoraciones', views.home, name="Decoraciones"),
    #urls >> BUFFETApp >> Comida
    path('Comida', views.home, name="Comida"),
    #urls >> BUFFETApp >> Bebidas
    path('Bebidas', views.home, name="Bebidas"),
    #urls >> BUFFETApp >> Mesas
    path('Mesas', views.home, name="Mesas"),
    #urls >> BUFFETApp >> Equipo
    path('Equipo', views.home, name="Equipo"),
    #urls >> BUFFETApp >> Personal
    path('Personal', views.home, name="Personal"),
    #urls >> BUFFETApp >> Transporte
    path('Transporte', views.home, name="Transporte"),
]