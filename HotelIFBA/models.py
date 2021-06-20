from django.db import models
from django.conf import settings

class Endereco(models.Model):
    rua = models.CharField(max_length=200, null=False, blank=False)
    numero = models.IntegerField(null=False, blank=False)
    complemento = models.CharField(max_length=200, null=False, blank=False)
    bairro = models.CharField(max_length=50, null=False, blank=False)
    cidade = models.CharField(max_length=100, null=False, blank=False)
    pais = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.rua

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nomeCliente = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=100)
    dtNascimento = models.DateField()
    endereco = models.OneToOneField(Endereco, on_delete=models.SET_NULL, null=True)
    telefone = models.CharField(max_length=100)
    idNumero = models.CharField(max_length=100)
    idData = models.DateField()
    email = models.EmailField(null=False)
    senha = models.CharField(max_length=25, null=False)    
    def __str__(self):
        return self.nomeCliente


class Colaborador(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nomeCompleto = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=9)
    ctps = models.CharField(max_length=10)
    cargo = models.CharField(max_length=100)
    admissao = models.DateTimeField()
    jornadaDiaria = models.IntegerField()
    endereco = models.CharField(max_length=200)

    def __str__(self):
        return self.nomeCompleto


class Empresa(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nomeEmpresa = models.CharField(max_length=100)
    proprietario = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=14)
    endereco = models.OneToOneField(Endereco, on_delete=models.SET_NULL, null=True)
    telefone = models.CharField(max_length=11, null="True")
    categoria = models.CharField(max_length=100, null="True")
    email = models.EmailField(null=False)
    
    def __str__(self):
        return self.nomeEmpresa

        
class Reserva(models.Model): 
    id = models.AutoField(primary_key=True)
    dataEntrada = models.DateTimeField()
    dataSaida = models.DateTimeField()
    tipoQuarto = models.CharField(max_length=50) # Suíte, p/ uma pessoa, p/ duas pessoas

    def __str__(self):
        return self.dataEntrada

class Estadia(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quarto = models.ForeignKey("Quarto", on_delete=models.CASCADE, related_name='quarto')
    dataEntrada = models.DateTimeField()
    dataSaida = models.DateTimeField()
    #dados = models.ForeignKey("DadosPagamento", on_delete=models.CASCADE, related_name='dadosPagamento')
    def __str__(self):
        return self.id

class DadosPagamento(models.Model):
    id = models.AutoField(primary_key=True)
    titular = models.CharField(max_length=50)
    numeroCartao = models.CharField(max_length=15)
    agencia = models.CharField(max_length=6)
    conta = models.CharField(max_length=6)
    digito = models.IntegerField()
    chavepix = models.CharField(max_length=50)

    def __str__ (self):
        return self.id

class Quarto(models.Model):
    id = models.AutoField(primary_key=True)
    numeroQuarto = models.IntegerField()
    andar = models.IntegerField()
    categoria = models.CharField(max_length=50)
    interfoneNumero = models.IntegerField()

    def __str__ (self):
        return self.numeroQuarto