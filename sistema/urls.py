# coding=utf-8


from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required  #Staff
from django.urls import reverse_lazy
from sistema.api import viewset

app_name = 'sistema'






urlpatterns = [
    path('', include('sistema.api.urls')),

    path('', staff_member_required(views.DashboardView.as_view(), login_url=reverse_lazy('sistema:login')), name='dashboard'),

    #Login e logout
    path('login/', auth_views.login, {'template_name': 'sistema/login.html'}, name='login'),
    path('logout/', auth_views.logout, {'next_page': reverse_lazy('sistema:dashboard')}, name='logout'),


    path('empresa/cadastrarempresa/', staff_member_required(
        views.EmpresaCreateView.as_view(), login_url=reverse_lazy('sistema:login')
    ), name='cadastrarempresa'),

    path('empresa/editarempresa/<int:pk>/', staff_member_required(
        views.EmpresaEditView.as_view(), login_url=reverse_lazy('sistema:login')
    ), name='editarempresa'),

    path('empresa/deletarempresa/<int:pk>/', staff_member_required(
        views.EmpresaDeleteView.as_view(), login_url=reverse_lazy('sistema:login')
    ), name='deletarempresa'),

    path('usuarios/editarusuario/<int:pk>/mudarsenha', staff_member_required(
        views.UsuariosPasswordUpdateView.as_view(), login_url=reverse_lazy('sistema:login')
    ), name='mudarsenhausuario'),

    path('usuarios/cadastrarusuario/', staff_member_required(
        views.UsuariosCreateView.as_view(), login_url=reverse_lazy('sistema:login')
    ), name='cadastrarusuario'),

    path('usuarios/listarusuarios/', staff_member_required(
        views.UsuariosListView.as_view(), login_url=reverse_lazy('sistema:login')
    ), name='listarusuarios'),

    path('usuarios/editarusuario/<int:pk>/', staff_member_required(
        views.UsuariosUpdateView.as_view(), login_url=reverse_lazy('sistema:login')
    ), name='editarusuario'),

    path('usuarios/deletarusuario/<int:pk>/', staff_member_required(
        views.UsuariosDeleteView.as_view(), login_url=reverse_lazy('sistema:login')
    ), name='deletarusuario'),



    path('empreendimentos/listarempreendimentos/', staff_member_required(
        views.EmpreendimentoListView.as_view(), login_url=reverse_lazy('sistema:login')
    ), name='listarempreendimentos'),
    path('empreendimentos/cadastrarempreendimento/', staff_member_required(
        views.EmpreendimentoCreateView.as_view(), login_url=reverse_lazy('sistema:login')
    ), name='cadastrarempreendimento'),
    path('empreendimentos/editarempreendimento/<int:pk>/', staff_member_required(
        views.EmpreendimentoUpdateView.as_view(), login_url=reverse_lazy('sistema:login')
    ), name='editarempreendimento'),
    path('empreendimentos/deletarempreendimento/<int:pk>/', staff_member_required(
        views.EmpreendimentoDeleteView.as_view(), login_url=reverse_lazy('sistema:login')
    ), name='deletarempreendimento'),


    path('empreendimentos/areascomuns/', staff_member_required(
        views.AreasComunsListView.as_view(), login_url=reverse_lazy('sistema:login')
    ), name='listarareascomuns'),
    path('empreendimentos/areascomuns/cadastrarareacomum', staff_member_required(
        views.AreaComumCreateView.as_view(), login_url=reverse_lazy('sistema:login')
    ), name='cadastrarareacomum'),
    path('empreendimentos/areascomuns/editarareacomum/<int:pk>/', staff_member_required(
        views.AreaComumUpdateView.as_view(), login_url=reverse_lazy('sistema:login')
    ), name='editarareacomum'),
    path('empreendimentos/areascomuns/deletarareacomum/<int:pk>/', staff_member_required(
        views.AreaComumDeleteView.as_view(), login_url=reverse_lazy('sistema:login')
    ), name='deletarareacomum'),


    path('empreendimentos/blocos/listarblocos/', staff_member_required(
        views.BlocoListView.as_view(), login_url=reverse_lazy('sistema:login')
    ), name='listarblocos'),
    path('empreendimentos/blocos/cadastrarbloco/', staff_member_required(
        views.BlocoCreateView.as_view(), login_url=reverse_lazy('sistema:login')
    ), name='cadastrarbloco'),
    path('empreendimentos/blocos/editarbloco/<int:pk>/', staff_member_required(
        views.BlocoUpdateView.as_view(), login_url=reverse_lazy('sistema:login')
    ), name='editarbloco'),
    path('empreendimentos/blocos/deletarbloco/<int:pk>/', staff_member_required(
        views.BlocoDeleteView.as_view(), login_url=reverse_lazy('sistema:login')
    ), name='deletarbloco'),


    path('empreendimentos/blocos/listarapartamentos/', staff_member_required(
        views.ApartamentoListView.as_view(), login_url=reverse_lazy('sistema:login')
    ), name='listarapartamentos'),
    path('empreendimentos/blocos/cadastrarapartamento/', staff_member_required(
        views.ApartamentoCreateView.as_view(), login_url=reverse_lazy('sistema:login')
    ), name='cadastrarapartamento'),
    path('empreendimentos/blocos/editarapartamento/<int:pk>/', staff_member_required(
        views.ApartamentoUpdateView.as_view(), login_url=reverse_lazy('sistema:login')
    ), name='editarapartamento'),
    path('empreendimentos/blocos/deletarapartamento/<int:pk>/', staff_member_required(
        views.ApartamentoDeleteView.as_view(), login_url=reverse_lazy('sistema:login')
    ), name='deletarapartamento'),
    path('json/apartamentos/proprietario/<int:pk>', staff_member_required(
         views.ApartamentoProprietarioListJson.as_view(), login_url=reverse_lazy('sistema:login')
    ), name='apartamentoproprietario'),


    path('problemas/listarcategorias/', staff_member_required(
        views.CategoriaDeProblemaListView.as_view(), login_url=reverse_lazy('sistema:login')
    ), name='categoriasdeproblemas'),
    path('problemas/cadastrarcategoria/', staff_member_required(
        views.CategoriaDeProblemaCreateView.as_view(), login_url=reverse_lazy('sistema:login')
    ), name='cadastrarcategoriadeproblema'),
    path('problemas/editarcategoria/<int:pk>/', staff_member_required(
        views.CategoriaDeProblemaUpdateView.as_view(), login_url=reverse_lazy('sistema:login')
    ), name='editarcategoriadeproblema'),
    path('problemas/deletarcategoria/<int:pk>/', staff_member_required(
        views.CategoriaDeProblemaDeleteView.as_view(), login_url=reverse_lazy('sistema:login')
    ), name='deletarcategoriadeproblema'),


    path('chamados/listarchamados/', staff_member_required(
        views.ChamadoListView.as_view(), login_url=reverse_lazy('sistema:login')
    ), name='listarchamados'),
    path('chamados/cadastrarchamado/', staff_member_required(
        views.ChamadoCreateView.as_view(), login_url=reverse_lazy('sistema:login')
    ), name='cadastrarchamado'),
    path('chamados/editarchamado/<int:pk>/', staff_member_required(
        views.ChamadoUpdateView.as_view(), login_url=reverse_lazy('sistema:login')
    ), name='editarchamado'),
    path('chamados/deletarchamado/<int:pk>/', staff_member_required(
        views.ChamadoDeleteView.as_view(), login_url=reverse_lazy('sistema:login')
    ), name='deletarchamado'),

    path('chamados/imprimir/<int:pk>/', staff_member_required(
        views.ChamadoPrintView.as_view(), login_url=reverse_lazy('sistema:login')
    ), name='imprimirchamado'),


    path('chamados/deletarevento/<int:pk>/', staff_member_required(
        views.EventoChamadoDeleteView.as_view(), login_url=reverse_lazy('sistema:login')
    ), name='deletareventochamado'),


    path('filtro/chamado/', staff_member_required(
        views.RelatorioChamadoFiltro.as_view(), login_url=reverse_lazy('sistema:login')
    ), name='filtrochamado'),



]
