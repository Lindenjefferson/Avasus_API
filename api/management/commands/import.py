from django.core.management.base import BaseCommand
import api.modulos.EixoTematico.EixoTematicoService as eixoTematicoService


class Command(BaseCommand):
    help = 'Importar itens automaticamente.'

    def add_arguments(self, parser):
        parser.add_argument('-t', '--tipo', type=str, help='Tipo do item a ser importad.o')

    def handle(self, *args, **kwargs):
        tipo = kwargs['tipo']
        if not tipo:
            print("Nenhum tipo de importação informada.")
        elif tipo == "eixos-tematicos":
            print("Importando eixos tematicos.")
            eixos = [
                {"id": "1", "nome": "Síflis e outras IST"},
                {"id": "2", "nome": "Covid-19"},
                {"id": "3", "nome": "Preceptoria"},
                {"id": "4", "nome": "Doenças Raras"},
                {"id": "5", "nome": "Web Palestas"},
                {"id": "6", "nome": "Sistema Prisional"},
                {"id": "7", "nome": "OPAS"}
            ]
            for eixo in eixos:
                eixoTematicoService.cadastrar(eixo)
            print("Importação finalizada.")
        else:
            print("Nenhuma opção encontrada para este tipo.")