from django.http.response import JsonResponse
from api.models import Eixo_Tematico
import api.modulos.EixoTematico.EixoTematicoSerializer as eixoTematicoSerializer


def listar_todos():
    eixos_tematicos = Eixo_Tematico.objects.all()
    response = eixoTematicoSerializer.Eixo_Tematico(eixos_tematicos, many=True).data
    return JsonResponse(response, safe=False)


def cadastrar(eixo_tematico_data):
    eixo_tematico_data["nome"] = str(eixo_tematico_data["nome"]).lower().strip()
    if not Eixo_Tematico.objects.filter(nome=eixo_tematico_data["nome"]).exists():
        return JsonResponse({'message': 'Eixo tematico ja cadastrado com esse nome.'})
    eixo_tematico_serializer = eixoTematicoSerializer.EixoTematicoCadastroSerializer(data=eixo_tematico_data)
    eixo_tematico_serializer.save()
    return JsonResponse({'message': 'Adicionado com sucesso'})


def atualizar(id, eixo_tematico_data):
    try:
        eixo_tematico = Eixo_Tematico.objects.get(id=id)
        eixo_tematico_data["nome"] = str(eixo_tematico_data["nome"]).lower().strip()
        if not Eixo_Tematico.objects.filter(nome=eixo_tematico_data["nome"]).exists():
            return JsonResponse({'message': 'Eixo tematico ja cadastrado com esse nome.'})
        eixo_tematico_serializer = eixoTematicoSerializer.EixoTematicoCadastroSerializer(eixo_tematico, data=eixo_tematico_data)
        eixo_tematico_serializer.save()
        return JsonResponse({'message': 'Atualizado com sucesso'})
    except Eixo_Tematico.DoesNotExist:
        return JsonResponse({'message': 'Id não encontrado'}, status=400)


def deletar(id):
    try:
        eixo_tematico = Eixo_Tematico.objects.get(id=id)
        eixo_tematico.delete()
        return JsonResponse({'message': 'Deletado com sucesso'})
    except Eixo_Tematico.DoesNotExist:
        return JsonResponse({'message': 'Id não encontrado'}, status=400)