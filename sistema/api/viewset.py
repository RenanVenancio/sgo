from .serializers import *
from rest_framework import permissions
from rest_framework import generics
from sistema.models import *
"""APIs de Gerenciamento"""
from rest_framework import filters
from django.db.models import FilteredRelation, Q, Prefetch

class EmpreendimentoListViewAPI(generics.ListAPIView):
    '''Todos os Empreendimentos, blocos, apartamentos relacionados a esse usuário'''
    serializer_class = EmpreendimentoSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        
        # TRAZ TODOS OS EMP results = Empreendimento.objects.prefetch_related(Prefetch('bloco_set__apartamento_set', queryset=Apartamento.objects.filter(proprietario=3)))
        results = Empreendimento.objects.filter(bloco__apartamento__proprietario=user.pk).distinct()
        return results


class BlocoListViewAPI(generics.ListAPIView):
    serializer_class = BlocoSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        emp = self.request.GET.get('empreendimento')
        if (emp):
            return Bloco.objects.filter(empreendimento=emp, apartamento__proprietario=user.pk).distinct()
        else:
            return Bloco.objects.filter(apartamento__proprietario=user.pk).distinct()

 


class ApartamentoListViewAPI(generics.ListAPIView):
    serializer_class = ApartamentoSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        bloco = self.request.GET.get('bloco')
        user = self.request.user
        if (bloco):
            return Apartamento.objects.filter(proprietario=user.pk, bloco=bloco).distinct()
        else:
            return Apartamento.objects.filter(proprietario=user.pk).distinct()



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

