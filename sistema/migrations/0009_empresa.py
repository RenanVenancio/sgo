# Generated by Django 2.0.4 on 2019-06-13 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0008_auto_20190612_1936'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(blank=True, max_length=20, unique=True, verbose_name='Cnpj')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome fantasia')),
                ('endereco', models.CharField(max_length=150, verbose_name='Endereço')),
                ('bairro', models.CharField(max_length=50, verbose_name='Bairro')),
                ('cidade', models.CharField(max_length=50, verbose_name='Cidade')),
                ('estado', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], default='PB', max_length=2, verbose_name='Estado')),
                ('telefone1', models.CharField(blank=True, max_length=15, null=True)),
                ('telefone2', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(blank=True, max_length=255)),
                ('sobre', models.TextField(verbose_name='Sobre a Empresa')),
                ('dataCadastro', models.DateField(auto_now_add=True, verbose_name='Data de cadastro')),
            ],
        ),
    ]
