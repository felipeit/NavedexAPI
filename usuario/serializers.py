from usuario.models import Usuario, Projeto
from rest_framework import serializers


class RootSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'name', 'birthdate', 'admission_date', 'job_role']


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'name', 'birthdate', 'admission_date', 'job_role', 'projetos']

class ProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projeto
        fields = ['id', 'name']

    def create(self, validated_data):
        if self.initial_data.keys == 'lista_usuarios':
            lista_usuarios = self.initial_data['lista_usuarios']
            name = self.initial_data['name']
            projeto = Projeto.objects.get(name=name)
            for a in lista_usuarios:
                Usuario.objects.update(projetos=projeto.id)
            return projeto
        return super(ProjetoSerializer, self).create(validated_data)

class UsuarioDetailSerializer(serializers.ModelSerializer):
    projetos = serializers.SerializerMethodField('teste')

    class Meta:
        model = Usuario
        fields = fields = ['id', 'name', 'birthdate', 'admission_date', 'job_role', 'projetos']

    def teste(self, instance):
        if instance.projetos != None:
            obj = Projeto.objects.get(id=instance.projetos.id)
            return {
                "id": obj.id, 
                "name": obj.name
                }


class ProjetoDetailSerializer(serializers.ModelSerializer):
    navers = serializers.SerializerMethodField('usuarios')
    
    class Meta:
        model = Projeto
        fields = ['id', 'name', 'navers']

    def usuarios(self, instance):
        lista_usuarios = []
        for a in instance.usuario_set.values():
            print(a)
            obj = {
                "id": a['id'],
                "name": a['name'],
                "birthdate": a['birthdate'],
                "admission_date": a['admission_date'],
                "job_role": a['job_role']
            }
            lista_usuarios.append(obj)
        return lista_usuarios