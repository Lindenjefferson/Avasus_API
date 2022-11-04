from dataclasses import field
from rest_framework import serializers
from api.models import Certificado

class CertificadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificado
        fields = ('id')