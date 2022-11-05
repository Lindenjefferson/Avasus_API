from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework import permissions
from django.http.request import HttpRequest
import api.modulos.EixoTematico.EixoTematicoService as eixoTematicoService


class EixoTematicoView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @csrf_exempt
    def get(self, request: HttpRequest):
        return eixoTematicoService.listar_todos()
