from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import api.services.CertificadoService as certificadoService


@csrf_exempt
def certificado_api(request, id):
    if request.GET and id == 0:
        return certificadoService.listarTodos()
    elif request.GET and id != 0:
        return certificadoService.baixar(id)
    elif request.method == 'POST':
        certificado = JSONParser().parse(request)
        return certificadoService.gerar(certificado)
