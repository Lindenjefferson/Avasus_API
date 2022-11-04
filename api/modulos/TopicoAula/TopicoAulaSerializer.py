from dataclasses import field
from rest_framework import serializers
from api.models import Topico_Aula

class TopicoAulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topico_Aula
        fields = ('id')