"""
URL configuration for PWEB project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers, serializers, viewsets
from django.conf import settings
from django.conf.urls.static import static
from Usuario.views import Login,logoutUsuario
from django.contrib.auth.decorators import login_required

from Decoraciones.models import Tipo,Carrito,catalogo

class TipoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tipo
        fields = ['Tip']

# ViewSets define the view behavior.
class TipoViewSet(viewsets.ModelViewSet):
    queryset = Tipo.objects.all()
    serializer_class = TipoSerializer

class CarritoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Carrito
        fields = ['nombre','precio','rutaI']

# ViewSets define the view behavior.
class CarritoViewSet(viewsets.ModelViewSet):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer

class CatalogoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = catalogo
        fields = ['nombre','precio','imagen','tipo']

# ViewSets define the view behavior.
class CatalogoViewSet(viewsets.ModelViewSet):
    queryset = catalogo.objects.all()
    serializer_class = CatalogoSerializer

#class PedidoSerializer(serializers.HyperlinkedModelSerializer):
#    class Meta:
#        model = Pedido
#        fields = ['NombreC','telefono','direccion','fecha']

# ViewSets define the view behavior.
#class PedidoViewSet(viewsets.ModelViewSet):
#    queryset = Pedido.objects.all()
#    serializer_class = PedidoSerializer

router = routers.DefaultRouter()
router.register(r'Tipo', TipoViewSet)
router.register(r'Carrito', CarritoViewSet)
router.register(r'Catalogo', CatalogoViewSet)
#router.register(r'Pedido', PedidoViewSet)

urlpatterns = [
    path('rest/', include(router.urls)),
    path('api-auth/',include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('', include('Decoraciones.urls', namespace='Decoraciones' )),
    path('Usuario/', include('Usuario.urls', namespace='usuario')),
    path('Usuario/', include('django.contrib.auth.urls')),
    path('accounts/login/',Login.as_view(), name="login"),
    path('logout/',login_required(logoutUsuario), name="logout"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
