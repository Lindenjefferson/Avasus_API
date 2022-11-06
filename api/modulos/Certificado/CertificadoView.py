from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework import permissions
from django.http.request import HttpRequest
import api.modulos.Certificado.CertificadoService as certificadoService


class GerarCertificadoView(APIView):
    permission_classes = [permissions.AllowAny]

    @csrf_exempt
    def get(self, request: HttpRequest, curso_id: int):
        return certificadoService.gerar(curso_id, request.user.username)


class BaixarCertificadoView(APIView):
    permission_classes = [permissions.AllowAny]

    @csrf_exempt
    def get(self, request: HttpRequest, curso_id: int):
        return certificadoService.baixar(curso_id)


class ValidarCertificadoView(APIView):
    permission_classes = [permissions.AllowAny]

    @csrf_exempt
    def get(self, request: HttpRequest, token: str):
        return certificadoService.validar(token)