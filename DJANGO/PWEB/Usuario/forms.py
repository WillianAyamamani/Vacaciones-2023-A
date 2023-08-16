from typing import Any
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from Usuario.models import Usuario
from django import forms

class FormularioLogin(AuthenticationForm):
    def __init__(self,*args, **kwargs):
        super(FormularioLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de Usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'

class FormularioUser(forms.ModelForm):
    password1 = forms.CharField(label = "Contraseña", widget = forms.PasswordInput(
        attrs = {
               'class' : 'form-control',
               'placeholder' : 'Ingrese su contraseña ...'  ,
               'id' : 'password1',
                'required' : 'required',
        }
    ))
    password2 =  forms.CharField(label = 'Contraseña de Confirmacion', widget = forms.PasswordInput(
        attrs = {
               'class' : 'form-control',
               'placeholder' : 'Ingrese nuevamente su contraseña ...'  ,
               'id' : 'password2',
                'required' : 'required',
        }
    ))

    class Meta:
        model = Usuario
        fields = ('email','userName','nombres','apellidos')
        widgets = {
            'email': forms.EmailInput(
                attrs={
                'class': 'form-control',
                'placeholder': 'Correo Electronico',
                }
            ),
            'nombres': forms.TextInput(
                attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su NOMBRE',
                }
            ),
            'apellidos': forms.TextInput(
                attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese sus APELLIDOS',
                }
            ),
            'userName': forms.TextInput(
                attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su Nombre de Usuario',
                }
            ),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')     
        password2 = self.cleaned_data.get('password2')     
        if(password1 and password2 and password1 != password2):
            raise forms.ValidationError('las contraseñas no coinciden')
        return password2
    def save(self, commit = True):
        user = super().save(commit = False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
'''class Pedidos(forms.ModelForm):

    class Meta:
        model = Pedido
        fields = ('NombreC','ApellidosC', 'telefono','Correo','direccion','fecha')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fecha'].label = 'Fecha (A-M-D)'
'''