from .serializers import *
from rest_framework import permissions
from rest_framework import generics
from sistema.models import *
"""APIs de Gerenciamento"""
from rest_framework import filters

class EmpreendimentoCreateViewAPI(generics.ListCreateAPIView):
    queryset = Empreendimento.objects.all()
    serializer_class = EmpreendimentoSerializer

    def perform_create(self, serializer):
        serializer.save()


class EmpreendimentoDetailsViewAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empreendimento.objects.all()
    serializer_class = EmpreendimentoSerializer


class BlocoSerializerCreateViewAPI(generics.ListCreateAPIView):
    queryset = Bloco.objects.all()
    serializer_class = BlocoSerializer

    def perform_create(self, serializer):
        serializer.save()


class BlocoSerializerDetailsViewAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bloco.objects.all()
    serializer_class = BlocoSerializer


class ApartamentoSerializerCreateViewAPI(generics.ListCreateAPIView):
    queryset = Apartamento.objects.all()
    serializer_class = ApartamentoSerializer

    def perform_create(self, serializer):
        serializer.save()


class ApartamentoSerializerDetailsViewAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Apartamento.objects.all()
    serializer_class = ApartamentoSerializer


class ApartamentoProprietarioSerializerDetailsViewAPI(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ApartamentoProprietarioSerializer
    def get_queryset(self):
        user = self.request.user
        results = Apartamento.objects.filter(proprietario=user)
        self.search_fields = ('nomeEmpreendimento', 'bloco', 'apartamento')
        return results


class CategoriaDeProblemaCreateViewAPI(generics.ListCreateAPIView):
    queryset = CategoriaDeProblema.objects.all()
    serializer_class = CategoriaDeProblemaSerializer

    def perform_create(self, serializer):
        serializer.save()


class CategoriaDeProblemaDetailsViewAPI(generics.RetrieveUpdateDestroyAPIView):
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

