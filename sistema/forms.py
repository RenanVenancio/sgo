# coding=utf-8
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms
from .models import *

class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuarios
        #fields = '__all__'
        exclude = ['password', 'last_login', 'is_active', 'date_joined']


class UsuarioEditForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        exclude = ['password', 'last_login', 'is_active', 'date_joined']

class UsuarioPasswordChangeForm(UserCreationForm):
    class Meta:
        model = Usuarios
        fields = ['password1', 'password2']


class EmpreendimentoForm(forms.ModelForm):
    class Meta:
        model = Empreendimento
        fields = ['nomeEmpreendimento']


class AreaComumForm(forms.ModelForm):
    class Meta:
        model = AreaComum
        fields = ['nomeArea', ]


class BlocoForm(forms.ModelForm):
    class Meta:
        model = Bloco
        fields = ['empreendimento', 'bloco']


class ApartamentoForm(forms.ModelForm):
    class Meta:
        model = Apartamento
        fields = ['bloco', 'apartamento', 'dono']


class CategoriaDeProblemaForm(forms.ModelForm):
    class Meta:
        model = CategoriaDeProblema
        fields = ['nomeCategoria']


class ChamadoForm(forms.ModelForm):
    class Meta:
        model = Chamado
        fields = '__all__'
        #exclude = ['protocolo']














