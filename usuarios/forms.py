from django import forms
from sistema.models import Usuario

class UsuarioForm(forms.ModelForm):
    model = Usuario
    fields = ['nome', 'sobrenome', 'cpf', 'telefone', 'email', 'endereco', 'imagem',] #campos