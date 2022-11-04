from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from api.modulos.Professor.ProfessorView import ProfessorView, ProfessorDetailView
from api.modulos.Autenticacao.TokenView import TokenView

urlpatterns = [
    path('login', TokenView.as_view()),
    path('login/refresh', TokenRefreshView.as_view()),
    path('professor', ProfessorView.as_view()),
    path('professor/<int:prof_id>', ProfessorDetailView.as_view())
]
