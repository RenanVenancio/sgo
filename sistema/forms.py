# coding=utf-8
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms
from .models import *

class UsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'


class UsuarioEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email' , 'is_staff']

class UsuarioPasswordChangeForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['password1', 'password2']


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

'''
class SubcategoriaDeProblemaForm(forms.ModelForm):
    class Meta:
        model = SubcategoriaDeProblema
        fields = ['nomeSubcategoria', 'categoria']


class ProblemaForm(forms.ModelForm):
    class Meta:
        model = Problema
        fields = ['subcategoria', 'nomeProblema', 'prioridade']

'''


class ChamadoForm(forms.ModelForm):
    class Meta:
        model = Chamado
        fields = '__all__'














