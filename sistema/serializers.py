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
        fields = ('id', 'dataCadastro', 'bloco', 'apartamento', 'proprietario')
        read_only_fields = ('id',)


class CategoriaDeProblemaSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = CategoriaDeProblema
        fields = ('id', 'dataCadastro', 'nomeCategoria')
        read_only_fields = ('id',)



class ChamadoSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Chamado
        fields = '__all__'
        read_only_fields = ('id',)


