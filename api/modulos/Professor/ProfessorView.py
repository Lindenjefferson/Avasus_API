from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework import permissions
from django.http.request import HttpRequest
from rest_framework.parsers import JSONParser
import api.modulos.Professor.ProfessorService as professorService


class ProfessorView(APIView):
    permission_classes = [permissions.AllowAny]

    @csrf_exempt
    def get(self, request: HttpRequest):
        # print(request.user.username)
        return professorService.listar_todos()

    @csrf_exempt
    def post(self, request: HttpRequest):
        professor = JSONParser().parse(request)
        return professorService.cadastrar(professor)


class ProfessorDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @csrf_exempt
    def get(self, request: HttpRequest, prof_id: int):
        return professorService.detalhar(prof_id)

    @csrf_exempt
    def put(self, request: HttpRequest, prof_id: int):
        professor = JSONParser().parse(request)
        return professorService.atualizar(prof_id, professor)

    @csrf_exempt
    def delete(self, request: HttpRequest, prof_id: int):
        return professorService.deletar(prof_id)
