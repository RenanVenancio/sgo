# coding=utf-8


from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required  #Staff
from django.urls import reverse_lazy
from rest_framework.authtoken.views import obtain_auth_token 


app_name = 'sistema'

urlpatterns = [
    # Temporáriamente comentado, ainda plajejando qual será a tela pricipal do sistema
    #TODO: Fazer a tela de dashboard com as estatiticas
    path('', login_required(views.IndexListView.as_view(), login_url=reverse_lazy('sistema:login')), name='index'),
    path('', login_required(views.ChamadoListView.as_view(), login_url=reverse_lazy('sistema:login')), name='index'),

    path('login/', auth_views.login, {'template_name': 'sistema/login.html'}, name='login'),
    path('logout/', auth_views.logout, {'next_page': reverse_lazy('sistema:index')}, name='logout'),


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


    path('problemas/listarsubcategorias/', staff_member_required(
        views.SubcategoriaDeProblemaListView.as_view(), login_url=reverse_lazy('sistema:login')
    ), name='subcategoriasdeproblemas'),
    path('problemas/cadastrarsubcategoria/', staff_member_required(
        views.SubcategoriaDeProblemaCreateView.as_view(), login_url=reverse_lazy('sistema:login')
    ), name='cadastrarsubcategoriadeproblema'),
    path('problemas/editarsubcategoria/<int:pk>/', staff_member_required(
        views.SubcategoriaDeProblemaUpdateView.as_view(), login_url=reverse_lazy('sistema:login')
    ), name='editarsubcategoriadeproblema'),
    path('problemas/removersubcategoria/<int:pk>/', staff_member_required(
        views.SubcategoriaDeProblemaDeleteView.as_view(), login_url=reverse_lazy('sistema:login')
    ), name='deletarsubcategoriadeproblema'),


    path('problemas/listarproblemas/', staff_member_required(
        views.ProblemaListView.as_view(), login_url=reverse_lazy('sistema:login')
    ), name='listarproblemas'),
    path('problemas/cadastrarproblema/', staff_member_required(
        views.ProblemaCreateView.as_view(), login_url=reverse_lazy('sistema:login')
    ), name='cadastrarproblema'),
    path('problemas/editarproblema/<int:pk>/', staff_member_required(
        views.ProblemaUpdateView.as_view(), login_url=reverse_lazy('sistema:login')
    ), name='editarproblema'),
    path('problemas/deletarproblema/<int:pk>/', staff_member_required(
        views.ProblemaDeleteView.as_view(), login_url=reverse_lazy('sistema:login')
    ), name='deletarproblema'),


    path('chamados/listarchamados/', login_required(
        views.ChamadoListView.as_view(), login_url=reverse_lazy('sistema:login')
    ), name='listarchamados'),
    path('chamados/cadastrarchamado/', login_required(
        views.ChamadoCreateView.as_view(), login_url=reverse_lazy('sistema:login')
    ), name='cadastrarchamado'),
    path('chamados/editarchamado/<int:pk>/', login_required(
        views.ChamadoUpdateView.as_view(), login_url=reverse_lazy('sistema:login')
    ), name='editarchamado'),
    path('chamados/deletarchamado/<int:pk>/', login_required(
        views.ChamadoDeleteView.as_view(), login_url=reverse_lazy('sistema:login')
    ), name='deletarchamado'),


    # APIs de gerenecimento
    path('api/empreendimentos/',
        views.EmpreendimentoCreateViewAPI.as_view(),
        name='apiempreendimento'),
    path('api/empreendimentos/<int:pk>/',
        views.EmpreendimentoDetailsViewAPI.as_view(),
        name='apidetailempreendimento'),


    path('api/blocos/',
        views.BlocoSerializerCreateViewAPI.as_view(),
        name='apiblocos'),
    path('api/blocos/<int:pk>/',
        views.BlocoSerializerDetailsViewAPI.as_view(),
        name='apidetailbloco'),


    path('api/apartamentos/',
        views.ApartamentoSerializerCreateViewAPI.as_view(),
        name='apiapartamentos'),
    path('api/apartamentos/<int:pk>/',
        views.ApartamentoSerializerDetailsViewAPI.as_view(),
        name='apidetailapartamentos'),


    path('api/categoriasdeproblemas/',
        views.CategoriaDeProblemaCreateViewAPI.as_view(),
        name='apicategoriasdeproblemas'),
    path('api/categoriasdeproblemas/<int:pk>/',
        views.CategoriaDeProblemaDetailsViewAPI.as_view(),
        name='apidetailcategoriasdeproblemas'),


    path('api/subcategoriadeproblemas/',
        views.SubcategoriaDeProblemaCreateViewAPI.as_view(),
        name='apisubcategoriadeproblemas'),
    path('api/subcategoriadeproblemas/<int:pk>/',
        views.SubcategoriaDeProblemaDetailsViewAPI.as_view(),
        name='apidetailsubcategoriadeproblemas'),


    path('api/problemas/',
        views.ProblemaCreateViewAPI.as_view(),
        name='apiproblemas'),
    path('api/problemas/<int:pk>/',
        views.ProblemaDetailsViewAPI.as_view(),
        name='apidetailproblemas'),
    #FIXME: A view precisa gerar o protocolo automaticamente
    path('api/chamadosany/',
        views.ChamadoCreateViewAPIAny.as_view(),
        name='apichamadosany'),
    path('api/chamados/',
        views.ChamadoCreateViewAPI.as_view(),
        name='apichamados'),
    path('api/chamados/<int:pk>/',
        views.ChamadoDetailsViewAPI.as_view(),
        name='apidetailchamados'),

    path('api/chamados/', #Renan Testes
         views.ChamadoDetailsViewAPI.as_view(),
         name='apilistarchamados'),


    # Autenticação via Token
    path('get-token/', obtain_auth_token),
]
