from email.policy import default
from sqlite3 import Date
from django.db import models

# Create your models here.

class Professor(models.Model):
    id = models.AutoField(primary_key=True)
    cpf = models.CharField(unique=True, max_length=20)
    nome = models.CharField(max_length=120)
    data_nascimento = models.DateField()
    titulacao = models.CharField(max_length=120)
    termo_uso = models.BooleanField(default=False)

class Eixo_Tematico(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=120)

class PLano_Curso(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=120)
    objetivo_geral = models.CharField(max_length=250)
    ementa = models.CharField(max_length=500)
    carga_horaria = models.IntegerField()
    professor_responsavel = models.ForeignKey(Professor, on_delete=models.CASCADE)
    eixo_tematico = models.ForeignKey(Eixo_Tematico, on_delete=models.CASCADE)
    status = models.CharField(max_length=15)
    avaliacao = models.FloatField()

class Topico_Aula(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=120)
    descricao = models.CharField(max_length=500)
    curso = models.ForeignKey(PLano_Curso, on_delete=models.CASCADE)

class Certificado(models.Model):
    id = models.AutoField(primary_key=True)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    curso = models.ForeignKey(PLano_Curso, on_delete=models.CASCADE)
    data = models.DateField()
    codigo = models.CharField(unique=True, max_length=120)
    assinado = models.BooleanField()