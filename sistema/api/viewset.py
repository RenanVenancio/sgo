from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .serializers import *
from rest_framework import permissions
from rest_framework import generics
from sistema.models import *
from rest_framework import filters


class EmpreendimentoListViewAPI(ReadOnlyModelViewSet):
    '''
    list:
        Traz todos os empreendimentos onde o usuario logado possui apartamentos.

    retrieve:
        Forneça o id do empreendimento para filtrar
    '''
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = EmpreendimentoSerializer

    def get_queryset(self):
        user = self.request.user
        
        results = Empreendimento.objects.filter(bloco__apartamento__proprietario=user.pk).distinct()
        return results


class BlocoListViewAPI(ReadOnlyModelViewSet):
    '''
    list:
        Aceita filtro pelo id do empreendimento forneça o id do mesmo como parametro na Url
        EX: localhost:8000/listarblocos/?empreendimento=2
        caso não sejam passados parametros serão retornados todos os blocos onde o
        usuário logado possuir apartamentos.


    read:
        Forneça o id de um bloco para recuperar o mesmo
    '''
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    serializer_class = BlocoSerializer

    def get_queryset(self):
        user = self.request.user
        emp = self.request.GET.get('empreendimento')
        if (emp):
            return Bloco.objects.filter(empreendimento=emp, apartamento__proprietario=user.pk).distinct()
        else:
            return Bloco.objects.filter(apartamento__proprietario=user.pk).distinct()


class ApartamentoListViewAPI(ReadOnlyModelViewSet):
    '''
    list:
        Traz a listagem apenas dos apartamentos do usuário.
        aceita filtrar pelo id do bloco
        EX: listarapartamentos/?bloco=2    <-Traz todos apartamentos do usuário no bloco 2


    read:
        Forneça o id do apartamento na url para trazer o apartamento.

    '''
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    serializer_class = ApartamentoSerializer

    def get_queryset(self):
        bloco = self.request.GET.get('bloco')
        user = self.request.user
        if (bloco):
            return Apartamento.objects.filter(proprietario=user.pk, bloco=bloco).distinct()
        else:
            return Apartamento.objects.filter(proprietario=user.pk).distinct()


class ApartamentoListaGeral(ReadOnlyModelViewSet):
    '''
    list:
        Traz todos apartamentos do usuário logado junto com seus respectivos blocos e empreendimentos relacionados


    read:
        Forneça um id de um apartamentos do usuário logado para trazer o apartamento com seus respectivos blocos e
        empreendimentos relacionados.

    '''
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    serializer_class = ApartamentoProprietarioSerializer

    def get_queryset(self):
        user = self.request.user
        results = Apartamento.objects.filter(proprietario=user.pk)
        return results


class CategoriaDeProblemaListViewAPI(ReadOnlyModelViewSet):
    '''
    list:
        Traz todas as categorias de problema cadastradas


    read:
        Forneça um id na url para trazer apenas a categoria desejada.

    '''
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    queryset = CategoriaDeProblema.objects.all()
    serializer_class = CategoriaDeProblemaSerializer


class AreaComumListViewAPI(ReadOnlyModelViewSet):
    '''
    list:
        Traz a listagem de todas as áreas comuns cadastradas no sistema.


    read:
        Forneça o id e uma área comum cadastrada para recuperar a mesma
    '''
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (TokenAuthentication,)

    queryset = AreaComum.objects.all()
    serializer_class = AreaComumSerializer

#Gerencia dos chamados
class ChamadoCreateViewAPI(ModelViewSet):    #Criar chamados
    '''
    list:
        Traz a listagem de chamados abertos pelo usuario logado, mas os campos Apartamento, area comum, categoria
        de problemas vem apenas com os ids.


    create:
        Essa url abre um novo chamado.


    retrieve:
        Recupera um chamado já existente pelo id passado na Url.


    update:
        Use essa url para atualizar um chamado.


    partial_update:
        Essa url também faz uma atualização em um chamado, mas e atualização pode ser feita em apenas um ou mais
        campos caso necessário, ao invés de atualizar o registro inteiro.


    delete:
        Utilize essa url para deletar um chamado passando o id do mesmo na Url
    '''

    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = ChamadoCreateUpdateSerializer

    def get_queryset(self):
        user = self.request.user
        return Chamado.objects.filter(usuario=user.pk)


    def perform_create(self, serializer):
        usuario = Usuarios.objects.get(pk=self.request.user.pk)
        serializer.save(usuario=usuario)


class ChamadoListViewAPI(ReadOnlyModelViewSet):    #Listar chamados
    '''
    list:
        Aceita filter Backends busca nos campos [Protocolo ou Descrição]
        Traz os campos como apartamento, cat de problema, área comum como string


    read:
        Forneça um id de um chamado para visualizar
        OBS: Traz os campos como apartamento, cat de problema, área comum como string.

    '''
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self): #Definingo queryset para mostrar apenas chamados do usuario logado
        user = self.request.user
        return Chamado.objects.filter(usuario=user.pk)

    serializer_class = ChamadoListSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('protocolo', 'descricao')


'''
class ChamadoDetailsViewAPI(ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (TokenAuthentication,)

    serializer_class = ChamadoCreateUpdateSerializer

    def get_queryset(self):
        user = self.request.user
        return Chamado.objects.filter(usuario=user.pk)
'''