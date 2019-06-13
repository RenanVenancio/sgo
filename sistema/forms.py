# coding=utf-8
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms
from .models import *
from django.core.exceptions import ValidationError
class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'


class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuarios
        #fields = '__all__'
        exclude = ['password', 'last_login', 'is_active', 'date_joined']


class UsuarioEditForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        exclude = ['password', 'last_login', 'is_active', 'date_joined', 'apartamentos']


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
        fields = ['bloco', 'apartamento', 'proprietario', 'inicioGarantia']

    def clean_inicioGarantia(self):
        cleaned_data = super(ApartamentoForm, self).clean()
        inicioGarantia = cleaned_data.get("inicioGarantia")
        proprietario = cleaned_data.get("proprietario")

        if(inicioGarantia == None) and (not (proprietario == None)):
            raise ValidationError("Selecione a data de início da garantia do apartamento.")
        return inicioGarantia

class CategoriaDeProblemaForm(forms.ModelForm):
    class Meta:
        model = CategoriaDeProblema
        fields = ['nomeCategoria']


class ChamadoForm(forms.ModelForm):
    class Meta:
        model = Chamado
        fields = '__all__'
        #exclude = ['protocolo']

    def clean_envolveAreaComum(self):
        cleaned_data = super(ChamadoForm, self).clean()
        envolveAreaComum = cleaned_data.get("envolveAreaComum")
        areaComum = cleaned_data.get("areaComum")

        if(envolveAreaComum == True) and (areaComum == None):
            raise ValidationError("Selecione uma área comum.")
        return envolveAreaComum


class EventoChamadoForm(forms.ModelForm):
    class Meta:
        model = EventosChamado
        fields = ['descricaoEvento']
        #exclude = ['protocolo']












