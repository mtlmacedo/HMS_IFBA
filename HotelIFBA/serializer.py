from rest_framework import serializers
from HotelIFBA.models import Empresa

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ['nomeEmpresa', 'cnpj', 'proprietario']