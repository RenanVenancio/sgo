# coding=utf-8

from django import forms
from .models import *


class EmpreendimentoForm(forms.ModelForm):
    class Meta:
        model = Empreendimento
        fields = ['nomeEmpreendimento']


class BlocoForm(forms.ModelForm):
    class Meta:
        model = Bloco
        fields = ['empreendimento', 'bloco']


class ApartamentoForm(forms.ModelForm):
    class Meta:
        model = Apartamento
        fields = ['bloco', 'apartamento']


class CategoriaDeProblemaForm(forms.ModelForm):
    class Meta:
        model = CategoriaDeProblema
        fields = ['nomeCategoria']


class SubcategoriaDeProblemaForm(forms.ModelForm):
    class Meta:
        model = SubcategoriaDeProblema
        fields = ['nomeSubcategoria', 'categoria']


class ProblemaForm(forms.ModelForm):
    class Meta:
        model = Problema
        fields = ['subcategoria', 'nomeProblema', 'prioridade']


class ChamadoForm(forms.ModelForm):
    class Meta:
        model = Chamado
        fields = [
            'statusChamado', 'nome', 'cpf', 'email',  'telefoneFixo', 'telefoneCelular', 'apartamento',
            'aptEnvolvidos', 'problema', 'img1', 'img2', 'img3', 'descricao'
        ]














