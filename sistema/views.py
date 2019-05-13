# coding=utf-8
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from rest_framework import generics
from .models import *
from .forms import *
from .serializers import *
from rest_framework import permissions

class IndexListView(generic.TemplateView):
    # Temporáriamente comentado, ainda plajejando qual será a tela pricipal do sistema
    # template_name = 'sistema/home.html'
    template_name = 'sistema/chamados/listarchamados.html'


"""Gerenciamento de usuários"""
class UsuariosCreateView(generic.CreateView):
    
    model = User
    form_class = UsuarioForm
    template_name = 'sistema/usuarios/cadastrodeusuarios.html'
    success_url = reverse_lazy('sistema:listarusuarios')



class UsuariosListView(generic.ListView):

    queryset = User.objects.all()
    context_object_name = 'usuarios'
    template_name = 'sistema/usuarios/listarusuarios.html'


class UsuariosUpdateView(generic.UpdateView):

    model = User
    form_class = UsuarioEditForm
    template_name = 'sistema/usuarios/editarusuario.html'
    success_url = reverse_lazy('sistema:listarusuarios')

    '''
    def get_context_data(self, **kwargs):
        context = {}
        if self.object:
            context['usuarios'] = self.object
            context_object_name = self.get_context_object_name(self.object)
            if context_object_name:
                context[context_object_name] = self.object
        context.update(**kwargs)
        return super(generic.UpdateView, self).get_context_data(**context)
    '''

class UsuariosPasswordUpdateView(generic.UpdateView):
    model = User
    form_class = UsuarioPasswordChangeForm
    template_name = 'sistema/usuarios/mudarsenha.html'
    success_url = reverse_lazy('sistema:listarusuarios')


class UsuariosDeleteView(generic.DeleteView):

    model = User
    success_url = reverse_lazy('sistema:listarusuarios')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

"""Fim de empgerenciamento de usuários"""

"""Gerenciamento de empreendimentos"""
class EmpreendimentoListView(generic.ListView):

    queryset = Empreendimento.objects.all().order_by('-pk')
    context_object_name = 'empreendimentos'
    template_name = 'sistema/empreendimentos/listarempreendimentos.html'


class EmpreendimentoCreateView(generic.CreateView):

    model = Empreendimento
    form_class = EmpreendimentoForm
    template_name = 'sistema/empreendimentos/cadastrarempreendimento.html'
    success_url = reverse_lazy('sistema:listarempreendimentos')


class EmpreendimentoUpdateView(generic.UpdateView):

    model = Empreendimento
    form_class = EmpreendimentoForm
    template_name = 'sistema/empreendimentos/editarempreendimento.html'
    success_url = reverse_lazy('sistema:listarempreendimentos')

    def get_context_data(self, **kwargs):
        context = {}
        if self.object:
            context['empreendimento'] = self.object
            context_object_name = self.get_context_object_name(self.object)
            if context_object_name:
                context[context_object_name] = self.object
        context.update(**kwargs)
        return super(generic.UpdateView, self).get_context_data(**context)


class EmpreendimentoDeleteView(generic.DeleteView):

    model = Empreendimento
    success_url = reverse_lazy('sistema:listarempreendimentos')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class BlocoListView(generic.ListView):

    queryset = Bloco.objects.all().order_by('-pk')
    context_object_name = 'blocos'
    template_name = 'sistema/empreendimentos/listarblocos.html'


class BlocoCreateView(generic.CreateView):

    model = Bloco
    form_class = BlocoForm
    template_name = 'sistema/empreendimentos/cadastrarbloco.html'
    success_url = reverse_lazy('sistema:listarblocos')


class BlocoUpdateView(generic.UpdateView):

    model = Bloco
    form_class = BlocoForm
    template_name = 'sistema/empreendimentos/editarbloco.html'
    success_url = reverse_lazy('sistema:listarblocos')

    def get_context_data(self, **kwargs):
        context = {}
        if self.object:
            context['bloco'] = self.object
            context_object_name = self.get_context_object_name(self.object)
            if context_object_name:
                context[context_object_name] = self.object
        context.update(**kwargs)
        return super(generic.UpdateView, self).get_context_data(**kwargs)


class BlocoDeleteView(generic.DeleteView):

    model = Bloco
    success_url = reverse_lazy('sistema:listarblocos')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class ApartamentoListView(generic.ListView):

    queryset = Apartamento.objects.all().order_by('-pk')
    context_object_name = 'apartamentos'
    template_name = 'sistema/empreendimentos/listarapartamentos.html'


class ApartamentoCreateView(generic.CreateView):

    model = Apartamento
    form_class = ApartamentoForm
    template_name = 'sistema/empreendimentos/cadastrodeapartamento.html'
    success_url = reverse_lazy('sistema:listarapartamentos')


class ApartamentoUpdateView(generic.UpdateView):

    model = Apartamento
    form_class = ApartamentoForm
    template_name = 'sistema/empreendimentos/editarapartamento.html'
    success_url = reverse_lazy('sistema:listarapartamentos')

    def get_context_data(self, **kwargs):
        context = {}
        if self.object:
            context['apartamento'] = self.object
            context_object_name = self.get_context_object_name(self.object)
            if context_object_name:
                context[context_object_name] = self.object
        context.update(**kwargs)
        return super(generic.UpdateView, self).get_context_data(**kwargs)


class ApartamentoDeleteView(generic.DeleteView):

    model = Apartamento
    success_url = reverse_lazy('sistema:listarapartamentos')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


"""Fim gerenciamento de empreendimentos"""


"""Inicio gerenciamento de tipos de problema"""

class CategoriaDeProblemaListView(generic.ListView):

    queryset = CategoriaDeProblema.objects.all().order_by('-pk')
    context_object_name = 'categorias'
    template_name = 'sistema/problemas/listarcategorias.html'


class CategoriaDeProblemaCreateView(generic.CreateView):

    model = CategoriaDeProblema
    form_class = CategoriaDeProblemaForm
    template_name = 'sistema/problemas/cadastrodecategoria.html'
    success_url = reverse_lazy('sistema:categoriasdeproblemas')


class CategoriaDeProblemaUpdateView(generic.UpdateView):

    model = CategoriaDeProblema
    form_class = CategoriaDeProblemaForm
    template_name = 'sistema/problemas/editarcategoria.html'
    success_url = reverse_lazy('sistema:categoriasdeproblemas')

    def get_context_data(self, **kwargs):
        context = {}
        if self.object:
            context['categoria'] = self.object
            context_object_name = self.get_context_object_name(self.object)
            if context_object_name:
                context[context_object_name] = self.object
        return super(generic.UpdateView, self).get_context_data(**context)


class CategoriaDeProblemaDeleteView(generic.DeleteView):

    model = CategoriaDeProblema
    success_url = reverse_lazy('sistema:categoriasdeproblemas')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class SubcategoriaDeProblemaListView(generic.ListView):

    queryset = SubcategoriaDeProblema.objects.all().order_by('-pk')
    context_object_name = 'subcategorias'
    template_name = 'sistema/problemas/listarsubcategorias.html'


class SubcategoriaDeProblemaCreateView(generic.CreateView):

    model = SubcategoriaDeProblema
    form_class = SubcategoriaDeProblemaForm
    template_name = 'sistema/problemas/cadastrodesubcategoria.html'
    success_url = reverse_lazy('sistema:subcategoriasdeproblemas')


class SubcategoriaDeProblemaUpdateView(generic.UpdateView):

    model = SubcategoriaDeProblema
    form_class = SubcategoriaDeProblemaForm
    template_name = 'sistema/problemas/editarsubcategoria.html'
    success_url = reverse_lazy('sistema:subcategoriasdeproblemas')

    def get_context_data(self, **kwargs):
        context = {}
        if self.object:
            context['subcategoria'] = self.object
            context_object_name = self.get_context_object_name(self.object)
            if context_object_name:
                context[context_object_name] = self.object
        context.update(**kwargs)
        return super(generic.UpdateView, self).get_context_data(**context)


class SubcategoriaDeProblemaDeleteView(generic.DeleteView):

    model = SubcategoriaDeProblema
    success_url = reverse_lazy('sistema:subcategoriasdeproblemas')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class ProblemaListView(generic.ListView):

    queryset = Problema.objects.all().order_by('-dataCadastro').order_by('prioridade')
    context_object_name = 'problemas'
    template_name = 'sistema/problemas/listarproblemas.html'


class ProblemaCreateView(generic.CreateView):

    model = Problema
    form_class = ProblemaForm
    template_name = 'sistema/problemas/cadastrodeproblema.html'
    success_url = reverse_lazy('sistema:listarproblemas')


class ProblemaUpdateView(generic.UpdateView):

    model = Problema
    form_class = ProblemaForm
    template_name = 'sistema/problemas/editarproblema.html'
    success_url = reverse_lazy('sistema:listarproblemas')

    def get_context_data(self, **kwargs):
        context = {}
        if self.object:
            context['problema'] = self.object
            context_object_name = self.get_context_object_name(self.object)
            if context_object_name:
                context[context_object_name] = self.object
        context.update(**kwargs)
        return super(generic.UpdateView, self).get_context_data(**context)


class ProblemaDeleteView(generic.DeleteView):

    model = Problema
    success_url = reverse_lazy('sistema:listarproblemas')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


"""Fim gerenciamento de tipos de problema"""

"""Inicio gerenciamento de chamados"""


class ChamadoListView(generic.ListView):

    queryset = Chamado.objects.all().order_by('-protocolo')
    context_object_name = 'chamados'
    template_name = 'sistema/chamados/listarchamados.html'


class ChamadoCreateView(generic.CreateView):

    model = Chamado
    form_class = ChamadoForm
    template_name = 'sistema/chamados/cadastrarchamado.html'
    success_url = reverse_lazy('sistema:listarchamados')

    def get_context_data(self, **kwargs):
        context = super(generic.CreateView, self).get_context_data(**kwargs)
        context['empreendimentos'] = Empreendimento.objects.all().order_by('nomeEmpreendimento')
        context['blocos'] = Bloco.objects.all().order_by('empreendimento__nomeEmpreendimento')
        context['apartamentos'] = Apartamento.objects.all().order_by('apartamento')
        return context


class ChamadoUpdateView(generic.UpdateView):

    model = Chamado
    form_class = ChamadoForm
    template_name = 'sistema/chamados/editarchamado.html'
    success_url = reverse_lazy('sistema:listarchamados')

    def get_context_data(self, **kwargs):
        context = {}
        if self.object:
            context['chamado'] = self.object
            context_object_name = self.get_context_object_name(self.object)
            if context_object_name:
                context[context_object_name] = self.object
        context.update(**context)
        return super(generic.UpdateView, self).get_context_data(**kwargs)


class ChamadoDeleteView(generic.DeleteView):

    model = Chamado
    success_url = reverse_lazy('sistema:listarchamados')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


"""Fim gerenciamento de chamados"""

"""APIs de Gerenciamento"""

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


class CategoriaDeProblemaCreateViewAPI(generics.ListCreateAPIView):
    queryset = CategoriaDeProblema.objects.all()
    serializer_class = CategoriaDeProblemaSerializer

    def perform_create(self, serializer):
        serializer.save()


class CategoriaDeProblemaDetailsViewAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoriaDeProblema.objects.all()
    serializer_class = CategoriaDeProblemaSerializer


class SubcategoriaDeProblemaCreateViewAPI(generics.ListCreateAPIView):
    queryset = SubcategoriaDeProblema.objects.all()
    serializer_class = SubcategoriaDeProblemaSerializer

    def perform_create(self, serializer):
        serializer.save()


class SubcategoriaDeProblemaDetailsViewAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubcategoriaDeProblema.objects.all()
    serializer_class = SubcategoriaDeProblemaSerializer


class ProblemaCreateViewAPI(generics.ListCreateAPIView):
    queryset = Problema.objects.all()
    serializer_class = ProblemaSerializer

    def perform_create(self, serializer):
        serializer.save()


class ProblemaDetailsViewAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Problema.objects.all()
    serializer_class = ProblemaSerializer

class ChamadoCreateViewAPIAny(generics.ListCreateAPIView):
    queryset = Chamado.objects.none()
    serializer_class = ChamadoSerializer
    permission_classes = (permissions.AllowAny,)

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