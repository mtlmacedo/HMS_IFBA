from django import urls
from django.contrib import admin, auth
from django.urls import path, include
from hmsifba.views import *
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'usuarios', UserViewSet)
router.register(r'grupos', GroupViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="HMS IFBA",
      default_version='v1.0.0',
      description="Sistema de Gerenciamento de Hotéis(HMS) implementado em Python/Django",
      terms_of_service="https://www.google.com/policies/terms/",
      authors="Matheus Alves e Matheus Macedo",
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('login/', obtain_auth_token, name="login"),
    path('register/', registration_view, name="register"),
    path('logout/', logout),

    path('empresas/', get_empresa),
    path('empresas/<int:pk>', detalhar_empresa),

    path('quartos/', get_quarto),
    path('quartos/<int:pk>', detalhar_quarto),
    path('quartos-disponiveis/<int:pk>', quartos_disponiveis),

    path('estadias/', get_estadia),
    path('estadias/<int:pk>', detalhar_estadia),

    path('reservas/', get_reserva),
    path('reservas/<int:pk>', detalhar_reserva),

    path('servicos/', get_tipo_servico),
    path('servico/<int:pk>', detalhar_tipo_servico),

    path('clientes/', get_cliente),
    path('clientes/<int:pk>', detalhar_cliente),

    path('colaboradores/', get_colaborador),
    path('colaboradores/<int:pk>', detalhar_colaborador),

    path('estatisticas/', get_estatistica),
]
