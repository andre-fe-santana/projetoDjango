from django.utils import timezone
from django.db import models


class Usuario (models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    endereco = models.CharField(max_length=100)
    data_cadastro = models.DateField(default=timezone.now)
    ativo = models.BooleanField(default=True)
    # foto = 
