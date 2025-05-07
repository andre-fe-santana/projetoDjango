from django import forms
from sistema.models import Filme

class FilmeForm(forms.ModelForm):
    class Meta: #sintaxe pra declarar os campos
        model = Filme
        fields = [
            'nome',
            'ano_lancamento',
            'estudio',
            'genero',
            'sinopse',
        ]