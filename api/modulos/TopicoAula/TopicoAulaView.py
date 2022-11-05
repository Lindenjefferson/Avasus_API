from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework import permissions
from django.http.request import HttpRequest
from rest_framework.parsers import JSONParser
import api.modulos.TopicoAula.TopicoAulaService as topicoAulaService


class TopicoAulaView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @csrf_exempt
    def get(self, request: HttpRequest, curso_id: int):
        return topicoAulaService.listar_por_curso(curso_id)

    @csrf_exempt
    def post(self, request: HttpRequest, curso_id: int):
        topico = JSONParser().parse(request)
        return topicoAulaService.cadastrar(topico, curso_id)