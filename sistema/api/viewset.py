from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .serializers import *
from rest_framework import permissions
from rest_framework import generics
from sistema.models import *
from rest_framework import filters


class EmpreendimentoListViewAPI(ReadOnlyModelViewSet):
    '''Todos os Empreendimentos onde o usuario possui aptos'''
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = EmpreendimentoSerializer

    def get_queryset(self):
        user = self.request.user
        results = Empreendimento.objects.filter(bloco__apartamento__proprietario=user.pk).distinct()
        return results


class BlocoListViewAPI(ReadOnlyModelViewSet):
    '''Todos os Blocos onde o usuario possui aptos'''
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
    '''Todos os Apartamentos do usuario'''
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
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    serializer_class = ApartamentoProprietarioSerializer

    def get_queryset(self):
        user = self.request.user
        results = Apartamento.objects.filter(proprietario=user.pk)
        return results


class CategoriaDeProblemaListViewAPI(ReadOnlyModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    queryset = CategoriaDeProblema.objects.all()
    serializer_class = CategoriaDeProblemaSerializer


class AreaComumListViewAPI(ReadOnlyModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    queryset = AreaComum.objects.all()
    serializer_class = AreaComumSerializer

#Gerencia dos chamados
class ChamadoCreateViewAPI(ModelViewSet):    #Criar chamados
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
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self): #Definingo queryset para mostrar apenas chamados do usuario logado
        user = self.request.user
        return Chamado.objects.filter(usuario=user.pk)

    serializer_class = ChamadoListSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('protocolo', 'descricao')


class ChamadoDetailsViewAPI(ModelViewSet): #atualia e deleta
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    serializer_class = ChamadoCreateUpdateSerializer

    def get_queryset(self):
        user = self.request.user
        return Chamado.objects.filter(usuario=user.pk)
