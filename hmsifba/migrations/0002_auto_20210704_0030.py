# Generated by Django 3.2.4 on 2021-07-04 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hmsifba', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estatistica',
            old_name='trimestre',
            new_name='semestre',
        ),
        migrations.RemoveField(
            model_name='estatistica',
            name='faturamentoDoTrimestre',
        ),
        migrations.RemoveField(
            model_name='estatistica',
            name='taxaOcupacaoQuartos',
        ),
        migrations.AddField(
            model_name='estatistica',
            name='faturamentoSemestre',
            field=models.FloatField(default=10, help_text='Total do faturamento referente ao semestre'),
            preserve_default=False,
        ),
    ]