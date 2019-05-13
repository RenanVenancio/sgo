from rest_framework import serializers
from .models import *

class EmpreendimentoSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Empreendimento
        fields = ('id', 'dataCadastro', 'nomeEmpreendimento')
        read_only_fields = ('id',)


class BlocoSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Bloco
        fields = ('id', 'dataCadastro', 'bloco', 'empreendimento')
        read_only_fields = ('id',)


class ApartamentoSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Apartamento
        fields = ('id', 'dataCadastro', 'bloco', 'apartamento')
        read_only_fields = ('id',)


class CategoriaDeProblemaSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = CategoriaDeProblema
        fields = ('id', 'dataCadastro', 'nomeCategoria')
        read_only_fields = ('id',)


class SubcategoriaDeProblemaSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = SubcategoriaDeProblema
        fields = ('id', 'dataCadastro', 'nomeSubcategoria', 'categoria')
        read_only_fields = ('id',)


class ProblemaSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Problema
        fields = ('id', 'dataCadastro', 'subcategoria', 'nomeProblema', 'prioridade')
        read_only_fields = ('id',)


class ChamadoSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Chamado
        fields = ('id', 'dataCadastro', 'dataInteracao', 'protocolo', 'statusChamado', 'nome',
         'cpf','telefoneFixo', 'telefoneCelular', 'email', 'apartamento', 'aptEnvolvidos',
         'problema', 'descricao', 'img1', 'img2', 'img3')
        read_only_fields = ('id',)