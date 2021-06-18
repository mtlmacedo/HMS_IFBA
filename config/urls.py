from django.contrib import admin
from django.urls import path, include
from HotelIFBA.views import EmpresasViewSet, ClienteViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('empresas', EmpresasViewSet)
router.register('clientes', ClienteViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
