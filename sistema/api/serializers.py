from rest_framework import serializers
from sistema.models import *




class ApartamentoSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    bloco = serializers.StringRelatedField(many=False, read_only=True)
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Apartamento
        fields = ('id', 'apartamento', 'proprietario', 'bloco', 'inicioGarantia')
        read_only_fields = ('id', 'inicioGarantia')


class BlocoSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    #apartamento_set = ApartamentoSerializer(many=True, read_only=True)
    empreendimento = serializers.StringRelatedField(many=False, read_only=True)

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Bloco
        fields = ('empreendimento', 'id', 'bloco',)
        read_only_fields = ('id',)

class EmpreendimentoSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    #bloco_set = BlocoSerializer(many=True, read_only=True)
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Empreendimento
        fields = ('id', 'nomeEmpreendimento',)
        read_only_fields = ('id',)




class NestedEmpreendimentoSerialize(serializers.ModelSerializer):
    class Meta:
        model = Empreendimento
        fields = ['id', 'nomeEmpreendimento']



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
        fields = ['id', 'apartamento', 'proprietario', 'inicioGarantia' , 'bloco']



class CategoriaDeProblemaSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = CategoriaDeProblema
        fields = ('id', 'dataCadastro', 'nomeCategoria')
        read_only_fields = ('id',)




class AreaComumSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = AreaComum
        fields = ('id', 'nomeArea')
        read_only_fields = ('id',)



class EventoChamadoSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventosChamado
        fields = ['descricaoEvento']


class ChamadoCreateUpdateSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    ultimo_evento = serializers.SerializerMethodField()
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Chamado
        fields = ['id', 'dataCadastro', 'statusChamado', 'protocolo', 'ultimo_evento', 'categoriaProblema', 'usuario', 'envolveAreaComum', 'areaComum', 'apartamento', 'descricao', 'img', 'novosEventos', 'feedbackUsuario']
        read_only_fields = ('id', 'dataCadastro', 'protocolo', 'usuario', 'ultimo_evento', 'statusChamado')

    def get_ultimo_evento(self, obj): #Filtra e traz o ultimo evento
        evento = EventosChamado.objects.filter(chamado=obj.pk).first()
        return str(evento)


class ChamadoListSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    ultimo_evento = serializers.SerializerMethodField()
    categoriaProblema = serializers.StringRelatedField(many=False, read_only=True)
    areaComum = serializers.StringRelatedField(many=False, read_only=True)
    apartamento = serializers.StringRelatedField(many=False, read_only=True)

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Chamado
        fields = ['id', 'dataCadastro', 'protocolo', 'statusChamado', 'ultimo_evento', 'categoriaProblema', 'usuario', 'envolveAreaComum', 'areaComum', 'apartamento', 'descricao', 'img', 'novosEventos', 'feedbackUsuario']
        read_only_fields = ('id', 'dataCadastro', 'protocolo', 'usuario', 'statusChamado')


    def get_ultimo_evento(self, obj): #Filtra e traz o ultimo evento
        evento = EventosChamado.objects.filter(chamado=obj.pk).first()
        return str(evento)