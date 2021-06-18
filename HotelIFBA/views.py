from rest_framework import viewsets
from HotelIFBA.models import Empresa
from HotelIFBA.serializer import EmpresaSerializer

class EmpresasViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
