from rest_framework import viewsets
from HotelIFBA.models import Cliente, Empresa
from HotelIFBA.serializer import EmpresaSerializer, ClienteSerializer

class EmpresasViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
