from dataclasses import field
from rest_framework import serializers
from api.models import PLano_Curso

class PlanoCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PLano_Curso
        fields = ('id', 'titulo', 'carga_horaria', 'professor_responsavel', 'eixo_tematico', 'status')


class PlanoCursoDetalhadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PLano_Curso
        fields = ('id', 'titulo', 'objetivo_geral', 'ementa', 'carga_horaria', 'professor_responsavel', 'eixo_tematico', 'status', 'avaliacao')