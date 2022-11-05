from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework import permissions
from django.http.request import HttpRequest
from rest_framework.parsers import JSONParser
import api.modulos.Professor.ProfessorService as professorService


class ProfessorView(APIView):
    permission_classes = [permissions.AllowAny]

    @csrf_exempt
    def post(self, request: HttpRequest):
        professor = JSONParser().parse(request)
        return professorService.cadastrar(professor)


class PerfilProfessor(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @csrf_exempt
    def get(self, request: HttpRequest):
        return professorService.detalhar(request.user.username)