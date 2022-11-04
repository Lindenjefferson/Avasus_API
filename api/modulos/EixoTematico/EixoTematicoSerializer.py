from dataclasses import field
from rest_framework import serializers
from api.models import Eixo_Tematico

class EixoTematicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eixo_Tematico
        fields = ('id', 'nome')

class EixoTematicoCadastroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eixo_Tematico
        fields = ('nome')