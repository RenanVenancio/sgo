# coding=utf-8

from datetime import datetime, timezone
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from random import randint
from django.urls import reverse
# Imports para funcionamento do DRFToken auth
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.contrib.auth.models import User

ENUM_ESTADOS = (
	('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'),
	('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'),
	('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'),
	('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'),
	('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'),
	('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'),
	('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'),
	('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'),
	('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'),
	('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')
)


ENUM_STATUS = (
    ('Em analise', 'Em analise'),
    ('Em andamento', 'Em andamento'),
    ('Finalizado', 'Finalizado'),
)


class Empresa(models.Model):
    cnpj = models.CharField('Cnpj', max_length=20, unique=True, blank=True)
    nome = models.CharField('Nome fantasia', max_length=100, blank=False, null=False)
    endereco = models.CharField('Endereço', max_length=150)
    bairro = models.CharField('Bairro', max_length=50)
    cidade = models.CharField('Cidade', max_length=50)
    estado = models.CharField('Estado', choices=ENUM_ESTADOS, max_length=2, default='PB')
    telefone1 = models.CharField(max_length=15, blank=True, null=True)
    telefone2 = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True)
    sobre = models.TextField('Sobre a Empresa')
    dataCadastro = models.DateField('Data de cadastro', auto_now_add=True)


class Empreendimento(models.Model):
    dataCadastro = models.DateTimeField('Data de cadastro', auto_now_add=True)
    nomeEmpreendimento = models.CharField('Nome', max_length=150, unique=True)

    def get_absolute_url(self):
        return reverse('sistema:editarempreendimento', kwargs={'pk': self.pk})

    def __str__(self):
        return self.nomeEmpreendimento

    class Meta:
        ordering = ['-pk']
        verbose_name = 'Empreendimento'
        verbose_name_plural = 'Empreendimentos'


class AreaComum(models.Model):
    dataCadastro = models.DateTimeField('Data de cadastro', auto_now_add=True)
    nomeArea = models.CharField('Nome', max_length=150, unique=True)

    def get_absolute_url(self):
        return reverse('sistema:editarareacomum', kwargs={'pk': self.pk})

    def __str__(self):
        return self.nomeArea

    class Meta:
        ordering = ['-pk']
        verbose_name = 'Area Comum'
        verbose_name_plural = 'Áreas Comuns'


class Bloco(models.Model):
    dataCadastro = models.DateTimeField('Data de cadastro', auto_now_add=True)
    empreendimento = models.ForeignKey('sistema.Empreendimento', on_delete=models.PROTECT,
                                       verbose_name='Empreendimento')
    bloco = models.CharField('Bloco', max_length=15)

    def get_absolute_url(self):
        return reverse('sistema:editarbloco', kwargs={'pk': self.pk})

    def __str__(self):
        return self.empreendimento.nomeEmpreendimento + " - Bloco: " + self.bloco

    class Meta:
        ordering = ['-pk']
        verbose_name = 'Bloco'
        verbose_name_plural = 'Blocos'


class Apartamento(models.Model):
    dataCadastro = models.DateTimeField('Data de cadastro', auto_now_add=True)
    bloco = models.ForeignKey('sistema.Bloco', on_delete=models.PROTECT, verbose_name='Bloco')
    apartamento = models.CharField('Apartamento', max_length=6)
    proprietario = models.ForeignKey('sistema.Usuarios', on_delete=models.PROTECT, blank=True, null=True) #Define o proprietário do apto
    inicioGarantia = models.DateField('Inicio da Garantia', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('sistema:editarapartamento', kwargs={'pk': self.pk})

    def get_proprietario(self):
        return self.proprietario

    class Meta:
        ordering = ['-pk']
        verbose_name = 'Apartamentos'
        verbose_name_plural = 'Apartamentos'

    def __str__(self):
        return "Apto: " + self.apartamento + " - Bloco " + self.bloco.bloco + " - " + self.bloco.empreendimento.nomeEmpreendimento


class CategoriaDeProblema(models.Model):
    dataCadastro = models.DateTimeField('Data de cadastro', auto_now_add=True)
    nomeCategoria = models.CharField('Categoria', max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse('sistema:editarcategoriadeproblema', kwargs={'pk': self.pk})

    def __str__(self):
        return self.nomeCategoria

    class Meta:
        ordering = ['-pk']
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Chamado(models.Model):
    protocolo = models.CharField('Protocolo', max_length=30, unique=True, blank=True)
    prioridade = models.PositiveSmallIntegerField('Prioridade', validators=[MinValueValidator(1), MaxValueValidator(5)], default=1)
    statusChamado = models.CharField('Status do chamado', choices=ENUM_STATUS, max_length=20, default='Em analise')
    dataCadastro = models.DateField('Data de cadastro', auto_now_add=True)
    dataInteracao = models.DateTimeField('Data de interação', auto_now=True)
    categoriaProblema = models.ForeignKey('sistema.CategoriaDeProblema', on_delete=models.PROTECT,
                                          verbose_name='Categoria do problema')
    usuario=models.ForeignKey('sistema.Usuarios', on_delete=models.PROTECT, null=False)
    envolveAreaComum= models.BooleanField(verbose_name='Problema em área comum', default=False)
    areaComum=models.ForeignKey('sistema.AreaComum', on_delete=models.PROTECT, verbose_name='Selecione uma Área comum', blank=True, null=True)
    apartamento = models.ForeignKey('sistema.Apartamento', on_delete=models.PROTECT, blank=False, null=False)
    descricao = models.TextField('Descreva o problema')
    img = models.ImageField('Envie uma foto', upload_to='sistema/chamados', blank=True)
    novosEventos= models.BooleanField(verbose_name='Novos eventos disponíveis', default=False)
    feedbackUsuario = models.PositiveSmallIntegerField('Feedback dado pelo Usuário', validators=[MinValueValidator(0), MaxValueValidator(5)], default=0, blank=True, null=True)


    def get_absolute_url(self):
        return reverse('sistema:editarchamado', kwargs={'pk': self.pk})

    def __str__(self):
        return self.protocolo

    def save(self, *args, **kwargs):
        if(not self.protocolo):
            self.protocolo = datetime.today().strftime('%d%m%Y%H%M%S') + str(randint(1000, 2000))
            super(Chamado, self).save(*args, **kwargs)
        else:
            super(Chamado, self).save(*args, **kwargs)

        if(not EventosChamado.objects.filter(chamado=self.pk)):
            evento = EventosChamado()
            evento.descricaoEvento = 'Chamado iniciado'
            evento.chamado = Chamado.objects.get(pk=self.pk)
            evento.save()

    class Meta:
        ordering = ['-pk']
        verbose_name = 'Chamado'
        verbose_name_plural = 'Chamados'



class EventosChamado(models.Model):
    dataCadastro = models.DateField('Data de cadastro', auto_now_add=True)
    descricaoEvento = models.CharField('Evento', max_length=90)
    chamado=models.ForeignKey('sistema.Chamado', on_delete=models.CASCADE, null=False)

    def __str__(self):
        dataFormatada = datetime.strptime(str(self.dataCadastro), "%Y-%m-%d")
        return dataFormatada.strftime('%d/%m/%y') + '#$%' + self.descricaoEvento

    def save(self, *args, **kwargs):
        Chamado.objects.filter(id=self.chamado.pk).update(novosEventos=True)
        super(EventosChamado, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-pk']
        verbose_name = 'Evento de Chamado'
        verbose_name_plural = 'Eventos de Chamados'


#Extendendo user padão do django
class Usuarios(User):           #Sempre usar essa classe dentro do sistema
    cpf = models.CharField(max_length=20, blank=False, unique=True, null=False)
    telefone1 = models.CharField(max_length=15, blank=True, null=True)
    telefone2 = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return 'CPF: ' + self.cpf + ' - NOME: ' + self.get_full_name()
