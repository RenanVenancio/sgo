from django.urls import path, include
from rest_framework import routers

from sistema.api import viewset
from rest_framework.authtoken.views import obtain_auth_token
#Swagger



router = routers.DefaultRouter()


router.register(r'usuario', viewset.UsuarioViewApi, base_name='Usuarios')
router.register(r'empresa', viewset.EmpresaListViewAPI, base_name='Empresa')
router.register(r'listarempreendimentos', viewset.EmpreendimentoListViewAPI, base_name='Empreendimento')
router.register(r'listarblocos', viewset.BlocoListViewAPI, base_name='Bloco')
router.register(r'listarapartamentos', viewset.ApartamentoListViewAPI, base_name='Apartamento')
router.register(r'listageralapartamentos', viewset.ApartamentoListaGeral, base_name='Apartamento')
router.register(r'listarcategoriasdeproblema', viewset.CategoriaDeProblemaListViewAPI, base_name='CategoriaDeProblema')
router.register(r'listarareascomuns', viewset.AreaComumListViewAPI, base_name='AreaComum')
router.register(r'imagem', viewset.ImagemUploadViewAPI, base_name='ImagemUpload')
router.register(r'chamado', viewset.ChamadoCreateViewAPI, base_name='Chamado')
router.register(r'listarchamados', viewset.ChamadoListViewAPI, base_name='Chamado')

urlpatterns = [

    path('api/', include(router.urls)),
    path('obter-token/', obtain_auth_token, name='api_token_auth'),


]
