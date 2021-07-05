# Generated by Django 3.2.4 on 2021-07-05 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeCliente', models.CharField(help_text='Nome do Cliente', max_length=100, null=True)),
                ('nacionalidade', models.CharField(help_text='Nacionalidade', max_length=50)),
                ('data_nascimento', models.DateField(help_text='Data de Nascimento')),
                ('endereco', models.CharField(blank=True, help_text='Endereço', max_length=200, null=True)),
                ('telefone', models.CharField(help_text='Telefone', max_length=11, null=True)),
                ('numero_id', models.IntegerField(help_text='Número de Identificação')),
                ('data_exp', models.DateField(help_text='Data de Expedição')),
                ('email', models.EmailField(help_text='E-mail da Empresa', max_length=256, null=True)),
                ('senha', models.CharField(help_text='Senha do Cliente', max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='DadosPagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titular', models.CharField(help_text='Titular do Cartão', max_length=50)),
                ('numeroCartao', models.CharField(help_text='Número do Cartão', max_length=15)),
                ('agencia', models.CharField(help_text='Agência do Cartão', max_length=6)),
                ('conta', models.CharField(help_text='Conta', max_length=6)),
                ('digito', models.IntegerField(help_text='Digito do Cartão')),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeEmpresa', models.CharField(help_text='Nome da Empresa', max_length=100, null=True)),
                ('proprietario', models.CharField(help_text='Proprietário', max_length=50, null=True)),
                ('endereco', models.CharField(help_text='Endereço', max_length=200, null=True)),
                ('telefone', models.CharField(help_text='Telefone', max_length=11, null=True)),
                ('categoria', models.CharField(help_text='Categoria', max_length=100, null=True)),
                ('email', models.EmailField(help_text='E-mail da Empresa', max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Estatistica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semestre', models.CharField(help_text='Período correspondente ao cálculo', max_length=256)),
                ('clienteId', models.CharField(help_text='Id do cliente', max_length=256)),
                ('custoTotalCliente', models.FloatField(help_text='Custo total de um determinado cliente')),
                ('taxaQuartosVendidos', models.FloatField(help_text='Número de quartos vendidos em relação ao número total de quartos')),
                ('faturamentoSemestre', models.FloatField(help_text='Total do faturamento referente ao semestre')),
                ('faturamentoAnual', models.FloatField(help_text='Faturamento do ano')),
                ('clientePremium', models.CharField(help_text='Cliente com maior gasto', max_length=256)),
                ('ano', models.CharField(help_text='Ano', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Quarto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroQuarto', models.IntegerField(help_text='Número do Quarto')),
                ('andar', models.IntegerField(help_text='Andar do Quarto')),
                ('categoria', models.CharField(max_length=50)),
                ('interfoneNumero', models.IntegerField(blank=True, help_text='Número do Interfone', null=True)),
                ('capacidade', models.IntegerField(help_text='Capacidade do Quarto', null=True)),
                ('disponibilidade', models.BooleanField(default=True, help_text='Quarto Disponível')),
            ],
        ),
        migrations.CreateModel(
            name='TipoServico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preco', models.DecimalField(decimal_places=2, help_text='Preço Diário', max_digits=10)),
                ('tipo', models.CharField(max_length=256)),
                ('qtd_pessoas', models.IntegerField(default=1, help_text='Quantidade de Pessoas')),
                ('epoca_ano', models.CharField(choices=[('Reveillón', 'Reveillón'), ('Carnaval', 'Carnaval'), ('Feriado', 'Feriado'), ('São João', 'São João'), ('Natal', 'Natal'), ('Dia Útil', 'Dia Útil')], help_text='Época do Ano', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataEntrada', models.DateTimeField(help_text='Data de Entrada da Reserva')),
                ('dataSaida', models.DateTimeField(help_text='Data de Saída da Reserva')),
                ('qtd_pessoas', models.IntegerField(null=True)),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='HotelIFBAReservaCliente', to='hmsifba.cliente')),
                ('quarto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='HotelIFBAReservaQuarto', to='hmsifba.quarto')),
                ('servico', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='HotelIFBAReservaServico', to='hmsifba.tiposervico')),
            ],
        ),
        migrations.CreateModel(
            name='Estadia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_cartao', models.CharField(help_text='Cartão de acesso', max_length=15)),
                ('dataEntrada', models.DateTimeField(help_text='Data de Entrada da Estadia')),
                ('dataSaida', models.DateTimeField(help_text='Data de Saída da Estadia')),
                ('qtd_pessoas', models.IntegerField(help_text='Quantidade de Pessoas')),
                ('qtd_quartos', models.IntegerField(help_text='Quantidade de Quartos')),
                ('mundanca_quarto', models.BooleanField(default=False, help_text='Solicitação de Mudança de Quarto')),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cliente', to='hmsifba.cliente')),
                ('dadosPagamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dadosPagamento', to='hmsifba.dadospagamento')),
                ('quarto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quarto', to='hmsifba.quarto')),
                ('reserva', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reserva', to='hmsifba.reserva')),
                ('servico', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='servico', to='hmsifba.tiposervico')),
            ],
        ),
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeCompleto', models.CharField(help_text='Nome Completo', max_length=200)),
                ('login', models.CharField(help_text='Login de acesso', max_length=200, null=True)),
                ('senha', models.CharField(help_text='Senha de acesso', max_length=20, null=True)),
                ('cpf', models.CharField(help_text='CPF do Colaborador', max_length=11)),
                ('cargo', models.CharField(choices=[('R', 'Recepcionista'), ('G', 'Gerente')], max_length=100)),
                ('admissao', models.DateTimeField(help_text='Data de Admissão', null=True)),
                ('jornadaDiaria', models.IntegerField(help_text='Jornada Diária')),
                ('empresa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='empresaPertencente', to='hmsifba.empresa')),
            ],
        ),
    ]
