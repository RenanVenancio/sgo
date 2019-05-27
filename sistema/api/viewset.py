from .serializers import *
from rest_framework import permissions
from rest_framework import generics
from sistema.models import *
"""APIs de Gerenciamento"""
from rest_framework import filters
from django.db.models import Prefetch
from django.db.models import FilteredRelation, Q
class EmpreendimentoListViewAPI(generics.ListAPIView):
    '''Todos os Empreendimentos, blocos, apartamentos relacionados a esse usuário'''
    serializer_class = EmpreendimentoSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        blo = Bloco.objects.all()
        # FUNCIONOU results = Empreendimento.objects.prefetch_related(Prefetch('bloco_set__apartamento_set', queryset=Apartamento.objects.filter(proprietario=3)))
        #results = Empreendimento.objects.annotate(bloco__apartamento__proprietario=FilteredRelation('nomeEmpreendimento', condition=Q(bloco__apartamento__proprietario=5)))
        #results = Empreendimento.objects.filter(Q(bloco__apartamento__isnull=False) & Q(bloco__apartamento__proprietario=5) & Q(bloco__apartamento__proprietario__isnull=False)).distinct()
        results = Empreendimento.objects.prefetch_related(Prefetch('bloco_set__apartamento_set', queryset=Apartamento.objects.filter(Q(proprietario=3) & Q(proprietario__isnull=False)))).filter(Q(bloco__apartamento__isnull=False))
        return results





class BlocoListViewAPI(generics.ListAPIView):
    serializer_class = BlocoSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        results = Bloco.objects.filter(apartamento__proprietario=user.pk).distinct()

        return results


class ApartamentoListViewAPI(generics.ListAPIView):
    serializer_class = ApartamentoSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        results = Apartamento.objects.filter(proprietario=user.pk).distinct()

        return results



#REmover
class ApartamentoProprietarioSerializerDetailsViewAPI(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ApartamentoProprietarioSerializer
    def get_queryset(self):
        user = self.request.user
        results = Apartamento.objects.filter(proprietario=user)
        self.search_fields = ('nomeEmpreendimento', 'bloco', 'apartamento')
        return results





class CategoriaDeProblemaListViewAPI(generics.ListAPIView):
    queryset = CategoriaDeProblema.objects.all()
    serializer_class = CategoriaDeProblemaSerializer




class ChamadoCreateViewAPIAny(generics.ListCreateAPIView):
    queryset = Chamado.objects.none()
    serializer_class = ChamadoSerializer

    # permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer):
        serializer.save()


class ChamadoCreateViewAPI(generics.ListCreateAPIView):
    queryset = Chamado.objects.all()
    serializer_class = ChamadoSerializer

    def perform_create(self, serializer):
        serializer.save()


class ChamadoDetailsViewAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chamado.objects.all()
    serializer_class = ChamadoSerializer


"""Fim APIs de gerenciamento"""

class AptoCascata(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = EmpSerializer
    def get_queryset(self):
        user = self.request.user
        print(Apartamento.bloco)
        results = Empreendimento.objects.filter(bloco__apartamento__proprietario=user.pk)
        return results
