from django.db.models import fields
from rest_framework import serializers
from HotelIFBA.models import *
from django.contrib.auth.models import User, Group

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = User
        fields = ['username', 'password']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ['id', 'nomeEmpresa', 'proprietario', 'endereco', 'telefone', 'categoria', 'email']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nomeCliente', 'nacionalidade', 'data_nascimento', 'endereco', 'telefone', 'numero_id', 'data_exp', 'email']

class ColaboradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colaborador
        fields = ['id', 'nomeCompleto', 'cpf', 'cargo', 'admissao', 'jornadaDiaria', 'login', 'senha']

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ['id', 'dataEntrada', 'dataSaida', 'quarto', 'qtd_pessoas', 'servico', 'cliente']

class EstadiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estadia
        fields = ['id', 'numero_cartao', 'cliente', 'quarto', 'dataEntrada', 'dataSaida', 'dadosPagamento', 'qtd_pessoas', 'qtd_quartos', 'reserva', 'mundanca_quarto']

class QuartoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quarto
        fields = ['id', 'numeroQuarto', 'andar', 'categoria', 'interfoneNumero', 'capacidade', 'disponibilidade']

class TipoServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoServico
        fields = ['id', 'tipo', 'preco']

class EstatisticaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estatistica
        fields = ['id','trimestre','taxaOcupacaoQuartos','taxaQuartosVendidos','faturamentoDoTrimestre','faturamentoAnual','ano','clientePremium']