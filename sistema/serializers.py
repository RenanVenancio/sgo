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




class NestedEmpreendimentoSerialize(serializers.ModelSerializer):
    class Meta:
        model = Empreendimento
        fields = ['nomeEmpreendimento', 'id']



class NestedBlocoSerialize(serializers.ModelSerializer):
    empreendimento = NestedEmpreendimentoSerialize(many=False, read_only=True)
    class Meta:
        model = Bloco
        fields = ['id', 'bloco', 'empreendimento']



class ApartamentoProprietarioSerializer(serializers.ModelSerializer): #Serializa os apartamentos pelo id do proprietario
    """Serializer to map the Model instance into JSON format."""
    bloco = NestedBlocoSerialize(many=False, read_only=True)
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Apartamento
        fields = ['id', 'apartamento', 'proprietario', 'bloco']





'''
class ApartamentoProprietarioSerializer(serializers.ModelSerializer): #Serializa os apartamentos pelo id do proprietario
    """Serializer to map the Model instance into JSON format."""
    bloco = serializers.StringRelatedField(many=False)
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Apartamento
        fields = '__all__'
'''

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
        fields = ['categoriaProblema', 'usuario', 'envolveAreaComum', 'areaComum', 'apartamento', 'descricao', 'img']
        read_only_fields = ('id',)


