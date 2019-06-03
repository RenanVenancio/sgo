from django.urls import path, include
from rest_framework import routers

from sistema.api import viewset
from rest_framework.authtoken.views import obtain_auth_token
#Swagger
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view


router = routers.DefaultRouter()
schema_view = get_swagger_view ( title = ' API do SGO ' )

router.register(r'listarempreendimentos', viewset.EmpreendimentoListViewAPI, base_name='Empreendimento')
router.register(r'listarblocos', viewset.BlocoListViewAPI, base_name='Bloco')
router.register(r'listarapartamentos', viewset.ApartamentoListViewAPI, base_name='Apartamento')
router.register(r'listageralapartamentos', viewset.ApartamentoListaGeral, base_name='Apartamento')
router.register(r'listarcategoriasdeproblema', viewset.CategoriaDeProblemaListViewAPI, base_name='CategoriaDeProblema')
router.register(r'listarareascomuns', viewset.AreaComumListViewAPI, base_name='AreaComum')
router.register(r'chamado', viewset.ChamadoCreateViewAPI, base_name='Chamado')
router.register(r'listarchamados', viewset.ChamadoListViewAPI, base_name='Chamado')

urlpatterns = [

    path('api/', include(router.urls)),
    path('obter-token/', obtain_auth_token, name='api_token_auth'),
    path('api/docs/', schema_view) #Url da documentação da API



]
