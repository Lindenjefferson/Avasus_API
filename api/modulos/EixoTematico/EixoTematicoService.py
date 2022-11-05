from rest_framework.response import Response
from rest_framework import status
from api.models import Eixo_Tematico
import api.modulos.EixoTematico.EixoTematicoSerializer as eixoTematicoSerializer


def listar_todos():
    eixos_tematicos = Eixo_Tematico.objects.all()
    response = eixoTematicoSerializer.Eixo_Tematico(eixos_tematicos, many=True).data
    return Response(response, status=status.HTTP_200_OK)
