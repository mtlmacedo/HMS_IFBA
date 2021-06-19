from rest_framework import viewsets
from HotelIFBA.models import Cliente, Empresa, Colaborador
from HotelIFBA.serializer import EmpresaSerializer, ClienteSerializer, ColaboradorSerializer

class EmpresasViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ColaboradorViewSet(viewsets.ModelViewSet):
    queryset = Colaborador.objects.all()
    serializer_class = ColaboradorSerializer