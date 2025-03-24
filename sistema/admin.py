from django.contrib import admin
from sistema import models

# Aqui fica o registro do Usuário (classe)
@admin.register(models.Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'email', 'ativo',)