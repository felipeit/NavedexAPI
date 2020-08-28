from usuario.models import Usuario, Projeto
from rest_framework import viewsets
from rest_framework import permissions
from usuario.serializers import (
    UsuarioSerializer, 
    RootSerializer, 
    ProjetoSerializer, 
    ProjetoDetailSerializer, 
    UsuarioDetailSerializer)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.decorators import action


class ApiRoot(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]
    def list(self, request):
        queryset = Usuario.objects.all()
        serializer = RootSerializer(queryset, many=True)
        return Response(serializer.data)

class Cadastro(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(method='post', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT, 
    properties={
        'email': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'password': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
    }
    ))
    @action(detail=False, methods=['post'])
    def create_user(self, *args, **kwargs):
        if self.request.data['email'] and self.request.data['password']:
            email = self.request.data['email']
            password = self.request.data['password']
            data = {"email":email, "password":password}
            Usuario.objects.create_superuser(**data)
            return Response({"Message":"Success!"}, status=status.HTTP_201_CREATED)
        return Response({"Message":"Error!"}, status=status.HTTP_400_BAD_REQUEST)

class UsuarioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, *args, **kwargs):
        id = int(self.kwargs['pk'])
        instance = Usuario.objects.get(id=id)
        serializer = UsuarioDetailSerializer(instance)
        return Response(serializer.data)

class ProjetoViewSet(viewsets.ModelViewSet):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, *args, **kwargs):
        instance = Projeto.objects.get(id=self.kwargs['pk'])
        serializer = ProjetoDetailSerializer(instance)
        return Response(serializer.data)