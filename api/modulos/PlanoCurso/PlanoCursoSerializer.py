from dataclasses import field
from rest_framework import serializers
from api.models import PLano_Curso

class PlanoCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PLano_Curso
        fields = ('id')