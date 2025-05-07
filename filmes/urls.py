from django.urls import path
from filmes import views

urlpatterns = [
    path('cadastrar/', views.criarFilme, name='cadastro'),
    path('', views.mostrarFilmes, name='filmes'), # Primeira página que aparece quando você acessa "Filmes"
]
