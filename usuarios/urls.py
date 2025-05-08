from django.urls import path
from usuarios import views

urlpatterns = [
    path('cadastrar/', views.criarUsuario, name="criarUsuario"),
    path('', views.mostrarUsuarios, name="mostrarUsuarios"),
    path('login/', views.login, name="login")
]
