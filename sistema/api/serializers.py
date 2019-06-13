from rest_framework import serializers
from sistema.models import *
from datetime import datetime
from datetime import date

class EmpresaSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    #bloco_set = BlocoSerializer(many=True, read_only=True)
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Empresa
        fields = ('cnpj', 'nome', 'endereco', 'bairro', 'cidade', 'estado', 'telefone1', 'telefone2', 'email', 'sobre')


class ApartamentoSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    bloco = serializers.StringRelatedField(many=False, read_only=True)
    tempoPercorridoGarntia = serializers.SerializerMethodField()

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Apartamento
        fields = ('id', 'apartamento', 'proprietario', 'bloco', 'inicioGarantia', 'tempoPercorridoGarntia')
        read_only_fields = ('id', 'inicioGarantia')

    def get_tempoPercorridoGarntia(self, obj): #Filtra e traz o ultimo evento
        iniGatantia = obj.inicioGarantia
        iniGatantia = str(iniGatantia.strftime("%d-%m-%Y"))
        hoje = str(date.today().strftime("%d-%m-%Y"))

        date_format = "%d-%m-%Y"
        a = datetime.strptime(iniGatantia, date_format)
        b = datetime.strptime(hoje, date_format)
        anos = b.year - a.year
        meses = b.month - a.month
        meses = abs(meses)
        dias = b - a

        if (anos > 0) and (meses > 0):
            return 'Decorrido(s) ' + str(anos) + ' Ano(s) e ' + str(meses) + ' Mês(ses)'
        elif(anos == 0) and (dias.days > 0):
            return 'Decorrido(s) ' + str(dias.days) + ' Dia(s)'
        elif(anos > 0) and (meses == 0):
            return 'Decorrido(s) ' + str(anos) + ' Ano(s)'
        elif(dias.days < 0):
            return 'Inicia em ' + str(iniGatantia)



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
    tempoPercorridoGarntia = serializers.SerializerMethodField()

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Apartamento
        fields = ['id', 'apartamento', 'proprietario', 'inicioGarantia', 'tempoPercorridoGarntia', 'bloco']

    def get_tempoPercorridoGarntia(self, obj): #Filtra e traz o ultimo evento
        iniGatantia = obj.inicioGarantia
        iniGatantia = str(iniGatantia.strftime("%d-%m-%Y"))
        hoje = str(date.today().strftime("%d-%m-%Y"))

        date_format = "%d-%m-%Y"
        a = datetime.strptime(iniGatantia, date_format)
        b = datetime.strptime(hoje, date_format)
        anos = b.year - a.year
        meses = b.month - a.month
        meses = abs(meses)
        dias = b - a

        if (anos > 0) and (meses > 0):
            return 'Decorrido(s) ' + str(anos) + ' Ano(s) e ' + str(meses) + ' Mês(ses)'
        elif(anos == 0) and (dias.days > 0):
            return 'Decorrido(s) ' + str(dias.days) + ' Dia(s)'
        elif(anos > 0) and (meses == 0):
            return 'Decorrido(s) ' + str(anos) + ' Ano(s)'
        elif(dias.days < 0):
            return 'Inicia em ' + str(iniGatantia)


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
    numChamadosAbertosHoje = serializers.SerializerMethodField()
    ultimo_evento = serializers.SerializerMethodField()
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Chamado
        fields = ['id', 'dataCadastro', 'statusChamado', 'protocolo', 'ultimo_evento', 'categoriaProblema', 'usuario', 'envolveAreaComum', 'areaComum', 'apartamento', 'descricao', 'img', 'novosEventos', 'feedbackUsuario', 'numChamadosAbertosHoje']
        read_only_fields = ('id', 'dataCadastro', 'protocolo', 'usuario', 'ultimo_evento', 'statusChamado', 'numChamadosAbertosHoje')

    def get_ultimo_evento(self, obj): #Filtra e traz o ultimo evento
        evento = EventosChamado.objects.filter(chamado=obj.pk).first()
        return str(evento)

    def get_numChamadosAbertosHoje(self, obj): #Filtra e traz o ultimo evento
        hoje = str(date.today().strftime("%Y-%m-%d"))
        nrChamados = int(Chamado.objects.filter(usuario=obj.usuario, dataCadastro=hoje).count())

        return nrChamados


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