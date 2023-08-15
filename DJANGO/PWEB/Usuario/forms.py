from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from Decoraciones.models import Pedido

class Registro(UserCreationForm):
    email = forms.EmailField(max_length=50)
    last_name= forms.CharField(max_length=120)
    first_name= forms.CharField(max_length=120)

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

class Pedidos(forms.ModelForm):

    class Meta:
        model = Pedido
        fields = ('NombreC','ApellidosC', 'telefono','Correo','direccion','fecha')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fecha'].label = 'Fecha (A-M-D)'