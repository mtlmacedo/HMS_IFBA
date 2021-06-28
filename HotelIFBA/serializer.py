from django.db.models import fields
from rest_framework import serializers
from HotelIFBA.models import *

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ['nomeEmpresa', 'cnpj', 'proprietario', 'endereco', 'telefone', 'categoria', 'email']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nomeCliente', 'nacionalidade', 'dtNascimento', 'endereco', 'telefone', 'idNumero', 'idData', 'email', 'senha']

class ColaboradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colaborador
        fields = ['id', 'nomeCompleto', 'cpf', 'rg', 'ctps', 'cargo', 'admissao', 'jornadaDiaria', 'endereco']

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ['id', 'dataEntrada', 'dataSaida', 'tipoQuarto', 'qtdPessoas']

class EstadiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estadia
        fields = ['id', 'cliente', 'quarto', 'dataEntrada', 'dataSaida', 'dadosPagamento']

class QuartoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quarto
        fields = ['numeroQuarto', 'andar', 'categoria', 'interfoneNumero', 'capacidade']