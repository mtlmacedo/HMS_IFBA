from rest_framework import viewsets
from HotelIFBA.models import Cliente, Empresa, Colaborador, Reserva, Estadia
from HotelIFBA.serializer import EmpresaSerializer, ClienteSerializer, ColaboradorSerializer, ReservaSerializer, EstadiaSerializer

class EmpresasViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ColaboradorViewSet(viewsets.ModelViewSet):
    queryset = Colaborador.objects.all()
    serializer_class = ColaboradorSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class EstadiaViewSet(viewsets.ModelViewSet):
    queryset = Estadia.objects.all()
    serializer_class = EstadiaSerializer