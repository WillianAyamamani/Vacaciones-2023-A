from django.urls import path
from Decoraciones import views
urlpatterns = [
    path('', views.Home, name="Inicio"),
    path('Bebidas/', views.Bebidas, name="Bebidas"),
    path('Bocaditos/', views.Bocaditos, name="Bocaditos"),
    path('Equipos/', views.Equipos, name="Equipos"),
    path('Decoraciones/', views.Decoraciones, name="Decoraciones"),
]
