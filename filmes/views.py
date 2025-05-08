from django.shortcuts import render, redirect
from filmes.forms import FilmeForm
from sistema.models import Filme

def mostrarFilmes(request):
    filmes = Filme.objects.all()

    context = {
        'filmes': filmes
    }

    return render(
        request,
        'filmes/listar.html',
        context, 
    )

def criarFilme(request):
    if request.method == 'POST':
        form = FilmeForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/filmes') #vai levar pra mostrar a lista de filmes

    else: # GET
        form = FilmeForm()

    return render(
        request,
        'filmes/cadastro.html',
        {'form': form}
    )

        