from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework import permissions
from django.http.request import HttpRequest
from rest_framework.parsers import JSONParser
import api.modulos.PlanoCurso.PlanoCursoService as planoCursoService

class PLanoCursoView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @csrf_exempt
    def post(self, request: HttpRequest):
        curso = JSONParser().parse(request)
        return planoCursoService.cadastrar(curso, request.user.username)

    @csrf_exempt
    def get(self, request: HttpRequest):
        return planoCursoService.listar_meus_cursos(request.user.username)


class PLanoCursoDetalhadoView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @csrf_exempt
    def get(self, request: HttpRequest, curso_id: int):
        return planoCursoService.detalhar(curso_id)


class AdminListarCursosView(APIView):
    permission_classes = [permissions.IsAdminUser]

    @csrf_exempt
    def get(self, request: HttpRequest):
        return planoCursoService.listar_todos()


class AdminAlterarStatusCursosView(APIView):
    permission_classes = [permissions.IsAdminUser]

    @csrf_exempt
    def put(self, request: HttpRequest, curso_id: int):
        status = JSONParser().parse(request)
        return planoCursoService.alterar_status(curso_id, status)