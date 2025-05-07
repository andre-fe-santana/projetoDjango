from django.shortcuts import render, redirect
from filmes.forms import FilmeForm

# Create your views here.
def cadastro(request):
    return render(
        request,
        'cadastro.html'
    )

def criarFilme(request):
    if request.method == 'POST':
        form = FilmeForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            # return redirect('/filmes') #vai levar pra mostrar a lista de filmes

    else: # GET
        form = FilmeForm()

    return render(
        request,
        'cadastro.html',
        {'form': form}
    )

        