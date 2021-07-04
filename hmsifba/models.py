from django.db import models
from django.db.models.fields.related import ForeignKey


class Empresa(models.Model):
    nomeEmpresa = models.CharField(max_length=100, help_text='Nome da Empresa', blank=False, null=True)
    proprietario = models.CharField(max_length=50, help_text='Proprietário', blank=False, null=True)
    endereco = models.CharField(max_length=200, help_text='Endereço', blank=False, null=True)
    telefone = models.CharField(max_length=11, help_text='Telefone', null=True)
    categoria = models.CharField(max_length=100, help_text='Categoria', blank=False, null=True)
    email = models.EmailField(max_length=256, help_text='E-mail da Empresa', null=True, blank=False)
    
    def __str__(self):
        return self.nomeEmpresa

class Cliente(models.Model):
    nomeCliente = models.CharField(max_length=100, help_text='Nome do Cliente', blank=False, null=True)
    nacionalidade = models.CharField(max_length=50, help_text='Nacionalidade')
    data_nascimento = models.DateField(help_text='Data de Nascimento')
    endereco = models.CharField(max_length=200, help_text='Endereço', blank=True, null=True)
    telefone = models.CharField(max_length=11, help_text='Telefone', null=True)
    numero_id = models.IntegerField(help_text='Número de Identificação')
    data_exp = models.DateField(help_text='Data de Expedição')
    email = models.EmailField(max_length=256, help_text='E-mail da Empresa', null=True, blank=False)
    senha = models.CharField(max_length=25, help_text='Senha do Cliente')    

    def __str__(self):
        return self.nomeCliente


class Colaborador(models.Model):

    COLAB_CHOICES = (
        ("R", "Recepcionista"),
        ("G", "Gerente"),
    )

    nomeCompleto = models.CharField(max_length=200, help_text='Nome Completo', blank=False, null=False)
    login = models.CharField(max_length=200, help_text='Login de acesso', blank=False, null=True)
    senha = models.CharField(max_length=20, help_text='Senha de acesso', blank=False, null=True)
    cpf = models.CharField(max_length=11, help_text='CPF do Colaborador', blank=False, null=False)
    cargo = models.CharField(max_length=100, choices=COLAB_CHOICES, blank=False, null=False)
    admissao = models.DateTimeField(help_text='Data de Admissão', blank=False, null=True)
    jornadaDiaria = models.IntegerField(help_text='Jornada Diária')
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="empresaPertencente", null=True)

    def __str__(self):
        return self.nomeCompleto

class TipoServico(models.Model):
    PERIODO_CHOICES = (
        ("Reveillón", "Reveillón"),
        ("Carnaval", "Carnaval"),
        ("Feriado","Feriado"),
        ("São João", "São João"),
        ("Natal", "Natal"),
        ("Dia Útil","Dia Útil")
    )

    preco = models.DecimalField(max_digits=10, decimal_places=2, help_text='Preço Diário')
    tipo = models.CharField(max_length=256, blank=False, null=False)
    qtd_pessoas = models.IntegerField(help_text='Quantidade de Pessoas', default=1, blank=False, null=False)
    epoca_ano = models.CharField(max_length=50, choices=PERIODO_CHOICES, help_text='Época do Ano', blank=False, null=False)

    def __str__(self):
        return self.tipo

class Quarto(models.Model):
    numeroQuarto = models.IntegerField(help_text='Número do Quarto')
    andar = models.IntegerField(help_text='Andar do Quarto')
    categoria = models.CharField(max_length=50)
    interfoneNumero = models.IntegerField(help_text='Número do Interfone', blank=True, null=True)
    capacidade = models.IntegerField(help_text='Capacidade do Quarto', blank=False, null=True)
    disponibilidade = models.BooleanField(default=True, help_text='Quarto Disponível')

    def __str__ (self):
        return self.categoria

class DadosPagamento(models.Model):
    titular = models.CharField(max_length=50, help_text='Titular do Cartão')
    numeroCartao = models.CharField(max_length=15, help_text='Número do Cartão')
    agencia = models.CharField(max_length=6, help_text='Agência do Cartão')
    conta = models.CharField(max_length=6, help_text='Conta')
    digito = models.IntegerField(help_text='Digito do Cartão')

    def __str__ (self):
        return self.titular
        
class Reserva(models.Model):
    dataEntrada = models.DateTimeField(help_text='Data de Entrada da Reserva')
    dataSaida = models.DateTimeField(help_text='Data de Saída da Reserva')
    qtd_pessoas = models.IntegerField(null=True) 
    quarto = models.ForeignKey(Quarto, on_delete=models.CASCADE, related_name="HotelIFBAReservaQuarto", blank=False, null=True)
    servico = models.ForeignKey(TipoServico, on_delete=models.CASCADE, related_name="HotelIFBAReservaServico", blank=False, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="HotelIFBAReservaCliente", blank=False, null=True)

    #def __str__(self):
     #  return self.dataEntrada

class Estadia(models.Model):
    numero_cartao = models.CharField(max_length=15, help_text="Cartão de acesso")
    dataEntrada = models.DateTimeField(help_text='Data de Entrada da Estadia')
    dataSaida = models.DateTimeField(help_text='Data de Saída da Estadia')
    qtd_pessoas = models.IntegerField(help_text='Quantidade de Pessoas')
    qtd_quartos = models.IntegerField(help_text='Quantidade de Quartos')
    mundanca_quarto = models.BooleanField(default=False, help_text='Solicitação de Mudança de Quarto')
    reserva = ForeignKey(Reserva, on_delete=models.CASCADE, related_name="reserva", blank=True, null=True)
    quarto = models.ForeignKey(Quarto, on_delete=models.CASCADE, related_name="quarto", blank=False, null=True)
    cliente = models.ForeignKey("Cliente", on_delete=models.CASCADE, related_name='cliente', null=True)
    
    servico = models.ForeignKey(TipoServico, on_delete=models.CASCADE, related_name="servico", blank=False, null=True)
    dadosPagamento = models.ForeignKey(DadosPagamento, on_delete=models.CASCADE, related_name='dadosPagamento', blank=False, null=False)
    #def __str__(self):
     #   return self.dataEntrada

class Estatistica(models.Model):
    semestre = models.CharField(help_text='Período correspondente ao cálculo', max_length=256)
    clienteId = models.CharField(help_text='Id do cliente', max_length=256)
    custoTotalCliente = models.FloatField(help_text='Custo total de um determinado cliente')
    taxaQuartosVendidos = models.FloatField(help_text='Número de quartos vendidos em relação ao número total de quartos')
    faturamentoSemestre = models.FloatField(help_text='Total do faturamento referente ao semestre')
    faturamentoAnual = models.FloatField(help_text='Faturamento do ano')
    clientePremium = models.CharField(help_text='Cliente com maior gasto', max_length=256)
    ano = models.CharField(help_text='Ano', max_length=256)   
    
    def __str__(self):
        return self.semestre