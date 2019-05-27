from django.urls import path
from sistema.api import viewset
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [

    #NOVAS URLS TODAS VÃO RETORNAR RESULTADOS BASEADAS NO USER LOGADO'''
    path('api/apartamentos/proprietario/',  # RETORNA TODOS OS APTOS > BLOCOS > EMPREENDIMENTOS. DO USUARIO LOGADO
         viewset.ApartamentoProprietarioSerializerDetailsViewAPI.as_view(),
         name='apidetailapartamentosproprietario'),
    #FIM NOVAS URLS'''

    # APIs de gerenecimento
    path('api/empreendimentos/',
         viewset.EmpreendimentoListViewAPI.as_view(),
         name='apiempreendimento'),

    path('api/blocos/',
         viewset.BlocoListViewAPI.as_view(),
         name='apiblocos'),

    path('api/apartamentos/',
         viewset.ApartamentoListViewAPI.as_view(),
         name='apiapartamentos'),

    path('api/categoriasdeproblemas/',
         viewset.CategoriaDeProblemaListViewAPI.as_view(),
         name='apidetailcategoriasdeproblemas'),

    path('api/chamadosany/',
         viewset.ChamadoCreateViewAPIAny.as_view(),
         name='apichamadosany'),
    path('api/chamados/',
         viewset.ChamadoCreateViewAPI.as_view(),
         name='apichamados'),
    path('api/chamados/<int:pk>/',
         viewset.ChamadoDetailsViewAPI.as_view(),
         name='apidetailchamados'),

    path('api/chamados/',  # Renan Testes
         viewset.ChamadoDetailsViewAPI.as_view(),
         name='apilistarchamados'),

    path('api/take/',  # Renan Testes
         viewset.AptoCascata.as_view(),
         name='apilistarapt'),

    # Autenticação via Token
    path('get-token/', obtain_auth_token),

]