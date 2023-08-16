from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.


class UsuarioManager(BaseUserManager):
    def create_user(self, email, userName, nombres, apellidos, password=None):
        if not email:
            raise ValueError('El usuario requiere un email!')
        
        usuario = self.model(
            email=self.normalize_email(email),
            userName=userName,  # Usa 'userName' en lugar de 'username'
            nombres=nombres, 
            apellidos=apellidos,
        )
        
        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self, email, userName, nombres, apellidos, password):
        usuario = self.create_user( 
            email,
            userName=userName,
            nombres=nombres, 
            apellidos=apellidos,
            password=password,
        )   
        usuario.usuario_admin = True
        usuario.save()
        return usuario


class Usuario (AbstractBaseUser):
    userName = models.CharField('nombre de Usuario', unique= True, max_length=100)
    email = models.EmailField('Correo Electronico',unique=True, max_length=25)
    nombres = models.CharField('Nombres', max_length=50,blank=True,null=True)
    apellidos = models.CharField('Apellidos', max_length=250,blank=True,null=True)
    perfil = models.ImageField("Imagen",null=True, blank=True, upload_to="img/")
    usuario_activo = models.BooleanField(default = True)
    usuario_admin =models.BooleanField(default = False)
    objeto = UsuarioManager()

    USERNAME_FIELD = 'userName'
    REQUIRED_FIELDS = ['email','nombres','apellidos']

    def __str__(self):
        return f'{self.nombres},{self.apellidos}'
    

    def has_perm(self,perm,obj = None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    
    @property
    def is_staff(self):
        return self.usuario_admin
