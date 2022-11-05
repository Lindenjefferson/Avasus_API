from rest_framework.response import Response
from rest_framework import status
from api.models import PLano_Curso, Topico_Aula
import api.modulos.TopicoAula.TopicoAulaSerializer as TopicoAulaSerializer


def listar_por_curso(curso_id: int):
    if PLano_Curso.objects.filter(id=curso_id).exists() == False:
        return Response({'message': 'Curso não existente'}, status=status.HTTP_400_BAD_REQUEST)
    topicos = Topico_Aula.objects.filter(curso=curso_id)
    response = TopicoAulaSerializer.TopicoAulaSerializer(topicos, many=True).data
    return Response(response, status=status.HTTP_200_OK)       

def cadastrar(topico_data: dict, curso_id: int):
    if PLano_Curso.objects.filter(id=curso_id).exists() == False:
        return Response({'message': 'Curso não existente'}, status=status.HTTP_400_BAD_REQUEST)
    if PLano_Curso.objects.get(id=curso_id).status != "aprovado":
        return Response({'message': 'Curso ainda não aprovado'}, status=status.HTTP_400_BAD_REQUEST)
    if Topico_Aula.objects.filter(curso=curso_id).count() == 5:
        return Response({'message': 'Maximo de topicos de aula ja cadastrados'}, status=status.HTTP_400_BAD_REQUEST)
    topico_data.update(curso=curso_id)
    topico = TopicoAulaSerializer.CadastroTopicoAulaSerializer(data=topico_data)
    if not topico.is_valid():
        return Response({'message': 'Falha ao cadastrar'}, status=status.HTTP_400_BAD_REQUEST)
    topico.save()
    return Response({'message': 'Adicionado com sucesso'}, status=status.HTTP_200_OK)
