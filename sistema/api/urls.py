from django.urls import path
from sistema.api import viewset
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
# APIs de gerenecimento
    path('api/empreendimentos/',
         viewset.EmpreendimentoCreateViewAPI.as_view(),
         name='apiempreendimento'),
    path('api/empreendimentos/<int:pk>/',
         viewset.EmpreendimentoDetailsViewAPI.as_view(),
         name='apidetailempreendimento'),

    path('api/blocos/',
         viewset.BlocoSerializerCreateViewAPI.as_view(),
         name='apiblocos'),
    path('api/blocos/<int:pk>/',
         viewset.BlocoSerializerDetailsViewAPI.as_view(),
         name='apidetailbloco'),

    path('api/apartamentos/',
         viewset.ApartamentoSerializerCreateViewAPI.as_view(),
         name='apiapartamentos'),
    path('api/apartamentos/<int:pk>/',
         viewset.ApartamentoSerializerDetailsViewAPI.as_view(),
         name='apidetailapartamentos'),

    path('api/categoriasdeproblemas/',
         viewset.CategoriaDeProblemaCreateViewAPI.as_view(),
         name='apicategoriasdeproblemas'),
    path('api/categoriasdeproblemas/<int:pk>/',
         viewset.CategoriaDeProblemaDetailsViewAPI.as_view(),
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

    # Autenticação via Token
    path('get-token/', obtain_auth_token),

]