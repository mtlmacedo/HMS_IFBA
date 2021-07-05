from django.db.models import fields
from rest_framework import serializers
from hmsifba.models import *
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
        fields = ['id', 'nomeCliente', 'email', 'nacionalidade', 'data_nascimento', 'endereco', 'telefone', 'numero_id', 'data_exp']

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
        fields = ['id', 'tipo', 'preco', 'epoca_ano' ]

class DadosPagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DadosPagamento
        fields = ['id', 'titular', 'agencia', 'conta', 'digito']

class EstatisticaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estatistica
        fields = ['id','trimestre','taxaOcupacaoQuartos','taxaQuartosVendidos','faturamentoDoTrimestre','faturamentoAnual','ano','clientePremium']

class RegistrationSerializer(serializers.ModelSerializer):
    email =  models.EmailField(max_length=256)
    username = models.CharField(max_length=100)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2']
        extra_kwargs = {
                'password': {'write_only': True},
        }	


    def	save(self):        
        
        usuario = User(
                    email=self.validated_data['email'],
                    
                )
        email = self.validated_data['email']
        username = self.validated_data['username']
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        if not email:
            raise serializers.ValidationError({'email': 'Invalid Email'})
        if not username:
            raise serializers.ValidationError({'username': 'Invalid Username'})
        usuario.set_password(password)
        usuario.save()
        return usuario

