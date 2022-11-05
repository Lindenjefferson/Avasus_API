from rest_framework.response import Response
from rest_framework import status
from api.models import PLano_Curso, Professor, Eixo_Tematico
import api.modulos.PlanoCurso.PlanoCursoSerializer as PlanoCursoSerializer

ID_NOT_FOUND = "Id não encontrado."


def cadastrar(curso_data: dict, prof_cpf: str):
    prof = Professor.objects.get(cpf=prof_cpf)
    if Eixo_Tematico.objects.filter(id=curso_data["eixo_tematico"]).exists() == False:
        return Response({'message': 'Area tematica não existente'}, status=status.HTTP_400_BAD_REQUEST)
    curso_data.update(professor_responsavel=prof.id)
    curso_data.update(status="pendente")
    curso = PlanoCursoSerializer.PlanoCursoDetalhadoSerializer(data=curso_data)
    if not curso.is_valid():
        return Response({'message': 'Falha ao cadastrar'}, status=status.HTTP_400_BAD_REQUEST)
    curso.save()
    return Response({'message': 'Adicionado com sucesso'}, status=status.HTTP_200_OK)


def listar_meus_cursos(prof_cpf: str):
    prof = Professor.objects.get(cpf=prof_cpf)
    cursos = PLano_Curso.objects.filter(professor_responsavel=prof.id)
    response = PlanoCursoSerializer.PlanoCursoSerializer(cursos, many=True).data
    for curso in response:
        curso.update(eixo_tematico=Eixo_Tematico.objects.get(id=curso.get("eixo_tematico")).nome)
        curso.pop("professor_responsavel")
    return Response(response, status=status.HTTP_200_OK)


def detalhar(id: int):
    try:
        curso = PLano_Curso.objects.get(id=id)
        response = PlanoCursoSerializer.PlanoCursoDetalhadoSerializer(curso).data
        response.update(eixo_tematico=Eixo_Tematico.objects.get(id=response.get("eixo_tematico")).nome)
        response.update(professor_responsavel=Professor.objects.get(id=response.get("professor_responsavel")).nome)
        return Response(response, status=status.HTTP_200_OK)
    except PLano_Curso.DoesNotExist:
        return Response({'message': ID_NOT_FOUND}, status=status.HTTP_400_BAD_REQUEST)


def listar_todos():
    cursos = PLano_Curso.objects.all()
    response = PlanoCursoSerializer.PlanoCursoSerializer(cursos, many=True).data
    for curso in response:
        curso.update(eixo_tematico=Eixo_Tematico.objects.get(id=curso.get("eixo_tematico")).nome)
        curso.update(professor_responsavel=Professor.objects.get(id=curso.get("professor_responsavel")).nome)
    return Response(response, status=status.HTTP_200_OK)    


def alterar_status(curso_id: int, data: dict):
    try:
        curso = PLano_Curso.objects.get(id=curso_id)
        if str(data["status"]).strip().lower() == "aprovado": curso.status = "aprovado"
        elif str(data["status"]).strip().lower() == "recusado": curso.status = "recusado"
        else: return Response({'message': "status não permitido"}, status=status.HTTP_400_BAD_REQUEST)
        curso.save()
        return Response(status=status.HTTP_200_OK)
    except PLano_Curso.DoesNotExist:
        return Response({'message': ID_NOT_FOUND}, status=status.HTTP_400_BAD_REQUEST)
