# coding=utf-8

from datetime import datetime
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from random import randint
from django.urls import reverse
# Imports para funcionamento do DRFToken auth
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.dispatch import receiver

ENUM_STATUS = (
    ('Aberto', 'Aberto'),
    ('Em atendimento', 'Em atendimento'),
    ('Encerrado', 'Encerrado'),
)


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


class Bloco(models.Model):

    dataCadastro = models.DateTimeField('Data de cadastro', auto_now_add=True)
    empreendimento = models.ForeignKey('sistema.Empreendimento', on_delete=models.CASCADE, verbose_name='Empreendimento')
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
    bloco = models.ForeignKey('sistema.Bloco', on_delete=models.CASCADE, verbose_name='Bloco')
    apartamento = models.CharField('Apartamento', max_length=6)

    def get_absolute_url(self):
        return reverse('sistema:editarapartamento', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-pk']
        verbose_name = 'Apartamentos'
        verbose_name_plural = 'Apartamentos'

    def __str__(self):
        return "Ap: " + self.apartamento + " - " + self.bloco.bloco + " - " + self.bloco.empreendimento.nomeEmpreendimento


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


class SubcategoriaDeProblema(models.Model):

    dataCadastro = models.DateTimeField('Data de cadastro', auto_now_add=True)
    nomeSubcategoria = models.CharField('Subcategoria', max_length=100, unique=True)
    categoria = models.ForeignKey('sistema.CategoriaDeProblema', on_delete=models.CASCADE, verbose_name='Categoria')

    def get_absolute_url(self):
        return reverse('sistema:editarsubcategoriadeproblema', kwargs={'pk': self.pk})

    def __str__(self):
        return self.nomeSubcategoria

    class Meta:
        ordering = ['-pk']
        verbose_name = 'Subcategoria'
        verbose_name_plural = 'Subcategorias'


class Problema(models.Model):

    dataCadastro = models.DateTimeField('Data de cadastro', auto_now_add=True)
    subcategoria = models.ForeignKey('sistema.SubcategoriaDeProblema', on_delete=models.CASCADE, verbose_name='Subcategoria')
    nomeProblema = models.CharField('Problema', max_length=80, unique=True)
    prioridade = models.PositiveSmallIntegerField('Prioridade', validators=[MinValueValidator(1), MaxValueValidator(5)])

    def get_absolute_url(self):
        return reverse('sistema:editarproblema', kwargs={'pk': self.pk})

    def __str__(self):
        return self.nomeProblema

    class Meta:
        ordering = ['-pk']
        verbose_name = 'Problema'
        verbose_name_plural = 'Problemas'


class Chamado(models.Model):

    dataCadastro = models.DateField('Data de cadastro', auto_now_add=True)
    dataInteracao = models.DateTimeField('Data de interação', auto_now=True)
    protocolo = models.CharField('Protocolo', max_length=30, unique=True)
    statusChamado = models.CharField('Status do chamado', choices=ENUM_STATUS, max_length=20, default='Aberto')
    nome = models.CharField('Nome', max_length=150)
    cpf = models.CharField('Cpf', max_length=11)
    telefoneFixo = models.CharField('Telefone fixo', max_length=10, blank=True, null=True)
    telefoneCelular = models.CharField('Telefone celular', max_length=11)
    email = models.EmailField('E-mail', max_length=150)
    apartamento = models.ForeignKey('sistema.Apartamento', on_delete=models.CASCADE, verbose_name='Apartamento')
    aptEnvolvidos = models.BooleanField('Envolve outro apartamento?')
    problema = models.ForeignKey('sistema.Problema', on_delete=models.CASCADE, verbose_name='Problema')
    descricao = models.TextField('Descreva o problema')
    img1 = models.ImageField('Imagem 1', upload_to='sistema/chamados')
    img2 = models.ImageField('Imagem 2', upload_to='sistema/chamados')
    img3 = models.ImageField('Imagem 3', upload_to='sistema/chamados')

    def get_absolute_url(self):
        return reverse('sistema:editarchamado', kwargs={'pk': self.pk})

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        self.protocolo = datetime.today().strftime('%d%m%Y%H%M%S') + str(randint(1000, 2000))
        super(Chamado, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-pk']
        verbose_name = 'Chamado'
        verbose_name_plural = 'Chamados'




# This receiver handles token creation immediately a new user is created.
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)