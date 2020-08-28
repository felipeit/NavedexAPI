from rest_framework import routers
from usuario import viewsets


router = routers.DefaultRouter()

router.register('', viewsets.ApiRoot, basename='Usuario')
router.register('usuario', viewsets.UsuarioViewSet)
router.register('projetos', viewsets.ProjetoViewSet)
router.register('', viewsets.Cadastro, basename='user')