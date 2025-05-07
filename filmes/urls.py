from django.urls import path
from filmes import views

urlpatterns = [
    path('cadastro/', views.criarFilme, name='cadastro'),
]
