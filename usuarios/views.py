from django.shortcuts import render, redirect
from usuarios.forms import UsuarioForm

# Create your views here.

def login(request): #request é requisição
    return render(
        request,
        'usuarios/login.html',
    )
    

def criarUsuario(request):
    # Verificar se a requisição será do tipo GET ou POST
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES) # Será criada um objeto Usuario(model) com os dados enviados 
        #POST -> são os campos do forms (nome, sobrenome, etc.) preenchidos
        #FILES -> é para passar as imagens
        
        #Fazendo validação dos forms
        if form.is_valid():
            form.save()
            return redirect('/usuario/login') #você só vai redirecionar caso o formulário SEJA válido
    
    else:
        # Se a requisição for GET, exibir o formulário de cadastro
        form = UsuarioForm() #mostra o formulário em branco, afinal nenhum 

    return render(
        request,
        'usuarios/cadastro.html',
        {'form': form}
    )

