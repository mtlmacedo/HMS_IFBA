from django.db import models

class Empresa(models.Model):
    nomeEmpresa = models.CharField(max_length=100)
    proprietario = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=14)

    def __str__(self):
        return self.nomeEmpresa

class Colaborador(models.Model):
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
        
class Reserva(models.Model): 
    dataEntrada = models.DateTimeField()
    dataSaida = models.DateTimeField()
    tipoQuarto = models.CharField(max_length=50) # Suíte, p/ uma pessoa, p/ duas pessoas

    def __str__(self):
        return self.dataEntrada