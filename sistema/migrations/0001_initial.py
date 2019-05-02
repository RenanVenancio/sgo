# Generated by Django 2.0.4 on 2018-05-14 02:39

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataCadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data de cadastro')),
                ('apartamento', models.CharField(max_length=6, verbose_name='Apartamento')),
            ],
            options={
                'verbose_name': 'Apartamentos',
                'verbose_name_plural': 'Apartamentos',
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='Bloco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataCadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data de cadastro')),
                ('bloco', models.CharField(max_length=15, verbose_name='Bloco')),
            ],
            options={
                'verbose_name': 'Bloco',
                'verbose_name_plural': 'Blocos',
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='CategoriaDeProblema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataCadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data de cadastro')),
                ('nomeCategoria', models.CharField(max_length=100, unique=True, verbose_name='Categoria')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='Chamado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataCadastro', models.DateField(auto_now_add=True, verbose_name='Data de cadastro')),
                ('dataInteracao', models.DateTimeField(auto_now=True, verbose_name='Data de interação')),
                ('protocolo', models.CharField(max_length=30, unique=True, verbose_name='Protocolo')),
                ('statusChamado', models.CharField(choices=[('Aberto', 'Aberto'), ('Em atendimento', 'Em atendimento'), ('Encerrado', 'Encerrado')], default='Aberto', max_length=20, verbose_name='Status do chamado')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome')),
                ('cpf', models.PositiveIntegerField(verbose_name='Cpf')),
                ('telefoneFixo', models.PositiveIntegerField(blank=True, null=True, verbose_name='Telefone fixo')),
                ('telefoneCelular', models.PositiveIntegerField(verbose_name='Telefone celular')),
                ('email', models.EmailField(max_length=150, verbose_name='E-mail')),
                ('aptEnvolvidos', models.BooleanField(verbose_name='Envolve outro apartamento?')),
                ('descricao', models.TextField(verbose_name='Descreva o problema')),
                ('img1', models.ImageField(upload_to='sistema/chamados', verbose_name='Imagem 1')),
                ('img2', models.ImageField(upload_to='sistema/chamados', verbose_name='Imagem 2')),
                ('img3', models.ImageField(upload_to='sistema/chamados', verbose_name='Imagem 3')),
                ('apartamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.Apartamento', verbose_name='Apartamento')),
            ],
            options={
                'verbose_name': 'Chamado',
                'verbose_name_plural': 'Chamados',
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='Empreendimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataCadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data de cadastro')),
                ('nomeEmpreendimento', models.CharField(max_length=150, unique=True, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Empreendimento',
                'verbose_name_plural': 'Empreendimentos',
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='Problema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataCadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data de cadastro')),
                ('nomeProblema', models.CharField(max_length=80, unique=True, verbose_name='Problema')),
                ('prioridade', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Prioridade')),
            ],
            options={
                'verbose_name': 'Problema',
                'verbose_name_plural': 'Problemas',
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='SubcategoriaDeProblema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataCadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data de cadastro')),
                ('nomeSubcategoria', models.CharField(max_length=100, unique=True, verbose_name='Subcategoria')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.CategoriaDeProblema', verbose_name='Categoria')),
            ],
            options={
                'verbose_name': 'Subcategoria',
                'verbose_name_plural': 'Subcategorias',
                'ordering': ['-pk'],
            },
        ),
        migrations.AddField(
            model_name='problema',
            name='subcategoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.SubcategoriaDeProblema', verbose_name='Subcategoria'),
        ),
        migrations.AddField(
            model_name='chamado',
            name='problema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.Problema', verbose_name='Problema'),
        ),
        migrations.AddField(
            model_name='bloco',
            name='empreendimento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.Empreendimento', verbose_name='Empreendimento'),
        ),
        migrations.AddField(
            model_name='apartamento',
            name='bloco',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.Bloco', verbose_name='Bloco'),
        ),
    ]
