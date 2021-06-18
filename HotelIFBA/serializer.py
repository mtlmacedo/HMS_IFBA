from django.db.models import fields
from rest_framework import serializers
from HotelIFBA.models import Cliente, Empresa

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ['nomeEmpresa', 'cnpj', 'proprietario', 'endereco', 'telefone', 'categoria', 'email']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nomeCliente', 'nacionalidade', 'dtNascimento', 'endereco', 'telefone', 'idNumero', 'idData', 'email', 'senha']