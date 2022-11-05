from dataclasses import field
from rest_framework import serializers
from api.models import Professor


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ('id', 'cpf', 'nome', 'data_nascimento', 'titulacao', 'termo_uso')


class CadastroProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ('cpf', 'nome', 'data_nascimento', 'titulacao')
