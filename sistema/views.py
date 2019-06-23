# coding=utf-8
from django.contrib.admin import StackedInline
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models import F, Count, Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.test import override_settings
from django.urls import reverse_lazy
from django.views import generic
from rest_framework import generics, permissions
from .forms import *
from django.views.generic import View
import json
from datetime import datetime, timedelta
from datetime import date
from .models import *
from django.core.mail import get_connection


class DashboardView(generic.ListView):

    context = {}
    def get(self, request):
        #Pegando datas passadas via GET
        periodoInicial = self.request.GET.get('periodoInicial')
        periodoFinal = self.request.GET.get('periodoFinal')


        #Se não for passada nenhuma data, pegue a a atual - 30 dias
        if periodoInicial and periodoFinal:
            pass
        else:
            dataEntrada = date.today()
            dataEntrada = dataEntrada - timedelta(30)
            periodoInicial = str(dataEntrada.strftime("%Y-%m-%d"))
            periodoFinal = str(date.today().strftime("%Y-%m-%d"))

        #Passando as datas pro contexto
        self.context['periodoInicial'] = periodoInicial
        self.context['periodoFinal'] = periodoFinal


        #Coletando os dados das categorias nos chamados para inserir no gráfico ABC
        categorias = Chamado.objects.all().values(catProblema=F('categoriaProblema__nomeCategoria'))\
            .annotate(ocorrencias=Count('catProblema'))\
            .order_by('-ocorrencias').filter(dataCadastro__range=[periodoInicial, periodoFinal])

        categoriasSoma = categorias.filter(dataCadastro__range=[periodoInicial, periodoFinal]).aggregate(Sum('ocorrencias'))
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
        #Fim dos dados do grafico ABC


        '''GRAFICO DE EMPREENDIMENTOS'''
        #Coletando os dados das categorias nos chamados para inserir no gráfico ABC
        chamados = Chamado.objects.all().values(emprendimento=F('apartamento__bloco__empreendimento__nomeEmpreendimento'))\
            .annotate(ocorrencias=Count('emprendimento'))\
            .order_by('-ocorrencias').filter(dataCadastro__range=[periodoInicial, periodoFinal])

        contagemEmpreendimentos = categorias.filter(dataCadastro__range=[periodoInicial, periodoFinal]).aggregate(Sum('ocorrencias'))
        contagemEmpreendimentos = contagemEmpreendimentos['ocorrencias__sum']

        nomesEmpreendimentos = []          #Nomes das categorias dos problemas
        qtdOcorrenciaEmpreendimento = []  #Quantidade de vezes que o problema ocorre
        percentEmpreendimento = []      #Porcentagem
        percentAccEmpreendimento = []   #Porcentagem acumulada


        for ind, i in enumerate(chamados):
            nomesEmpreendimentos.append(i['emprendimento'])
            qtdOcorrenciaEmpreendimento.append(i['ocorrencias'])
            percentEmpreendimento.append((   ((i['ocorrencias'] / contagemEmpreendimentos) * 100))  )
            if(ind == 0):
                percentAccEmpreendimento.append(percentEmpreendimento[ind])
            else:
                percentAccEmpreendimento.append(  ((percentEmpreendimento[ind] + percentAccEmpreendimento[ind - 1]))   )


        #Passando os dados para o contexto
        self.context['rotulosGraficoEmpreendimento'] = json.dumps(nomesEmpreendimentos)
        self.context['dadosGraficoEmpreendimento'] = json.dumps(qtdOcorrenciaEmpreendimento)
        self.context['dadosPercentEmpreendimento'] = json.dumps(percentEmpreendimento)
        self.context['dadosPercentAccEmpreendimento'] = json.dumps(percentAccEmpreendimento)
        #Fim dos dados do grafico ABC

        '''FIM GRAFICO EMPREENDIMENTOS'''


        #Coletando os dados dos feedbacks nos chamados para inserir no gráfico
        feedbacks = Chamado.objects.all().values('feedbackUsuario').annotate(contagem=Count('feedbackUsuario'))\
            .filter(feedbackUsuario__gte=1, dataCadastro__range=[periodoInicial, periodoFinal]).order_by('feedbackUsuario')

        feedbacksSoma = feedbacks.aggregate(Sum('contagem'))
        feedbacksSoma = feedbacksSoma['contagem__sum']
        feedbacksRotulos = []
        percentFeedbacks = []      #Porcentagem dos feedbacks



        for i in feedbacks:
            i['percentual'] = (i['contagem'] / feedbacksSoma) * 100
            feedbacksRotulos.append(str(i['feedbackUsuario']) + ' Estrela(s)')
            percentFeedbacks.append(i['percentual'])
        #Passando a porcentagem dos feedbacks para o grafico
        self.context['percentFeedbacks'] = json.dumps(percentFeedbacks)
        self.context['rotulosFeedbacks'] = json.dumps(feedbacksRotulos)

        #Fim grafico feedbacks


        chamado = Chamado.objects.filter(dataCadastro__range=[periodoInicial, periodoFinal]).count()
        self.context['chamados'] = chamado

        chamadosAnalise = Chamado.objects.filter(statusChamado='Em analise', dataCadastro__range=[periodoInicial, periodoFinal]).count()
        self.context['chamadosAnalise'] = chamadosAnalise

        chamadosFinalizados = Chamado.objects.filter(statusChamado='Finalizado', dataCadastro__range=[periodoInicial, periodoFinal]).count()
        self.context['chamadosFinalizados'] = chamadosFinalizados

        usuarios =  Usuarios.objects.filter(date_joined__range=[periodoInicial, periodoFinal + ' 23:59:59']).count()
        self.context['usuarios'] = usuarios

        template_name = 'sistema/dashboard/dashboard.html'
        return render(request, template_name, self.context)
'''Fim da tela do Dashboard'''


class EmpresaCreateView(generic.CreateView):
    reverse_lazy('sistema:listarusuarios')
    model = Empresa
    form_class = EmpresaForm
    template_name = 'sistema/empresa/cadastrarempresa.html'
    success_url = reverse_lazy('sistema:dashboard')

    def get(self, request, *args, **kwargs):
        empresa = Empresa.objects.all() #Consultando empresas cadastradas
        if empresa:
            return redirect('sistema:editarempresa', pk=empresa[0].pk) #Caso exista redirecione para edição
        else:
            return self.post(request, *args, **kwargs)


'''Gerenciamento da empresa'''
class EmpresaEditView(generic.UpdateView):

    model = Empresa
    form_class = EmpresaForm
    template_name = 'sistema/empresa/editarempresa.html'
    success_url = reverse_lazy('sistema:dashboard')


class EmpresaDeleteView(generic.DeleteView):

    model = Empresa
    success_url = reverse_lazy('sistema:dashboard')
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
'''Fim gerenciamento da empresa'''

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

    queryset = Chamado.objects.all().order_by('protocolo')
    context_object_name = 'chamados'
    template_name = 'sistema/chamados/listarchamados.html'


class ChamadoCreateView(generic.CreateView):

    model = Chamado
    form_class = ChamadoForm
    template_name = 'sistema/chamados/cadastrarchamado.html'
    success_url = reverse_lazy('sistema:listarchamados')

from django.contrib.messages.views import SuccessMessageMixin

class ChamadoUpdateView(SuccessMessageMixin, generic.UpdateView):

    model = Chamado
    form_class = ChamadoForm
    template_name = 'sistema/chamados/editarchamado.html'
    success_message = "Chamado alterado com sucesso!"
    #success_url = reverse_lazy('sistema:listarchamados')

    def post(self, request, *args, **kwargs):

        if request.POST.get('descEvento'):
            novoEvento = EventosChamado()
            novoEvento.descricaoEvento = request.POST.get('descEvento')
            idChamado = request.POST.get('chamado')
            chamado = Chamado.objects.get(pk=idChamado)


            novoEvento.chamado = chamado
            novoEvento.save()






        return super(generic.UpdateView, self).post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = {}
        if self.object:
            context['chamado'] = self.object
            context_object_name = self.get_context_object_name(self.object)
            if context_object_name:
                context[context_object_name] = self.object
        context.update(**context)

        return super(generic.UpdateView, self).get_context_data(**kwargs)

    def dataCadastro(self):
        return self.object.dataCadastro

    def protocolo(self):
        return self.object.protocolo

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



class ChamadoPrintView(generic.UpdateView):
    context = {}

    def get(self, request, **kwargs):

        idChamado = kwargs['pk']

        empresa = Empresa.objects.all()
        self.context['empresa'] = empresa[0]
        chamado = Chamado.objects.get(id=idChamado)
        self.context['chamado'] = chamado

        return render(request, 'sistema/chamados/imprimirchamado.html', self.context)



class RelatorioChamadoFiltro(View):
    context = {}
    def get(self, request):

        query_usuarios =  Usuarios.objects.all()
        self.context['usuarios'] = query_usuarios

        query_empreendimentos =  Empreendimento.objects.all()
        self.context['empreendimentos'] = query_empreendimentos

        query_categoriasDeProblemas =  CategoriaDeProblema.objects.all()
        self.context['categorias'] = query_categoriasDeProblemas

        query_areasComuns =  AreaComum.objects.all()
        self.context['areasComuns'] = query_areasComuns

        statusChamado = self.request.GET.get('status-chamado')
        dataInicial = self.request.GET.get('data-inicial')
        dataFinal = self.request.GET.get('data-final')
        empreendimento = self.request.GET.get('empreendimento')
        proprietario = self.request.GET.get('proprietario')
        categoria = self.request.GET.get('categoria')
        areasComuns = self.request.GET.get('area-comum')
        prioridade = self.request.GET.get('prioridade')


        self.context['prioridade_get'] = prioridade.split(";")[0] + " a " +  prioridade.split(";")[1] if prioridade else "None"
        self.context['status_get'] = statusChamado if statusChamado else "Todos"
        self.context['dataInicial_get'] = dataInicial if dataInicial else "Todos"
        self.context['dataFinal_get'] = dataFinal if dataFinal else "Todos"
        self.context['area_get'] = query_areasComuns.get(pk=areasComuns) if areasComuns else "Todos"
        self.context['proprietario_get'] = query_usuarios.get(pk=proprietario) if proprietario else "Todos"
        self.context['categoria_get'] = query_categoriasDeProblemas.get(pk=categoria) if categoria else "Todos"
        self.context['empreendimento_get'] = query_empreendimentos.get(pk=categoria) if categoria else "Todos"

        if statusChamado or proprietario or dataFinal or dataFinal or empreendimento or categoria or areasComuns or prioridade:

            filters = {}
            if statusChamado:
                filters['statusChamado'] = statusChamado

            if dataInicial and dataFinal:
                filters['dataCadastro__range'] = [dataInicial, dataFinal]

            if empreendimento:
                filters['apartamento__bloco__empreendimento'] = empreendimento

            if proprietario:
                filters['usuario'] = proprietario

            if categoria:
                filters['categoriaProblema'] = categoria

            if areasComuns:
                filters['areaComum'] = areasComuns

            if prioridade:
                filters['prioridade__range'] = prioridade.split(";")


            chamadoFiltrado = Chamado.objects.filter(**filters)

            self.context['chamados'] = chamadoFiltrado
            return render(request, 'relatorios/chamado/chamadoslista.html', self.context)


        template_name = 'relatorios/chamado/filtragens.html'
        return render(request, template_name, self.context)


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
