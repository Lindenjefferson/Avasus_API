from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
import api.modulos.EixoTematico.EixoTematicoService as eixoTematicoService