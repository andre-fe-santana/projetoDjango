from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sistema.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('filmes/', include('filmes.urls')),
]

# http://127.0.0.1:8000/ => A home do projeto inteiro
# http://127.0.0.1:8000/admin => A tela de admin
# http://127.0.0.1:8000/usuario => A página inicial do app usuário
