# Generated by Django 3.2.4 on 2021-06-18 23:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HotelIFBA', '0003_rename_emai_empresa_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='endereço',
            new_name='endereco',
        ),
    ]
