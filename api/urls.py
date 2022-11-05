from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from api.modulos.Professor.ProfessorView import ProfessorView, PerfilProfessor
from api.modulos.Autenticacao.TokenView import TokenView
from api.modulos.EixoTematico.EixoTematicoView import EixoTematicoView
from api.modulos.PlanoCurso.PlanoCursoView import PLanoCursoView, PLanoCursoDetalhadoView, AdminListarCursosView, AdminAlterarStatusCursosView
from api.modulos.TopicoAula.TopicoAulaView import TopicoAulaView


urlpatterns = [
    path('login', TokenView.as_view()),
    path('login/refresh', TokenRefreshView.as_view()),
    path('eixos-tematicos', EixoTematicoView.as_view()),
    path('professor', ProfessorView.as_view()),
    path('professor/perfil', PerfilProfessor.as_view()),
    path('professor/curso', PLanoCursoView.as_view()),
    path('professor/curso/<int:curso_id>', PLanoCursoDetalhadoView.as_view()),
    path('professor/curso/<int:curso_id>/topico', TopicoAulaView.as_view()),
    path('admin/curso', AdminListarCursosView.as_view()),
    path('admin/curso/<int:curso_id>', AdminAlterarStatusCursosView.as_view())
]
