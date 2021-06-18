from django.contrib import admin
from django.urls import path, include
from HotelIFBA.views import EmpresasViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'empresas', EmpresasViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
