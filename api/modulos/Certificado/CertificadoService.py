from rest_framework.response import Response
from rest_framework import status
from datetime import date
from api.models import PLano_Curso, Certificado, Professor
import secrets, io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader

def gerar(curso_id: int, prof_cpf: str):
    curso = PLano_Curso.objects.filter(id=curso_id)
    if not curso.exists():
        return Response({'message': 'Curso não existente'}, status=status.HTTP_400_BAD_REQUEST)
    if curso.get().status != "aprovado":
        return Response({'message': 'Curso não aprovado'}, status=status.HTTP_400_BAD_REQUEST)
    if Certificado.objects.filter(curso=curso_id).exists():
        return baixar(curso_id)   
    Certificado.objects.create(
        professor=Professor.objects.get(cpf=prof_cpf),
        curso=curso.get(),
        data_criacao=date.today(),
        codigo=secrets.token_urlsafe()
    )
    return baixar(curso_id)


def validar(token: str):
    if Certificado.objects.filter(codigo=token).exists():
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


def baixar(curso_id: int):
    certificado = Certificado.objects.filter(curso=curso_id)
    if not certificado.exists():
        return Response({'message': 'Certificado não gerado para este curso'}, status=status.HTTP_400_BAD_REQUEST)
    return gerar_pdf(certificado.get())


def gerar_pdf(certificado: Certificado):
    buf = io.BytesIO()
    canva = canvas.Canvas(buf, pagesize=letter)
    canva.drawImage
    objeto = canva.beginText()
    objeto.setTextOrigin(inch/2, inch*10)
    objeto.setFont("Helvetica", 14)
    conteudo = [certificado.curso.professor_responsavel.nome + " - " + certificado.curso.professor_responsavel.cpf, "",
    "Nome do curso: " + certificado.curso.titulo,
    "Área Temática: " + certificado.curso.eixo_tematico.nome,
    "Carga Horária: " + str(certificado.curso.carga_horaria) + " hrs",
    "Data de emissão: " + certificado.data_criacao.strftime("%d/%m/%Y"),
    "Código de autenticação: " + certificado.codigo] 
    for linha in conteudo:
        objeto.textLine(str(linha))
    imagem =  ImageReader(r"api/utils/imagens/assinatura.png")
    canva.drawImage(imagem, 180, 50, 260, 150)
    canva.drawText(objeto)
    canva.showPage()
    canva.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename="Certificado.pdf")