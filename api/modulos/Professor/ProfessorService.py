from rest_framework.response import Response
from rest_framework import status
from api.models import Professor
from datetime import datetime, date
import api.modulos.Professor.ProfessorSerializer as ProfessorSerializer
import api.modulos.Usuario.UsuarioService as UsuarioService

ID_NOT_FOUND = "Id não encontrado."


def detalhar(cpf: str):
    try:
        professor = Professor.objects.get(cpf=cpf)
        response = ProfessorSerializer.ProfessorSerializer(professor).data
        response.update(idade = calcular_idade(
            datetime.strptime(response.get("data_nascimento"), '%Y-%m-%d').date()
        ))
        return Response(response, status=status.HTTP_200_OK)
    except Professor.DoesNotExist:
        return Response({'message': ID_NOT_FOUND}, status=status.HTTP_400_BAD_REQUEST)


def cadastrar(professor_data: dict):
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


def calcular_idade(data: date): 
    hoje = date.today() 
    idade = hoje.year - data.year - ((hoje.month, hoje.day) < (data.month, data.day)) 
    return idade 


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
