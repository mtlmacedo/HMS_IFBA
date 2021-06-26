from django.db import models
from django.conf import settings
from django.utils import timezone
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Usuario(models.Model):
	username = models.CharField(max_length=20, primary_key=True, unique=True, blank=False, null=False)
	cpf = models.CharField(max_length=11)
	telefone = models.CharField(max_length=20)

	REQUIRED_FIELDS = ['username', 'cpf', 'telefone']

	def __str__(self):
		return self.username

class Endereco(models.Model):
    rua = models.CharField(max_length=200)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=200)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)

    def __str__(self):
        return self.rua

class Cliente(models.Model):
    nomeCliente = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=100)
    dtNascimento = models.DateField()
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=100)
    idNumero = models.CharField(max_length=100)
    idData = models.DateField()
    email = models.EmailField(null=True)
    senha = models.CharField(max_length=25)    

    def __str__(self):
        return self.nomeCliente


class Colaborador(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    nomeCompleto = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=9)
    ctps = models.CharField(max_length=10)
    cargo = models.CharField(max_length=100)
    admissao = models.DateTimeField()
    jornadaDiaria = models.IntegerField()
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)

    def __str__(self):
        return self.nomeCompleto


class Empresa(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    nomeEmpresa = models.CharField(max_length=100)
    proprietario = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=14)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=11, null="True")
    categoria = models.CharField(max_length=100, null="True")
    email = models.EmailField(null=True)
    
    def __str__(self):
        return self.nomeEmpresa

        
class Reserva(models.Model): 
    dataEntrada = models.DateTimeField()
    dataSaida = models.DateTimeField()
    tipoQuarto = models.CharField(max_length=50) # Suíte Presidencial, Comum
    qtdPessoas = models.IntegerField(null=True) 

    def __str__(self):
        return self.tipoQuarto

class DadosPagamento(models.Model):
    titular = models.CharField(max_length=50)
    numeroCartao = models.CharField(max_length=15)
    agencia = models.CharField(max_length=6)
    conta = models.CharField(max_length=6)
    digito = models.IntegerField()
    chavepix = models.CharField(max_length=50)

    def __str__ (self):
        return self.titular

class Estadia(models.Model):
    cliente = models.ForeignKey("Cliente", on_delete=models.CASCADE, related_name='cliente', null=True)
    quarto = models.ForeignKey("Quarto", on_delete=models.Aggregate, related_name='quarto', null=True)
    dataEntrada = models.DateTimeField()
    dataSaida = models.DateTimeField()
    dadosPagamento = models.ForeignKey(DadosPagamento, on_delete=models.CASCADE)

    def __str__(self):
        return self.cliente


class Quarto(models.Model):
    QUARTO_CHOICES = ('Solteiro', 
                    'Duplo Solteiro', 
                    'Casal', 
                    'Dormitório', 
                    'Suíte Master'),
    
    numeroQuarto = models.IntegerField()
    andar = models.IntegerField()
    categoria = models.CharField(max_length=50)
    interfoneNumero = models.IntegerField()
    capacidade = models.IntegerField()

    def __str__ (self):
        return self.categoria