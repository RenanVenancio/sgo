# coding=utf-8
from django.contrib.admin import StackedInline
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models import F, Count, Sum
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from rest_framework import generics, permissions
from .forms import *
from django.views.generic import View
import json
from datetime import datetime
from datetime import date
from decimal import Decimal
'''Tela do Dashboard'''
class DashboardView(generic.ListView):

    context = {}
    def get(self, request):
        #Coletando os dados das categorias nos chamados para inserir no gráfico ABC
        categorias = Chamado.objects.all().values(catProblema=F('categoriaProblema__nomeCategoria')).annotate(ocorrencias=Count('catProblema')).order_by('-ocorrencias')
        categoriasSoma = categorias.aggregate(Sum('ocorrencias'))
        categoriasSoma = categoriasSoma['ocorrencias__sum']

        nomesCatProblemas = []          #Nomes das categorias dos problemas
        qtdOcorrenciaCatProblemas = []  #Quantidade de vezes que o problema ocorre
        percent = []      #Porcentagem
        percentAcc = []   #Porcentagem acumulada


        for ind, i in enumerate(categorias):
            nomesCatProblemas.append(i['catProblema'])
            qtdOcorrenciaCatProblemas.append(i['ocorrencias'])
            percent.append((   ((i['ocorrencias'] / categoriasSoma) * 100))  )
            if(ind == 0):
                percentAcc.append(percent[ind])
            else:
                percentAcc.append(  ((percent[ind] + percentAcc[ind - 1]))   )



        #Passando os dados para o contexto
        self.context['rotulosGrafico'] = json.dumps(nomesCatProblemas)
        self.context['dadosGrafico'] = json.dumps(qtdOcorrenciaCatProblemas)
        self.context['dadosPercent'] = json.dumps(percent)
        self.context['dadosPercentAcc'] = json.dumps(percentAcc)



        feedbacks = Chamado.objects.all().values('feedbackUsuario').annotate(contagem=Count('feedbackUsuario')).order_by('feedbackUsuario')





        chamado = Chamado.objects.count()
        self.context['chamados'] = chamado

        chamadosAnalise = Chamado.objects.filter(statusChamado='Em analise').count()
        self.context['chamadosAnalise'] = chamadosAnalise

        chamadosFinalizados = Chamado.objects.filter(statusChamado='Finalizado').count()
        self.context['chamadosFinalizados'] = chamadosFinalizados


        usuarios =  Usuarios.objects.all().count()
        self.context['usuarios'] = usuarios

        template_name = 'sistema/dashboard/dashboard.html'
        return render(request, template_name, self.context)
'''Fim da tela do Dashboard'''

"""Gerenciamento de usuários"""
class UsuariosCreateView(generic.CreateView):
    
    model = Usuarios
    form_class = UsuarioForm
    template_name = 'sistema/usuarios/cadastrodeusuarios.html'
    success_url = reverse_lazy('sistema:listarusuarios')


class UsuariosListView(generic.ListView):

    queryset = Usuarios.objects.all()
    context_object_name = 'usuarios'
    template_name = 'sistema/usuarios/listarusuarios.html'


class UsuariosUpdateView(generic.UpdateView):

    model = Usuarios
    form_class = UsuarioEditForm
    template_name = 'sistema/usuarios/editarusuario.html'
    success_url = reverse_lazy('sistema:listarusuarios')


    def apartamentos(self):
        return Apartamento.objects.select_related('bloco__empreendimento').filter(proprietario=self.object.pk)

class UsuariosPasswordUpdateView(generic.UpdateView):
    model = Usuarios
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
'''Fim do gerenciamento de tipos de problema'''

'''Inicio do gerenciamento de Áreas comuns'''
class AreasComunsListView(generic.ListView):

    queryset = AreaComum.objects.all().order_by('-pk')
    context_object_name = 'areasComuns'
    template_name = 'sistema/empreendimentos/listarareascomuns.html'


class AreaComumCreateView(generic.CreateView):

    model = AreaComum
    form_class = AreaComumForm
    template_name = 'sistema/empreendimentos/cadastrarareacomum.html'
    success_url = reverse_lazy('sistema:listarareascomuns')


class AreaComumUpdateView(generic.UpdateView):

    model = AreaComum
    form_class = AreaComumForm
    template_name = 'sistema/empreendimentos/editarareacomum.html'
    success_url = reverse_lazy('sistema:listarareascomuns')

    def get_context_data(self, **kwargs):
        context = {}
        if self.object:
            context['areaComum'] = self.object
            context_object_name = self.get_context_object_name(self.object)
            if context_object_name:
                context[context_object_name] = self.object
        return super(generic.UpdateView, self).get_context_data(**context)


class AreaComumDeleteView(generic.DeleteView):

    model = AreaComum
    success_url = reverse_lazy('sistema:listarareascomuns')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

'''Fim do gerenciamento de areas comuns'''


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
        context['apartamentos'] = Apartamento.objects.all()
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

    def garantia(self):
        print(self.object.protocolo)

        iniGatantia = self.object.apartamento.inicioGarantia
        iniGatantia = str(iniGatantia.strftime("%d-%m-%Y"))
        hoje = self.object.dataCadastro
        hoje = str(hoje.strftime("%d-%m-%Y"))

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


    def eventos(self): #Retorna os eventos do chamado para a view
        return EventosChamado.objects.filter(chamado=self.object.pk)

    def ultimoEvento(self):     #Retorna o ultimo evento ocorrido
        return EventosChamado.objects.filter(chamado=self.object.pk).latest('pk')


class ChamadoDeleteView(generic.DeleteView):

    model = Chamado
    success_url = reverse_lazy('sistema:listarchamados')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class EventoChamadoDeleteView(generic.DeleteView):

    model = EventosChamado

    def get(self, request, *args, **kwargs):
        pk =self.kwargs['pk']
        evento = EventosChamado.objects.get(pk=pk)
        pkChamado = evento.chamado.pk
        self.success_url = reverse_lazy('sistema:editarchamado', kwargs={'pk': pkChamado})

        return self.post(request, *args, **kwargs)


class EventoChamadoCreateView(View):

    def post(self, request):

        if request.method == "POST":
            novoEvento = EventosChamado()
            novoEvento.descricaoEvento = request.POST.get('descricaoEvento')
            idChamado = request.POST.get('chamado')
            novoEvento.chamado = Chamado.objects.get(id=request.POST.get('chamado'))

            novoEvento.save()

        return redirect('sistema:editarchamado', pk=idChamado)



"""Fim gerenciamento de chamados"""


from sistema.api.serializers import ApartamentoProprietarioSerializer
class ApartamentoProprietarioListJson(generics.ListAPIView):
    ''''
    get:
    Popula os selects dos chamados no site.
    '''
    serializer_class = ApartamentoProprietarioSerializer
    permission_classes = (permissions.AllowAny,)
    def get_queryset(self):
        user = self.kwargs['pk']
        results = Apartamento.objects.filter(proprietario=user)
        return results
