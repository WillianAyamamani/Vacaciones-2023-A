from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
# Create your views here.
class Login(LoginView):
    template_name = 'login.html'
def Logout(request):
    logout(request)
    return redirect('Inicio')
