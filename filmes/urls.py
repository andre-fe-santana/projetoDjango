from django.urls import path
from filmes import views

urlpatterns = [
    path('cadastrar/', views.criarFilme, name='cadastrarFilme'),
    path('', views.mostrarFilmes, name='listarFilmes'), # Primeira página que aparece quando você acessa "Filmes"
]
