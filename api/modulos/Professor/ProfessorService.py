from rest_framework.response import Response
from rest_framework import status
from api.models import Professor
from datetime import datetime
import api.modulos.Professor.ProfessorSerializer as ProfessorSerializer
import api.modulos.Usuario.UsuarioService as UsuarioService

ID_NOT_FOUND = "Id não encontrado."


def listar_todos():
    professores = Professor.objects.all()
    response = ProfessorSerializer.ProfessorSerializer(professores, many=True).data
    return Response(response, status=status.HTTP_200_OK)


def detalhar(id):
    try:
        professor = Professor.objects.get(id=id)
        response = ProfessorSerializer.ProfessorSerializer(professor).data
        return Response(response, status=status.HTTP_200_OK)
    except Professor.DoesNotExist:
        return Response({'message': ID_NOT_FOUND}, status=status.HTTP_400_BAD_REQUEST)


def cadastrar(professor_data):
    retorno_usuario = UsuarioService.criar_usuario(professor_data)
    if (retorno_usuario != None):
        return Response({'message': retorno_usuario}, status=status.HTTP_400_BAD_REQUEST)
    validacao_professor = validar_prof(professor_data)
    if (validacao_professor != None):
        return Response({'message': validacao_professor}, status=status.HTTP_400_BAD_REQUEST)
    professor_serializer = ProfessorSerializer.CadastroProfessorSerializer(data=professor_data)
    if not professor_serializer.is_valid():
        return Response({'message': 'Falha ao cadastrar'}, status=status.HTTP_400_BAD_REQUEST)
    professor_serializer.save()
    return Response({'message': 'Adicionado com sucesso'}, status=status.HTTP_200_OK)


def atualizar(id, professor_data):
    try:
        professor = Professor.objects.get(id=id)
        validacao_professor = validar_prof(professor_data)
        if (validacao_professor != None):
            return Response({'message': validacao_professor}, status=status.HTTP_400_BAD_REQUEST)
        professor_serializer = ProfessorSerializer.EdicaoProfessorSerializer(professor, data=professor_data)
        if not professor_serializer.is_valid():
            return Response({'message': 'Falha ao atualizar'}, status=status.HTTP_400_BAD_REQUEST)
        professor_serializer.save()
        return Response({'message': 'Atualizado com sucesso'}, status=status.HTTP_200_OK)
    except Professor.DoesNotExist:
        return Response({'message': ID_NOT_FOUND}, status=status.HTTP_400_BAD_REQUEST)


def deletar(id):
    try:
        professor = Professor.objects.get(id=id)
        professor.delete()
        return Response({'message': 'Deletado com sucesso'}, status=status.HTTP_200_OK)
    except Professor.DoesNotExist:
        return Response({'message': ID_NOT_FOUND}, status=status.HTTP_400_BAD_REQUEST)


def validar_prof(professor_data):
    professor_data["titulacao"] = str(
        professor_data["titulacao"]).lower().strip()
    if not validar_data(professor_data["data_nascimento"]):
        return 'Data de nascimento invalida'
    elif not validar_titulacao(professor_data["titulacao"]):
        return 'Titulação invalida, valido apenas: graduação, especialização, mestrado e doutorado'
    else:
        return None


def validar_titulacao(titulo: str):
    if titulo == "graduação" or titulo == "especialização" or titulo == "mestrado" or titulo == "doutorado":
        return True
    else:
        return False


def validar_data(data):
    try:
        datetime.strptime(data, '%Y-%m-%d')
        return True
    except ValueError:
        return False
